---
title: Following
---

Following commands tell Baritone to pathfind toward a moving
entity — players, mobs, or a fixed list picked by type or name.
The `FollowProcess` rebuilds a composite goal every tick from
the live entity list, so if the target moves, gets farther away,
or dies, Baritone re-evaluates without a new command.

## Settings Index

Alphabetical. Each link jumps to the section that discusses the setting.

- [followOffsetDirection](#where-to-stand)
- [followOffsetDistance](#where-to-stand)
- [followRadius](#where-to-stand)
- [followTargetMaxDistance](#target-selection)

## follow

Aliases: `follow`

Tell Baritone to follow one or more entities. The exact form
depends on whether you want to follow *everything* of a kind
(group form) or a specific list of entities or players (typed
form).

### Subcommands

#### follow entities

Follow every `LivingEntity` that isn't you — mobs, players,
villagers, anything alive. Wide net; you almost always want a
more specific form in practice.

#### follow players

Follow every `Player` other than yourself.

#### follow entity `<type1> [<type2> ...]`

Follow entities by type. Accepts one or more namespaced entity
IDs (e.g. `minecraft:skeleton`, `minecraft:horse`). All living
instances of the listed types become follow targets. Tab
completion offers the entity-type registry.

#### follow player `<name1> [<name2> ...]`

Follow specific players by name. Accepts one or more usernames.
Tab completion offers players currently in view.

### Arguments

- `<group|list>` — one of `entities`, `players`, `entity`, or
  `player`. Required.
- `<target...>` — one or more entity types (after `entity`) or
  player names (after `player`). Required for the typed forms;
  at least one must resolve to something in range.

### Error states

- `No valid entities in range!` — typed form received no
  entities that match and are currently loaded within
  `followTargetMaxDistance`. Get closer, or raise the limit.

### Tab completion

First argument: the four subcommand keywords. Subsequent
arguments: entity-type IDs (for `entity`) or nearby player
names (for `player`). No completion once an argument has been
rejected as invalid.

## Best Practices

Guidance comes from the `FollowProcess` implementation and the
default values in `Settings.java`.

### Where to stand

By default Baritone stops within 3 blocks of the target and
doesn't care which side. The offset settings let you instead
hold a fixed position relative to the target — handy for
shepherding a player into a base or staying out of their line
of fire.

- `followOffsetDistance` (Double, default `0`) — offset in
  blocks from the target position. `0` means "go to the entity
  itself"; any non-zero value means "aim for a point this many
  blocks away from the entity in `followOffsetDirection`."
- `followOffsetDirection` (Float, default `0`) — compass bearing
  in degrees for that offset. Ignored when `followOffsetDistance`
  is `0`. Example: `followOffsetDistance = 5`,
  `followOffsetDirection = 0`, `followRadius = 0` parks you
  precisely 5 blocks north of the target.
- `followRadius` (Integer, default `3`) — tolerance in blocks
  around whichever position (the entity or the offset point) is
  considered "close enough." Lower values track tighter but
  replan more often; raise it for loose escorts.

### Target selection

- `followTargetMaxDistance` (Integer, default `0`) — hard cap on
  how far a candidate entity can be from you and still count as
  a valid target. `0` disables the cap entirely (follow anyone
  the game has loaded). Useful when a `follow entity skeleton`
  sweep would otherwise drag Baritone across the whole render
  distance.

## Notes & Limitations

- The target list is a live filter, not a snapshot. A new
  skeleton spawning inside your render distance while you have
  `follow entity skeleton` active will be added automatically;
  one despawning or dying is removed.
- You can only run one follow filter at a time. A new `follow`
  command replaces the previous filter; `cancel` clears it.
- `cancelOnGoalInvalidation` (documented on the Basic page)
  applies here: if the target moves and the remaining path no
  longer ends in the goal, the path is cancelled and replanned.
- Two entries in the `FollowGroup` enum — `FRIENDLY` and
  `HOSTILE` — exist in the source but are commented out. There
  is no `follow friendly` or `follow hostile` subcommand despite
  what older discussions may suggest.
