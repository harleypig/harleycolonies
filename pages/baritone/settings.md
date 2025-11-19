# Baritone Settings Documentation

This document provides a comprehensive reference for all Baritone settings, organized by capability.

Settings can be modified using the `#set` command in-game, or by editing the `settings.txt` file in your `minecraft/baritone/` directory.

## Quick Links

- [Basic Permissions & Actions](settings_basic) - Core permissions for breaking, placing, sprinting, etc.
- [Pathfinding & Movement](settings_pathing) - Pathfinding algorithm, movement types, and path optimization
- [Mining](settings_mining) - Mining behavior, ore detection, and mining-related settings
- [Building & Schematics](settings_building) - Schematic building, block substitution, and builder behavior
- [Farming](settings_farming) - Crop farming and replanting settings
- [Rendering & Visual](settings_rendering) - Visual rendering, colors, and display options
- [Chat & Control](settings_chat) - Chat commands, prefixes, and control settings
- [Performance & Caching](settings_performance) - Chunk caching, performance optimization, and memory management
- [Elytra](settings_elytra) - Elytra flight and pathfinding settings
- [Advanced/Internal](settings_advanced) - Advanced A* settings, internal optimizations, and debugging

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

- **Total Settings**: 226
- **User-Configurable**: 226
- **Java-Only (API)**: 0
