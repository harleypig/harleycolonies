---
title: Cookbook
---

Task-oriented recipes — multi-command workflows and setting
combinations that solve a concrete problem. Each recipe links
out to the topic pages for the underlying settings and
commands.

**A note on defaults.** Every recipe below lists the full set of
settings that are related to the task, not just the ones the
recipe changes. Each `#set` line is annotated `# default` if
that value is already the out-of-box default, or `# default: X`
if the recipe is overriding a different default. The reason to
include defaults explicitly is that these related settings are
the ones you're most likely to want to tweak for your own
situation — seeing them all at once gives you a complete menu.
When pasting into chat, paste only the `#set <name> <value>`
portion; when pasting into
`.minecraft/baritone/settings.txt`, drop the `#set` prefix (the
trailing `# ...` annotations are valid comments in that file).

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
  interacting with. See [freeLook](look#free-look).
- `smoothLook true` — interpolate yaw/pitch over
  `smoothLookTicks` ticks instead of snapping. See
  [smoothLook](look#smoothing).
- `inventoryMoveOnlyIfStationary true` and
  `ticksBetweenInventoryMoves 5` — pace inventory packets. See
  [inventory](inventory#anticheat-safe-pacing).
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
  sessions. See [Look and Rotation](look).
- `pruneRegionsFromRAM true` (default) plus
  `cachedChunksExpirySeconds -1` (default) — RAM bounded to
  ~1024 blocks of cached regions, disk cache never expires.
  The cache is self-correcting, so old data never causes wrong
  pathing. See [eviction](caching#eviction).
- `chunkPackerQueueMaxSize 2000` (default) — if you churn
  chunks faster than the packer can keep up (fast travel,
  elytra), the packer sheds oldest work instead of queueing
  unbounded. See [packer backpressure](caching#packer-backpressure).
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
  [timeouts](pathfinding#timeouts).
- `pruneRegionsFromRAM false` — never drop cached regions from
  RAM. With a roaming bot this can grow large; trade disk reads
  for resident memory. See [eviction](caching#eviction).
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
  [rendering](rendering).
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

## Flatten a selection from the top down

**Problem.** You want to flatten terrain (or any filled
region) using `sel cleararea`, but the default bottom-up
build order means Baritone digs the lowest layer first and
leaves you standing in a pit under intact stone. Dark pockets
spawn mobs while you work.

**Solution.** Turn on layered building with top-down order
*before* you run `cleararea`. All `sel` fill actions dispatch
through `BuilderProcess.build`, so they obey `buildInLayers`
and `layerOrder` the same way a schematic build does.

The block below lists every layered-building setting —
`layerHeight`, `startAtLayer`, and `skipFailedLayers` aren't
required for the minimal recipe but are shown so you can see
the complete set of knobs and tune them for your specific
flatten:

```
#set buildInLayers true          # default: false
#set layerOrder true             # default: false (false = bottom-up, true = top-down)
#set layerHeight 1               # default
#set startAtLayer 0              # default
#set skipFailedLayers false      # default
#sel pos1
<stand at the opposite corner>
#sel pos2
#sel cleararea
```

What each line does:

- `buildInLayers true` — clear one Y-level at a time instead
  of pathing freely through the cuboid.
- `layerOrder true` — process layers from highest Y to lowest
  instead of lowest to highest. The top of the selection goes
  first, so the cleared region stays open to the sky as you
  work down.
- `sel pos1` / `sel pos2` — two corners of the cuboid to
  flatten. See [sel](building#sel--selection--s) for
  alternative ways to build selections (e.g., via the
  selection wand).
- `sel cleararea` — shortcut for `sel set air`. Runs against
  every active selection.

**When the selection is tall.** `layerHeight 1` means one pass
per Y-level; for a 30-block-tall hill that's 30 passes and a
lot of vertical repositioning. Bump it up:

```
#set layerHeight 3               # default: 1
```

The trade-off is that inside each 3-block slice the builder
can reach blocks in any order, so you briefly see a
3-layer-deep dig face instead of a flat ceiling. For daylight
work that's fine; for night work with mobs nearby, keep
`layerHeight 1`.

**Resetting afterwards.** `buildInLayers` and `layerOrder`
stay on until you turn them off, and they affect normal
`build <schematic>` runs too (that's what they're designed
for). If you were only using them for this one clear:

```
#set reset buildInLayers
#set reset layerOrder
#set reset layerHeight
```

Or click the "click to revert" line each `#set` command
printed — one click per setting, no typing. See
[`set`](system#set-setting-settings).

**Relevant settings:**
[buildInLayers](building#layered-building),
[layerOrder](building#layered-building),
[layerHeight](building#layered-building),
[startAtLayer](building#layered-building),
[skipFailedLayers](building#layered-building).

**Related:**
[sel cleararea](building#sel--selection--s),
[Best Practices: Layered building](building#layered-building).

## Replace a selection with dirt, keeping grass blocks

**Problem.** You want to normalize the terrain in a selection to
dirt — digging up whatever sand, gravel, stone, etc. happens to
be there — but you don't want to touch the grass blocks on top.
If you do touch them, surrounding grass will spread back onto
the freshly-placed dirt, the builder will see grass where it
asked for dirt, and it will keep breaking and re-placing the
top layer forever.

**Solution.** Tell the builder that grass blocks are an
acceptable substitute for dirt, then fill the selection with
dirt. `sel set dirt` dispatches through `BuilderProcess.build`,
so it honors [`buildValidSubstitutes`](building#block-matching-tolerance)
the same way a schematic build does: the builder looks at each
position, sees grass where it wanted dirt, and treats it as
already-correct instead of breaking it.

The block below shows the three block-matching-tolerance
settings that are most relevant here. Only `buildValidSubstitutes`
changes; the others are shown at default so you know what
Baritone is doing with unmentioned blocks.

```
#set buildValidSubstitutes dirt->grass_block   # default: {} (empty)
#set buildIgnoreBlocks                         # default: [] (empty)
#set buildIgnoreExisting false                 # default
#sel pos1
<stand at the opposite corner>
#sel pos2
#sel set dirt
```

What each line does:

- `buildValidSubstitutes dirt->grass_block` — at any position
  where the fill asks for dirt, a grass block is accepted as-is.
  Existing dirt is also accepted (identical blocks always match);
  everything else gets dug up and replaced.
- `sel pos1` / `sel pos2` — corners of the cuboid to normalize.
- `sel set dirt` — fill the selection with dirt. Grass blocks
  are skipped thanks to the substitute mapping.

**Why not `sel replace`?** The [`sel replace`](building#fill-actions)
action needs an explicit list of blocks to swap out —
`sel replace stone sand gravel dirt`, for instance. That works
if you know exactly which blocks are in the selection, but it
won't touch anything you forgot to list. The `buildValidSubstitutes`
approach inverts the question: replace *everything* with dirt
except the one block type you want to preserve.

**Variants.** To keep other dirt-adjacent blocks too (podzol,
coarse dirt, dirt paths), extend the substitute list:

```
#set buildValidSubstitutes dirt->grass_block,podzol,coarse_dirt,dirt_path   # default: {} (empty)
```

Dirt-to-dirt mappings aren't needed — identical blocks always
match without a substitute entry.

**Resetting afterwards.** `buildValidSubstitutes` persists and
will affect subsequent `build <schematic>` runs (any schematic
calling for dirt will also accept grass at that position — often
not what you want for a real build). Clear it when you're done:

```
#set reset buildValidSubstitutes
```

Or click the "click to revert" line the `#set` command printed.

**Relevant settings:**
[buildValidSubstitutes](building#block-matching-tolerance),
[buildSubstitutes](building#block-matching-tolerance),
[buildIgnoreBlocks](building#block-matching-tolerance).

**Related:**
[sel set](building#fill-actions),
[sel replace](building#fill-actions),
[Best Practices: Block-matching tolerance](building#block-matching-tolerance).

## Create a schematic of a spawner farm

**Heads up: this is mostly outside Baritone's wheelhouse.**
Baritone is a pathfinding and block-placement bot — it builds
*from* schematics and clears or fills selected regions, but it
doesn't design structures and it doesn't save schematics.
Creating the schematic itself is a Litematica job. Baritone can
only help with prep (clearing, bulk fills, material gathering)
and pasting existing schematics.

**Before you start:** read
[Don't break spawners](#dont-break-spawners-or-existing-torches-while-clearing-or-building)
— it's very easy to lose the spawner to a stray
`sel cleararea` or a mistimed `mine`.

1. **Pick and prep the build site.**
   - `#goto <x> <y> <z>` — pathfind in.
   - `#sel pos1` / `#sel pos2` at opposite corners to define
     the volume.
   - `#sel cleararea` — empty the volume. **Make sure the
     spawner is outside the selection**, or skip this step.

2. **Build the farm.** Baritone won't design it. Options:
   - **By hand** in creative.
   - **WorldEdit** (`//set`, `//walls`, `//cyl`, ...) for bulk
     geometry.
   - **Baritone `sel` helpers** for the simple bits:
     - `#sel fill <block>` — fill solid.
     - `#sel walls <block>` — four vertical walls only
       (floor and ceiling untouched).
     - `#sel shell <block>` — all six outer faces. Does not
       clear the interior — if you want a hollow box, run
       `#sel cleararea` first, then `#sel shell`.
     - `#sel sphere` / `#sel hsphere` / `#sel cylinder` /
       `#sel hcylinder` — inscribed solid or hollow
       spheres/cylinders inside the selection's bounding box.
     - `#sel replace <from> <to>` — swap blocks in place.

3. **Save the schematic with Litematica** (not Baritone).
   - Litematica Area Editor (`M` → Area Editor), set corners
     around the finished farm.
   - `Save Schematic` → `.litematic` under
     `.minecraft/schematics/`.

4. **(Optional) Rebuild elsewhere with Baritone.**
   - Load the schematic in Litematica so it renders as a ghost.
   - `#litematica` — Baritone places blocks to match the
     Litematica projection. (`#schematica` is the legacy mod,
     generally unavailable on modern MC versions.)
   - Or, for `.schem` / `.schematic` files you just want to
     drop without the Litematica ghost, `#build <filename> <x> <y> <z>`.

**Gotchas.**

- `sel` fill actions operate on the current selection's
  bounding box only. The built-in shapes
  (`set`/`walls`/`shell`/`sphere`/`hsphere`/`cylinder`/`hcylinder`)
  cover cuboids and inscribed ellipsoids; anything more
  procedural — branching tunnels, shaped rooms, diagonal
  layouts — needs WorldEdit or an external editor.
- `cleararea`, `fill`, and `shell` will all happily destroy or
  wall in a spawner. See
  [Don't break spawners](#dont-break-spawners-or-existing-torches-while-clearing-or-building).
- Spawner farms depend on exact light levels, water-column
  heights, and mob-cap geometry. Verify manually before saving;
  Baritone and Litematica won't flag a design flaw.
- Litematica saves blocks; tile-entity inventories (chest or
  hopper contents) generally do not round-trip.

**Related:**
[Don't break spawners](#dont-break-spawners-or-existing-torches-while-clearing-or-building),
[sel](building#sel--selection--s),
[build](building#build),
[litematica](building#litematica),
[schematica](building#schematica).

## Don't break spawners (or existing torches) while clearing or building

**Problem.** You're either clearing an area with `sel cleararea`
or building a schematic around an existing mob spawner, and you
don't want Baritone to break the spawner — losing a spawner
destroys it permanently in survival. Same question for torches
you've already placed around the spawner: you want them to stay,
without having to add them to the schematic.

**Solution.** Add the blocks you want to preserve to
[`buildIgnoreBlocks`](building#block-matching-tolerance).
Whenever the builder looks at a position that's air in the
schematic but contains one of these blocks in the world, it
treats the position as already-correct and moves on.

The settings below are the full block-matching-tolerance knobs
that interact with this recipe. Only `buildIgnoreBlocks`
changes; `buildValidSubstitutes` is shown empty because you'd
reach for it next if the schematic asks for non-air at a
spawner (see below).

```
#set buildIgnoreBlocks spawner,torch,wall_torch   # default: [] (empty)
#set buildValidSubstitutes                        # default: {} (empty)
#set buildIgnoreExisting false                    # default
#set okIfAir                                      # default: [] (empty)
#sel pos1
<stand at the opposite corner>
#sel pos2
#sel cleararea
```

What each line does:

- `buildIgnoreBlocks spawner,torch,wall_torch` — treat these
  three blocks as "effectively air" when the schematic wants
  air. `wall_torch` is the side-mounted variant; include it
  separately from the standing `torch`. Add
  `soul_torch,soul_wall_torch` if you use soul fire lighting.
- `sel cleararea` — shortcut for `sel set air`. The builder
  still visits every cell in the cuboid, but it skips the
  protected blocks instead of breaking them.

**The air caveat.** `buildIgnoreBlocks` only fires when the
schematic asks for air at a position. It's perfect for
`sel cleararea` (where every cell is air) and for schematic
builds whose schematic is air at the spawner/torch positions —
but if your schematic explicitly asks for stone (or any non-air
block) where a spawner currently sits, the spawner will be
broken regardless of this list. Two fixes for that case:

- **Preferred: include the spawner in the schematic.** Place a
  spawner block at that position in your schematic editor. The
  world spawner's block state matches, so the builder leaves it
  alone. The spawner's NBT (the mob type) isn't compared — only
  the block state — so you don't need to match the mob type in
  the schematic.
- **Alternative: use `buildValidSubstitutes`** for each block
  type the schematic asks for at the spawner's position. For
  example, if the schematic has a stone floor covering the
  spawner:

  ```
  #set buildValidSubstitutes stone->spawner   # default: {} (empty)
  ```

  Now any position where the schematic wants stone but the world
  has a spawner is treated as correct. The same trick works for
  torches if your schematic asks for solid blocks where your
  existing wall torches are, but it gets awkward fast — one
  mapping per schematic block type. Fixing the schematic is
  usually easier.

**Can Baritone auto-place torches on spawners?** No — there is
no built-in "find spawners and light them" command. The mob-
spawner settings that do exist
([`mobSpawnerAvoidanceCoefficient`](pathfinding#avoidance),
[`mobSpawnerAvoidanceRadius`](pathfinding#avoidance)) only
influence pathing costs, telling Baritone to route around
spawners rather than through them. They do nothing about
lighting.

If you want spawners lit automatically, the closest workaround
is to save a tiny schematic — a spawner with torches on each
side at the positions you want — and `build <schematic> <x> <y> <z>`
at each known spawner's location. The spawner itself will match
what's already there (see above); the torches will be placed
around it. That works per-spawner but requires you to know each
spawner's coordinates first. Finding spawners is a separate
problem Baritone doesn't solve either — they don't emit a block
signal that [`find`](mining#find) can latch onto because they're
block entities rather than ores.

**Resetting afterwards.** `buildIgnoreBlocks` persists until
cleared and applies to every subsequent `build` / `sel` run —
often that's what you want, so leaving it on is fine. Clear it
if you want a future schematic to actually replace torches or
spawners:

```
#set reset buildIgnoreBlocks
```

**Relevant settings:**
[buildIgnoreBlocks](building#block-matching-tolerance),
[buildValidSubstitutes](building#block-matching-tolerance),
[buildSubstitutes](building#block-matching-tolerance),
[mobSpawnerAvoidanceCoefficient](pathfinding#avoidance),
[mobSpawnerAvoidanceRadius](pathfinding#avoidance).

**Related:**
[sel cleararea](building#fill-actions),
[Best Practices: Block-matching tolerance](building#block-matching-tolerance).
