---
title: AppleSkin
categories:
  - mc-food
  - map-information
---

[Website](https://www.curseforge.com/minecraft/mc-mods/appleskin) | [Issues](https://github.com/squeek502/AppleSkin/issues) | [Source](https://github.com/squeek502/AppleSkin)

Client/Server: client

**AppleSkin** is a client-side mod that enhances food and hunger
mechanics by displaying detailed information in tooltips and HUD overlays.
It shows hunger and saturation values for food items, displays saturation
and exhaustion levels on the hunger bar, and provides visual feedback
when holding food. The mod also adds food statistics to the F3 debug
overlay.

### Configuration

Below are the available options and their defaults. Paths and lists use
the same names as in the mod's config file.

#### Tooltip Settings

- `showFoodValuesInTooltip` (default: `true`)
  - Shows the hunger and saturation values of food in its tooltip while
    holding SHIFT.

- `showFoodValuesInTooltipAlways` (default: `true`)
  - Shows the hunger and saturation values of food in its tooltip
    automatically (without needing to hold SHIFT).

#### HUD Overlay Settings

- `showSaturationHudOverlay` (default: `true`)
  - Shows your current saturation level overlayed on the hunger bar.

- `showFoodValuesHudOverlay` (default: `true`)
  - Shows the hunger (and saturation if `showSaturationHudOverlay` is
    `true`) that would be restored by food you are currently holding.

- `showFoodValuesHudOverlayWhenOffhand` (default: `true`)
  - Enables the hunger/saturation/health overlays for food in your
    off-hand.

- `showFoodExhaustionHudUnderlay` (default: `true`)
  - Shows your food exhaustion as a progress bar behind the hunger bars.

- `showFoodHealthHudOverlay` (default: `true`)
  - Shows estimated health restored by food on the health bar.

- `showVanillaAnimationsOverlay` (default: `true`)
  - Health/hunger overlay will shake to match Minecraft's icon animations.

- `maxHudOverlayFlashAlpha` (default: `0.65`, range: 0.0–1.0)
  - Alpha value of the flashing icons at their most visible point (1.0 =
    fully opaque, 0.0 = fully transparent).

#### Debug Overlay Settings

- `showFoodStatsInDebugOverlay` (default: `true`)
  - Adds a line that shows your hunger, saturation, and exhaustion level
    in the F3 debug overlay.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.20.1-0.1.2
- harleycolonies-1.21.1

