---
title: Structurize
categories:
  - world-structures
  - server-utility
  - cosmetic
---

[Website](https://www.curseforge.com/minecraft/mc-mods/structurize) | [Issues](https://github.com/ldtteam/structurize/issues) | [Source](https://github.com/ldtteam/structurize)

Client/Server: both

**Structurize** provides tools for creating, scanning, and placing
blueprints and schematics in Minecraft. The mod is used by MineColonies
for building placement but can also be used standalone for copying and
pasting structures. It includes a scan tool for creating blueprints, a
build tool for placing them, and configurable rendering and gameplay
options.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config files.

#### Client Settings

These settings are configured in `structurize-client.toml`.

- `blueprint.renderer.render_placeholders_nice` (default: `false`)
  - If disabled, show placeholders as normal blocks. If enabled, render:
    any (light) -> nothing, fluid (blue) -> dimension default fluid, solid
    (brown) -> worldgen block, tag (transparent) -> content block. Fluid
    and solid only work in singleplayer/for LAN owner, else it's just best
    guess. Currently without auto-updating.

- `blueprint.renderer.share_previews` (default: `false`)
  - Enabling this will send most of your active previews to nearby
    players. When enabled, other players can see your blueprint previews.

- `blueprint.renderer.see_shared_previews` (default: `false`)
  - Once enabled, you will see previews from other players within sensible
    distance. When enabled, you can see blueprint previews shared by other
    players.

- `blueprint.renderer.light_level` (default: `15`)
  - Light level for blueprint rendering. `-1` for same as current vanilla
    world, `0` to `15` (min to max) for static light level. Range: `-1` to
    `15`.

- `blueprint.renderer.transparency` (default: `-1.0`)
  - From `0` (transparent) to `1` (opaque). ALPHA FEATURE, reported bugs
    may not receive fix. (Minus values also mean disabled). Range: `-1.0`
    to `1.0`.

- `gameplay.scan_tool_scrolling` (default: `false`)
  - Sneak+scroll on the hotbar switches scan tool slots. When enabled,
    you can scroll through scan tool slots while sneaking.

#### Server Settings

These settings are configured in `structurize-server.toml`.

- `gameplay.ignoreSchematicsFromJar` (default: `false`)
  - Should the default schematics be ignored (from the jar)? When enabled,
    default schematics included with the mod are not loaded.

- `gameplay.allowPlayerSchematics` (default: `false`)
  - Should player-made schematics be allowed? When enabled, players can
    create and use custom schematics.

- `gameplay.maxOperationsPerTick` (default: `1000`)
  - Max world operations per tick (max blocks to place, remove, or
    replace). Higher values allow faster building but may cause lag.
    Range: `0` to `100000`.

- `gameplay.maxCachedChanges` (default: `50`)
  - Max amount of undos saved. A higher number requires more memory.
    Range: `0` to `250`.

- `gameplay.maxCachedSchematics` (default: `100`)
  - Max amount of schematics to be cached on the server. Range: `0` to
    `100000`.

- `gameplay.maxBlocksChecked` (default: `1000`)
  - Max amount of blocks checked by a possible worker. Range: `0` to
    `100000`.

- `gameplay.schematicBlockLimit` (default: `100000`)
  - How many blocks at most can be inside one scanned blueprint. Range:
    `1000` to `1000000`.

- `gameplay.iteratorType` (default: `"default"`)
  - Currently supports `'default'`, `'inwardcircle'`, `'hilbert'`,
    `'random'` and `'inwardcircleheight1'` to `'inwardcircleheight4'`.
    Determines the order in which blocks are placed when building.

- `teleport.teleportAllowed` (default: `true`)
  - If creative-mode players can use the scan tool to teleport to/from
    their builds. When enabled, creative players can teleport using the
    scan tool.

- `teleport.teleportBuildDirection` (default: `"SOUTH"`)
  - When teleporting to a build, land on this side of it. Allowed values:
    `DOWN`, `UP`, `NORTH`, `SOUTH`, `WEST`, `EAST`.

- `teleport.teleportBuildDistance` (default: `3`)
  - When teleporting to a build, land this far away from it. Range: `1` to
    `16`.

- `teleport.teleportSafety` (default: `true`)
  - Allow teleporting a little distance away if the landing area is
    blocked; disable to teleport exactly to target. When enabled, the mod
    finds a safe landing spot near the target.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.20.1-0.1.2
- harleycolonies-1.21.1

