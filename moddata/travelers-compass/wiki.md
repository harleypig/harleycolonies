---
title: Traveler's Compass
---

**Traveler's Compass** is a powerful search tool that allows players to
locate blocks, entities, items, containers, and more in the world. The
compass can search for specific blocks, fluids, containers, villagers,
spawners, mobs, players, dropped items, and loot drops. It includes
configurable search ranges, filters, HUD display options, and integration
with JEI/REI/EMI and Jade/TOP. The mod also supports XP costs for searches
to balance gameplay.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config files.

#### General Search Settings

These settings are configured in `travelerscompass-common.toml`.

- `general.enable_blocks_search` (default: `true`)
  - Allows the compass to locate specific blocks in the world.

- `general.enable_fluids_search` (default: `true`)
  - Allows the compass to locate fluid blocks (water, lava, etc.).

- `general.enable_containers_search` (default: `true`)
  - Allows the compass to locate all container types based on their
    contents.

- `general.enable_villagers_search` (default: `true`)
  - Allows searching for villagers based on their trades.

- `general.enable_spawners_search` (default: `true`)
  - Allows the compass to locate spawners by their mob type.

- `general.enable_mobs_search` (default: `true`)
  - Allows the compass to locate specific mobs by their spawn eggs.

- `general.enable_inventories_search` (default: `true`)
  - Allows the compass to locate Entities based on items in their
    inventory.

- `general.enable_players_inventories_search` (default: `true`)
  - Allows the compass to locate players based on items in their
    inventory.

- `general.enable_item_entities_search` (default: `true`)
  - Allows the compass to locate dropped items on the ground.

- `general.enable_drops_search` (default: `true`)
  - Allows the compass to locate mobs based on their potential loot drops.

- `general.enable_block_containers_search` (default: `true`)
  - Allows the compass to search inside block containers (chests, furnaces,
    barrels, etc.). Requires `enable_containers_search` to be enabled.

#### Behavior Settings

- `behavior.chunk_search_range` (default: `10`)
  - Maximum search radius in chunks from the player. Applies to any block
    scanning search mode. Range: greater than `0`.

- `behavior.entities_search_range` (default: `200`)
  - Maximum search radius in blocks from the player. Applies to any entity.
    Range: greater than `0`.

- `behavior.wide_search_range` (default: `16`)
  - Maximum search radius in chunks from the player. Applies to any block.
    Range: greater than `0`.

- `behavior.search_interval` (default: `40`)
  - Delay in ticks between search updates (20 ticks = 1 second). Range:
    greater than `1`.

- `behavior.chunks_scans_per_tick_on_server` (default: `8`)
  - Maximum number of chunk scan operations per tick, shared across all
    players on the server. This value has a direct impact on server
    performance. Range: `0` to `199`.

- `behavior.chunks_scans_per_compass` (default: `3`)
  - Maximum chunk scans per compass per search cycle. Limits individual
    compass performance impact. Range: `0` to `199`.

- `behavior.force_chunk_generation_limit` (default: `2`)
  - Maximum new chunks that can be generated or loaded per tick during
    search. Set to `0` to disable searching in ungenerated chunks. High
    values may cause lag spikes. Range: `0` to `199`.

- `behavior.max_cached_locations` (default: `180`)
  - Limits how many matching locations per compass will be stored after
    scanning. Only the closest or most relevant targets will be cached,
    based on priority and distance. Range: greater than `0`.

#### Search Filters

- `search-filters.mods_filter_type` (default: `"BLACKLIST"`)
  - Filter mode for mod namespaces. Allowed values: `WHITELIST`,
    `BLACKLIST`.

- `search-filters.mods_filter` (default: `[]`)
  - List of mod namespaces to filter. Example: `["minecraft", "ae2",
    "alexscaves"]`.

- `search-filters.items_filter_type` (default: `"BLACKLIST"`)
  - Filter mode for specific items. Allowed values: `WHITELIST`,
    `BLACKLIST`.

- `search-filters.items_filter` (default: `[]`)
  - List of item IDs to filter. Example: `["minecraft:carrot",
    "minecraft:diamond_ore"]`.

- `search-filters.item_tags_filter_type` (default: `"BLACKLIST"`)
  - Filter mode for item tags. Allowed values: `WHITELIST`, `BLACKLIST`.

- `search-filters.item_tags_filter` (default: `[]`)
  - List of item tags to filter. Example: `["minecraft:logs", "c:ores"]`.

- `search-filters.entities_filter_type` (default: `"BLACKLIST"`)
  - Filter mode for entities. Allowed values: `WHITELIST`, `BLACKLIST`.

- `search-filters.entities_filter` (default: `[]`)
  - List of entity IDs to filter. Example: `["minecraft:enderman",
    "aether:valkyrie"]`.

#### HUD Settings

- `hud.enable_hud` (default: `true`)
  - Enables the compass HUD overlay.

- `hud.hud_show_coords` (default: `true`)
  - Shows target coordinates in the HUD.

- `hud.default_x_hud_offset` (default: `0`)
  - Base x HUD offset in pixels.

- `hud.default_y_hud_offset` (default: `0`)
  - Base y HUD offset in pixels.

- `hud.default_hud_scale` (default: `1.0`)
  - Default HUD scale.

#### Compatibility Settings

- `compatibility.enable_lootr_search` (default: `true`)
  - Enables Lootr containers searching when Lootr mod is installed.

- `compatibility.lootr_search_mode` (default: `"ALL"`)
  - Lootr search behavior. Allowed values: `CLOSED`, `OPENED`, `ALL`.

- `compatibility.jei_compatibility` (default: `true`)
  - Enable dragging items from the JEI panel into Compass inventory.

- `compatibility.rei_compatibility` (default: `true`)
  - Enable dragging items from the REI panel into Compass inventory.

- `compatibility.emi_compatibility` (default: `true`)
  - Enable dragging items from the EMI panel into Compass inventory.

- `compatibility.jade_compatibility` (default: `true`)
  - Enable displaying Block/Entity search info in the Jade info panel.

- `compatibility.the_one_probe_compatibility` (default: `true`)
  - Enable displaying Block/Entity search info in the TOP info panel.

#### Search Cost Settings

These settings are configured in `travelerscompass-cost.toml`.

- `search-cost.search_xp_cost` (default: `false`)
  - When enabled, adding items to the compass inventory costs experience
    levels.

- `search-cost.items_search_cost` (default: `[]`)
  - XP costs for searching specific items. Format:
    `"modid:item=consumed_levels/required_levels"`. Example:
    `["minecraft:diamond_ore=4/20", "minecraft:ancient_debris=20/40"]`.

- `search-cost.tags_search_cost` (default: `[]`)
  - Defines XP costs for adding items or blocks based on tags. Works for
    both item tags and block tags. If an item has a cost defined both in
    `items_search_cost` and here, the `items_search_cost` value takes
    priority. Example: `["minecraft:planks=1/3"]`.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

