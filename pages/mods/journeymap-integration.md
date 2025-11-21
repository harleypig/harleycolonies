---
title: JourneyMap Integration
categories:
  - mc-addons
  - map-information
---

[Website](https://www.curseforge.com/minecraft/mc-mods/journeymap-integration) | [Issues](https://github.com/frank89722/JourneyMapIntegration/issues) | [Source](https://github.com/frank89722/JourneyMapIntegration)

Client/Server: both

**JourneyMap Integration** provides integration between JourneyMap and
various other mods, allowing waypoints and markers to be shared between
systems. The mod integrates with FTB Chunks, Waystones, and provides
configurable waypoint messaging. It also includes options for managing
JourneyMap default configurations.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `jmi-client.toml`.

#### FTB Chunks Integration

- `FTBChunks.ftbChunks` (default: `true`)
  - Enable FTBChunks Integration. When enabled, the mod integrates with
    FTB Chunks for claimed chunk overlays.

- `FTBChunks.claimedChunkOverlayOpacity` (default: `0.17499999701976776`)
  - Opacity of the claimed chunk overlay on the map. Range: `0.0` to `1.0`.

- `FTBChunks.disableFTBFunction` (default: `true`)
  - Disable conflict functions for FTBChunks (MiniMap, Waypoint beam, Death
    waypoint). When enabled, conflicting features are disabled to prevent
    overlap.

#### Waystones Integration

- `Waystones.waystones` (default: `true`)
  - Enable Waystones Integration. When enabled, waystones appear as
    markers on the JourneyMap.

- `Waystones.wayStoneMarkerColor` (default: `16777215`)
  - The color code for Waystone marker. You can generate the color code
    from https://www.mathsisfun.com/hexadecimal-decimal-colors.html. Range:
    `0` to `16777215`.

#### Waypoint Message Settings

- `WaypointMessage.waypointMessageBlocks` (default: `[]`)
  - List of block IDs and tags for WaypointMessage. Example:
    `["#forge:ores/diamond", "minecraft:diamond_block"]`. When blocks in
    this list are found, waypoint messages are displayed.

- `WaypointMessage.emptyHandOnly` (default: `true`)
  - Only show waypoint messages when holding an empty hand. When enabled,
    messages only appear when not holding any items.

#### JourneyMap Default Config

- `JourneyMap Default Config.defaultConfigVersion` (default: `-1`)
  - When local JM default config version is older than
    `defaultConfigVersion` it will copy everything under
    `/config/jmdefaultconfig/` to `/journeymap/` and replace the existing
    files. Set to `-1` to disable. Range: greater than `-1`.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.20.1-0.1.2
- harleycolonies-1.21.1

