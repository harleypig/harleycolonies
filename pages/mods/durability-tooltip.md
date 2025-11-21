---
title: Durability Tooltip
categories:
  - armor-weapons-tools
  - cosmetic
  - map-information
---

[Website](https://www.curseforge.com/minecraft/mc-mods/durability-tooltip) | [Issues](https://github.com/SuperMartijn642/DurabilityTooltip/issues) | [Source](https://github.com/SuperMartijn642/DurabilityTooltip)

Client/Server: both

**Durability Tooltip** enhances item tooltips by displaying detailed
durability information for tools, weapons, and armor. The mod provides
multiple display styles including numbers, text descriptions, and visual
bars, with customizable colors and formatting options. This makes it easier
for players to quickly assess the condition of their equipment.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `durabilitytooltip-common.toml`.

#### Display Style

- `Client.tooltipStyle` (default: `"NUMBERS"`)
  - What should be the style of the tooltip? `NUMBERS` means 'Durability:
    30 / 100', `TEXT` means 'Durability: pristine/slightly damaged/nearly
    broken', `BAR` means 'Durability: [███▒▒▒▒▒▒▒]'. Allowed values:
    `BAR`, `NUMBERS`, `TEXT`.

- `Client.showTooltipHint` (default: `true`)
  - Should the tooltip include the 'Durability:' hint? When enabled, the
    word "Durability:" is shown before the durability information.

#### Color Settings

- `Client.tooltipColorStyle` (default: `"VARYING"`)
  - What colors should be used for the reactive part (numbers/text/bar
    characters) of the tooltip? `BASE` means use the base color, `GOLD`
    means always gold, `VARYING` means green/orange/red depending on
    remaining durability. Allowed values: `BASE`, `GOLD`, `VARYING`.

- `Client.baseTooltipColor` (default: `"GRAY"`)
  - What should be the base text color of the tooltip? Allowed values:
    `BLACK`, `DARK_BLUE`, `DARK_GREEN`, `DARK_AQUA`, `DARK_RED`,
    `DARK_PURPLE`, `GOLD`, `GRAY`, `DARK_GRAY`, `BLUE`, `GREEN`, `AQUA`,
    `RED`, `LIGHT_PURPLE`, `YELLOW`, `WHITE`, `OBFUSCATED`, `BOLD`,
    `STRIKETHROUGH`, `UNDERLINE`, `ITALIC`, `RESET`.

#### Filtering Options

- `Client.onlyVanillaTools` (default: `false`)
  - Should the durability tooltip only be shown on vanilla tools? When
    enabled, modded tools won't show durability tooltips, only vanilla
    Minecraft tools will.

- `Client.showWhenFull` (default: `true`)
  - Should the durability tooltip be shown when a tool is not damaged?
    When enabled, durability is shown even for items at full durability.

- `Client.blackListedMods` (default: `"tconstruct,supplementaries"`)
  - Which mods should be blacklisted? Items from blacklisted mods won't
    show the durability tooltip. Enter mod IDs separated by commas. Range:
    `0` to `100` characters.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1
- harleycolonies-1.20.1-0.1.2

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.20.1-0.1.2
- harleycolonies-1.21.1

