#!/usr/bin/env python3
"""
Generate Baritone command documentation from Java source files.

This script parses command classes and generates comprehensive markdown documentation
organized by capability groups.
"""

import re
import os
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class Command:
    """Represents a single command with all its metadata."""
    names: List[str]
    short_desc: str
    long_desc: List[str]
    is_hidden: bool = False
    is_alias: bool = False
    alias_target: str = ""  # For CommandAlias instances
    file_path: str = ""  # Source file path


def extract_string_literal(text: str) -> str:
    """Extract string literal from Java code, handling escaped quotes."""
    # Remove surrounding quotes
    text = text.strip()
    if text.startswith('"') and text.endswith('"'):
        text = text[1:-1]
    # Handle escaped characters
    text = text.replace('\\"', '"').replace('\\n', '\n').replace('\\\\', '\\')
    return text


def parse_command_names(constructor_line: str) -> List[str]:
    """Extract command names from constructor super() call."""
    # Match: super(baritone, "name1", "name2", ...)
    match = re.search(r'super\s*\(\s*[^,]+,\s*(.+?)\s*\)', constructor_line)
    if not match:
        return []
    
    args = match.group(1)
    names = []
    
    # Handle Arrays.asList("name1", "name2")
    as_list_match = re.search(r'Arrays\.asList\s*\(\s*(.+?)\s*\)', args)
    if as_list_match:
        args = as_list_match.group(1)
    
    # Extract string literals
    for match in re.finditer(r'"([^"]*)"', args):
        names.append(match.group(1))
    
    return names


def parse_get_short_desc(content: str) -> str:
    """Extract short description from getShortDesc() method."""
    # Match: return "description";
    pattern = r'public\s+String\s+getShortDesc\s*\([^)]*\)\s*\{[^}]*return\s+"([^"]+)";'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return extract_string_literal(match.group(1))
    
    # Try with multiline
    pattern = r'getShortDesc\s*\([^)]*\)\s*\{[^}]*return\s+"([^"]+)";'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return extract_string_literal(match.group(1))
    
    return ""


def parse_get_long_desc(content: str) -> List[str]:
    """Extract long description from getLongDesc() method."""
    # Match: return Arrays.asList("line1", "line2", ...);
    pattern = r'public\s+List<String>\s+getLongDesc\s*\([^)]*\)\s*\{[^}]*return\s+Arrays\.asList\s*\(\s*(.+?)\s*\);'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        args = match.group(1)
        lines = []
        # Extract all string literals
        for match in re.finditer(r'"([^"]*)"', args):
            lines.append(extract_string_literal(match.group(1)))
        return lines
    
    # Try Collections.singletonList
    pattern = r'return\s+Collections\.singletonList\s*\(\s*"([^"]+)"\s*\);'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return [extract_string_literal(match.group(1))]
    
    return []


def parse_hidden_from_help(content: str) -> bool:
    """Check if command overrides hiddenFromHelp() to return true."""
    # Look for: return true; in hiddenFromHelp method
    pattern = r'hiddenFromHelp\s*\([^)]*\)\s*\{[^}]*return\s+true'
    return bool(re.search(pattern, content, re.DOTALL))


def parse_command_file(file_path: Path) -> Optional[Command]:
    """Parse a command Java file and extract command information."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if it's not a Command subclass (check for extends Command)
    if 'extends Command' not in content and 'extends CommandAlias' not in content:
        return None
    
    # Extract constructor (handle public, protected, or package-private)
    constructor_match = re.search(r'(?:public|protected)?\s+\w+\s*\([^)]*IBaritone[^)]*\)\s*\{[^}]*super\s*\([^)]+\)', content, re.DOTALL)
    if not constructor_match:
        return None
    
    constructor_line = constructor_match.group(0)
    names = parse_command_names(constructor_line)
    
    if not names:
        return None
    
    short_desc = parse_get_short_desc(content)
    long_desc = parse_get_long_desc(content)
    is_hidden = parse_hidden_from_help(content)
    
    # Check if it's a CommandAlias
    is_alias = 'CommandAlias' in content or 'extends CommandAlias' in content
    alias_target = ""
    if is_alias:
        # Extract target from CommandAlias constructor
        target_match = re.search(r'this\.target\s*=\s*"([^"]+)"', content)
        if target_match:
            alias_target = target_match.group(1)
        else:
            # Try from constructor parameter
            target_match = re.search(r'String\s+target[^,]*,\s*"([^"]+)"', content)
            if target_match:
                alias_target = target_match.group(1)
    
    return Command(
        names=names,
        short_desc=short_desc,
        long_desc=long_desc,
        is_hidden=is_hidden,
        is_alias=is_alias,
        alias_target=alias_target,
        file_path=str(file_path)
    )


def parse_execution_control_commands(file_path: Path) -> List[Command]:
    """Parse ExecutionControlCommands.java which has anonymous Command classes."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    commands = []
    
    # Find all anonymous Command instances: variableName = new Command(baritone, "name1", "name2") { ... }
    # Pattern: variableName = new Command(baritone, "name1", "name2", ...) {
    for match in re.finditer(r'(\w+Command)\s*=\s*new\s+Command\s*\(\s*baritone,\s*', content):
        # Extract the names from the constructor call
        start_pos = match.end()
        paren_count = 1
        i = start_pos
        names_start = i
        
        # Find the closing paren of the constructor
        while i < len(content) and paren_count > 0:
            if content[i] == '(':
                paren_count += 1
            elif content[i] == ')':
                paren_count -= 1
            i += 1
        
        if paren_count != 0:
            continue
        
        constructor_args = content[names_start:i-1]
        
        # Extract all string literals (command names)
        names = []
        for name_match in re.finditer(r'"([^"]+)"', constructor_args):
            names.append(name_match.group(1))
        
        if not names:
            continue
        
        # Find the opening brace
        while i < len(content) and content[i] != '{':
            i += 1
        
        if i >= len(content):
            continue
        
        # Find matching closing brace
        brace_count = 1
        start_brace = i
        i += 1
        while i < len(content) and brace_count > 0:
            if content[i] == '{':
                brace_count += 1
            elif content[i] == '}':
                brace_count -= 1
            i += 1
        
        command_block = content[start_brace:i]
        
        short_desc = parse_get_short_desc(command_block)
        long_desc = parse_get_long_desc(command_block)
        is_hidden = parse_hidden_from_help(command_block)
        
        commands.append(Command(
            names=names,
            short_desc=short_desc,
            long_desc=long_desc,
            is_hidden=is_hidden,
            file_path=str(file_path)
        ))
    
    return commands


def parse_default_commands(file_path: Path) -> Dict[str, str]:
    """Parse DefaultCommands.java to get command registration order and discover all commands."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract all command instantiations
    commands_map = {}
    
    # Match: new CommandName(baritone)
    pattern = r'new\s+(\w+Command)\(baritone\)'
    for match in re.finditer(pattern, content):
        cmd_class = match.group(1)
        # Get the variable name or just use class name
        commands_map[cmd_class] = cmd_class
    
    # Match CommandAlias instances
    pattern = r'new\s+CommandAlias\s*\([^)]+\)'
    for match in re.finditer(pattern, content):
        # Extract the full line
        line_start = content.rfind('\n', 0, match.start())
        line_end = content.find('\n', match.end())
        line = content[line_start:line_end] if line_end != -1 else content[line_start:]
        commands_map[f"alias_{match.start()}"] = line.strip()
    
    return commands_map


def categorize_command(command: Command) -> str:
    """Categorize a command based on its name and description."""
    name_lower = ' '.join(command.names).lower()
    desc_lower = (command.short_desc + ' ' + ' '.join(command.long_desc)).lower()
    
    # Pathfinding & Navigation
    if any(name in name_lower for name in ['goal', 'goto', 'path', 'thisway', 'surface', 'axis', 'come']):
        return 'pathfinding'
    
    # Mining & Resources
    if any(name in name_lower for name in ['mine', 'find', 'blacklist', 'pickup']):
        return 'mining'
    
    # Building
    if any(name in name_lower for name in ['build', 'tunnel', 'sel']):
        return 'building'
    
    # Farming
    if 'farm' in name_lower:
        return 'farming'
    
    # Following & Entities
    if 'follow' in name_lower:
        return 'following'
    
    # Waypoints
    if any(name in name_lower for name in ['waypoint', 'wp', 'sethome', 'home']):
        return 'waypoints'
    
    # Exploration
    if any(name in name_lower for name in ['explore', 'explorefilter']):
        return 'exploration'
    
    # Rendering
    if 'render' in name_lower:
        return 'rendering'
    
    # Elytra
    if 'elytra' in name_lower:
        return 'elytra'
    
    # Schematic Tools
    if any(name in name_lower for name in ['litematica', 'schematica']):
        return 'schematic'
    
    # System & Control (default)
    return 'system'


def format_long_desc(long_desc: List[str]) -> str:
    """Format long description for markdown."""
    if not long_desc:
        return ""
    
    formatted = []
    for line in long_desc:
        line = line.strip()
        if line:
            formatted.append(line)
        else:
            formatted.append("")
    
    return '\n'.join(formatted)


def generate_main_index(commands: List[Command], output_dir: Path):
    """Generate the main COMMANDS.md index file."""
    # Count commands by category
    categorized = {}
    for cmd in commands:
        if cmd.is_hidden:
            continue
        cat = categorize_command(cmd)
        if cat not in categorized:
            categorized[cat] = []
        categorized[cat].append(cmd)
    
    category_names = {
        'pathfinding': 'Pathfinding & Navigation',
        'mining': 'Mining & Resources',
        'building': 'Building',
        'farming': 'Farming',
        'following': 'Following & Entities',
        'waypoints': 'Waypoints',
        'exploration': 'Exploration',
        'rendering': 'Rendering',
        'elytra': 'Elytra',
        'schematic': 'Schematic Tools',
        'system': 'System & Control'
    }
    
    content = """# Baritone Commands Documentation

This document provides a comprehensive reference for all Baritone commands, organized by capability.

Commands can be executed in-game using the `#` prefix (default), or without a prefix if `chatControl` is enabled.

## Quick Links

"""
    
    for cat, cat_name in sorted(category_names.items()):
        count = len(categorized.get(cat, []))
        if count > 0:
            filename = f'COMMANDS_{cat.upper()}.md'
            content += f"- [{cat_name}]({filename}) - {count} command{'s' if count != 1 else ''}\n"
    
    content += """
## Using Commands

### Command Prefix

Baritone commands use the `#` prefix by default. For example:
- `#goal 100 64 200` - Set a goal
- `#mine diamond_ore` - Mine diamonds
- `#help` - Show help

You can also use commands without the prefix if `chatControl` is enabled (default: `true`).

### Command Aliases

Many commands have multiple names (aliases). For example:
- `cancel`, `c`, `stop` all refer to the same command
- `waypoints`, `waypoint`, `wp` all refer to the same command

All aliases are shown together in the documentation.

### Tab Completion

Baritone supports tab completion for commands and their arguments. Press `Tab` while typing a command to see available completions.

### Getting Help

Use the `#help` command to see all available commands, or `#help <command>` to see detailed help for a specific command.

## Statistics

- **Total Commands**: {total}
- **Visible Commands**: {visible}
- **Hidden Commands**: {hidden}
- **Command Aliases**: {aliases}
""".format(
        total=len(commands),
        visible=len([c for c in commands if not c.is_hidden]),
        hidden=len([c for c in commands if c.is_hidden]),
        aliases=len([c for c in commands if c.is_alias])
    )
    
    with open(output_dir / 'COMMANDS.md', 'w', encoding='utf-8') as f:
        f.write(content)


def generate_category_file(category: str, category_commands: List[Command], output_dir: Path):
    """Generate a markdown file for a specific category."""
    category_names = {
        'pathfinding': 'Pathfinding & Navigation',
        'mining': 'Mining & Resources',
        'building': 'Building',
        'farming': 'Farming',
        'following': 'Following & Entities',
        'waypoints': 'Waypoints',
        'exploration': 'Exploration',
        'rendering': 'Rendering',
        'elytra': 'Elytra',
        'schematic': 'Schematic Tools',
        'system': 'System & Control'
    }
    
    category_title = category_names.get(category, category.title())
    
    content = f"""# {category_title}

This document contains all commands related to {category_title.lower()}.

## Commands

"""
    
    # Sort commands alphabetically by primary name
    category_commands.sort(key=lambda c: c.names[0].lower() if c.names else '')
    
    for cmd in category_commands:
        if cmd.is_hidden:
            continue
        
        # Command names and aliases
        names_str = ', '.join([f'`{name}`' for name in cmd.names])
        content += f"### {names_str}\n\n"
        
        if cmd.is_alias and cmd.alias_target:
            content += f"**Type**: Alias → `{cmd.alias_target}`  \n\n"
        
        if cmd.short_desc:
            content += f"**Description**: {cmd.short_desc}  \n\n"
        
        if cmd.long_desc:
            formatted_desc = format_long_desc(cmd.long_desc)
            if formatted_desc:
                content += f"{formatted_desc}\n\n"
        
        content += "---\n\n"
    
    # Add back to index link
    content += "\n[← Back to Commands Index](COMMANDS.md)\n"
    
    filename = f'COMMANDS_{category.upper()}.md'
    with open(output_dir / filename, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    """Main entry point."""
    # Determine paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    commands_dir = project_root / 'src' / 'main' / 'java' / 'baritone' / 'command' / 'defaults'
    docs_dir = project_root / 'docs'
    
    if not commands_dir.exists():
        print(f"Error: Commands directory not found at {commands_dir}")
        return 1
    
    # Create docs directory if it doesn't exist
    docs_dir.mkdir(exist_ok=True)
    
    print(f"Scanning {commands_dir}...")
    commands = []
    
    # Parse all command files (including *Commands.java plural)
    all_files = list(commands_dir.glob('*Command.java')) + list(commands_dir.glob('*Commands.java'))
    for file_path in sorted(set(all_files)):  # Remove duplicates
        if file_path.name == 'DefaultCommands.java':
            # Parse CommandAlias instances from DefaultCommands.java
            print(f"  Parsing {file_path.name} (for CommandAlias instances)...")
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find CommandAlias instances: new CommandAlias(baritone, names, "desc", "target")
            # Pattern 1: Arrays.asList("name1", "name2"), "desc", "target"
            pattern1 = r'new\s+CommandAlias\s*\(\s*baritone,\s*Arrays\.asList\s*\(\s*([^)]+)\s*\)\s*,\s*"([^"]+)"\s*,\s*"([^"]+)"'
            for match in re.finditer(pattern1, content):
                names_str = match.group(1)
                desc = match.group(2)
                target = match.group(3)
                names = [n.strip().strip('"') for n in names_str.split(',')]
                commands.append(Command(
                    names=names,
                    short_desc=desc,
                    long_desc=[f"This command is an alias, for: {target} ..."],
                    is_alias=True,
                    alias_target=target,
                    file_path=str(file_path)
                ))
                print(f"    Found alias: {', '.join(names)} → {target}")
            
            # Pattern 2: "name", "desc", "target"
            pattern2 = r'new\s+CommandAlias\s*\(\s*baritone,\s*"([^"]+)"\s*,\s*"([^"]+)"\s*,\s*"([^"]+)"'
            for match in re.finditer(pattern2, content):
                name = match.group(1)
                desc = match.group(2)
                target = match.group(3)
                commands.append(Command(
                    names=[name],
                    short_desc=desc,
                    long_desc=[f"This command is an alias, for: {target} ..."],
                    is_alias=True,
                    alias_target=target,
                    file_path=str(file_path)
                ))
                print(f"    Found alias: {name} → {target}")
            continue
        
        if file_path.name == 'ExecutionControlCommands.java':
            print(f"  Parsing {file_path.name} (special handling)...")
            exec_commands = parse_execution_control_commands(file_path)
            commands.extend(exec_commands)
            print(f"    Found {len(exec_commands)} commands")
        else:
            print(f"  Parsing {file_path.name}...")
            cmd = parse_command_file(file_path)
            if cmd:
                commands.append(cmd)
                print(f"    Found command: {', '.join(cmd.names)}")
    
    print(f"\nFound {len(commands)} total commands")
    
    # Categorize commands
    categorized = {}
    for cmd in commands:
        cat = categorize_command(cmd)
        if cat not in categorized:
            categorized[cat] = []
        categorized[cat].append(cmd)
    
    print(f"Categorized into {len(categorized)} groups:")
    for cat, cat_commands in sorted(categorized.items()):
        visible = len([c for c in cat_commands if not c.is_hidden])
        print(f"  {cat}: {visible} visible commands")
    
    # Generate main index
    print("Generating COMMANDS.md...")
    generate_main_index(commands, docs_dir)
    
    # Generate category files
    for category, cat_commands in categorized.items():
        print(f"Generating COMMANDS_{category.upper()}.md...")
        generate_category_file(category, cat_commands, docs_dir)
    
    print(f"\nDocumentation generated successfully in {docs_dir}/")
    print("\nFiles generated:")
    print("  - COMMANDS.md (main index)")
    for category in sorted(categorized.keys()):
        filename = f'COMMANDS_{category.upper()}.md'
        print(f"  - {filename}")
    
    return 0


if __name__ == '__main__':
    exit(main())

