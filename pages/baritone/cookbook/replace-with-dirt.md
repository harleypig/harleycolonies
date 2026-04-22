---
title: Replace a selection with dirt, keeping grass blocks
---

See the [cookbook index](../cookbook) for the `# default` /
`# default: X` annotation convention used below.

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
so it honors [`buildValidSubstitutes`](../building#block-matching-tolerance)
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

**Why not `sel replace`?** The [`sel replace`](../building#fill-actions)
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
[buildValidSubstitutes](../building#block-matching-tolerance),
[buildSubstitutes](../building#block-matching-tolerance),
[buildIgnoreBlocks](../building#block-matching-tolerance).

**Related:**
[sel set](../building#fill-actions),
[sel replace](../building#fill-actions),
[Best Practices: Block-matching tolerance](../building#block-matching-tolerance).
