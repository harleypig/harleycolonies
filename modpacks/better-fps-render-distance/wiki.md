---
title: Better Fps - Render Distance[Forge]
---

**Better Fps - Render Distance** enhances Minecraft's performance by
optimizing chunk rendering. The mod replaces Minecraft's default square
render distance with a 3D circular radius, reducing the number of chunks
rendered and improving FPS. It allows adjustable horizontal and vertical
scaling of the render distance, providing fine-grained control over
rendering performance. The mod is client-side only and works by stretching
the chunk render distance sphere in different dimensions.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `betterfpsdist.json`.

#### Render Distance Scaling

- `verticalScaling.verticalScaling` (default: `2.0`)
  - The amount by which the chunk render distance sphere is stretched
    vertically. A higher value renders more chunks above and below the
    player, improving visibility but reducing performance. Range: `0.5` to
    `10.0`.

- `horizontalScaling.horizontalScaling` (default: `1.0`)
  - The amount by which the chunk render distance sphere is stretched
    horizontally. A higher value renders more chunks in the horizontal
    plane, improving visibility but reducing performance. Range: `0.05` to
    `2.0`.

#### Entity Rendering

- `affectEntities.affectEntities` (default: `true`)
  - Enables the distance stretch to also affect entity rendering. When
    enabled, entities follow the same stretched render distance as chunks.
    When disabled, entities use the standard render distance regardless of
    the scaling settings.

#### Debug Settings

- `debugMode.debugMode` (default: `false`)
  - Enables debug mode, which displays how many sections are being hidden.
    A section is an area of 16x16x16 blocks. This can be useful for
    fine-tuning render distance settings to balance performance and
    visibility.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

