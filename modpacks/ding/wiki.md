---
title: Ding (Forge)
---

**Ding** plays a sound notification when Minecraft finishes loading,
providing audio feedback that the game is ready to play. The mod can also
play sounds when resources are reloaded or when connecting to a server.
This is particularly useful for players who want to know when the game has
finished loading without constantly checking the screen.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `ding.toml`.

#### Load Sound Settings

- `load.playOnLoad` (default: `true`)
  - Play sound when the game loads. When enabled, a sound plays when
    Minecraft finishes loading.

- `load.name` (default: `"entity.experience_orb.pickup"`)
  - Resource location based name of the sound file to play when Minecraft
    finishes loading. Examples: `"ui.button.click"` or
    `"entity.experience_orb.pickup"`. This can also be a mod sound if the
    mod is installed, e.g., `modname:modsound.boing`. If you want to use
    external sounds, consider looking into mods that add resources.

- `load.volume` (default: `0.25`)
  - Volume of the sound (when Minecraft loads). Range: `0.0` to `10.0`.

- `load.pitch` (default: `1.0`)
  - Pitch of the sound (when Minecraft loads). Range: `0.0` to `10.0`.

- `load.category` (default: `"master"`)
  - Sound category for the sound played when Minecraft finishes loading.
    Examples: `"ambient"` or `"music"`. Defaults to `"master"` if Ding
    cannot find your category.

#### Resources Reload Sound Settings

- `resourcesReload.playOnResourcesReload` (default: `true`)
  - Play sound when resources complete reloading. Requires game to be
    restarted when changing this option.

- `resourcesReload.nameResourcesReload` (default: `"entity.experience_orb.pickup"`)
  - Resource location based name of the sound file to play when resources
    complete reloading. See `load.name` for format details.

- `resourcesReload.volumeResourcesReload` (default: `0.25`)
  - Volume of the sound (when resources complete reloading). Range: `0.0`
    to `10.0`.

- `resourcesReload.pitchResourcesReload` (default: `1.0`)
  - Pitch of the sound (when resources complete reloading). Range: `0.0` to
    `10.0`.

- `resourcesReload.categoryResourcesReload` (default: `"master"`)
  - Sound category for the sound played when resources complete reloading.
    See `load.category` for details.

#### World Load Sound Settings

- `world.playOnWorld` (default: `false`)
  - Play sound when the world loads after connecting to a server. Requires
    game to be restarted when changing this option.

- `world.nameWorld` (default: `"entity.experience_orb.pickup"`)
  - Resource location based name of the sound file to play when the world
    finishes loading (after connecting to a server). See `load.name` for
    format details.

- `world.volumeWorld` (default: `0.25`)
  - Volume of the sound (when the world loads after connecting to a
    server). Range: `0.0` to `10.0`.

- `world.pitchWorld` (default: `1.0`)
  - Pitch of the sound (when the world loads after connecting to a
    server). Range: `0.0` to `10.0`.

- `world.categoryWorld` (default: `"master"`)
  - Sound category for the sound played when the world finishes loading.
    See `load.category` for details.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

