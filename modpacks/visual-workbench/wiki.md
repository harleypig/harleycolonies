---
title: Visual Workbench
---

**Visual Workbench** enhances the crafting table by displaying crafting
ingredients visually on the table surface. The mod shows items placed on
the crafting grid as 3D models on the table, rotates them to face the
closest player, and can display the crafting result. This provides visual
feedback for crafting operations and makes the crafting process more
immersive.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config files.

#### Client Settings

These settings are configured in `visualworkbench-client.toml`.

- `rotate_ingredients` (default: `"CLOSEST_PLAYER"`)
  - Rotate crafting table contents so they always face the closest player.
    Allowed values: `CLOSEST_PLAYER` (rotate to face closest player),
    `CRAFTING_PLAYER` (rotate to face the player using the table),
    `NEVER` (no rotation).

- `flat_rendering` (default: `false`)
  - Makes crafting table contents lay flat on the table instead of
    floating above. When enabled, items appear to sit directly on the
    crafting table surface.

- `render_result` (default: `true`)
  - Render the result of the crafting operation in addition to crafting
    table contents. When enabled, the crafted item is displayed on the
    table along with the ingredients.

#### Common Settings

These settings are configured in `visualworkbench-common.toml`.

- `disable_vanilla_workbench` (default: `true`)
  - Leftover vanilla crafting tables in a world become unusable until they
    are broken and replaced. When enabled, vanilla crafting tables must be
    replaced with Visual Workbench crafting tables to function.

- `convert_vanilla_workbench_during_world_gen` (default: `true`)
  - Replace vanilla crafting tables created in structures during world
    generation. Does not affect already generated blocks. When enabled,
    structures spawn with Visual Workbench crafting tables instead of
    vanilla ones.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

