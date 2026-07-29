---
title: [EMF] Entity Model Features [Fabric & Forge]
---

**Entity Model Features** allows resource pack creators to add custom
models and animations to entities using OptiFine-style model definitions.
The mod supports custom entity models, animations, holograms, and various
rendering modes. It provides extensive compatibility with OptiFine resource
packs and includes performance optimizations for model rendering.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `entity_model_features.json`.

#### General Settings

- `logModelCreationData` (default: `false`)
  - Log model creation data to console. Useful for debugging model loading
    issues.

- `debugOnRightClick` (default: `false`)
  - Enable debug mode on right-click. When enabled, right-clicking entities
    shows debug information.

- `renderModeChoice` (default: `"NORMAL"`)
  - Render mode choice for entity models.

- `vanillaModelHologramRenderMode_2` (default: `"OFF"`)
  - Render mode for vanilla model holograms.

- `modelExportMode` (default: `"NONE"`)
  - Model export mode. Set to export models for debugging.

- `modelUpdateFrequency` (default: `"Average"`)
  - Frequency at which models are updated.

- `animationLODDistance` (default: `20`)
  - Distance at which animation level of detail (LOD) is applied.

- `retainDetailOnLowFps` (default: `true`)
  - Retain model detail when FPS is low.

- `retainDetailOnLargerMobs` (default: `true`)
  - Retain model detail for larger mobs.

- `animationFrameSkipDuringIrisShadowPass` (default: `true`)
  - Skip animation frames during Iris shadow pass for performance.

- `preventFirstPersonHandAnimating` (default: `false`)
  - Prevent first-person hand animations.

- `onlyClientPlayerModel` (default: `false`)
  - Only apply custom models to the client player.

- `doubleChestAnimFix` (default: `true`)
  - Fix double chest animation issues.

- `resetPlayerModelEachRender` (default: `true`)
  - Reset player model each render frame.

- `resetPlayerModelEachRender_v2` (default: `true`)
  - Reset player model each render frame (v2).

- `onlyDebugRenderOnHover` (default: `false`)
  - Only show debug rendering when hovering over entities.

- `enforceOptifineSubFoldersVariantOnly` (default: `true`)
  - Enforce OptiFine subfolder variant requirements.

- `enforceOptiFineAnimSyntaxLimits` (default: `true`)
  - Enforce OptiFine animation syntax limits.

- `allowOptifineFallbackProperties` (default: `true`)
  - Allow OptiFine fallback properties.

- `showReloadErrorToast` (default: `true`)
  - Show error toast notifications when reloading resources.

#### Override Settings

- `entityRenderModeOverrides` (default: `{}`)
  - Override render modes for specific entities.

- `entityVanillaHologramOverrides` (default: `{}`)
  - Override vanilla hologram settings for specific entities.

- `modelsNamesDisabled` (default: `[]`)
  - List of model names to disable.

- `allowEBEModConfigModify` (default: `true`)
  - Allow Entity Block Entity mod config modifications.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

