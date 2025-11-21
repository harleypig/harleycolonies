---
title: Default Options
categories:
  - mc-miscellaneous
---

[Website](https://www.curseforge.com/minecraft/mc-mods/default-options) | [Issues](https://github.com/ModdingForBlockheads/DefaultOptions/issues) | [Source](https://github.com/ModdingForBlockheads/DefaultOptions)

Client/Server: both

**Default Options** allows modpack creators to set default game options
for newly created worlds. The mod can configure default difficulty settings
and optionally lock difficulty to prevent players from changing it. This is
useful for modpacks that want to ensure a consistent gameplay experience
across all players.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `defaultoptions-common.toml`.

#### Difficulty Settings

- `defaultDifficulty` (default: `"NORMAL"`)
  - The default difficulty selected for newly created worlds. Allowed
    values: `PEACEFUL`, `EASY`, `NORMAL`, `HARD`.

- `lockDifficulty` (default: `false`)
  - Set to `true` if the difficulty for new world's should be locked to
    the specific default. This cannot be unlocked by players without
    external tools! Probably a bad idea. Not recommended. When enabled,
    players cannot change the difficulty setting in-game.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.20.1-0.1.2
- harleycolonies-1.21.1

