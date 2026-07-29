---
title: Entity Culling Fabric/Forge
---

**Entity Culling** improves rendering performance by culling (not
rendering) entities and block entities that are not visible to the player.
The mod uses frustum culling and other optimization techniques to skip
rendering entities that are behind walls or outside the player's view,
significantly improving FPS, especially in areas with many entities or
block entities.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `entityculling.json`.

#### General Settings

- `configVersion` (default: `7`)
  - Configuration version. Used internally to track config format changes.

- `renderNametagsThroughWalls` (default: `true`)
  - Whether nametags should render through walls. When enabled, entity
    nametags are visible even when the entity itself is culled.

- `tracingDistance` (default: `128`)
  - Distance in blocks to trace for culling calculations. Higher values
    provide more accurate culling but use more resources.

- `debugMode` (default: `false`)
  - Enable debug mode for troubleshooting culling behavior.

- `sleepDelay` (default: `10`)
  - Delay in ticks before entities enter sleep mode when culled.

- `hitboxLimit` (default: `50`)
  - Maximum number of hitboxes to check for culling.

- `captureRate` (default: `5`)
  - Rate at which to capture entity visibility data.

- `tickCulling` (default: `true`)
  - Enable tick culling. When enabled, entities that are culled also skip
    their tick updates, improving performance.

- `disableF3` (default: `false`)
  - Disable F3 debug screen modifications.

- `skipEntityCulling` (default: `false`)
  - Skip entity culling entirely. When enabled, entities are never culled.

- `skipBlockEntityCulling` (default: `false`)
  - Skip block entity culling entirely. When enabled, block entities are
    never culled.

- `blockEntityFrustumCulling` (default: `true`)
  - Enable frustum culling for block entities. When enabled, block entities
    outside the camera frustum are not rendered.

#### Whitelists

- `blockEntityWhitelist` (default: `["create:rope_pulley",
  "botania:flame_ring", "minecraft:beacon", "create:hose_pulley",
  "betterend:eternal_pedestal", "botania:magic_missile",
  "botania:falling_star"]`)
  - List of block entities that should never be culled. These block
    entities will always be rendered regardless of visibility.

- `entityWhitelist` (default: `["botania:mana_burst", "drg_flares:drg_flares",
  "quark:soul_bead"]`)
  - List of entities that should never be culled. These entities will
    always be rendered regardless of visibility.

- `tickCullingWhitelist` (default: extensive list including boats, displays,
  contraptions, etc.)
  - List of entities that should never have their ticks culled, even if
    they are visually culled. These entities will continue to tick even
    when not rendered.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

