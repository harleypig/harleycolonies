---
title: Clean Tooltips
---

**Clean Tooltips** enhances item tooltips by providing cleaner formatting
and color-coded sections for durability and enchantments. The mod improves
readability of tooltips with better spacing, color coding for curses and
enchantments, and organized sections. This makes it easier to quickly
identify important information about items.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `clean_tooltips-client.toml`.

#### Durability Settings

- `durability.enabled` (default: `true`)
  - Should the Durability section be enabled? When enabled, durability
    information is displayed in a dedicated section of the tooltip.

#### Enchantment Settings

- `enchantments.enabled` (default: `true`)
  - Should the fancied up Enchantment section be used? When enabled,
    enchantments are displayed with enhanced formatting and color coding.

- `enchantments.color.curse` (default: `"RED"`)
  - The color curses should have. Allowed values: `BLACK`, `DARK_BLUE`,
    `DARK_GREEN`, `DARK_AQUA`, `DARK_RED`, `DARK_PURPLE`, `GOLD`, `GRAY`,
    `DARK_GRAY`, `BLUE`, `GREEN`, `AQUA`, `RED`, `LIGHT_PURPLE`, `YELLOW`,
    `WHITE`, `OBFUSCATED`, `BOLD`, `STRIKETHROUGH`, `UNDERLINE`, `ITALIC`,
    `RESET`.

- `enchantments.color.normal` (default: `"GREEN"`)
  - The color normal enchantments should have. Uses the same color values
    as `curse`.

- `enchantments.color.max_level` (default: `"GOLD"`)
  - The color max level enchantments should have. Uses the same color
    values as `curse`.

#### Color Settings

- `color.enabled` (default: `true`)
  - Should the fancied up Color section be used? When enabled, color
    information is displayed in a dedicated section.

#### Gap Settings

- `gap.enabled` (default: `true`)
  - Should sections of the tooltip have spacing between them? When
    enabled, visual spacing is added between different tooltip sections for
    better readability.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

