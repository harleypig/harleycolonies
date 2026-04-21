---
title: Pathfinding & Navigation
---

Pathfinding is Baritone's core loop: given a goal, compute a sequence
of movements that reaches it, then execute them. The commands on this
page all boil down to "set a goal, start pathing, or both." The
settings cover what movements Baritone is allowed to make, how it
estimates cost, how long it spends thinking, and what it does when
things go wrong mid-path.

Pathfinding settings are the largest cluster in Baritone. They're
organized by topic below rather than alphabetically; the index at
the top links to each named setting.

## Settings Index

Alphabetical. Each link jumps to the section that discusses the
setting.

- [allowBreak](#movement-rules-what-baritone-may-do)
- [allowBreakAnyway](#movement-rules-what-baritone-may-do)
- [allowDiagonalAscend](#movement-rules-what-baritone-may-do)
- [allowDiagonalDescend](#movement-rules-what-baritone-may-do)
- [allowDownward](#movement-rules-what-baritone-may-do)
- [allowJumpAtBuildLimit](#movement-rules-what-baritone-may-do)
- [allowOvershootDiagonalDescend](#movement-rules-what-baritone-may-do)
- [allowParkour](#movement-rules-what-baritone-may-do)
- [allowParkourAscend](#movement-rules-what-baritone-may-do)
- [allowParkourPlace](#movement-rules-what-baritone-may-do)
- [allowPlace](#movement-rules-what-baritone-may-do)
- [allowPlaceInFluidsFlow](#movement-rules-what-baritone-may-do)
- [allowPlaceInFluidsSource](#movement-rules-what-baritone-may-do)
- [allowSprint](#movement-rules-what-baritone-may-do)
- [allowVines](#movement-rules-what-baritone-may-do)
- [allowWalkOnBottomSlab](#movement-rules-what-baritone-may-do)
- [allowWaterBucketFall](#movement-rules-what-baritone-may-do)
- [assumeSafeWalk](#movement-rules-what-baritone-may-do)
- [assumeStep](#movement-rules-what-baritone-may-do)
- [assumeWalkOnLava](#movement-rules-what-baritone-may-do)
- [assumeWalkOnWater](#movement-rules-what-baritone-may-do)
- [avoidance](#avoidance)
- [avoidBreakingMultiplier](#cost-tuning)
- [avoidUpdatingFallingBlocks](#fall-safety)
- [axisHeight](#goal-behavior)
- [backfill](#backfill)
- [backtrackCostFavoringCoefficient](#cost-tuning)
- [blacklistClosestOnFailure](#goal-behavior)
- [blockBreakAdditionalPenalty](#cost-tuning)
- [blockBreakSpeed](#execution-details)
- [blockPlacementPenalty](#cost-tuning)
- [blockReachDistance](#execution-details)
- [cancelOnGoalInvalidation](#goal-behavior)
- [considerPotionEffects](#execution-details)
- [costHeuristic](#cost-tuning)
- [costVerificationLookahead](#timeouts)
- [cutoffAtLoadBoundary](#path-shape-and-planning)
- [disconnectOnArrival](#goal-behavior)
- [distanceTrim](#path-shape-and-planning)
- [enterPortal](#goal-behavior)
- [failureTimeoutMS](#timeouts)
- [jumpPenalty](#cost-tuning)
- [maxCostIncrease](#timeouts)
- [maxFallHeightBucket](#fall-safety)
- [maxFallHeightNoWater](#fall-safety)
- [maxPathHistoryLength](#path-shape-and-planning)
- [minimumImprovementRepropagation](#path-shape-and-planning)
- [mobAvoidanceCoefficient](#avoidance)
- [mobAvoidanceRadius](#avoidance)
- [mobSpawnerAvoidanceCoefficient](#avoidance)
- [mobSpawnerAvoidanceRadius](#avoidance)
- [movementTimeoutTicks](#timeouts)
- [notificationOnPathComplete](#goal-behavior)
- [overshootTraverse](#movement-rules-what-baritone-may-do)
- [pathCutoffFactor](#path-shape-and-planning)
- [pathCutoffMinimumLength](#path-shape-and-planning)
- [pathHistoryCutoffAmount](#path-shape-and-planning)
- [pathingMapDefaultSize](#internal-data-structures)
- [pathingMapLoadFactor](#internal-data-structures)
- [pathingMaxChunkBorderFetch](#path-shape-and-planning)
- [pathThroughCachedOnly](#path-shape-and-planning)
- [pauseMiningForFallingBlocks](#fall-safety)
- [planAheadFailureTimeoutMS](#timeouts)
- [planAheadPrimaryTimeoutMS](#timeouts)
- [planningTickLookahead](#path-shape-and-planning)
- [primaryTimeoutMS](#timeouts)
- [rightClickContainerOnArrival](#goal-behavior)
- [simplifyUnloadedYCoord](#path-shape-and-planning)
- [slowPath](#timeouts)
- [slowPathTimeDelayMS](#timeouts)
- [slowPathTimeoutMS](#timeouts)
- [splicePath](#path-shape-and-planning)
- [sprintAscends](#movement-rules-what-baritone-may-do)
- [sprintInWater](#movement-rules-what-baritone-may-do)
- [strictLiquidCheck](#execution-details)
- [walkOnWaterOnePenalty](#cost-tuning)
- [walkWhileBreaking](#execution-details)

Path-rendering settings (`renderPath`, `renderPathAsLine`,
`pathRenderLineWidthPixels`, `colorCurrentPath`, etc.) live on the
[rendering](rendering#path-rendering) page. Follow-radius settings
(`followOffsetDistance`, `followRadius`, etc.) live on the
[following](following) page.

## Commands

### goal

Aliases: `goal`

Set or clear Baritone's current goal without starting pathing. The
goal is a destination, not an instruction to move — `path` picks it
up and starts walking there, but `goal` alone just parks the target.

Coordinates accept `~` and `~<offset>` like vanilla Minecraft
commands, resolved against your current position.

#### Subcommands

- `goal` — set the goal to your current feet position.
- `goal reset` / `goal clear` / `goal none` — erase the goal.
  Prints `There was no goal to clear` if there wasn't one.
- `goal <y>` — `GoalYLevel` at the given Y.
- `goal <x> <z>` — `GoalXZ`. Y is ignored once you arrive at the
  column.
- `goal <x> <y> <z>` — `GoalBlock` at an exact position.

#### Tab completion

- Single-argument completion includes `reset`, `clear`, `none`, and
  `~`.
- Coordinate positions offer `~` as completions.

### goto

Aliases: `goto`

Set a goal *and* start pathing in one command. The most common way
to say "go there."

Two argument shapes:

- **Coordinates** — same forms as `goal` (`goto <y>`,
  `goto <x> <z>`, `goto <x> <y> <z>`). Uses
  `ICustomGoalProcess.setGoalAndPath`.
- **Block name** — `goto <block>` hands off to
  `GetToBlockProcess.getToBlock(destination)`. Baritone searches
  its chunk cache for a matching block and paths to the nearest
  instance. Blocks that aren't in the cache are found through the
  normal exploration mechanic if `exploreForBlocks` is on.

Unlike `goal`, `goto` with no argument is not valid — there's no
reason to path to where you already are.

#### Tab completion

Block name for the single-argument form only. Coordinate arguments
get no tab completion because the parser can't distinguish a
half-typed block name from a half-typed `~` offset.

### path

Aliases: `path`

Start pathing toward the currently-set goal. Runs `repack` first so
the path uses a fresh view of the chunks around you, then calls
`customGoalProcess.path()`.

Has no argument. If no goal is set, Baritone logs the error through
the normal process channel rather than crashing — it simply has
nothing to path to.

### invert

Aliases: `invert`

Wrap the current goal in `GoalInverted`, which flips the cost
function: Baritone paths *away* from the goal instead of toward it.
Useful for "get me out of here" when you have a coordinate you
want to avoid rather than reach.

Running `invert` a second time unwraps the `GoalInverted` back to
the original goal — it toggles rather than stacking wrappers.

#### Error states

- `No goal` — no goal is currently set. Use `goal <...>` first.

### axis

Aliases: `axis`, `highway`

Set a `GoalAxis` — the nearest X=0 or Z=0 line, at the Y level
specified by [`axisHeight`](#goal-behavior). Pairs with the
highway-building conventions common on anarchy servers.

Doesn't start pathing on its own; follow with `path` (or use `goto`
forms) if you want motion.

### come

Aliases: `come`

Set `GoalBlock(ctx.viewerPos())` and start pathing there. The
target is your *camera* position, not your feet. Useful with
hacked clients where the freecam key moves your view while your
player stays still — `come` sends Baritone to wherever you're
looking from.

### surface

Aliases: `surface`, `top`

Find the closest open-air block above you and path there. The
logic walks upward from `max(playerY, seaLevel)` until it finds a
non-air block, then sets `GoalBlock` one block above it. Meant for
"get me out of this cave / mineshaft / shelter."

#### Error states

- `Already at surface` — you're above sea level and the block
  above your head is already air; the command does nothing rather
  than pathing back downward.
- `No higher location found` — the scan reached world height
  without hitting anything solid to stand on. Rare, but possible
  in sky dimensions or broken chunks.

### thisway

Aliases: `thisway`, `forward`

Create a `GoalXZ` `<distance>` blocks in the direction your head
is facing. Doesn't start pathing — use `path` afterward, or use
`goto` if you already know the coordinate you want.

Direction is taken from `ctx.player().getYHeadRot()`, so it tracks
where you're *looking*, not the last direction you were moving.

#### Arguments

- `<distance>` — required. Accepts decimals.

#### Error states

- Argument-count errors if `<distance>` is missing.

### Other goal-setting commands

Several commands live on other topic pages but set pathing goals.
Cross-references:

- [`waypoint goto` / `wp g`](waypoints#wp-goto-g) — path to a saved
  waypoint.
- [`home`](waypoints#home) — path to your saved home waypoint.
- [`follow`](following) — follow an entity type.
- [`mine`](mining#mine) — set an ore mining goal and path to it.
- [`click`](system#click) — GUI goal picker (left-click a block to
  set `GoalBlock`, right-click to set the block above).

## Best Practices

The rest of this page walks through the pathfinding settings by
topic. Use the [settings index](#settings-index) above to jump
directly to a specific setting.

Most of the defaults are carefully tuned — change one setting at a
time and test, rather than flipping a dozen at once.

### Movement rules: what Baritone may do

These gate what kinds of movement the planner will even consider.
The `allow*` settings are toggles; the `assume*` settings tell
the planner to trust environmental/modded behavior that vanilla
doesn't guarantee.

- `allowBreak` (Boolean, default `true`) — may break blocks along
  the path. Turn off to force Baritone to walk around obstacles
  instead of through them.
- `allowBreakAnyway` (List of Block, default empty) — blocks that
  can still be broken even when `allowBreak` is off. Useful for
  leaves, tall grass, and other low-value obstacles.
- `allowSprint` (Boolean, default `true`) — may sprint. Turn off
  if you're on a server that flags sprint-cornering as an
  anticheat violation.
- `allowPlace` (Boolean, default `true`) — may place blocks (for
  pillaring, bridging, sneak-placing). Turn off for pure
  navigation where you don't want to consume inventory.
- `allowPlaceInFluidsSource` (Boolean, default `true`) — may place
  blocks in fluid source blocks.
- `allowPlaceInFluidsFlow` (Boolean, default `true`) — may place
  blocks in flowing fluid.
- `allowDownward` (Boolean, default `true`) — may mine straight
  down. Off forces staircases instead of shafts.
- `allowDiagonalAscend` (Boolean, default `false`) — may step up
  diagonally. "Pretty safe, much safer than diagonal descend."
- `allowDiagonalDescend` (Boolean, default `false`) — may step
  down diagonally. Slightly unsafe in the nether because it can
  brush adjacent unchecked blocks.
- `allowOvershootDiagonalDescend` (Boolean, default `true`) —
  allow sprinting through a descend-then-diagonal combination
  where the player overshoots the landing by one block. Unrelated
  to `allowDiagonalDescend` despite the similar name.
- `allowParkour` (Boolean, default `false`) — may attempt parkour
  jumps. Unreliable around corners and overshoots landings. Turn
  on for fast travel if you can tolerate occasional fall damage.
- `allowParkourAscend` (Boolean, default `true`) — parkour-step up.
  Only takes effect when `allowParkour` is also on.
- `allowParkourPlace` (Boolean, default `false`) — place blocks
  mid-parkour. "Actually pretty reliable" per the comment; doesn't
  add meaningful risk beyond `allowParkour`.
- `allowVines` (Boolean, default `false`) — use vine movements.
  The source comment flat-out says "Almost never turn this on lol"
  — they cause infinite-loop traps in some geometries.
- `allowWalkOnBottomSlab` (Boolean, default `true`) — treat bottom
  slabs as walkable. Turn off on servers where slab pathing is
  flaky; leave on if your base has slab floors.
- `allowWaterBucketFall` (Boolean, default `true`) — fall arbitrary
  distances and place a water bucket under yourself to survive.
  "Reliability: questionable" per the source comment.
- `allowJumpAtBuildLimit` (Boolean, default `false`) — may jump
  while standing at the build limit (feet at y=256 on legacy
  maps). Off by default because it breaks on some large anarchy
  servers.
- `assumeStep` (Boolean, default `false`) — assume step-assist is
  active; don't jump on ascends. Turn on only if another mod
  provides step functionality.
- `assumeSafeWalk` (Boolean, default `false`) — don't sneak on
  backplace traverses. The warning in the source: sneak-backplacing
  *through* a chest with this on will open the chest rather than
  place against it. Leave off unless you know your layout is safe.
- `assumeWalkOnWater` (Boolean, default `false`) — treat still
  water as walkable. Pairs with Jesus mode / Frost Walker;
  enabling without the actual ability will get you drowned.
- `assumeWalkOnLava` (Boolean, default `false`) — treat lava as
  walkable. "If you have Fire Resistance and Jesus then I guess
  you could turn this on lol."
- `sprintAscends` (Boolean, default `true`) — jump and sprint a
  block early on ascends when safe.
- `sprintInWater` (Boolean, default `true`) — keep sprinting when
  entering water.
- `overshootTraverse` (Boolean, default `true`) — accept a
  traverse as successful even if the player ends up one block
  past the destination. Helps when server movement speed is above
  20 m/s.

### Cost tuning

Baritone's A* uses these to decide which path is "cheapest." The
defaults reflect real 1.13+ vanilla tick counts — change them only
if you want Baritone to prefer a different style of path.

- `costHeuristic` (Double, default `3.563`) — the big A* setting.
  Must stay *slightly below* `WALK_ONE_BLOCK_COST` (~3.56) to
  guarantee the optimal path. Raising it past 3.57 (sprinting) or
  4.64 (walking) trades path quality for search speed. Below
  3.5 is always wasted computation. The source comment gives the
  full theory; safest default is the one shipped.
- `backtrackCostFavoringCoefficient` (Double, default `0.5`) —
  discourages circling back. `1.0` disables the feature.
- `blockBreakAdditionalPenalty` (Double, default `2`) — tiebreaker
  nudge so Baritone avoids breaking blocks when the paths are
  otherwise equivalent. Makes fire (break cost 0) not free.
- `blockPlacementPenalty` (Double, default `20`) — deliberately
  high to conserve placement blocks. Decrease if you have bulk
  cobble and want more bridging.
- `jumpPenalty` (Double, default `2`) — extra cost for pressing
  space (ascend, pillar, parkour) because jumping burns hunger.
- `walkOnWaterOnePenalty` (Double, default `3`) — extra cost per
  water block walked, because swimming drains hunger fast.
- `avoidBreakingMultiplier` (Double, default `.1`) — multiplier on
  the break cost of `blocksToAvoidBreaking` (chests, furnaces,
  etc.). Values above 1 flip the sign to "encourage breaking."

### Avoidance

Soft exclusion zones around things you'd rather not path near.
All four `mob*` / `mobSpawner*` settings are gated behind the
`avoidance` master toggle for performance — they're off by default
because building the avoidance map can stall the main thread for
~200 ms when there are lots of mobs around.

- `avoidance` (Boolean, default `false`) — master toggle for the
  four settings below. Off means they do nothing.
- `mobAvoidanceCoefficient` (Double, default `1.5`) — cost
  multiplier near hostile mobs. `1.0` disables; below `1.0` goes
  out of its way to approach mobs.
- `mobAvoidanceRadius` (Integer, default `8`) — radius in blocks.
- `mobSpawnerAvoidanceCoefficient` (Double, default `2.0`) — same
  for mob spawners. Spawners get a higher default because they
  produce mobs faster than you can kill them.
- `mobSpawnerAvoidanceRadius` (Integer, default `16`) — spawners
  leak mobs farther than the mobs themselves typically roam, hence
  the larger radius.

### Fall safety

How far Baritone is willing to drop, and whether it's allowed to
trigger cascading sand/gravel falls.

- `maxFallHeightNoWater` (Integer, default `3`) — maximum fall
  distance onto solid ground without a water bucket. Three blocks
  deals no damage. Bump to 4 or 5 with Feather Falling IV.
- `maxFallHeightBucket` (Integer, default `20`) — maximum fall
  distance when a water bucket is available. Set below 23 (the
  unarmored kill threshold) on purpose because bucket clutch is
  not 100% reliable.
- `avoidUpdatingFallingBlocks` (Boolean, default `true`) — never
  break a block adjacent to unsupported sand or gravel. Prevents
  cascading falls that can bury you or destroy chunk layouts.
- `pauseMiningForFallingBlocks` (Boolean, default `true`) — after
  breaking, wait for falling blocks to settle before continuing.
  Turning off gets you a faster mine run at the risk of being
  buried.

### Timeouts

Budgets for how long the planner is allowed to think. If it finds
a path before the primary timeout, it stops; if not, it keeps
thinking up to the failure timeout.

- `primaryTimeoutMS` (Long, default `500`) — pathing ends after
  this much time *if* a valid path has been found. The typical
  case — Baritone spends 500 ms looking, then commits.
- `failureTimeoutMS` (Long, default `2000`) — hard ceiling. If no
  path has been found by now, the planner gives up with a
  failure.
- `planAheadPrimaryTimeoutMS` (Long, default `4000`) — same as
  `primaryTimeoutMS` but for the *plan-ahead* pass that extends
  the current path while you're already walking.
- `planAheadFailureTimeoutMS` (Long, default `5000`) — hard
  ceiling for plan-ahead.
- `movementTimeoutTicks` (Integer, default `100`) — if any single
  movement takes this many ticks beyond its cost estimate, cancel
  it and replan. Catches stuck-in-a-block cases.
- `maxCostIncrease` (Double, default `10`) — if a movement's cost
  jumps by more than this between calculation and execution (e.g.
  lava spread across the path), cancel and replan rather than
  walking into it.
- `costVerificationLookahead` (Integer, default `5`) — stop five
  movements before anything with `COST_INF`. Prevents walking up
  to a still-spreading lava flow and recalculating at the edge.
- `slowPath` (Boolean, default `false`) — debug mode. Calculate
  each node one-at-a-time so you can watch the search animate.
- `slowPathTimeDelayMS` (Long, default `100`) — milliseconds
  between nodes in `slowPath` mode.
- `slowPathTimeoutMS` (Long, default `40000`) — replaces
  `primaryTimeoutMS`/`failureTimeoutMS` when `slowPath` is on.

### Path shape and planning

What Baritone does with the path once it has one: splicing segments
together, trimming, discarding old history, planning ahead.

- `splicePath` (Boolean, default `true`) — when a new segment
  starts where the current one ends, splice them into one long
  path instead of queuing the second as a separate "next" segment.
  Off hurts planning-ahead performance; rarely worth disabling.
- `planningTickLookahead` (Integer, default `150`) — start
  planning the next segment when the remaining movements in the
  current one sum to less than this many ticks.
- `pathCutoffFactor` (Double, default `0.9`) — cut off the last
  10% of any path regardless of chunk-load state. Guards against
  paths terminating in unsafe partial chunks.
- `pathCutoffMinimumLength` (Integer, default `30`) — only apply
  the static cutoff to paths of at least this many movements.
- `maxPathHistoryLength` (Integer, default `300`) — once you're
  more than 300 movements into a path, discard the oldest
  segments.
- `pathHistoryCutoffAmount` (Integer, default `50`) — how many
  old movements to drop when the history is too long.
- `distanceTrim` (Boolean, default `true`) — drop incorrect
  positions from the builder's set once they're far enough away.
  Helps performance in huge schematics; hurts reliability at the
  extremes.
- `cutoffAtLoadBoundary` (Boolean, default `false`) — after
  calculating a path (possibly through cached chunks), cut it off
  at the loaded-chunk boundary. The comment notes this is safer
  to leave *off* nowadays; cached chunks are simplified but
  usually good enough.
- `pathThroughCachedOnly` (Boolean, default `false`) — only use
  cached chunks, ignoring loaded ones. The comment says "Never
  turn this on" — it exists for internal debugging.
- `pathingMaxChunkBorderFetch` (Integer, default `50`) — how many
  times pathing may step outside loaded/cached chunks before
  concluding "I've run out of known terrain" and stopping.
- `simplifyUnloadedYCoord` (Boolean, default `true`) — for
  `GoalBlock` in unloaded chunks, replace with `GoalXZ` until you
  get close enough for Y to matter. Saves huge amounts of search
  time on long-distance goals.
- `minimumImprovementRepropagation` (Boolean, default `true`) —
  don't repropagate cost improvements smaller than 0.01 ticks.
  They're floating-point noise.

### Goal behavior

What Baritone does when it arrives, when goals change, and how
specific goal types behave.

- `axisHeight` (Integer, default `120`) — Y level the `axis`
  command goes to when setting its `GoalAxis`.
- `notificationOnPathComplete` (Boolean, default `true`) — fire a
  desktop notification when pathing finishes.
- `disconnectOnArrival` (Boolean, default `false`) — log out of
  the server when the goal is reached. Useful for overnight AFK
  travel.
- `enterPortal` (Boolean, default `true`) — when the goal is a
  nether portal block, walk all the way in rather than stopping
  one block short.
- `rightClickContainerOnArrival` (Boolean, default `true`) — when
  `goto`ing a chest/furnace/ender chest, open it on arrival.
- `cancelOnGoalInvalidation` (Boolean, default `true`) — when the
  goal changes mid-path and the old path no longer ends at the
  goal, stop. Currently only active during `mine` and `follow`.
  Turn off if you want Baritone to finish walking to the old
  destination anyway (e.g. to pick up drops that were at the ore
  location).
- `blacklistClosestOnFailure` (Boolean, default `true`) — when
  `GetToBlockProcess` or `MineProcess` fails to find a path,
  mark the closest instance as unreachable and try the next one
  rather than giving up. `GetToBlock` blacklists the whole
  connected vein; `Mine` blacklists only individual blocks.

### Execution details

Low-level behavior Baritone uses while *executing* a path.

- `walkWhileBreaking` (Boolean, default `true`) — don't stop
  walking forward just because there's a block to break on the
  way. Faster, but can occasionally overshoot into the block
  you're breaking if your ping is bad.
- `blockBreakSpeed` (Integer, default `6`) — ticks between one
  instant break and the next. Default 6 matches vanilla. Only
  applies to non-one-tick breaks; values below 1 are clamped.
- `blockReachDistance` (Float, default `4.5`) — reach distance
  in blocks. 4.5 matches vanilla survival. Servers with
  extended-reach allowances may tolerate higher values.
- `considerPotionEffects` (Boolean, default `true`) — factor
  Haste, Mining Fatigue, etc. into break costs so the path cost
  matches reality.
- `strictLiquidCheck` (Boolean, default `false`) — don't break
  blocks adjacent to liquids. Enable if a mod adds non-vanilla
  fluid physics that could drown the pathing.

### Backfill

- `backfill` (Boolean, default `false`) — after breaking a
  block to pass through it, place a block back in its
  original position once you've moved on.

Runs as a dedicated `BackfillProcess`: every block Baritone
breaks while pathing gets recorded (position + pre-break
state), and the process later tries to place the original
block back from the hotbar. The effect is "leave no trail"
pathing — mined tunnels close up behind you.

Conflicts with [`allowParkour`](#movement-rules-what-baritone-may-do):
enabling both at once is rejected at runtime with
`Backfill cannot be used with allowParkour true`, and
`backfill` is force-toggled off. If you want backfill,
allowParkour has to stay off.

Other constraints and caveats:

- The block must still be in your inventory. Baritone pulls
  it up to the hotbar via `allowInventory` if needed; without
  [`allowInventory`](inventory), only hotbar stock is
  available.
- Backfill only places vanilla-identical blocks. A tunnel
  through stone backfills with stone only if you had stone;
  it won't guess a substitute.
- Backfill yields to other processes via `DEFER` when there's
  nothing to place, so it doesn't interfere with active
  pathing or mining.
- Placement respects all the normal rotation/reach rules, so
  backfilling may pause briefly mid-path to aim at an
  awkward spot.

### Internal data structures

Changing these won't usually improve anything. They exist for
rare low-memory or profiling scenarios.

- `pathingMapDefaultSize` (Integer, default `1024`) — initial
  capacity of the pathing hash map.
- `pathingMapLoadFactor` (Float, default `0.75`) — load factor.
  Lower is faster but uses more memory.

## Notes & Limitations

- `goal` and `goto` both accept the same coordinate forms, but
  `goal` *only* sets the goal. `goto` also calls `setGoalAndPath`,
  which means it implicitly starts pathing. Use `goal` when you
  want to stage the destination (e.g. before `invert`) without
  walking there.
- `goto <block>` goes through `GetToBlockProcess`, which searches
  the chunk cache — blocks outside your loaded+cached area aren't
  visible to it until exploration finds them. Run `repack` or
  walk through the area first if you know a block is there but
  Baritone claims it isn't.
- `invert` with no goal is an error, not a no-op. Set a goal
  first. Running it again unwraps instead of double-wrapping,
  so `invert; invert` leaves you with the original goal and a
  fresh path.
- `path` calls `repack` before pathing. Using `path` instead of
  just re-running `goto` is a good way to force a fresh chunk
  scan if you suspect the cache is stale.
- `surface` compares the block above your head to decide "already
  at surface." Standing on a grass block with a leaf canopy
  overhead counts as *not* at surface, so you may get pathing
  upward even in situations you'd subjectively call "outside."
- `come` uses camera position, not feet position, so it behaves
  differently in freecam than without. In regular survival the
  two coincide.
- `thisway` uses your head yaw, not your movement direction.
  Looking sideways while sprinting forward produces a `GoalXZ` to
  your side.
- Several settings on this page (`costHeuristic`,
  `primaryTimeoutMS`, `failureTimeoutMS`) interact with each
  other. Tuning one in isolation can make the others ineffective.
  Change in small increments.
- Settings defined in Java but marked `@JavaOnly` (like
  `allowJumpAt256`) don't appear in `set list` and can't be
  changed from chat — they exist to keep API consumers from
  breaking. See [`set`](system#set-setting-settings) for details
  on how the command filters them.
