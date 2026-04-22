---
title: Create a schematic of a spawner farm
---

**Heads up: this is mostly outside Baritone's wheelhouse.**
Baritone is a pathfinding and block-placement bot — it builds
*from* schematics and clears or fills selected regions, but it
doesn't design structures and it doesn't save schematics.
Creating the schematic itself is a Litematica job. Baritone can
only help with prep (clearing, bulk fills, material gathering)
and pasting existing schematics.

**Before you start:** read
[Don't break spawners](preserve-spawners) — it's very easy to
lose the spawner to a stray `sel cleararea` or a mistimed
`mine`.

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
  [Don't break spawners](preserve-spawners).
- Spawner farms depend on exact light levels, water-column
  heights, and mob-cap geometry. Verify manually before saving;
  Baritone and Litematica won't flag a design flaw.
- Litematica saves blocks; tile-entity inventories (chest or
  hopper contents) generally do not round-trip.

**Related:**
[Don't break spawners](preserve-spawners),
[sel](../building#sel--selection--s),
[build](../building#build),
[litematica](../building#litematica),
[schematica](../building#schematica).
