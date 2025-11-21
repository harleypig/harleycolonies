---
title: Just Enough Effect Descriptions (JEED)
categories:
  - map-information
  - mc-addons
---

[Website](https://www.curseforge.com/minecraft/mc-mods/just-enough-effect-descriptions-jeed) | [Issues](https://github.com/MehVahdJukaar/JustEnoughEffectDescriptions/issues) | [Source](https://github.com/MehVahdJukaar/JustEnoughEffectDescriptions)

Client/Server: both

**Just Enough Effect Descriptions (JEED)** enhances Minecraft's effect
tooltips by providing detailed descriptions of potion effects and status
effects in JEI/REI and other interfaces. The mod displays effect colors,
ingredients lists, and customizable tooltips, making it easier for players
to understand what effects do and how to obtain them. JEED integrates
seamlessly with JEI and REI, showing effect information alongside recipes
and items.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `jeed-client.toml`.

#### Display Settings

- `effect_color` (default: `true`)
  - Show effect colors in tooltip. When enabled, effect tooltips display
    the color associated with each effect, making them easier to identify
    visually.

- `effect_box` (default: `true`)
  - Draw a black box behind effect icons. When enabled, a black background
    is rendered behind effect icons, improving visibility and contrast
    against various backgrounds.

- `replace_vanilla_tooltips` (default: `true`)
  - Removes vanilla tooltips rendered when an effect renders small (square
    box). When enabled, JEED's enhanced tooltips replace the default
    vanilla tooltips for better information display.

#### Effect Filtering

- `ignore_derivative_potions` (default: `true`)
  - Ignore derivative potions (long and strong) when showing effects. When
    enabled, extended and enhanced versions of potions are not shown
    separately, reducing clutter in effect lists.

- `hidden_effects` (default: `[""]`)
  - A list of effects that should not be registered nor shown in JEI/REI.
    You can also use the 'hidden' mob_effect tag. Enter effect IDs to hide
    specific effects from display. Useful for hiding internal or debug
    effects.

#### Ingredients Display

- `ingredients_list` (default: `true`)
  - Show ingredients list along with an effect description. When enabled,
    tooltips display the items or ingredients needed to obtain each effect,
    helping players understand how to craft or obtain effects.

- `sort_ingredients` (default: `false`)
  - Sort ingredients list by their ID. When enabled, ingredients are sorted
    alphabetically by their item ID, providing a consistent ordering.

- `render_slots` (default: `false`)
  - Renders individual slots instead of a big one. Only works for REI. When
    enabled, REI displays ingredients in separate slots rather than a single
    combined display, providing more detailed visual representation.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.20.1-0.1.2
- harleycolonies-1.21.1

