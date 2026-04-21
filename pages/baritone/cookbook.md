---
title: Cookbook
---

Task-oriented recipes — multi-command workflows and setting
combinations that solve a concrete problem. Each recipe links
out to the topic pages for the underlying settings and
commands.

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

```
#set buildInLayers true
#set layerOrder true
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

**When the selection is tall.** The default `layerHeight=1`
means one pass per Y-level; for a 30-block-tall hill that's
30 passes and a lot of vertical repositioning. Bump it up:

```
#set layerHeight 3
```

The trade-off is that inside each 3-block slice the builder
can reach blocks in any order, so you briefly see a
3-layer-deep dig face instead of a flat ceiling. For daylight
work that's fine; for night work with mobs nearby, keep
`layerHeight=1`.

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
