---
title: Explorer's Compass
categories:
  - world-structures
  - adventure-rpg
  - map-information
  - armor-weapons-tools
---

[Website](https://www.curseforge.com/minecraft/mc-mods/explorers-compass) | [Issues](https://github.com/MattCzyr/ExplorersCompass/issues) | [Source](https://github.com/MattCzyr/ExplorersCompass)

Client/Server: both

**Explorer's Compass** helps players locate structures in Minecraft by
providing a compass that can search for and point to various structures
like villages, strongholds, monuments, and more. The mod displays structure
information on the HUD, including coordinates and distance, making
exploration easier and more efficient. It supports both vanilla and modded
structures and includes configurable search parameters.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config files.

#### Client Settings

These settings are configured in `explorerscompass-client.toml`.

- `Client.displayWithChatOpen` (default: `true`)
  - Displays Explorer's Compass information on the HUD even while chat is
    open. When enabled, structure information remains visible when the chat
    window is open.

- `Client.translateStructureNames` (default: `true`)
  - Attempts to translate structure names before fixing the unlocalized
    names. Translations may not be available for all structures. When
    enabled, structure names are displayed in the player's language when
    possible.

- `Client.overlayLineOffset` (default: `1`)
  - The line offset for information rendered on the HUD. This controls
    the vertical spacing of the overlay text. Range: `0` to `50`.

- `Client.overlaySide` (default: `"LEFT"`)
  - The side for information rendered on the HUD. Allowed values: `LEFT`,
    `RIGHT`. This determines which side of the screen the structure
    information overlay appears on.

#### General Settings

These settings are configured in `explorerscompass-common.toml`.

- `General.allowTeleport` (default: `true`)
  - Allows a player to teleport to a located structure when in creative
    mode, opped, or in cheat mode. When enabled, players with appropriate
    permissions can instantly teleport to structures they've located.

- `General.displayCoordinates` (default: `true`)
  - Allows players to view the precise coordinates and distance of a
    located structure on the HUD, rather than relying on the direction the
    compass is pointing. When enabled, exact coordinates and distance are
    displayed.

- `General.maxRadius` (default: `10000`)
  - The maximum radius that will be searched for a structure, in blocks.
    Raising this value will increase search accuracy but will potentially
    make the process more resource intensive. Range: `0` to `1000000`.

- `General.maxSamples` (default: `100000`)
  - The maximum number of samples to be taken when searching for a
    structure. Higher values provide more accurate results but use more
    resources. Range: `0` to `100000000`.

- `General.structureBlacklist` (default: `[]`)
  - A list of structures that the compass will not display in the GUI and
    will not be able to search for. Wildcard character `*` can be used to
    match any number of characters, and `?` can be used to match one
    character. Example: `["minecraft:stronghold", "minecraft:endcity",
    "minecraft:*village*"]`.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1
- harleycolonies-1.20.1-0.1.2

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.20.1-0.1.2
- harleycolonies-1.21.1

