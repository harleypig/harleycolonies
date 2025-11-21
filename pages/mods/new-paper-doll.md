---
title: Paper Doll
---



Client/Server: both

**Paper Doll** displays a small 3D model of the player character on the
screen, showing equipped armor, held items, and player pose. The doll
appears during specific actions like sprinting, swimming, or crouching,
providing visual feedback about the player's current state. The mod
includes configurable positioning, scaling, and display conditions.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `paperdoll-client.toml`.

#### Display Settings

- `first_person_only` (default: `true`)
  - Only show paper doll when in first-person mode. When enabled, the
    paper doll only appears in first-person view, not in third-person.

- `head_movement` (default: `"YAW"`)
  - Set axis the player head can move on. Allowed values: `YAW` (horizontal
    rotation only), `PITCH` (vertical rotation only), `BOTH` (both axes).

- `position` (default: `"TOP_LEFT"`)
  - Define a screen corner to align the paper doll display to. Allowed
    values: `TOP_LEFT`, `TOP_RIGHT`, `BOTTOM_LEFT`, `BOTTOM_RIGHT`.

- `display_actions` (default: `["paperdoll:sprinting", "paperdoll:swimming",
  "paperdoll:crawling", "paperdoll:crouching", "paperdoll:flying",
  "paperdoll:gliding"]`)
  - Display paper doll while performing these actions. Allowed values:
    `paperdoll:sprinting`, `paperdoll:swimming`, `paperdoll:crawling`,
    `paperdoll:crouching`, `paperdoll:flying`, `paperdoll:gliding`,
    `paperdoll:riding`, `paperdoll:spin_attacking`, `paperdoll:using`.

- `scale` (default: `4`)
  - Scale of paper doll. Also affected by video settings GUI scale. Range:
    `1` to `24`.

- `offset_y` (default: `0`)
  - Offset on y-axis from original doll position. Range: greater than
    `-2147483648`.

- `offset_x` (default: `0`)
  - Offset on x-axis from original doll position. Range: greater than
    `-2147483648`.

- `display_time` (default: `15`)
  - Amount of ticks the paper doll will be kept on screen after its
    display conditions are no longer met. Set to `0` to always display the
    doll. Range: greater than `0`.

- `potion_shift` (default: `true`)
  - Shift paper doll downwards when it would otherwise overlap with potion
    icons while showing in the top screen right corner. When enabled,
    prevents overlap with potion effect icons.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

