---
title: Structure Compass
---



Client/Server: both

**Structure Compass** helps players locate structures in Minecraft by
providing a compass that can search for and point to various structures.
The mod supports both vanilla and modded structures and includes
configurable search parameters. Structures can be marked as explored to
prevent re-finding them, and the mod supports asynchronous searching for
better performance.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `structurecompass-common.toml`.

#### General Settings

- `general.compassRange` (default: `10000`)
  - Sets the range in blocks in which the structure compasses can locate
    structures. Range: greater than `0`.

- `general.locateUnexplored` (default: `false`)
  - Defines if the structure compass should only locate unexplored
    structures. A structure is tagged as explored when the compass is used
    to find it. When enabled, the compass will skip structures that have
    already been found.

- `general.locateAsync` (default: `false`)
  - Defines if the structure compass should locate structures
    asynchronously. When enabled, structure searching happens on a
    separate thread, preventing server lag during searches.

- `general.structureBlacklist` (default: `[""]`)
  - Defines which structures can't be searched with the Structure Compass.
    Supports wildcard `*`. Example: `'minecraft:*'` will blacklist
    anything in the minecraft domain.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

