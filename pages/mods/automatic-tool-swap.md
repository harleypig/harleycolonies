---
title: Automatic Tool Swap
---



Client/Server: both

**Automatic Tool Swap** automatically switches to the best tool for
breaking blocks based on harvest level, tool type, and enchantments. The
mod searches your inventory for the optimal tool when you target a block
and swaps to it automatically. This eliminates the need to manually switch
tools, making mining and building more efficient.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `toolswap-client.toml`.

#### Tool Selection Settings

- `save` (default: `false`)
  - If this is on, tool with 1 durability left will be saved. Only works
    for BREAKING a block, not stripping, flattening, or tilting. When
    enabled, tools at minimum durability are not used to prevent breaking.

- `min_durability` (default: `1`)
  - If items should be saved, this is the minimum durability which they
    are allowed to have. Tools below this durability will not be used when
    `save` is enabled. Range: greater than `1`.

- `ignore_harvest_level` (default: `true`)
  - If this is on, harvest level of tools will be ignored on breaking
    blocks. Otherwise it will always search for the lowest possible tool.
    When enabled, the mod may use higher-tier tools even if lower-tier
    tools would work.

- `sneak_to_prevent` (default: `true`)
  - If this is on, sneaking will not swap your tool. When enabled, holding
    sneak prevents automatic tool swapping, allowing manual control.

- `sorttype` (default: `"LEVEL"`)
  - Set the mode in which order the tools will be chosen. Allowed values:
    `LEVEL` (sorted by harvest level, lowest first), `LEVEL_INVERTED`
    (sorted by harvest level, highest first), `LEFT_TO_RIGHT` (sorted from
    left to right), `RIGHT_TO_LEFT` (sorted from right to left),
    `ENCHANTED_FIRST` (sorted by harvest level, highest enchanted item
    first), `ENCHANTED_LAST` (sorted by harvest level, highest unenchanted
    item first).

- `ignore_empty_hand` (default: `"ALWAYS"`)
  - Choose the mode when swapping is fine. Allowed values: `ALWAYS`
    (always swap, ignore item in hand), `EMPTY_HAND` (only swap if your
    hand is empty), `ITEMS` (only swap if you hold any item), `TOOLS`
    (only swap if you hold any tool), `NO_TOOLS` (only swap if you hold
    any item excluding tools).

- `one_block_mode` (default: `false`)
  - Enable this option when playing OneBlock. It continuously searches for
    the most suitable tool every tick while mining, rather than only when
    a new block is targeted. When enabled, tool selection updates
    continuously during mining.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

