# Documentation Generators

This directory contains automatically generated documentation files. The source files are generated from the Baritone source code using Python scripts located in the `scripts/` directory.

## Generator Scripts

### `scripts/generate_settings_docs.py`

Generates comprehensive settings documentation from `src/api/java/baritone/api/Settings.java`.

**What it does:**
- Parses all settings from the Settings.java source file
- Extracts setting names, types, default values, and JavaDoc descriptions
- Categorizes settings into capability groups
- Generates markdown documentation files organized by category

**Generated files:**
- `docs/SETTINGS.md` - Main index with overview and usage instructions
- `docs/SETTINGS_BASIC.md` - Basic permissions & actions
- `docs/SETTINGS_PATHING.md` - Pathfinding & movement
- `docs/SETTINGS_MINING.md` - Mining-related settings
- `docs/SETTINGS_BUILDING.md` - Building & schematics
- `docs/SETTINGS_FARMING.md` - Farming settings
- `docs/SETTINGS_RENDERING.md` - Rendering & visual
- `docs/SETTINGS_CHAT.md` - Chat & control
- `docs/SETTINGS_PERFORMANCE.md` - Performance & caching
- `docs/SETTINGS_ELYTRA.md` - Elytra settings
- `docs/SETTINGS_ADVANCED.md` - Advanced/internal settings

**Usage:**
```bash
# From the baritone repository root
python3 scripts/generate_settings_docs.py
```

### `scripts/generate_commands_docs.py`

Generates comprehensive command documentation from command source files in `src/main/java/baritone/command/defaults/`.

**What it does:**
- Parses all command classes from the defaults package
- Extracts command names, aliases, descriptions, and usage information
- Handles special cases:
  - `ExecutionControlCommands.java` (anonymous Command classes)
  - `CommandAlias` instances from `DefaultCommands.java`
- Categorizes commands into capability groups
- Generates markdown documentation files organized by category

**Generated files:**
- `docs/COMMANDS.md` - Main index with overview and usage instructions
- `docs/COMMANDS_PATHFINDING.md` - Pathfinding & navigation commands
- `docs/COMMANDS_MINING.md` - Mining & resource commands
- `docs/COMMANDS_BUILDING.md` - Building commands
- `docs/COMMANDS_FARMING.md` - Farming commands
- `docs/COMMANDS_FOLLOWING.md` - Following & entity commands
- `docs/COMMANDS_WAYPOINTS.md` - Waypoint commands
- `docs/COMMANDS_EXPLORATION.md` - Exploration commands
- `docs/COMMANDS_RENDERING.md` - Rendering commands
- `docs/COMMANDS_SYSTEM.md` - System & control commands
- `docs/COMMANDS_ELYTRA.md` - Elytra commands
- `docs/COMMANDS_SCHEMATIC.md` - Schematic tool commands

**Usage:**
```bash
# From the baritone repository root
python3 scripts/generate_commands_docs.py
```

## Requirements

Both scripts require:
- Python 3.6 or higher
- Standard library only (no external dependencies)
- To be run from the baritone repository root directory

## When to Regenerate

Regenerate the documentation when:
- New settings or commands are added to the source code
- Existing settings or commands are modified
- Descriptions or usage information changes
- Before committing changes that affect settings or commands

## Notes

- Both scripts automatically create the `docs/` directory if it doesn't exist
- Generated files are overwritten each time the scripts run
- The scripts parse Java source files using regex patterns
- Settings marked as `@JavaOnly` are excluded from user-facing documentation
- Commands marked as hidden (`hiddenFromHelp()`) are excluded from documentation
- Command aliases are included and shown together with their primary command names

