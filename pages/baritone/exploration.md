---
title: Exploration
---

Exploration commands tell Baritone to walk toward unexplored chunks,
apply a pre-loaded list of "already explored" chunks to avoid
re-visiting areas, or climb straight out of a cave to the surface.

The `ExploreProcess` works by picking the N closest uncached chunks
around a center point, building a composite goal to their centers, and
re-validating the path as new chunks load. Because the process
operates on Baritone's chunk cache, terrain you've never loaded
(directly or by flying over) counts as unexplored even if you've
technically been near it.

## Settings Index

Alphabetical. Each link jumps to the section that discusses the setting.

- [disableCompletionCheck](#completion-and-notifications)
- [exploreChunkSetMinimumSize](#chunk-selection)
- [exploreMaintainY](#movement)
- [notificationOnExploreFinished](#completion-and-notifications)
- [worldExploringChunkOffset](#chunk-selection)

## explore

Aliases: `explore`

Tell Baritone to explore randomly. If an `explorefilter` is active, it
is applied to exclude already-known chunks.

### Arguments

- `[<x> <z>]` — optional explore-center coordinates (`RelativeGoalXZ`,
  so relative forms like `~50 ~-100` work). If omitted, the command
  uses your current feet position as the origin.

### Tab completion

Coordinate completion (`RelativeGoalXZ`) for the first two arguments.

## explorefilter

Aliases: `explorefilter`

Apply an "explore filter" before running `explore`. The filter tells
the explore process which chunks have (or, with `invert`, have not)
been explored, so Baritone doesn't re-visit them.

JSON file format:

```json
[{"x": 0, "z": 0}, {"x": 1, "z": 0}, ...]
```

### Arguments

- `<path>` — path to the JSON file (`RelativeFile`, resolved against
  the parent of your Minecraft game directory — i.e. the directory
  that contains `.minecraft`, not `.minecraft` itself).
- `[invert]` — literal word `invert`. When present, the chunks listed
  in the file are treated as **not** explored (Baritone will go
  there) instead of explored (Baritone will avoid there).

### Error states

- `File not found` — path did not resolve to an existing file.
- `Invalid JSON syntax` — file exists but does not parse as JSON.
- `either "invert" or nothing` — the second argument was present but
  wasn't the literal word `invert`.

### Tab completion

File-path completion relative to the Minecraft parent directory for
the first argument.

## surface

Aliases: `surface`, `top`

Head toward the closest surface-like space directly above you. Used to
get out of caves, mines, ravines, or any enclosed space where you want
sky above you without manually pathing.

### Behavior

- If you're already above sea level **and** the block directly above
  you is air, the command prints `Already at surface` and exits
  without setting a goal.
- Otherwise it scans upward from `max(player Y, sea level)` to world
  height and sets a `GoalBlock` one block above the first non-air
  block it finds higher than the player.
- If no higher non-air block is found, prints `No higher location
  found`.

### Arguments

None. Tab completion is empty.

## Best Practices

### Chunk selection

- `exploreChunkSetMinimumSize` (Integer, default `10`) — the number of
  "closest uncached chunks" the explore process aims for per batch.
  Taken from the closest-N set even if chunks aren't strictly tied for
  distance. Raise it to get more chunks loaded per goal cycle at the
  cost of longer goals.
- `worldExploringChunkOffset` (Integer, default `0`) — while exploring,
  offset the chosen closest-uncached-chunk target by this many chunks
  on both axes. Setting it to your render distance can result in more
  efficient chunk loading because you're targeting the edge of the
  loaded area rather than its center.

### Movement

- `exploreMaintainY` (Integer, default `64`) — attempt to maintain
  this Y coordinate while exploring. Useful to keep Baritone on the
  surface instead of diving into caves en route. Set to `-1` to
  disable and let normal pathing rules decide the Y.

### Completion and notifications

- `disableCompletionCheck` (Boolean, default `false`) — skip the
  "all chunks explored" completion check. Turn this on if your
  explore filter is enormous and the completion check itself is
  becoming expensive; Baritone will then just keep going rather than
  noticing completion.
- `notificationOnExploreFinished` (Boolean, default `true`) — desktop
  notification when exploration finishes (either "Explored all chunks"
  on success, or "Exploration failed" on failure).

## Notes and Limitations

- `explore` picks chunks using Baritone's chunk cache plus the
  optional filter. It won't "un-explore" a chunk that Baritone has
  already cached — use `explorefilter` with `invert` to force it back
  toward specific coordinates.
- `explorefilter` paths are resolved against the parent of your
  Minecraft game directory, not against `.minecraft` itself. Use an
  absolute path if that's ambiguous.
- `surface` only searches straight up. If the ceiling above you has no
  path to open sky (e.g. you're under a solid overhang), it will set
  a goal you may not be able to reach via vertical pathing and you'll
  need to move laterally first.
- `exploreForBlocks` (documented on the Mining page) is related but
  distinct — it controls whether `mine` and `get-to-block` fall back
  to random exploration when they don't know any locations for the
  target block. It does not affect the `explore` command itself.
