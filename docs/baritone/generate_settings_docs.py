#!/usr/bin/env python3
"""
Generate Baritone settings documentation from Settings.java source file.

This script parses Settings.java and generates comprehensive markdown documentation
organized by capability groups.
"""

import re
import os
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class Setting:
    """Represents a single setting with all its metadata."""
    name: str
    type: str
    default_value: str
    description: str
    is_java_only: bool = False
    is_deprecated: bool = False
    raw_type: str = ""  # Full generic type like "Setting<Boolean>"


def parse_java_file(file_path: Path) -> List[Setting]:
    """Parse Settings.java and extract all settings."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    settings = []
    lines = content.split('\n')

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Look for JavaDoc comments
        if line.startswith('/**'):
            javadoc_lines = []
            i += 1

            # Collect JavaDoc content
            javadoc_parts = []
            current_para = []

            while i < len(lines):
                javadoc_line = lines[i].strip()
                if javadoc_line.startswith('*/'):
                    i += 1
                    break
                # Remove leading * and whitespace
                cleaned = re.sub(r'^\s*\*\s*', '', javadoc_line)
                if cleaned:
                    # Check for paragraph markers
                    if cleaned == '<p>' or cleaned == '</p>':
                        # Save current paragraph and start new one
                        if current_para:
                            javadoc_parts.append(' '.join(current_para))
                            current_para = []
                    else:
                        current_para.append(cleaned)
                i += 1

            # Add final paragraph
            if current_para:
                javadoc_parts.append(' '.join(current_para))

            # Join paragraphs with double newline
            description = '\n\n'.join(javadoc_parts).strip()

            # Look for @JavaOnly annotation
            is_java_only = False
            is_deprecated = False
            if i < len(lines):
                check_line = lines[i].strip()
                if '@JavaOnly' in check_line:
                    is_java_only = True
                    i += 1
                if '@Deprecated' in check_line:
                    is_deprecated = True
                    if not is_java_only:
                        i += 1

            # Look for the setting declaration
            if i < len(lines):
                setting_line = lines[i].strip()

                # Match: public final Setting<Type> settingName = new Setting<>(defaultValue);
                match = re.search(
                    r'public\s+final\s+Setting<([^>]+)>\s+(\w+)\s*=\s*new\s+Setting<[^>]*>\((.*?)\);',
                    setting_line
                )

                if match:
                    type_str = match.group(1).strip()
                    name = match.group(2).strip()
                    default_val = match.group(3).strip()

                    # Clean up default value
                    default_val = clean_default_value(default_val, type_str)

                    # Determine simplified type
                    simple_type = simplify_type(type_str)

                    settings.append(Setting(
                        name=name,
                        type=simple_type,
                        default_value=default_val,
                        description=description,
                        is_java_only=is_java_only,
                        is_deprecated=is_deprecated,
                        raw_type=type_str
                    ))

        i += 1

    return settings


def clean_default_value(value: str, type_str: str) -> str:
    """Clean and format default value for display."""
    # Remove trailing D, F, L suffixes
    value = re.sub(r'([0-9.]+)[DFLdf]$', r'\1', value)

    # Handle arrays/lists
    if 'Arrays.asList' in value:
        # Extract the list content
        match = re.search(r'Arrays\.asList\((.*?)\)', value, re.DOTALL)
        if match:
            items = match.group(1)
            # Try to extract block/item names
            items = re.sub(r'Blocks\.(\w+)\.asItem\(\)', r'\1', items)
            items = re.sub(r'Blocks\.(\w+)', r'\1', items)
            return f"[{items}]"

    if 'new ArrayList' in value or 'new HashMap' in value:
        if 'Arrays.asList' in value:
            # Already handled above
            pass
        else:
            return "[]" if 'ArrayList' in value else "{}"

    if 'new Vec3i' in value:
        match = re.search(r'new\s+Vec3i\(([^)]+)\)', value)
        if match:
            return f"Vec3i({match.group(1)})"

    if 'TimeUnit.' in value:
        # Handle TimeUnit conversions
        match = re.search(r'TimeUnit\.(\w+)\.toSeconds\((\d+)\)', value)
        if match:
            unit = match.group(1)
            amount = match.group(2)
            return f"{amount} {unit.lower()}"

    if 'Color.' in value:
        # Extract color name
        match = re.search(r'Color\.(\w+)', value)
        if match:
            return match.group(1)

    if value == 'null':
        return "null"

    # Clean up lambda expressions and complex defaults
    if '->' in value or 'lambda' in value or 'Consumer' in value or 'BiConsumer' in value:
        return "(Java function)"

    # Remove extra whitespace
    value = value.strip()

    # Handle strings
    if value.startswith('"') and value.endswith('"'):
        return value

    return value


def simplify_type(type_str: str) -> str:
    """Simplify Java type to a readable format."""
    # Remove generic parameters for display
    base_type = re.sub(r'<.*>', '', type_str).strip()

    type_map = {
        'Boolean': 'Boolean',
        'Integer': 'Integer',
        'Double': 'Double',
        'Float': 'Float',
        'Long': 'Long',
        'String': 'String',
        'List': 'List',
        'Map': 'Map',
        'Vec3i': 'Vec3i',
        'Color': 'Color',
        'Rotation': 'Rotation',
        'Mirror': 'Mirror',
        'Consumer': 'Consumer (Java-only)',
        'BiConsumer': 'BiConsumer (Java-only)'
    }

    for java_type, display_type in type_map.items():
        if java_type in base_type:
            return display_type

    return base_type


def categorize_setting(setting: Setting) -> str:
    """Categorize a setting based on its name and description."""
    name_lower = setting.name.lower()
    desc_lower = setting.description.lower()

    # Basic permissions
    if any(keyword in name_lower for keyword in ['allow', 'assume', 'use']):
        if 'elytra' in name_lower:
            return 'elytra'
        if any(keyword in name_lower for keyword in ['break', 'place', 'sprint', 'inventory', 'tool']):
            return 'basic'
        if any(keyword in name_lower for keyword in ['parkour', 'diagonal', 'downward', 'vines', 'slab', 'water', 'lava', 'step', 'safe']):
            return 'pathing'

    # Pathing
    if any(keyword in name_lower for keyword in ['path', 'cost', 'heuristic', 'timeout', 'movement', 'fall', 'jump', 'penalty']):
        return 'pathing'

    # Mining
    if any(keyword in name_lower for keyword in ['mine', 'ore', 'legitmine', 'internalmining']):
        return 'mining'

    # Building
    if any(keyword in name_lower for keyword in ['build', 'schematic', 'layer', 'substitute', 'ignore', 'okif']):
        return 'building'

    # Farming
    if any(keyword in name_lower for keyword in ['farm', 'replant', 'crop']):
        return 'farming'

    # Rendering
    if any(keyword in name_lower for keyword in ['render', 'color', 'opacity', 'fade', 'linewidth', 'selection']):
        return 'rendering'

    # Chat and control
    if any(keyword in name_lower for keyword in ['chat', 'prefix', 'echo', 'censor', 'control', 'command']):
        return 'chat'

    # Performance and caching
    if any(keyword in name_lower for keyword in ['cache', 'chunk', 'prune', 'packer', 'expiry', 'backfill']):
        return 'performance'

    # Elytra
    if 'elytra' in name_lower:
        return 'elytra'

    # Avoidance
    if any(keyword in name_lower for keyword in ['avoid', 'mob', 'spawner']):
        return 'pathing'

    # Waypoints
    if any(keyword in name_lower for keyword in ['waypoint', 'bed', 'death']):
        return 'basic'

    # Notifications
    if any(keyword in name_lower for keyword in ['notification', 'toast', 'desktop', 'log']):
        return 'chat'

    # Follow
    if 'follow' in name_lower:
        return 'pathing'

    # Items and tools
    if any(keyword in name_lower for keyword in ['item', 'tool', 'sword', 'silk', 'saver']):
        return 'basic'

    # Blocks lists
    if any(keyword in name_lower for keyword in ['block', 'throwaway', 'acceptable']):
        if 'build' in name_lower:
            return 'building'
        return 'basic'

    # Advanced/internal
    if any(keyword in name_lower for keyword in ['backtrack', 'repropagation', 'cutoff', 'splice', 'planning', 'lookahead', 'map', 'loadfactor']):
        return 'advanced'

    # Default to basic
    return 'basic'


def format_description(desc: str) -> str:
    """Format JavaDoc description for markdown."""
    # Remove HTML tags completely (including <p>, </p>, etc.)
    # But preserve paragraph breaks (double newlines)
    desc = re.sub(r'<[^>]+>', '', desc)
    # Convert @see links
    desc = re.sub(r'@see\s+<a\s+href="([^"]+)">([^<]+)</a>', r'See [\2](\1)', desc)
    desc = re.sub(r'@see\s+#(\w+)', r'See `\1`', desc)
    # Convert {@link #setting} to `setting`
    desc = re.sub(r'\{@link\s+#(\w+)\}', r'`\1`', desc)
    # Convert {@link Class#method} to `method`
    desc = re.sub(r'\{@link\s+[^#]+#(\w+)\}', r'`\1`', desc)
    # Clean up multiple spaces, but preserve paragraph breaks
    # First, protect paragraph breaks
    desc = desc.replace('\n\n', ' <PARA_BREAK> ')
    # Clean up multiple spaces
    desc = re.sub(r'\s+', ' ', desc)
    # Restore paragraph breaks
    desc = desc.replace(' <PARA_BREAK> ', '\n\n')
    return desc.strip()


def generate_main_index(settings: List[Setting], output_dir: Path):
    """Generate the main SETTINGS.md index file."""
    content = """# Baritone Settings Documentation

This document provides a comprehensive reference for all Baritone settings, organized by capability.

Settings can be modified using the `#set` command in-game, or by editing the `settings.txt` file in your `minecraft/baritone/` directory.

## Quick Links

- [Basic Permissions & Actions](SETTINGS_BASIC.md) - Core permissions for breaking, placing, sprinting, etc.
- [Pathfinding & Movement](SETTINGS_PATHING.md) - Pathfinding algorithm, movement types, and path optimization
- [Mining](SETTINGS_MINING.md) - Mining behavior, ore detection, and mining-related settings
- [Building & Schematics](SETTINGS_BUILDING.md) - Schematic building, block substitution, and builder behavior
- [Farming](SETTINGS_FARMING.md) - Crop farming and replanting settings
- [Rendering & Visual](SETTINGS_RENDERING.md) - Visual rendering, colors, and display options
- [Chat & Control](SETTINGS_CHAT.md) - Chat commands, prefixes, and control settings
- [Performance & Caching](SETTINGS_PERFORMANCE.md) - Chunk caching, performance optimization, and memory management
- [Elytra](SETTINGS_ELYTRA.md) - Elytra flight and pathfinding settings
- [Advanced/Internal](SETTINGS_ADVANCED.md) - Advanced A* settings, internal optimizations, and debugging

## Using Settings

### In-Game Commands

- `#set <setting>` - View current value of a setting
- `#set <setting> <value>` - Set a setting to a value
- `#set toggle <setting>` - Toggle a boolean setting
- `#set reset <setting>` - Reset a setting to default
- `#set reset all` - Reset all settings to defaults
- `#set list` - List all settings
- `#set modified` - List only modified settings
- `#set save` - Save settings to disk
- `#set load [filename]` - Load settings from file

### Settings File Format

Settings are saved in `minecraft/baritone/settings.txt` with the format:
```
settingname value
```

For example:
```
allowBreak true
blockBreakSpeed 6
costHeuristic 3.563
```

Comments can be added using `#` or `//`:
```
# This is a comment
allowBreak true
```

## Setting Types

- **Boolean**: `true` or `false`
- **Integer**: Whole numbers (e.g., `5`, `100`)
- **Double/Float**: Decimal numbers (e.g., `3.563`, `0.5`)
- **String**: Text values (e.g., `"#", "schematic"`)
- **List**: Comma-separated values (e.g., `dirt,cobblestone,stone`)
- **Map**: Key-value mappings (e.g., `stone->cobblestone,andesite`)
- **Color**: RGB color values or color names
- **Rotation/Mirror**: Enum values (e.g., `NONE`, `CLOCKWISE_90`)

## Notes

- Settings marked as `@JavaOnly` can only be modified programmatically via the API
- Some settings have dependencies on others (e.g., `allowParkourAscend` requires `allowParkour`)
- Default values are shown for each setting in the detailed documentation
- Settings are case-insensitive when using commands

## Statistics

- **Total Settings**: {total}
- **User-Configurable**: {user_configurable}
- **Java-Only (API)**: {java_only}
""".format(
        total=len(settings),
        user_configurable=len([s for s in settings if not s.is_java_only]),
        java_only=len([s for s in settings if s.is_java_only])
    )

    with open(output_dir / 'SETTINGS.md', 'w', encoding='utf-8') as f:
        f.write(content)


def generate_category_file(category: str, category_settings: List[Setting], output_dir: Path):
    """Generate a markdown file for a specific category."""
    category_names = {
        'basic': 'Basic Permissions & Actions',
        'pathing': 'Pathfinding & Movement',
        'mining': 'Mining',
        'building': 'Building & Schematics',
        'farming': 'Farming',
        'rendering': 'Rendering & Visual',
        'chat': 'Chat & Control',
        'performance': 'Performance & Caching',
        'elytra': 'Elytra',
        'advanced': 'Advanced/Internal'
    }

    category_title = category_names.get(category, category.title())

    content = f"""# {category_title}

This document contains all settings related to {category_title.lower()}.

## Settings

"""

    # Sort settings alphabetically
    category_settings.sort(key=lambda s: s.name.lower())

    for setting in category_settings:
        if setting.is_java_only:
            continue  # Skip Java-only settings in user docs

        content += f"### `{setting.name}`\n\n"
        content += f"**Type**: `{setting.type}`  \n"
        content += f"**Default**: `{setting.default_value}`  \n"

        if setting.is_deprecated:
            content += "**Status**: ⚠️ Deprecated  \n"

        content += "\n"

        desc = format_description(setting.description)
        if desc:
            # If description has paragraph breaks, preserve them
            if '\n\n' in desc:
                paragraphs = desc.split('\n\n')
                for para in paragraphs:
                    para = para.strip()
                    if para:
                        content += f"{para}\n\n"
            else:
                content += f"{desc}\n\n"
        else:
            content += "*No description available.*\n\n"

        content += "---\n\n"

    # Add back to index link
    content += "\n[← Back to Settings Index](SETTINGS.md)\n"

    filename = f'SETTINGS_{category.upper()}.md' if category != 'basic' else 'SETTINGS_BASIC.md'
    with open(output_dir / filename, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    """Main entry point."""
    # Determine paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    settings_file = project_root / 'src' / 'api' / 'java' / 'baritone' / 'api' / 'Settings.java'
    docs_dir = project_root / 'docs'

    if not settings_file.exists():
        print(f"Error: Settings.java not found at {settings_file}")
        return 1

    # Create docs directory if it doesn't exist
    docs_dir.mkdir(exist_ok=True)

    print(f"Parsing {settings_file}...")
    settings = parse_java_file(settings_file)
    print(f"Found {len(settings)} settings")

    # Categorize settings
    categorized = {}
    for setting in settings:
        category = categorize_setting(setting)
        if category not in categorized:
            categorized[category] = []
        categorized[category].append(setting)

    print(f"Categorized into {len(categorized)} groups:")
    for cat, cat_settings in sorted(categorized.items()):
        print(f"  {cat}: {len(cat_settings)} settings")

    # Generate main index
    print("Generating SETTINGS.md...")
    generate_main_index(settings, docs_dir)

    # Generate category files
    for category, cat_settings in categorized.items():
        print(f"Generating SETTINGS_{category.upper()}.md...")
        generate_category_file(category, cat_settings, docs_dir)

    print(f"\nDocumentation generated successfully in {docs_dir}/")
    print("\nFiles generated:")
    print("  - SETTINGS.md (main index)")
    for category in sorted(categorized.keys()):
        filename = f'SETTINGS_{category.upper()}.md' if category != 'basic' else 'SETTINGS_BASIC.md'
        print(f"  - {filename}")

    return 0


if __name__ == '__main__':
    exit(main())

