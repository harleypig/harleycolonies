---
title: Packed Up (Backpacks)
---



Client/Server: both

**Packed Up (Backpacks)** adds multiple tiers of backpacks with increasing
storage capacity. The mod includes Basic, Iron, Copper, Silver, Gold,
Diamond, and Obsidian backpacks, each with configurable inventory sizes.
Backpacks can be nested inside other backpacks (with configurable depth
limits), can be configured to persist on death, and have burn protection
options.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `packedup-common.toml`.

#### General Settings

- `General.allowBagInBag` (default: `true`)
  - Can backpacks be put inside other backpacks? When enabled, backpacks
    can be stored inside other backpacks, allowing for nested storage.

- `General.maxBagInBagLayer` (default: `-1`)
  - How many layers deep can you place backpacks inside backpacks? `-1`
    for infinite, `0` is the same as setting `allowBagInBag` to `false`.
    Range: `-1` to `5`.

- `General.keepBackpacksOnDeath` (default: `false`)
  - Should the backpack remain in the player's inventory if they die?
    When enabled, backpacks are not dropped on death, similar to keep
    inventory.

- `General.canBackpacksBurn` (default: `true`)
  - Should backpacks be destroyed by lava and fire? When enabled,
    backpacks can be destroyed by fire and lava. When disabled, backpacks
    are fireproof.

#### Backpack Settings

Each backpack tier (Basic, Iron, Copper, Silver, Gold, Diamond, Obsidian)
has the following settings:

- `Backpacks.[Tier].enable` (default: `true`)
  - Enable this backpack tier? When disabled, the backpack cannot be
    crafted or used.

- `Backpacks.[Tier].rows` (default: varies by tier)
  - How many rows does this backpack have? Range: `1` to `9`. Defaults:
    Basic: `3`, Iron: `4`, Copper: `4`, Silver: `5`, Gold: `5`, Diamond:
    `7`, Obsidian: `8`.

- `Backpacks.[Tier].columns` (default: `9`)
  - How many columns does this backpack have? Range: `1` to `13`. All
    tiers default to `9` columns.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

