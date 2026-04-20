---
title: Mining
---

Mining commands tell Baritone to search for specific blocks,
mine them, tunnel straight ahead, scan the chunk cache for
remembered ore positions, and pick up drops. The `MineProcess`
combines live world scans with cached-world lookups to find
targets, and can optionally be constrained to "legit" behavior
that only reacts to ores the player could actually see.

## Settings Index

Alphabetical. Each link jumps to the section that discusses the setting.

- [allowOnlyExposedOres](#exposed-ore-and-legit-mining)
- [allowOnlyExposedOresDistance](#exposed-ore-and-legit-mining)
- [exploreForBlocks](#scanning-and-cache)
- [extendCacheOnThreshold](#scanning-and-cache)
- [forceInternalMining](#internal-mining)
- [internalMiningAirException](#internal-mining)
- [legitMine](#exposed-ore-and-legit-mining)
- [legitMineIncludeDiagonals](#exposed-ore-and-legit-mining)
- [legitMineYLevel](#y-level-limits)
- [maxCachedWorldScanCount](#scanning-and-cache)
- [maxYLevelWhileMining](#y-level-limits)
- [mineDropLoiterDurationMSThanksLouca](#drops-and-pickup)
- [mineGoalUpdateInterval](#scanning-and-cache)
- [mineMaxOreLocationsCount](#scanning-and-cache)
- [mineScanDroppedItems](#drops-and-pickup)
- [minYLevelWhileMining](#y-level-limits)
- [notificationOnMineFail](#tools-and-notifications)
- [useSwordToMine](#tools-and-notifications)

## mine

Aliases: `mine`

Tell Baritone to search for and mine one or more block types.
Candidates come from both the loaded world (live scan) and the
chunk cache, so Baritone can start mining a vein it saw on an
earlier session if `chunkCaching` is on. The command triggers a
world repack immediately, then hands off to `MineProcess`.

### Arguments

- `[<quantity>]` — optional integer stop-condition. When present,
  Baritone mines this many drop items and then stops. Omit to
  mine indefinitely until cancelled.
- `<block> [<block> ...]` — one or more block IDs (namespaced
  fine, e.g. `minecraft:diamond_ore`). A vanilla short name like
  `diamond_ore` also resolves.

### Tab completion

Block-ID completion for the block arguments. If the first token
parses as an integer, it's taken as `<quantity>` and completion
continues for blocks.

## tunnel

Aliases: `tunnel`

Mine in a straight line in the direction you're facing. With no
arguments, it's a 1-wide × 2-tall tunnel driven forever ahead
via a `GoalStrictDirection`. With three arguments it becomes a
fixed-size box clear driven through `BuilderProcess.clearArea`.

### Arguments

- `<height> <width> <depth>` — optional triple of integers for
  fixed-size tunneling. Must satisfy `height ≥ 2`,
  `width ≥ 1`, `depth ≥ 1`, and `height ≤` the world's build
  limit, otherwise the command refuses with
  `Width and depth must at least be 1 block; Height must at
  least be 2 blocks, and cannot be greater than the build limit.`
  Width is centered on the player; odd widths extend an extra
  block to one side.

### Tab completion

None.

## find

Aliases: `find`

Query Baritone's chunk cache for remembered positions of one or
more blocks. Only blocks in `CachedChunk.BLOCKS_TO_KEEP_TRACK_OF`
are ever cached, so the completion list is restricted to that
set — uncached blocks simply won't return results.

Each found position prints as a clickable chat entry: clicking
issues a `goal <x> <y> <z>` command to that position.

### Arguments

- `<block> [<block> ...]` — one or more block IDs to look up.

### Error states

- `No positions known, are you sure the blocks are cached?` —
  the cache has no entry for any of the requested blocks.
  Either you haven't been near them yet with `chunkCaching` on,
  or the block isn't in the tracked set.

### Tab completion

Restricted to the cacheable-block set, namespaced-prefix matched
and sorted alphabetically.

## blacklist

Aliases: `blacklist`

Mark the current `GetToBlockProcess` target's closest instance
as unreachable and move on to the next nearest. Useful when
`goto <block>` keeps picking a block that can't actually be
reached (surrounded by lava, behind bedrock, etc.).

### Arguments

None.

### Error states

- `GetToBlockProcess is not currently active` — there's no
  active `goto <block>` to blacklist against.
- `No known locations, unable to blacklist` — the process is
  active but has no candidates to remove.

### Tab completion

None.

## pickup

Aliases: `pickup`

Walk to dropped item entities and collect them. This command
delegates to `FollowProcess` in its pickup mode, so it's a
follow-style behavior living under mining for convenience (main
use case is collecting ore drops that got knocked out of range).

### Arguments

- `[<item> ...]` — optional filter list. When empty, Baritone
  picks up every dropped item it sees. When non-empty, only
  stacks whose item is in the list are picked up.

### Tab completion

Item-ID completion for each argument.

## Best Practices

Guidance comes from setting defaults, the `MineProcess` source,
and comments on individual settings.

### Y-level limits

Hard clamps on the Y range Baritone is allowed to mine at.
Handy for keeping ore runs in the diamond layer without wasting
time on surface veins, and for legit-style strip mining.

- `minYLevelWhileMining` (Integer, default `0`) — minimum Y
  level to mine at. `0` disables the clamp. On worlds with
  negative Y, the value to set is **absolute** after subtracting
  the world's min height (e.g. Y = –55 on a –64 world → set to
  9). Counter-intuitive; read the setting comment in
  `Settings.java` if in doubt.
- `maxYLevelWhileMining` (Integer, default `2031`) — maximum Y
  level to mine ores at. Default is effectively "no cap."
- `legitMineYLevel` (Integer, default `-59`) — Y level legit
  strip mining descends to and operates at. Only used when
  `legitMine` is on.

### Exposed ore and legit mining

Two related knobs that make mining look more like a real player:
filter to ores the player could see, and/or force Baritone to
navigate there without X-ray hints.

- `allowOnlyExposedOres` (Boolean, default `false`) — restrict
  mining to ore blocks with an air-exposed face. Effective
  against ore-obfuscator anticheats on some servers.
- `allowOnlyExposedOresDistance` (Integer, default `1`) — how
  far out to look for the exposing air block. Increases
  calculation time dramatically as this grows; keep it small.
- `legitMine` (Boolean, default `false`) — disable X-ray-style
  ore discovery entirely. Baritone will only react to an ore
  once it is actually visible to the player (no cache, no
  peeking through walls). Forces exploration on regardless of
  `exploreForBlocks`.
- `legitMineIncludeDiagonals` (Boolean, default `false`) —
  expand the "visible" rule to include diagonal neighbors.
  Intentionally off by default because it causes weird cases
  (e.g. seeing ore across lava without being able to mine to
  it); enable only if you accept the tradeoff described in the
  setting comment.

### Internal mining

When mining adjacent targets, Baritone can opportunistically
break *two* blocks at once instead of repositioning.

- `forceInternalMining` (Boolean, default `true`) — if an ore
  has another ore directly above or below, set a `GoalBlock`
  that reaches both rather than splitting them into two goals.
- `internalMiningAirException` (Boolean, default `true`) — only
  apply the above optimization when the block adjacent to the
  goal isn't air. No effect unless `forceInternalMining` is on.

### Scanning and cache

`MineProcess` periodically scans both the live world and the
chunk cache for new candidates. These settings tune how often
that happens and how much it remembers.

- `mineGoalUpdateInterval` (Integer, default `5`) — rescan
  interval in ticks. Set to `0` to disable periodic rescans.
- `mineMaxOreLocationsCount` (Integer, default `64`) — cap on
  how many target positions `MineProcess` will track at a time.
  Additionally capped by `maxCachedWorldScanCount` for the
  cache side of the scan.
- `maxCachedWorldScanCount` (Integer, default `10`) — cap on
  results from the cached-world scan. Prevents the scan from
  walking outward through the entire cache once it has found
  "enough" hits.
- `extendCacheOnThreshold` (Boolean, default `false`) — when the
  cached scan returns a small-but-nonzero set, also scan the
  live world. Intended for beefy CPUs auto-mining from cache;
  leave off unless you're seeing Baritone ignore nearby
  cache-known ores.
- `exploreForBlocks` (Boolean, default `true`) — when Mine or
  `GetToBlock` doesn't know any locations, wander randomly
  instead of giving up. Overridden to "always on" by
  `legitMine`.

### Drops and pickup

- `mineScanDroppedItems` (Boolean, default `true`) — also treat
  matching dropped items as pathing targets. Keeps Baritone from
  ignoring ore drops it knocks out of reach.
- `mineDropLoiterDurationMSThanksLouca` (Long, default `250`) —
  after mining an ore, wait this many milliseconds to see if it
  drops an item before moving on. Named for the contributor who
  hunted down the timing bug.

### Tools and notifications

- `useSwordToMine` (Boolean, default `true`) — allow swords to
  be used for mining (fastest for some blocks, e.g. cobwebs
  and bamboo).
- `notificationOnMineFail` (Boolean, default `true`) — desktop
  notification when mining fails (no candidates, no reachable
  candidates, etc.).

## Notes & Limitations

- `find` only works for blocks in
  `CachedChunk.BLOCKS_TO_KEEP_TRACK_OF`. The cache is a
  simplified 2-bit representation and does not track every
  block type; arbitrary blocks simply aren't recorded.
- `blacklist` operates on `GetToBlockProcess`, not `MineProcess`.
  During a `mine` run, `MineProcess` already marks individual
  unreachable blocks automatically (see
  `blacklistClosestOnFailure` on the Basic page) — `blacklist`
  the command is only useful during `goto <block>`.
- `tunnel` with three arguments uses `BuilderProcess.clearArea`,
  so it follows the builder's rules for breaking, not the
  mining rules. Mining-specific settings like `legitMine` do
  not apply to a sized tunnel.
- `pickup` uses `FollowProcess`, so only one follow-family
  filter can be active at a time. Starting a `pickup` while
  `follow` is active replaces the follow filter.
