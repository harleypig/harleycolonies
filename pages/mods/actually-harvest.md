---
title: Actually Harvest (right click and XP)
categories:
  - technology-farming
  - utility-qol
  - mc-food
---

[Website](https://www.curseforge.com/minecraft/mc-mods/actually-harvest) | [Issues](https://github.com/wendall911/ActuallyHarvest/issues) | [Source](https://github.com/wendall911/ActuallyHarvest)

Client/Server: both

**Actually Harvest** lets you harvest mature crops by right‑clicking instead of
breaking them, optionally replanting automatically. It can grant experience
on harvest, supports blacklist/whitelist controls, and includes range
expansion for hoes (tier‑based and enchantment‑based). It can also allow
automation via fake players like Create’s Deployer.

### Configuration

Below are the available options and their defaults. Paths and lists use the
same names as in the mod’s config file.

#### General

- `allowEmptyHand` (default: `true`)
  - Harvest with an empty hand. When `false`, a hoe is required.

- `damageTool` (default: `false`)
  - If `true`, the tool used to harvest loses durability on use.

- `autoConfigMods` (default: `true`)
  - Automatically registers crops from installed mods.  
  - Note: If set to `false`, only crops defined in `harvestableCrops` will
    work.

- `replantCrops` (default: `true`)
  - Automatically replants crops after harvesting.

- `allowFakePlayer` (default: `true`)
  - Allows machines (e.g., Create’s Deployer) to perform right‑click harvests.

#### Experience (XP) Settings

- `xpFromHarvestChance` (default: `100`)
  - Percentage chance (0–100) to drop XP on harvest.

- `xpFromHarvestAmount` (default: `1`)
  - Fixed amount (0–10) of XP orbs to drop when `xpFromHarvestUseRange` is
    `false`.

- `xpFromHarvestUseRange` (default: `false`)
  - If `true`, use a range for XP instead of a fixed amount.

- `xpFromHarvestRangeAmount` (default: `"0-3"`)
  - Range string in the format `"min-max"` used when
    `xpFromHarvestUseRange = true`.

#### Harvest Targets

- `harvestableCrops` (default: `[]`)
  - Explicit list of harvestable crops.  
  - Format: `"harvestState[,afterHarvest]"`  
    Examples:
    - `"minecraft:wheat[age=7]"`
    - `"minecraft:cocoa[age=2,facing=north],minecraft:cocoa[age=0,facing=north]"`
  - Warning: If `autoConfigMods = false`, only entries in this list will be
    harvested.

- `harvestableBlocks` (default:  
  `["minecraft:sweet_berry_bush", "minecraft:cave_vines"]`)
  - Blocks where right‑click should simulate a use action instead of breaking,
    for built‑in right‑click harvest behavior (e.g., berry bushes, cave vines).

#### Hoe Range Expansion

- `expandHoeRange` (default: `true`)
  - Enables range expansion for hoes when right‑click harvesting.

- `smallTierExpansionRange` (default: `2`, range: 1–5)
  - Extra range for regular hoes (gold, wood, iron).

- `highTierExpansionRange` (default: `3`, range: 1–5)
  - Extra range for higher‑tier hoes (e.g., diamond, netherite).

- `expandHoeRangeEnchanted` (default: `true`)
  - If `true`, each level of Efficiency enchantment adds +1 to range.

- `maxHoeExpansionRange` (default: `11`, range: 1–11)
  - Hard limit on the total range after tier and enchant bonuses.

- `hoeItems` (default: `[]`)
  - Individual hoe items and their harvest tier for modded items not covered
    by tier detection.  
  - Format: `"modid:item-tier"` (e.g., `"minecraft:wooden_hoe-0"`).

#### Blacklists

- `blacklistCrops` (default: `[]`)
  - List of crops to exclude from right‑click harvest.  
  - Format: `"modid:block"`.

- `blacklistMods` (default: `[]`)
  - List of mods to exclude from right‑click harvest.  
  - Format: `"modid"`.

- `blacklistHeldItems` (default: `[]`)
  - Held items that should disable right‑click harvesting.  
  - Format: `"modid:item"`.
### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

