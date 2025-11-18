---
title: Style Packs
---

## Style Packs

All schematics must be organized into style packs, which are similar to
resource packs or data packs. Each style pack contains:

### The pack.json File

Every style pack requires a `pack.json` file with metadata:

```json
{
  "version": 1,
  "pack-format": 1,
  "desc": "Description of your style pack",
  "authors": ["Your Name"],
  "mods": [],
  "name": "Your Style Name",
  "icon": "icon.png"
}
```

Key requirements:

- `version`: Start at 1, increase for each release
- `pack-format`: Must be 1 currently
- `desc`: Description visible in build tool
- `authors`: Array of creator names
- `mods`: Array of required mod IDs (empty if vanilla only)
- `name`: Style pack display name
- `icon`: Optional icon filename

### Folder Structure

Style packs use a specific folder structure in `*/blueprints/yourstylename/`:

- `fundamentals/` - Core buildings (townhall, builder, etc.)
- `infrastructure/` - Roads, bridges, mineshafts
- `civilian/` - Residential and civic buildings
- `craftsmanship/` - Production buildings
- `combat/` - Military buildings
- `decorations/` - Non-functional decorations
  - `decorations/supplies/` - Supply camps and ships

Each folder can have `icon.png` and `icon_disabled.png` for the build tool interface.

