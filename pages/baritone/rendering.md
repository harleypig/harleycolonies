---
title: Rendering
---

Rendering settings control how Baritone draws its own state on
top of the game world — the computed path, the current goal, the
blocks it plans to break or place, the selection boxes used by
`sel` and `build`, and the optional cached-chunk overlay. The
`render` command forces a redraw if Minecraft's own chunk
rendering glitches out.

## Settings Index

Alphabetical. Each link jumps to the section that discusses the setting.

- [cachedChunksOpacity](#cached-chunk-overlay)
- [colorBestPathSoFar](#path-rendering)
- [colorBlocksToBreak](#block-action-rendering)
- [colorBlocksToPlace](#block-action-rendering)
- [colorBlocksToWalkInto](#block-action-rendering)
- [colorCurrentPath](#path-rendering)
- [colorGoalBox](#goal-rendering)
- [colorInvertedGoalBox](#goal-rendering)
- [colorMostRecentConsidered](#path-rendering)
- [colorNextPath](#path-rendering)
- [colorSelection](#selection-rendering)
- [colorSelectionPos1](#selection-rendering)
- [colorSelectionPos2](#selection-rendering)
- [goalRenderLineWidthPixels](#goal-rendering)
- [pathRenderLineWidthPixels](#path-rendering)
- [renderCachedChunks](#cached-chunk-overlay)
- [renderGoal](#goal-rendering)
- [renderGoalAnimated](#goal-rendering)
- [renderGoalIgnoreDepth](#goal-rendering)
- [renderGoalXZBeacon](#goal-rendering)
- [renderPath](#path-rendering)
- [renderPathAsLine](#path-rendering)
- [renderPathIgnoreDepth](#path-rendering)
- [renderSelection](#selection-rendering)
- [renderSelectionBoxes](#block-action-rendering)
- [renderSelectionBoxesIgnoreDepth](#block-action-rendering)
- [renderSelectionCorners](#selection-rendering)
- [renderSelectionIgnoreDepth](#selection-rendering)
- [selectionLineWidth](#selection-rendering)
- [selectionOpacity](#selection-rendering)
- [yLevelBoxSize](#goal-rendering)

## render

Aliases: `render`

Force Minecraft to rebuild every render chunk within your render
distance (horizontal square around the player, full world height
vertically). This doesn't affect Baritone's own overlays — it
tells the vanilla renderer to re-tessellate chunks that have
visually glitched (ghost blocks, missing faces, residual
overlays from a previous view distance change).

### Arguments

None.

### Tab completion

None.

## Conventions

A few patterns show up repeatedly below:

- **`...IgnoreDepth`** settings draw the overlay *through* walls
  rather than occluded by them. On by default for most overlays
  because the whole point is to see Baritone's plan even when
  it's around a corner. Turn off if the see-through look bothers
  you visually.
- **`color*`** settings take a named AWT `Color` (e.g. `RED`,
  `GREEN`, `MAGENTA`, `CYAN`) or a hex string. Defaults are
  listed per setting below.
- **Line-width** settings are in pixels and apply to the outline
  rendering only.

## Best Practices

All guidance comes from setting defaults and the comments in
`Settings.java`. Most of these settings are "taste" rather than
"configuration" — safe to experiment.

### Path rendering

Path rendering is what makes Baritone look alive: the pink/red
ribbon along the floor is the current computed path, with a
fainter secondary ribbon for the next path segment while the
planner is still extending ahead.

- `renderPath` (Boolean, default `true`) — master toggle for the
  path overlay.
- `renderPathAsLine` (Boolean, default `false`) — draw the path
  as a simple line instead of the ribbon. Cheaper visually and
  potentially easier on FPS on weak hardware.
- `renderPathIgnoreDepth` (Boolean, default `true`) — draw the
  path through terrain so you can see where Baritone plans to
  go behind walls.
- `pathRenderLineWidthPixels` (Float, default `5`) — line width
  of the path outline in pixels.
- `colorCurrentPath` (Color, default `RED`) — color of the
  currently-executing path segment.
- `colorNextPath` (Color, default `MAGENTA`) — color of the
  next segment, shown while the planner is still extending.
- `colorBestPathSoFar` (Color, default `BLUE`) — color of the
  best path the planner has found so far during an in-progress
  calculation. You only see this while pathfinding is actively
  running.
- `colorMostRecentConsidered` (Color, default `CYAN`) — color
  of the path to the most recently considered node while
  searching. Mostly a debugging aid.

### Goal rendering

- `renderGoal` (Boolean, default `true`) — master toggle for
  drawing the goal indicator.
- `renderGoalAnimated` (Boolean, default `true`) — draw the
  goal as an animated effect rather than a static box. Also
  animates `GoalXZ` beacons if `renderGoalXZBeacon` is on.
- `renderGoalIgnoreDepth` (Boolean, default `true`) — draw the
  goal through terrain.
- `renderGoalXZBeacon` (Boolean, default `false`) — render
  X/Z-only goals using the vanilla beacon-beam effect. Easier
  to spot at a distance. Combining this with
  `renderGoalIgnoreDepth` causes strange clipping artifacts —
  pick one or the other.
- `goalRenderLineWidthPixels` (Float, default `3`) — line width
  of the goal outline in pixels.
- `colorGoalBox` (Color, default `GREEN`) — color of the goal
  box.
- `colorInvertedGoalBox` (Color, default `RED`) — color of the
  goal box when the goal is "inverted" (the goal is a region to
  stay *out* of rather than reach).
- `yLevelBoxSize` (Double, default `15`) — size of the box
  rendered when the current goal is a `GoalYLevel`. Larger
  values make a Y-level goal easier to spot from a distance,
  smaller values keep it out of the way.

### Block action rendering

Boxes drawn around blocks Baritone is about to interact with
during building or complex pathing — the targets for breaking,
placing, and the "walk into" interaction (stepping onto a
block to trigger a pressure plate, portal, etc.).

- `renderSelectionBoxes` (Boolean, default `true`) — master
  toggle for these action boxes.
- `renderSelectionBoxesIgnoreDepth` (Boolean, default `true`) —
  draw them through terrain.
- `colorBlocksToBreak` (Color, default `RED`) — color of the
  "to break" boxes.
- `colorBlocksToPlace` (Color, default `GREEN`) — color of the
  "to place" boxes.
- `colorBlocksToWalkInto` (Color, default `MAGENTA`) — color of
  the "to walk into" boxes.

### Selection rendering

The `sel` command's selection boxes (used for building and
scaffolding) have their own rendering controls, separate from
the block-action boxes above.

- `renderSelection` (Boolean, default `true`) — master toggle
  for selection rendering.
- `renderSelectionBoxes` also gates the body of each selection;
  turn both off for a fully hidden selection.
- `renderSelectionCorners` (Boolean, default `true`) — draw
  the two corner markers (`pos1` / `pos2`).
- `renderSelectionIgnoreDepth` (Boolean, default `true`) — draw
  selection boxes through terrain.
- `selectionLineWidth` (Float, default `2`) — line width of the
  selection outline in pixels.
- `selectionOpacity` (Float, default `0.5`) — fill opacity of
  the selection box. `0` is fully transparent, `1` is fully
  opaque.
- `colorSelection` (Color, default `CYAN`) — color of the
  selection body.
- `colorSelectionPos1` (Color, default `BLACK`) — color of the
  first corner marker.
- `colorSelectionPos2` (Color, default `ORANGE`) — color of the
  second corner marker.

### Cached-chunk overlay

Optional debug view of Baritone's chunk cache. Useful on
low-render-distance servers to see the rough shape of
already-explored terrain beyond your render distance, but
expensive.

- `renderCachedChunks` (Boolean, default `false`) — render
  cached chunks as a semitransparent overlay. **Doesn't work
  with OptiFine**, and crashes randomly on some configurations.
  Enabling this may require reloading the world (disconnect /
  reconnect, dimension change, death) before it takes effect.
  FPS/CPU impact is severe because every chunk is compiled
  twice — once from the cache, once from the server when it
  comes into real render range.
  Semantic quirks worth knowing:
  - Flowing water is cached as AVOID and shows up as lava. As
    you get close enough for the real chunk to load, lava
    falls are replaced with water falls.
  - SOLID is rendered as the dimension's default stone type
    (stone in the overworld, netherrack in the nether, end
    stone in the end).
- `cachedChunksOpacity` (Float, default `0.5`) — opacity of the
  cached-chunk overlay. `0` = fully transparent (in which case
  turn off `renderCachedChunks` instead of setting opacity to
  zero), `1` = fully opaque.

## Notes & Limitations

- Elytra debug rendering (`elytraRenderRaytraces`,
  `elytraRenderHitboxRaytraces`, `elytraRenderSimulation`) lives
  on the [Elytra page](elytra#debug-rendering) alongside the
  rest of the elytra settings, not here.
- `render` only nudges Minecraft's own chunk renderer. If
  Baritone's overlays themselves look wrong (stale goals, stale
  path ribbons), cancel and re-issue the command rather than
  running `render`.
- `renderCachedChunks` is a known rough edge — the setting
  comment in `Settings.java` calls it out as crash-prone and
  incompatible with OptiFine. Treat it as opt-in diagnostic
  only, not as a long-running display.
