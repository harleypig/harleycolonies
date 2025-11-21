---
title: Comforts (Fabric/Forge/Quilt)
categories:
  - mc-miscellaneous
  - adventure-rpg
---

[Website](https://www.curseforge.com/minecraft/mc-mods/comforts) | [Issues](https://github.com/illusivesoulworks/comforts/issues) | [Source](https://github.com/illusivesoulworks/comforts)

Client/Server: both

**Comforts** enhances Minecraft by introducing portable sleeping solutions
that allow players to rest without altering their spawn points. This mod
provides sleeping bags for nighttime rest and hammocks for daytime rest,
making it ideal for adventurers who want to skip time without resetting
their home base spawn. Sleeping bags and hammocks come in all 16 standard
Minecraft colors and are stackable, making them convenient for travel.

### Features

- **Sleeping Bags**: Portable beds that allow players to sleep through the
  night without setting a spawn point. Crafted using three pieces of
  matching colored wool arranged in a straight line. Available in all 16
  colors and stackable up to 64.

- **Hammocks**: Portable sleeping solutions that allow players to sleep
  during the day, transitioning the game to night. Crafted using colored
  wool in the center, sticks at the top and bottom, and strings filling
  the remaining slots. Also available in all 16 colors.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `comforts-server.toml`.

#### General Settings

- `autoUse` (default: `true`)
  - If enabled, players automatically attempt to use sleeping bags when
    placed. When set to `true`, right-clicking a sleeping bag will
    immediately attempt to sleep.

- `restrictSleeping` (default: `false`)
  - If enabled, players cannot sleep again for a period of time after
    sleeping. This implements a well-rested mechanic that prevents
    players from sleeping too frequently.

- `restMultiplier` (default: `2.0`)
  - If `restrictSleeping` is `true`, this value determines the length of
    wait time before a player can sleep again. Larger numbers allow
    players to sleep sooner. Range: `1.0` to `20.0`.

#### Usage Restrictions

- `hammockUse` (default: `"DAY"`)
  - The time of day that hammocks can be used. Allowed values: `NONE`,
    `DAY`, `NIGHT`, `DAY_OR_NIGHT`.

- `sleepingBagUse` (default: `"NIGHT"`)
  - The time of day that sleeping bags can be used. Allowed values:
    `NONE`, `DAY`, `NIGHT`, `DAY_OR_NIGHT`.

#### Sleep Percentage

- `daySleepingPercentage` (default: `-1`)
  - What percentage of players must sleep to skip the day. A percentage
    value of `0` will allow the day to be skipped by just 1 player, and
    a percentage value of `100` will require all players to sleep before
    skipping the day. A value of less than `0` will default to the
    `playerSleepingPercentage` game rule. Range: `-1` to `100`.

#### Wake Time Offsets

- `dayWakeTimeOffset` (default: `0`)
  - The amount of time, in ticks, to add or remove from the new time
    after sleeping through a night. Positive values wake players later in
    the day, negative values wake them earlier. Range: `-2000` to `2000`.

- `nightWakeTimeOffset` (default: `0`)
  - The amount of time, in ticks, to add or remove from the new time
    after sleeping through a day. Positive values wake players later in
    the night, negative values wake them earlier. Range: `-2000` to
    `2000`.

#### Phantom Prevention

- `hammocksStopPhantoms` (default: `true`)
  - If enabled, attempting to sleep in hammocks stops phantoms from
    spawning. This prevents phantom mobs from appearing when players use
    hammocks during the day.

- `sleepingBagsStopPhantoms` (default: `true`)
  - If enabled, attempting to sleep in sleeping bags stops phantoms
    from spawning. This prevents phantom mobs from appearing when
    players use sleeping bags during the night.

#### Sleeping Bag Durability

- `sleepingBagBreakChance` (default: `0`)
  - The percentage chance that a sleeping bag will break upon use. A
    value of `0` means sleeping bags never break, while `100` means they
    always break. Range: `0` to `100`.

- `sleepingBagBreakChanceLuckMultiplier` (default: `0.0`)
  - The value that will be multiplied by a player's luck attribute and
    added to `sleepingBagBreakChance`. Positive values increase break
    chance with luck, negative values decrease it. Range: `-1.0` to
    `1.0`.

#### Status Effects

- `sleepingBagEffects` (default: `[]`)
  - The status effects to apply to players after using the sleeping bag.
    Format: `effect;duration(secs);power`. Each effect is specified as
    a string in the format `"minecraft:effect_name duration power"`.
    Example: `["minecraft:absorption 120 2", "minecraft:regeneration 120
    2"]`.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.20.1-0.1.2
- harleycolonies-1.21.1

