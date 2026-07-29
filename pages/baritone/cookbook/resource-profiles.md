---
title: Resource-usage profiles
---

Three setting profiles for different deployment contexts: one
that tries to look human to anticheat, one that's mostly
defaults but trims the anticheat-evasion overhead, and one that
trades CPU and RAM for raw throughput. A cross-profile diff at
the end lists every setting whose value varies between the
three, so you can mix and match.

See the [cookbook index](../cookbook) for the `# default` /
`# default: X` annotation convention used below.

## Profile: Good citizen (look human to anticheat)

**Scenario.** You're on a server where staff tolerates Baritone
but you'd rather not draw attention. You want movement, look,
and inventory interaction to look as human as they can — no
instant-snap rotations, no parkour micro-decisions, no inhuman
inventory shuffling.

```
#set antiCheatCompatibility true         # default
#set freeLook false                      # default: true
#set blockFreeLook false                 # default
#set smoothLook true                     # default: false
#set smoothLookTicks 5                   # default
#set randomLooking 0.01                  # default
#set randomLooking113 2                  # default
#set rightClickSpeed 4                   # default
#set blockBreakSpeed 6                   # default
#set allowSprint false                   # default: true
#set allowParkour false                  # default
#set allowParkourAscend false            # default: true (gated by allowParkour)
#set allowInventory true                 # default: false
#set inventoryMoveOnlyIfStationary true  # default: false
#set ticksBetweenInventoryMoves 5        # default: 1
#set itemSaver true                      # default: false
```

The deltas that matter most:

- `freeLook false` — send real rotations to the server so the
  direction you appear to look matches the block you're
  interacting with. See [freeLook](../look#free-look).
- `smoothLook true` — interpolate yaw/pitch over
  `smoothLookTicks` ticks instead of snapping. See
  [smoothLook](../look#smoothing).
- `inventoryMoveOnlyIfStationary true` and
  `ticksBetweenInventoryMoves 5` — pace inventory packets. See
  [inventory](../inventory#anticheat-safe-pacing).
- `allowSprint false` — vanilla players sprint in bursts; a
  perpetually-sprinting bot is a classic anticheat flag.
- `itemSaver true` — pause rather than snap a tool; a broken
  pickaxe re-drawing is a bot tell.

`rightClickSpeed` and `blockBreakSpeed` are already the vanilla-
game defaults — don't lower them for this profile. Leave
`randomLooking*` at their defaults too: the tiny yaw/pitch
jitter Baritone adds helps you blend in.

## Profile: Resource-friendly on a lax server

**Scenario.** Server staff don't care about bots, and you don't
care about looking human, but you also don't want Baritone
hogging your client or flooding the server with packets while
you do something else on the side. This profile is essentially
"defaults, but turn off the anticheat-evasion overhead."

```
#set antiCheatCompatibility false        # default: true
#set freeLook true                       # default
#set smoothLook false                    # default
#set randomLooking 0                     # default: 0.01
#set randomLooking113 0                  # default: 2
#set rightClickSpeed 4                   # default
#set blockBreakSpeed 6                   # default
#set allowSprint true                    # default
#set allowParkour false                  # default
#set allowInventory true                 # default: false
#set inventoryMoveOnlyIfStationary false # default
#set ticksBetweenInventoryMoves 1        # default
#set chunkCaching true                   # default
#set pruneRegionsFromRAM true            # default
#set chunkPackerQueueMaxSize 2000        # default
#set cachedChunksExpirySeconds -1        # default
#set repackOnAnyBlockChange true         # default
#set primaryTimeoutMS 500                # default
#set planAheadPrimaryTimeoutMS 4000      # default
```

Most of these are already the out-of-box defaults. Worth calling
out:

- `antiCheatCompatibility false`, `randomLooking 0`,
  `randomLooking113 0` — no jitter, no mandatory server-side
  rotation sync. Small per-tick savings that add up on long
  sessions. See [Look and Rotation](../look).
- `pruneRegionsFromRAM true` (default) plus
  `cachedChunksExpirySeconds -1` (default) — RAM bounded to
  ~1024 blocks of cached regions, disk cache never expires.
  The cache is self-correcting, so old data never causes wrong
  pathing. See [eviction](../caching#eviction).
- `chunkPackerQueueMaxSize 2000` (default) — if you churn
  chunks faster than the packer can keep up (fast travel,
  elytra), the packer sheds oldest work instead of queueing
  unbounded. See [packer backpressure](../caching#packer-backpressure).
- Leave `primaryTimeoutMS` and `planAheadPrimaryTimeoutMS` at
  default. Raising them is a CPU-for-completeness trade you
  don't want on a shared machine.

## Profile: Maximum throughput (CPU is cheap)

**Scenario.** Dedicated machine, you don't care about anticheat
or fan noise, and you want Baritone to path, mine, and build
as fast as the engine allows. Every setting here trades CPU or
RAM for speed, completeness, or both.

```
#set antiCheatCompatibility false        # default: true
#set freeLook true                       # default
#set blockFreeLook false                 # default
#set smoothLook false                    # default
#set randomLooking 0                     # default: 0.01
#set randomLooking113 0                  # default: 2
#set rightClickSpeed 1                   # default: 4
#set blockBreakSpeed 1                   # default: 6
#set allowSprint true                    # default
#set allowParkour true                   # default: false
#set allowParkourAscend true             # default
#set allowInventory true                 # default: false
#set inventoryMoveOnlyIfStationary false # default
#set ticksBetweenInventoryMoves 1        # default
#set itemSaver false                     # default
#set autoTool true                       # default
#set primaryTimeoutMS 2000               # default: 500
#set failureTimeoutMS 5000               # default: 2000
#set planAheadPrimaryTimeoutMS 10000     # default: 4000
#set planAheadFailureTimeoutMS 15000     # default: 5000
#set movementTimeoutTicks 200            # default: 100
#set chunkCaching true                   # default
#set pruneRegionsFromRAM false           # default: true
#set chunkPackerQueueMaxSize 10000       # default: 2000
#set repackOnAnyBlockChange true         # default
#set builderTickScanRadius 10            # default: 5
#set maxCachedWorldScanCount 20          # default: 10
#set renderPath false                    # default: true
#set renderGoal false                    # default: true
#set renderSelectionBoxes false          # default: true
#set renderSelection false               # default: true
#set renderCachedChunks false            # default
```

What's heavy here:

- `rightClickSpeed 1` / `blockBreakSpeed 1` — interact every
  tick. Values below 1 are clamped to 1.
- `primaryTimeoutMS 2000` / `failureTimeoutMS 5000` and their
  `planAhead*` twins raised 2-3× — let A\* search longer before
  giving up. More CPU per planning pass, but fewer dead-end
  re-plans and better long paths. See
  [timeouts](../pathfinding#timeouts).
- `pruneRegionsFromRAM false` — never drop cached regions from
  RAM. With a roaming bot this can grow large; trade disk reads
  for resident memory. See [eviction](../caching#eviction).
- `chunkPackerQueueMaxSize 10000` — let the packer buffer
  aggressively before shedding work, so fast elytra / long
  teleports don't leave cache gaps.
- `builderTickScanRadius 10` — the builder rescans a larger
  ring each tick for schematic discrepancies. More CPU, faster
  reaction to changes outside player reach.
- `maxCachedWorldScanCount 20` — more ore candidates per mining
  scan, larger per-tick cost.
- All `render*` turned off — disable path/goal/selection/cached-
  chunk geometry generation each frame. You lose the visual
  feedback; you gain client-side CPU and GPU. See
  [rendering](../rendering).
- `itemSaver false` — stop pausing to protect low-durability
  tools. If you're OK with breaks, remove the pacing stop.

Skip the `render*` turn-offs if you actually want to watch
Baritone work. They're the biggest perceptual difference; the
other settings only move numbers.

## Differences between the three profiles

Settings where at least two profiles disagree. For any setting
not listed here, all three profiles use the same value (see each
profile's full block above). Read the linked topic pages to
decide whether to pull a value between profiles for your own
mix.

- **antiCheatCompatibility** — Good citizen `true`; others `false`.
- **freeLook** — Good citizen `false`; others `true`.
- **smoothLook** — Good citizen `true`; others `false`.
- **randomLooking** — Good citizen `0.01`; others `0`.
- **randomLooking113** — Good citizen `2`; others `0`.
- **rightClickSpeed** — Max `1`; others `4`.
- **blockBreakSpeed** — Max `1`; others `6`.
- **allowSprint** — Good citizen `false`; others `true`.
- **allowParkour** — Max `true`; others `false`.
- **allowParkourAscend** — Good citizen `false`; others `true`.
- **inventoryMoveOnlyIfStationary** — Good citizen `true`;
  others `false`.
- **ticksBetweenInventoryMoves** — Good citizen `5`; others `1`.
- **itemSaver** — Good citizen `true`; others `false`.
- **primaryTimeoutMS** — Max `2000`; others `500`.
- **failureTimeoutMS** — Max `5000`; others `2000`.
- **planAheadPrimaryTimeoutMS** — Max `10000`; others `4000`.
- **planAheadFailureTimeoutMS** — Max `15000`; others `5000`.
- **movementTimeoutTicks** — Max `200`; others `100`.
- **pruneRegionsFromRAM** — Max `false`; others `true`.
- **chunkPackerQueueMaxSize** — Max `10000`; others `2000`.
- **builderTickScanRadius** — Max `10`; others `5`.
- **maxCachedWorldScanCount** — Max `20`; others `10`.
- **renderPath** / **renderGoal** / **renderSelectionBoxes** /
  **renderSelection** — Max `false`; others `true`.

Everything else (blockFreeLook, smoothLookTicks,
allowInventory, chunkCaching, cachedChunksExpirySeconds,
repackOnAnyBlockChange, renderCachedChunks, autoTool) is the
same across all three — mostly because these settings' defaults
are already the right answer in every profile.
