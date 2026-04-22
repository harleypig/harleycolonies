---
title: FAQ
---

## How can I get a list of blocks required for a schematic?

Use Litematica's built-in **Material List**. Baritone doesn't
have a pre-flight material-list command — the closest thing is
reactive: during a [`build`](building#build), if the build
stalls because items are missing from your inventory, Baritone
logs `Missing materials for at least: Nx <block>`. That's
useful while building, not for planning.

**Litematica (recommended).**

- `M` → **Schematic Placements** → select a placement →
  **Material List**, or `M` → **Material List** directly
  (operates on the currently-selected placement).
- Sort by name / needed / missing / available; toggle "Hide
  available" to see only what's still outstanding.
- **Write to File** dumps the list (plain text / CSV) to
  `.minecraft/config/litematica/material_lists/`, ready to feed
  to a spreadsheet or shopping macro.

Litematica works on `.litematic`, `.schem`, and `.schematic`
files — it converts on load — so this works regardless of which
format your schematic is in.

**Other tools.**

- **Amulet Editor** — actively maintained desktop editor. Opens
  all three formats; can export block counts.
- **MCEdit-Unified** — legacy, but still works on `.schematic`
  files and shows a block-analysis panel.
- WorldEdit's `//distr` counts blocks *in a world selection*,
  not inside a schematic file — so it only helps after you've
  already pasted the schematic.

**Rolling your own.** All three formats are NBT and documented:

- **Sponge Schematic Format** (`.schem`) — formal spec at
  [SpongePowered/Schematic-Specification](https://github.com/SpongePowered/Schematic-Specification).
  Palette + varint-packed `BlockData` byte array.
- **Litematica `.litematic`** — no formal spec, but the layout
  is in the Litematica source
  ([maruohon/litematica](https://github.com/maruohon/litematica),
  class `LitematicaSchematic`). Multi-region, palette + packed
  `long[]` bitstream (bits per entry =
  `ceil(log2(paletteSize))`, minimum 2). The bit-packing is the
  only non-trivial part.
- **Legacy MCEdit `.schematic`** — pre-1.13 flat block-ID array
  with a parallel data-value array. Simple but limited to legacy
  block IDs. Baritone still reads it via `MCEditSchematic`.

Any NBT library (Python `nbtlib` / `amulet-nbt`, Java
`Querz/NBT`, JS `prismarine-nbt`) plus the linked specs is
enough to write a short block-counter. Unless you need something
Litematica's material list can't do, the **Write to File**
button is the fast path.

**Related:**
[build](building#build),
[litematica](building#litematica),
[Cookbook: Create a schematic of a spawner farm](cookbook/spawner-farm-schematic).

## Is there a mod that tracks what I have against a list of blocks I need?

For a schematic, **yes — Litematica's Material List does this
live.** Once a schematic is loaded as a placement, the list
shows **Total / Missing / Available** columns; *Available* is
read from your inventory and updates as you mine, craft, or
unload chests. Sort by Missing (or toggle "Hide available") and
you have a shopping list that shrinks in real time. Same screen
covered above — no extra mod needed.

For an **arbitrary** list of blocks not tied to a schematic, I
don't know of a maintained mod that does target-vs-have
tracking. The usual workaround is to build a tiny throwaway
schematic in Litematica's Area Editor containing exactly the
blocks and quantities you want, then use its Material List as
the tracker.
