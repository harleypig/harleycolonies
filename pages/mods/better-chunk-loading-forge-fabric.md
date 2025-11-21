---
title: Better chunk loading[Forge/Fabric]
---



Client/Server: server

**Better chunk loading[Forge/Fabric]** enhances Minecraft's chunk loading
performance by predicting player movement and pre-loading chunks
asynchronously. This mod increases overall chunk loading speed and reduces
server load by dynamically adjusting the chunk loading area based on the
player's movement speed. The mod provides configurable prediction areas,
smart chunk loading, and various optimization features to improve
performance. It requires the Cupboard dependency and is only required on
the server side.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file.

#### Prediction Settings

- `enablePrediction.enablePrediction` (default: `true`)
  - Enables predictive chunk loading, which predicts player movement and
    preloads an area in the movement direction. When enabled, the mod
    anticipates where players are likely to move and loads chunks ahead of
    them.

- `predictionLoadingSpeed.predictionLoadingSpeed` (default: `1.0`)
  - Sets a modifier to prediction area loading speed. Increasing the value
    increases the speed at which chunks load around the player. Note that
    faster loading also means higher impact on TPS. Range: `0.01` to `10.0`.

- `predictionarea.predictionarea` (default: `7`)
  - Size of the area marked for preloading in chunks. This determines how
    many chunks ahead of the player will be preloaded. Maximum: `32`,
    minimum: `2`.

#### Smart Chunk Loading

- `enableSmartChunkLoading.enableSmartChunkLoading` (default: `true`)
  - Enables smart chunk loading around the player, which dynamically loads
    chunks around the player based on movement speed. This feature adjusts
    the vanilla chunk loading area to match the player's speed, reducing
    unnecessary server load.

- `smartChunkLoadingSpeed.smartChunkLoadingSpeed` (default: `1.0`)
  - Sets a modifier to smart chunk loading speed. Increasing the value
    increases the speed at which chunks load around the player. Note that
    faster loading also means higher impact on TPS. Range: `0.01` to `10.0`.

#### Optimization Features

- `preventWalkUnloaded.preventWalkUnloaded` (default: `true`)
  - Prevents players from moving into unloaded areas on the server side.
    This prevents the server from stalling and force-loading chunks when
    players walk into unloaded areas.

- `enableSmartPostProcessing.enableSmartPostProcessing` (default: `true`)
  - Enables smart post processing, which slightly improves general chunk
    loading speed by waiting with post processing (e.g., fluid updates)
    until neighboring chunks are loaded.

- `enableFasterChunkTasks.enableFasterChunkTasks` (default: `false`)
  - Enables faster world generation tasks. When enabled, world generation
    tasks are processed more quickly, which may improve chunk loading speed
    but could impact server performance.

- `optimizeWaiting.optimizeWaiting` (default: `true`)
  - Optimizes the time the world is stalled while waiting for a chunk to
    load. This reduces server lag when chunks are being loaded.

#### Debug Settings

- `debugLogging.debugLogging` (default: `false`)
  - Enables debug logging to show chunk loading changes. When enabled, the
    mod will log detailed information about chunk loading operations, which
    can be useful for troubleshooting performance issues.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

