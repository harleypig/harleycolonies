---
title: [ETF] Entity Texture Features - [Fabric & Forge]
---



Client/Server: client

**Entity Texture Features** allows resource pack creators to add custom
textures, emissive textures, and texture variations to entities using
OptiFine-style texture definitions. The mod supports custom entity
textures, emissive overlays, enchanted textures, armor and trim textures,
skin features, blinking animations, and various rendering optimizations.
It provides extensive compatibility with OptiFine resource packs.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `entity_texture_features.json`.

#### General Settings

- `enableCustomTextures` (default: `true`)
  - Enable custom entity textures from resource packs.

- `enableCustomBlockEntities` (default: `true`)
  - Enable custom block entity textures.

- `textureUpdateFrequency_V2` (default: `"Fast"`)
  - Frequency at which textures are updated.

- `enableEmissiveTextures` (default: `true`)
  - Enable emissive (glowing) textures for entities.

- `enableEnchantedTextures` (default: `true`)
  - Enable enchanted texture overlays.

- `enableEmissiveBlockEntities` (default: `true`)
  - Enable emissive textures for block entities.

- `emissiveRenderMode` (default: `"DULL"`)
  - Render mode for emissive textures.

- `alwaysCheckVanillaEmissiveSuffix` (default: `true`)
  - Always check for vanilla emissive texture suffixes.

- `enableArmorAndTrims` (default: `true`)
  - Enable custom armor and trim textures.

#### Skin Features

- `skinFeaturesEnabled` (default: `true`)
  - Enable skin features like transparency and custom textures.

- `skinTransparencyMode` (default: `"ETF_SKINS_ONLY"`)
  - Mode for skin transparency handling.

- `skinTransparencyInExtraPixels` (default: `true`)
  - Enable transparency in extra skin pixels.

- `skinFeaturesEnableTransparency` (default: `true`)
  - Enable transparency features for skins.

- `skinFeaturesEnableFullTransparency` (default: `false`)
  - Enable full transparency for skins.

- `tryETFTransparencyForAllSkins` (default: `false`)
  - Try ETF transparency for all skins, not just ETF-enabled ones.

- `enableEnemyTeamPlayersSkinFeatures` (default: `true`)
  - Enable skin features for enemy team players.

#### Animation Settings

- `enableBlinking` (default: `true`)
  - Enable blinking animations for entities.

- `blinkFrequency` (default: `150`)
  - Frequency of blinking animations in ticks.

- `blinkLength` (default: `1`)
  - Length of blink animation in ticks.

#### Performance Settings

- `advanced_IncreaseCacheSizeModifier` (default: `1.0`)
  - Modifier for cache size. Higher values use more memory but may improve
    performance.

- `debugLoggingMode` (default: `"None"`)
  - Debug logging mode. Set to enable detailed logging.

- `logTextureDataInitialization` (default: `false`)
  - Log texture data initialization.

- `hideConfigButton` (default: `false`)
  - Hide the config button in-game.

- `configButtonLoc` (default: `"BOTTOM_RIGHT"`)
  - Location of the config button on screen.

#### Compatibility Settings

- `optifine_limitRandomVariantGapsBy10` (default: `true`)
  - Limit random variant gaps by 10 for OptiFine compatibility.

- `optifine_allowWeirdSkipsInTrueRandom` (default: `true`)
  - Allow weird skips in true random for OptiFine compatibility.

- `optifine_preventBaseTextureInOptifineDirectory` (default: `true`)
  - Prevent base textures in OptiFine directory.

- `illegalPathSupportMode` (default: `"None"`)
  - Support mode for illegal file paths.

- `disableVanillaDirectoryVariantTextures` (default: `false`)
  - Disable variant textures in vanilla directory.

- `use3DSkinLayerPatch` (default: `true`)
  - Use 3D skin layer patch.

- `enableFullBodyWardenTextures` (default: `true`)
  - Enable full body textures for Wardens.

#### Override Settings

- `entityEmissiveOverrides` (default: `{}`)
  - Override emissive settings for specific entities.

- `propertiesDisabled` (default: `[]`)
  - List of properties to disable.

- `propertyInvertUpdatingOverrides` (default: `[]`)
  - Properties to invert updating for.

- `entityRandomOverrides` (default: `{}`)
  - Override random texture selection for specific entities.

- `entityEmissiveBrightOverrides` (default: `{}`)
  - Override emissive brightness for specific entities.

- `entityRenderLayerOverrides` (default: `{}`)
  - Override render layers for specific entities.

- `entityLightOverrides` (default: `{}`)
  - Override lighting for specific entities.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.20.1-0.1.2
- harleycolonies-1.21.1

