---
title: Don't break spawners while clearing or building
---

See the [cookbook index](../cookbook) for the `# default` /
`# default: X` annotation convention used below.

**Problem.** You're either clearing an area with `sel cleararea`
or building a schematic around an existing mob spawner, and you
don't want Baritone to break the spawner — losing a spawner
destroys it permanently in survival. Same question for torches
you've already placed around the spawner: you want them to stay,
without having to add them to the schematic.

**Solution.** Add the blocks you want to preserve to
[`buildIgnoreBlocks`](../building#block-matching-tolerance).
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
([`mobSpawnerAvoidanceCoefficient`](../pathfinding#avoidance),
[`mobSpawnerAvoidanceRadius`](../pathfinding#avoidance)) only
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
signal that [`find`](../mining#find) can latch onto because they're
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
[buildIgnoreBlocks](../building#block-matching-tolerance),
[buildValidSubstitutes](../building#block-matching-tolerance),
[buildSubstitutes](../building#block-matching-tolerance),
[mobSpawnerAvoidanceCoefficient](../pathfinding#avoidance),
[mobSpawnerAvoidanceRadius](../pathfinding#avoidance).

**Related:**
[sel cleararea](../building#fill-actions),
[Best Practices: Block-matching tolerance](../building#block-matching-tolerance).
