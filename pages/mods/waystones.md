---
title: Waystones
categories:
  - magic
  - adventure-rpg
  - server-utility
  - technology-player-transport
---

[Website](https://www.curseforge.com/minecraft/mc-mods/waystones) | [Issues](https://github.com/ModdingForBlockheads/Waystones/issues) | [Source](https://github.com/ModdingForBlockheads/Waystones)

Client/Server: both

**Waystones** adds a teleportation system to Minecraft through waystone
blocks that players can activate and use to travel between locations. The
mod includes various waystone types (regular, warp plates, warp stones,
scrolls), global waystones, sharestones for team-based teleportation, and
configurable XP costs and cooldowns. Waystones can spawn naturally in the
world and villages, and the mod integrates with JourneyMap, BlueMap, and
Dynmap.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `waystones-common.toml`.

#### General Settings

- `general.restrictedWaystones` (default: `["PLAYER"]`)
  - List of waystone origins that should prevent others from editing.
    `PLAYER` is special in that it allows only edits by the owner of the
    waystone.

- `general.defaultVisibility` (default: `"ACTIVATION"`)
  - Set to `"GLOBAL"` to have newly placed or found waystones be global by
    default. Allowed values: `ACTIVATION`, `GLOBAL`, `SHARD_ONLY`, and
    various colored sharestone types.

- `general.allowedVisibilities` (default: `[]`)
  - Add `"GLOBAL"` to allow every player to create global waystones.

- `general.warpStoneUseTime` (default: `32`)
  - The time in ticks that it takes to use a warp stone. This is the
    charge-up time when holding right-click.

- `general.warpPlateUseTime` (default: `15`)
  - The time in ticks that it takes to use a warp plate. This is the time
    the player has to stand on top for.

- `general.scrollUseTime` (default: `32`)
  - The time in ticks it takes to use a scroll. This is the charge-up time
    when holding right-click.

#### Inventory Button Settings

- `inventoryButton.inventoryButton` (default: `""`)
  - Set to `'NONE'` for no inventory button. Set to `'NEAREST'` for an
    inventory button that teleports to the nearest waystone. Set to `'ANY'`
    for an inventory button that opens the waystone selection menu. Set to a
    waystone name for an inventory button that teleports to a specifically
    named waystone.

- `inventoryButton.inventoryButtonX` (default: `58`)
  - The x position of the inventory button in the inventory.

- `inventoryButton.inventoryButtonY` (default: `60`)
  - The y position of the inventory button in the inventory.

- `inventoryButton.creativeInventoryButtonX` (default: `88`)
  - The x position of the inventory button in the creative menu.

- `inventoryButton.creativeInventoryButtonY` (default: `33`)
  - The y position of the inventory button in the creative menu.

#### World Generation Settings

- `worldGen.wildWaystoneStyle` (default: `"BIOME"`)
  - Set to `'DEFAULT'` to only generate the normally textured waystones.
    Set to `'MOSSY'` or `'SANDY'` to generate all as that variant. Set to
    `'BIOME'` to make the style depend on the biome it is generated in.
    Allowed values: `DEFAULT`, `MOSSY`, `SANDY`, `BLACKSTONE`, `DEEPSLATE`,
    `END_STONE`, `BIOME`.

- `worldGen.chunksBetweenWildWaystones` (default: `25`)
  - Approximate chunk distance between wild waystones being generated. Set
    to `0` to disable generation.

- `worldGen.wildWaystonesDimensionAllowList` (default: `["minecraft:the_end",
  "minecraft:the_nether", "minecraft:overworld"]`)
  - List of dimensions that wild waystones are allowed to spawn in. If
    left empty, all dimensions except those in
    `wildWaystonesDimensionDenyList` are used.

- `worldGen.wildWaystonesDimensionDenyList` (default: `[]`)
  - List of dimensions that wild waystones are not allowed to spawn in.
    Only used if `wildWaystonesDimensionAllowList` is empty.

- `worldGen.nameGenerationMode` (default: `"PRESET_FIRST"`)
  - Set to `'PRESET_FIRST'` to first use names from the
    `nameGenerationPresets`. Set to `'PRESET_ONLY'` to use only those
    custom names. Set to `'MIXED'` to have some waystones use custom names,
    and others random names. Allowed values: `PRESET_FIRST`, `RANDOM_ONLY`,
    `PRESET_ONLY`, `MIXED`.

- `worldGen.nameGenerationTemplate` (default: `"{MrPork}"`)
  - The template to use when generating new names. Supported placeholders
    are `{Biome}` (english biome name) and `{MrPork}` (the default name
    generator).

- `worldGen.nameGenerationPresets` (default: `[]`)
  - These names will be used for the PRESET name generation mode.

- `worldGen.spawnInVillages` (default: `"REGULAR"`)
  - Set to `REGULAR` to have waystones spawn in some villages. Set to
    `FREQUENT` to have waystones spawn in most villages. Set to `DISABLED`
    to disable waystone generation in villages. Allowed values: `DISABLED`,
    `REGULAR`, `FREQUENT`.

#### Teleport Settings

- `teleports.enableCosts` (default: `true`)
  - Set to `false` to simply disable all xp costs. See `warpRequirements`
    for more fine-grained control.

- `teleports.enableCooldowns` (default: `true`)
  - Set to `false` to simply disable all cooldowns. See `warpRequirements`
    for more fine-grained control.

- `teleports.warpRequirements` (default: `["[is_not_interdimensional]
  scaled_add_xp_cost(distance, 0.01)", "[is_interdimensional]
  add_xp_cost(27)", "[source_is_warp_plate] multiply_xp_cost(0)",
  "[target_is_global] multiply_xp_cost(0)", "min_xp_cost(0)",
  "max_xp_cost(27)", "[source_is_inventory_button] add_cooldown(inventory_button,
  300)"]`)
  - List of warp requirements with comma-separated parameters in
    parentheses. Conditions can be defined as comma-separated list in square
    brackets. Will be applied in order.

- `teleports.transportPets` (default: `"DISABLED"`)
  - Set to `ENABLED` to have nearby pets teleport with you. Set to
    `SAME_DIMENSION` to have nearby pets teleport with you only if you're
    not changing dimensions. Set to `DISABLED` to disable. Allowed values:
    `ENABLED`, `SAME_DIMENSION`, `DISABLED`.

- `teleports.transportLeashed` (default: `"ENABLED"`)
  - Set to `ENABLED` to have leashed mobs teleport with you. Set to
    `SAME_DIMENSION` to have leashed mobs teleport with you only if you're
    not changing dimensions. Set to `DISABLED` to disable. Allowed values:
    `ENABLED`, `SAME_DIMENSION`, `DISABLED`.

- `teleports.entityDenyList` (default: `["minecraft:wither"]`)
  - List of entities that cannot be teleported, either as pet, leashed, or
    on warp plates.

- `teleports.enableModifiers` (default: `true`)
  - Set to `true` to enable warp modifier items for applying status effects
    on teleports.

#### Client Settings

- `client.disableTextGlow` (default: `false`)
  - If enabled, the text overlay on waystones will no longer always render
    at full brightness.

#### Compatibility Settings

- `compatibility.journeyMap` (default: `true`)
  - If enabled, JourneyMap waypoints will be created for each activated
    waystone.

- `compatibility.preferJourneyMapIntegrationMod` (default: `true`)
  - If enabled, JourneyMap waypoints will only be created if the mod
    'JourneyMap Integration' is not installed.

- `compatibility.blueMap` (default: `true`)
  - If enabled, Waystones will add markers for waystones and sharestones to
    BlueMap.

- `compatibility.dynmap` (default: `true`)
  - If enabled, Waystones will add markers for waystones and sharestones
    to Dynmap.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1
- harleycolonies-1.20.1-0.1.2

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.20.1-0.1.2
- harleycolonies-1.21.1

