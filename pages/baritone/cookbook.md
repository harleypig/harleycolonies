---
title: Cookbook
---

Task-oriented recipes — multi-command workflows and setting
combinations that solve a concrete problem. Each recipe links
out to the topic pages for the underlying settings and
commands.

**A note on defaults.** Every recipe lists the full set of
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

## Recipes

- [Resource-usage profiles](cookbook/resource-profiles) — good
  citizen (look human to anticheat), resource-friendly on a lax
  server, and maximum throughput (CPU is cheap). Includes a
  cross-profile diff of every setting that varies.
- [Flatten a selection from the top down](cookbook/flatten-top-down)
  — use `buildInLayers` + `layerOrder` so `sel cleararea` digs
  the top layer first and leaves the cleared region open to the
  sky instead of pitting you in.
- [Replace a selection with dirt, keeping grass blocks](cookbook/replace-with-dirt)
  — use `buildValidSubstitutes` so `sel set dirt` treats
  existing grass as already-correct, avoiding the regrow-and-
  rebreak loop.
- [Create a schematic of a spawner farm](cookbook/spawner-farm-schematic)
  — how Baritone's `sel` helpers and Litematica divide the work
  of designing, saving, and rebuilding a spawner farm.
- [Don't break spawners while clearing or building](cookbook/preserve-spawners)
  — use `buildIgnoreBlocks` to skip spawners and existing
  torches during `sel cleararea` and schematic builds.
