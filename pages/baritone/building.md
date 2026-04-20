---
title: Building
---

Building commands hand Baritone a block-by-block plan and let it
path, break, and place until the plan matches reality. Plans come
from three sources: a schematic file on disk (`build`), an open
schematic in the Litematica or Schematica mod (`litematica`,
`schematica`), and ad-hoc volumetric operations against a
selection (`sel`). All four funnel through the same
`BuilderProcess`, so the settings on this page apply uniformly
regardless of which entry point you used.

The `sel` command is also the WorldEdit-style tool for creating
and transforming selections — the same selection objects used
by the click-based picker on the [`click`](system#click) command
and whose colors/line widths live on
[Selection rendering](rendering#selection-rendering).

## Settings Index

Alphabetical. Each link jumps to the section that discusses the setting.

- [breakCorrectBlockPenaltyMultiplier](#incorrect-block-pacing)
- [breakFromAbove](#break-from-above)
- [buildIgnoreBlocks](#block-matching-tolerance)
- [buildIgnoreDirection](#block-matching-tolerance)
- [buildIgnoreExisting](#block-matching-tolerance)
- [buildIgnoreProperties](#block-matching-tolerance)
- [buildInLayers](#layered-building)
- [buildOnlySelection](#selection-only-building)
- [buildRepeat](#build-repetition)
- [buildRepeatCount](#build-repetition)
- [buildRepeatSneaky](#build-repetition)
- [buildSchematicMirror](#orientation-rotation-and-mirror)
- [buildSchematicRotation](#orientation-rotation-and-mirror)
- [buildSkipBlocks](#block-matching-tolerance)
- [buildSubstitutes](#block-matching-tolerance)
- [buildValidSubstitutes](#block-matching-tolerance)
- [builderTickScanRadius](#scan-and-notifications)
- [goalBreakFromAbove](#break-from-above)
- [incorrectSize](#incorrect-block-pacing)
- [layerHeight](#layered-building)
- [layerOrder](#layered-building)
- [mapArtMode](#map-art)
- [notificationOnBuildFinished](#scan-and-notifications)
- [okIfAir](#block-matching-tolerance)
- [okIfWater](#block-matching-tolerance)
- [placeIncorrectBlockPenaltyMultiplier](#incorrect-block-pacing)
- [schematicFallbackExtension](#schematic-file-loading)
- [schematicOrientationX](#orientation-rotation-and-mirror)
- [schematicOrientationY](#orientation-rotation-and-mirror)
- [schematicOrientationZ](#orientation-rotation-and-mirror)
- [skipFailedLayers](#layered-building)
- [startAtLayer](#layered-building)

## build

Aliases: `build`

Load a schematic file from disk and start building it.

### Arguments

- `<filename>` — path relative to `.minecraft/schematics/`.
  If the filename has no extension, Baritone appends
  `schematicFallbackExtension` (default `schematic`). Absolute
  paths and `~` work via `RelativeFile`.
- `[<x> <y> <z>]` — optional build origin. Coordinates accept
  `~` relatives. Defaults to your feet position when omitted.
  This is the schematic's origin corner; see
  [Orientation, rotation, and mirror](#orientation-rotation-and-mirror)
  for which corner that is.

### Supported formats

The `SchematicSystem` registry holds three default formats on
this branch. Extension is matched case-insensitively:

- `.schematic` — MCEdit format.
- `.schem` — Sponge Schematic Specification, versions 1 and 2.
- `.litematic` — Litematica format, version 7 only (1.21+
  schematics). Older versions error out with
  "This litematic Version is too old."

### Error states

- `Cannot find <path>` — no file exists at the resolved path
  (with or without the fallback extension).
- `Cannot load <path> because I do not know which schematic
  format that is. Please rename the file to include the correct
  file extension.` — the file exists but has an unrecognized
  extension, and no fallback-extension file exists either.
- `Unsupported schematic format. Reckognized file extensions
  are: ...` — the file exists with a known extension but the
  registry rejected it. Happens when the registry doesn't
  include a parser for it at runtime (e.g. a mod that only
  registers its own format).
- `Couldn't load the schematic. Either your schematic is
  corrupt or this is a bug.` — parser returned null; almost
  always a corrupt file.

### Tab completion

File completer rooted at `.minecraft/schematics/` for the first
argument. `RelativeBlockPos` completer for the coordinate
arguments.

## sel / selection / s

Aliases: `sel`, `selection`, `s`

WorldEdit-style selection and volumetric-build tool. A
*selection* is a pair of block positions (`pos1` / `pos2`)
defining a cuboid; multiple selections can coexist, and fill
operations apply to all of them at once.

The bounding boxes are drawn through
[Selection rendering](rendering#selection-rendering) — the
`pos1` marker is also rendered separately, in its own color,
while you're mid-edit.

Alternative ways to create a selection: the
[`click`](system#click) command's left-click-drag.

### Subcommands

#### sel pos1 / p1 / 1

Set the first corner of a pending selection.

- No arguments: the corner becomes your viewer position (feet or
  camera depending on perspective).
- `<x> <y> <z>` — relative coordinates accepted via `~`.

#### sel pos2 / p2 / 2

Set the second corner and finalize the selection. Same argument
rules as `pos1`.

Errors with `Set pos1 first before using pos2` if no `pos1` is
pending.

#### sel clear / c

Remove every selection and clear any pending `pos1`. Prints
`Removed N selections`.

#### sel undo / u

Undo the most recent sel action in reverse order: a pending
`pos1` first, then the most recently-created selection (which
comes back as a `pos1` for re-edit). Errors with
`Nothing to undo!` when there's nothing to roll back.

#### Fill actions

Every fill action takes an optional `[<block>]` argument that
defaults to stone via `ForBlockOptionalMeta` if omitted (for
`set`/`walls`/etc.) or to air for `cleararea`. All fill actions
run against **every** current selection — they union into a
single `CompositeSchematic` with the lowest-coordinate corner as
the origin. If there are no selections you get
`No selections`.

- `sel set / fill / s / f [<block>]` — fill the full cuboid.
- `sel walls / w [<block>]` — fill only the four vertical walls.
- `sel shell / shl [<block>]` — walls plus a floor and ceiling.
- `sel sphere / sph [<block>]` — inscribed solid sphere (uses
  the selection dimensions as the sphere's bounding box).
- `sel hsphere / hsph [<block>]` — hollow inscribed sphere.
- `sel cylinder / cyl [<block>] [<axis>]` — inscribed solid
  cylinder. `<axis>` is `x`/`y`/`z`, default `y`.
- `sel hcylinder / hcyl [<block>] [<axis>]` — hollow inscribed
  cylinder.
- `sel cleararea / ca` — shortcut for `sel set air`.
- `sel replace / r <blocks...> <with>` — swap one or more block
  types for another. The last argument is the replacement; all
  preceding arguments are the targets.

All fill actions dispatch through `BuilderProcess.build`, so
they're subject to the same settings (layer order, retry on
missing blocks, etc.) as a schematic build.

#### sel copy / cp [<x> <y> <z>]

Capture every selection's blocks into a clipboard
(`StaticSchematic`). The optional offset defaults to your viewer
position and is used later by `paste` as a placement anchor.

Errors with `No selections`.

#### sel paste / p [<x> <y> <z>]

Build the clipboard at the given offset (default: viewer
position). Errors with `You need to copy a selection first` if
the clipboard is empty.

The clipboard persists until another `copy` or until the client
restarts. It is not serialized to disk.

#### sel expand / ex <target> <direction> <blocks>

Grow one or more selections along a direction. `<target>` is one
of:

- `all` / `a` — transform every selection.
- `newest` / `n` — only the most recently-created selection.
- `oldest` / `o` — only the first-created selection.

`<direction>` is a cardinal or vertical direction (`north`,
`south`, `east`, `west`, `up`, `down`). `<blocks>` is an
integer. Prints `Transformed N selections`.

#### sel contract / ct <target> <direction> <blocks>

Shrink along a direction. Same argument rules as `expand`.

#### sel shift / sh <target> <direction> <blocks>

Move the selection without resizing. Same argument rules as
`expand`.

### Error states

- `an action` (type error) — the first argument didn't match any
  sel action or alias.
- `Set pos1 first before using pos2` — as above.
- `Nothing to undo!` — as above.
- `No selections` — a fill, copy, or transform ran with no
  selections active.
- `No selections found` — same condition, different message,
  from the expand/contract/shift branch.
- `You need to copy a selection first` — paste with empty
  clipboard.
- `Invalid transform type` — expand/contract/shift got a
  `<target>` that isn't `all`/`newest`/`oldest`.

### Tab completion

- First argument: every action name and alias.
- After `pos1`/`pos2`: `RelativeBlockPos` completer.
- After a fill action: `ForBlockOptionalMeta` for the block;
  for `cylinder`/`hcylinder`, `ForAxis` for the axis argument.
- After `expand`/`contract`/`shift`: transform target names,
  then `ForDirection`.

## litematica

Aliases: `litematica`

Build a schematic currently loaded in the Litematica mod.

### Arguments

- `[<#>]` — optional 1-based placement index. Litematica can
  have multiple placements loaded; `litematica 2` builds the
  second. Defaults to 1 (the first placement) when omitted.

### Error states

- `Litematica is not present` — the Litematica mod isn't
  loaded. Install the mod or use `build <file>` instead.
- `List of placements has no entry <N>` — the requested
  placement index is out of range.
- Litematica version errors bubble up from the format parser:
  versions 4, 5, and 6 (pre-1.21) are rejected with "too old"
  messages.

### Tab completion

None.

## schematica

Aliases: `schematica`

Build a schematic currently loaded in the Schematica mod. This
is the legacy equivalent of `litematica` and generally isn't
available on modern Minecraft versions — Schematica has not been
maintained for current MC releases.

### Arguments

None.

### Error states

- `Schematica is not present` — the Schematica mod isn't loaded.
- `No schematic currently open` — the mod is present but no
  schematic is loaded.

### Tab completion

None.

## Best Practices

Guidance comes from the setting defaults and the `BuilderProcess`
implementation.

### Layered building

Build one horizontal layer at a time rather than pathing freely
across the whole schematic. Pairs well with tall builds where
the builder otherwise wastes time climbing scaffold that doesn't
exist yet.

- `buildInLayers` (Boolean, default `false`) — master toggle.
  When on, the builder won't consider blocks in the next layer
  until the current one is complete (within the
  `skipFailedLayers` exception).
- `layerOrder` (Boolean, default `false`) — direction.
  `false` = bottom to top, `true` = top to bottom.
- `layerHeight` (Integer, default `1`) — how many Y-levels count
  as one "layer". Raise this for very tall schematics where
  one-block-high layers cause too much oscillation.
- `startAtLayer` (Integer, default `0`) — skip the first N
  layers. Useful when you've already built the bottom of a
  schematic by other means, or when you're iterating on the
  upper portion.
- `skipFailedLayers` (Boolean, default `false`) — continue to
  the next layer if the current one can't be completed (missing
  blocks, unreachable positions). Off by default so that failures
  stall the build and get your attention.

### Build repetition

Tile a schematic repeatedly along one or more axes. Good for
repeating structures (farms, walls, pillars) without creating
a single huge schematic.

- `buildRepeat` (Vec3i, default `(0, 0, 0)`) — offset between
  repetitions. `(0, 0, 0)` disables repetition entirely. Set
  any single component non-zero to repeat along that axis; set
  multiple for a grid tile.
- `buildRepeatCount` (Integer, default `-1`) — how many times
  to repeat. `-1` is infinite (repeats until you cancel).
- `buildRepeatSneaky` (Boolean, default `true`) — don't tell
  the schematic it's been moved. Consequence: `sel replace` in a
  repeat will keep replacing the *same* relative positions every
  iteration. Left on by default for backward compatibility; turn
  off only if you know the schematic needs its absolute position
  to differ per tile.

### Orientation, rotation, and mirror

Control which corner of the schematic is the origin and whether
the schematic is transformed before building. The three
`schematicOrientation*` booleans together choose which of the
eight corners of the schematic bounding box is the anchor.

- `schematicOrientationX` (Boolean, default `false`) — `false`
  uses the low X corner, `true` uses the high X corner.
- `schematicOrientationY` (Boolean, default `false`) — same for
  Y.
- `schematicOrientationZ` (Boolean, default `false`) — same for
  Z.

Rotation and mirror apply *before* the origin choice is
evaluated:

- `buildSchematicRotation` (Rotation enum, default `NONE`) —
  values: `NONE`, `CLOCKWISE_90`, `CLOCKWISE_180`,
  `COUNTERCLOCKWISE_90`. The last value is named for the
  direction, so "rotate 270° clockwise" reads the same as
  "rotate 90° counterclockwise".
- `buildSchematicMirror` (Mirror enum, default `NONE`) —
  values: `NONE`, `FRONT_BACK` (mirror across local X),
  `LEFT_RIGHT` (mirror across local Z). Mirror is applied after
  rotation.

### Block-matching tolerance

How strict the builder is about what the schematic "wants" vs.
what's already in the world. The defaults are strict — tune
these when a schematic calls for specific blocks you don't have,
or when you want Baritone to stop caring about blocks it thinks
are wrong.

- `buildIgnoreBlocks` (List<Block>, default empty) — blocks to
  treat as air. If the schematic calls for air at a position but
  the position currently has a block on this list, the position
  is treated as already-correct. Use when a schematic assumes a
  clean tile but your world has natural grass/dirt/etc. in the
  way that you don't want the builder to break.
- `buildSkipBlocks` (List<Block>, default empty) — blocks whose
  schematic positions are always correct regardless of what's
  actually there. Use when some parts of the schematic are "not
  my problem" — e.g. glass panes in a design that you'd rather
  place by hand.
- `buildSubstitutes` (Map<Block, List<Block>>, default empty) —
  replacement mapping. If the schematic asks for `stone`,
  Baritone will place the first placeable block from the mapped
  list. Syntax:
  `stone->cobblestone,andesite,oak_planks->birch_planks,acacia_planks`.
  Chained mappings are comma-separated.
- `buildValidSubstitutes` (Map<Block, List<Block>>, default
  empty) — accepted-but-not-preferred mapping. If the schematic
  asks for `stone` and the position already contains
  `cobblestone`, it's treated as correct; Baritone won't break
  it to place stone. Same syntax as `buildSubstitutes`.
- `okIfAir` (List<Block>, default empty) — blocks the schematic
  asks for that can be satisfied by air. If the schematic calls
  for any block on this list, air is accepted at that position
  (and nothing on `buildIgnoreBlocks`).
- `buildIgnoreExisting` (Boolean, default `false`) — treat all
  non-air blocks as correct. The builder will only place into
  empty space. Use for "fill in the holes" workflows where
  you've done the demolition by hand.
- `buildIgnoreDirection` (Boolean, default `false`) — ignore
  facing/rotation properties on blocks like glazed terracotta,
  stairs, and repeaters. The block type needs to match; which
  way it points does not.
- `buildIgnoreProperties` (List<String>, default empty) —
  ignore specific named block-state properties. Finer-grained
  than `buildIgnoreDirection`. Example:
  `powered,waterlogged` ignores whether redstone devices are
  powered and whether blocks are waterlogged.
- `okIfWater` (Boolean, default `false`) — don't try to correct
  blocks that are currently water. Turn on before building
  something that crosses a river or in environments where water
  will re-flow faster than you can place.

### Selection-only building

- `buildOnlySelection` (Boolean, default `false`) — when on,
  any active `sel` selection masks the schematic: only the
  intersection of the schematic and the selection is built.
  Useful for iterating on a large schematic one region at a
  time. No effect when there are no selections.

### Schematic file loading

- `schematicFallbackExtension` (String, default `"schematic"`) —
  the extension `build` appends when you give it a filename with
  no extension. Switch to `"schem"` or `"litematic"` if your
  library is predominantly one of those other formats, so you
  don't have to type the extension every time.

### Scan and notifications

- `builderTickScanRadius` (Integer, default `5`) — how far
  (blocks) the builder scans each tick for schematic
  discrepancies. Five is player reach distance. Raise this only
  for very large schematics where rescanning the whole thing is
  costly enough that you'd rather scan a wider ring and catch
  changes farther from the player between passes.
- `notificationOnBuildFinished` (Boolean, default `true`) —
  desktop notification when the build completes.

### Break-from-above

Experimental behavior to break blocks while standing on them
rather than pathing around to a side.

- `breakFromAbove` (Boolean, default `false`) — allow standing
  above a block while mining it in `BuilderProcess`. Marked
  experimental in the source.
- `goalBreakFromAbove` (Boolean, default `false`) — in addition
  to allowing, set a goal up-and-to-the-side of every block
  scheduled to be broken. The comment warns: **never turn this
  on without also turning on `breakFromAbove`** — doing so
  breaks the pathing logic.

### Map art

- `mapArtMode` (Boolean, default `false`) — only care about the
  top block in each column. Everything below the surface of a
  schematic is ignored, which is correct for 128×128 map-art
  schematics that represent a flat image projected onto the
  world.

### Incorrect-block pacing

Tunable multipliers the planner uses when deciding whether to
revisit "wrong" blocks vs. press on. Defaults are fine for
normal builds; you'd touch these for optimization on a specific
schematic shape.

- `incorrectSize` (Integer, default `100`) — cap on the
  incorrect-block set. The builder won't track more than this
  many wrong positions at once. On very large schematics a
  larger value lets it plan over a wider horizon at the cost of
  CPU.
- `breakCorrectBlockPenaltyMultiplier` (Double, default `10.0`) —
  cost multiplier for breaking a block that is *already correct*
  in the schematic. High values discourage Baritone from taking
  a shortcut through a finished section of the build.
- `placeIncorrectBlockPenaltyMultiplier` (Double, default `2.0`)
  — cost multiplier for placing a block that's wrong for its
  position (e.g. temporary scaffold). Lower values let Baritone
  build scaffolding more aggressively; higher values push it
  toward cleaner pathing.

## Notes & Limitations

- The `build` command resolves paths relative to
  `.minecraft/schematics/`, not the Baritone directory. That's
  the standard location schematic-producing mods write to.
- `sel` transforms are applied to the whole selection object,
  not to the schematic or the world. Running `expand` on a
  selection that has already been filled does not retroactively
  extend the fill; you need to run the fill action again after
  the transform.
- The `sel` clipboard is per-session memory only. Restart the
  client and the clipboard is gone.
- Litematica placement indexing is 1-based in the command but
  0-based in `buildOpenLitematic`. If you write a script, know
  that `litematica 1` passes `0` to the builder.
- Schematica support is retained for historical reasons but is
  effectively dead on modern versions — the "schematica is not
  present" error is the expected outcome for almost everyone.
- `build` loads the file and starts immediately. There is no
  "dry run" or preview — pair it with a sensible
  `startAtLayer` / `buildInLayers` setup if you want to stage
  the build incrementally.
