---
title: Nature's Compass
---

**Nature's Compass** helps players locate specific biomes in Minecraft by
providing a compass that can search for and point to various biomes. The
mod displays biome information on the HUD, including coordinates and
distance, making biome exploration easier and more efficient. It supports
both vanilla and modded biomes and includes configurable search parameters
and teleportation options for creative/op players.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config files.

#### Client Settings

These settings are configured in `naturescompass-client.toml`.

- `Client.displayWithChatOpen` (default: `true`)
  - Displays Nature's Compass information even while chat is open. When
    enabled, biome information remains visible when the chat window is
    open.

- `Client.fixBiomeNames` (default: `true`)
  - Fixes biome names by adding missing spaces. Example: ForestHills
    becomes Forest Hills. When enabled, biome names are formatted with
    proper spacing for better readability.

- `Client.overlayLineOffset` (default: `1`)
  - The line offset for information rendered on the HUD. This controls
    the vertical spacing of the overlay text. Range: `0` to `50`.

- `Client.overlaySide` (default: `"LEFT"`)
  - The side for information rendered on the HUD. Allowed values: `LEFT`,
    `RIGHT`. This determines which side of the screen the biome
    information overlay appears on.

#### General Settings

These settings are configured in `naturescompass-common.toml`.

- `General.allowTeleport` (default: `true`)
  - Allows a player to teleport to a located biome when in creative mode,
    opped, or in cheat mode. When enabled, players with appropriate
    permissions can instantly teleport to biomes they've located.

- `General.displayCoordinates` (default: `true`)
  - Allows players to view the precise coordinates and distance of a
    located biome on the HUD, rather than relying on the direction the
    compass is pointing. When enabled, exact coordinates and distance are
    displayed.

- `General.radiusModifier` (default: `2500`)
  - `biomeSize * radiusModifier = maxSearchRadius`. Raising this value
    will increase search accuracy but will potentially make the process
    more resource intensive. Range: `0` to `1000000`.

- `General.sampleSpaceModifier` (default: `16`)
  - `biomeSize * sampleSpaceModifier = sampleSpace`. Lowering this value
    will increase search accuracy but will make the process more resource
    intensive. Range: `0` to `1000000`.

- `General.biomeBlacklist` (default: `[]`)
  - A list of biomes that the compass will not be able to search for,
    specified by resource location. The wildcard character `*` can be used
    to match any number of characters, and `?` can be used to match one
    character. Example: `["minecraft:savanna", "minecraft:desert",
    "minecraft:*ocean*"]`.

- `General.maxSamples` (default: `50000`)
  - The maximum number of samples to be taken when searching for a biome.
    Higher values provide more accurate results but use more resources.
    Range: `0` to `1000000`.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1
- harleycolonies-1.20.1-0.1.2

