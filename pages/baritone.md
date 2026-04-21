---
title: Baritone Documentation
---

This wiki documents the [Baritone](https://github.com/cabaletta/baritone)
Minecraft pathfinding and automation mod. Content is hand-
written against the source, not auto-generated: each topic
page groups the commands, settings, and behavior that belong
to one feature and explains them in context.

## Source reference

- **Repository:** https://github.com/cabaletta/baritone
- **Branch:** `1.21.1`
- **Pinned commit:** [`fb74e10`](https://github.com/cabaletta/baritone/commit/fb74e10248df894871bd49b62411a6c8841ada49)
  (merge of `1.20.5` → `1.21.1`, 2026-01-01)

Direct links to the most-referenced source files:

- [`Settings.java`](https://github.com/cabaletta/baritone/blob/1.21.1/src/api/java/baritone/api/Settings.java)
  — the single source of truth for every setting, its type,
  default value, and the javadoc that seeded much of the
  per-setting prose here.
- [`baritone/command/defaults/`](https://github.com/cabaletta/baritone/tree/1.21.1/src/main/java/baritone/command/defaults)
  — one class per chat command. When a page describes a
  command's subcommands, arguments, error states, or tab
  completion, the authoritative answer is in the matching
  `*Command.java`.

Behavior documented here reflects the state of `1.21.1` as of
the pinned commit. Later commits on the branch, or other
version branches (`1.19.4`, `1.20.1`, etc.), may differ —
consult the source on those branches if you're running a
different version.

## How the pages are organized

Each topic page follows the same shape:

1. A short opening paragraph describing the feature and when
   to reach for it.
2. A **Settings Index** — alphabetical list of every setting
   the page owns, linked to the section that discusses it.
3. **Commands** (where applicable) — each command documented
   with aliases, subcommands, arguments, error states, and tab
   completion.
4. **Best Practices** — settings grouped by theme, with
   explanations of how they interact and which combinations
   make sense.
5. **Notes & Limitations** — caveats and cross-references to
   related pages.

Settings live on their topic page, not in a flat reference.
For a hub-style list of every topic page with brief
descriptions, see [settings](baritone/settings).

## Topic pages

### Feature commands

- [Pathfinding & Navigation](baritone/pathfinding) — `goal`,
  `goto`, `path`, `invert`, `axis`, `come`, `surface`,
  `thisway`, plus movement rules, cost tuning, timeouts,
  avoidance, and backfill.
- [Building](baritone/building) — `build`, `sel`, `litematica`,
  `schematica`; schematic loading and builder behavior.
- [Mining](baritone/mining) — `mine`, `tunnel`, `find`,
  `blacklist`, `pickup`.
- [Farming](baritone/farming) — `farm` and harvest/replant
  behavior.
- [Following](baritone/following) — `follow` and target
  selection.
- [Exploration](baritone/exploration) — `explore`,
  `explorefilter`, chunk scanning.
- [Elytra](baritone/elytra) — `elytra` flight.
- [Waypoints](baritone/waypoints) — `waypoints`, `sethome`,
  `home`; bookmarking positions.

### Control & system

- [System & Control](baritone/system) — `set`, `help`,
  `version`, `click`, `reloadall`, `saveall`, `repack`, `gc`,
  `proc`, `eta`.
- [Execution Control](baritone/execution_control) — `pause`,
  `resume`, `paused`, `cancel`, `forcecancel`.

### Cross-cutting behavior

These pages own settings that affect many activities at once.

- [Chat & Control](baritone/chat) — prefix and chat-control
  settings, output channels, censoring, debug output.
- [Inventory](baritone/inventory) — inventory-to-hotbar moves
  and anticheat-safe pacing.
- [Tools & Item Handling](baritone/tools) — auto-tool,
  durability protection, silk-touch preference, right-click
  rate.
- [Look & Rotation](baritone/look) — freeLook, smoothing,
  randomization, anticheat rotation sync.
- [Rendering](baritone/rendering) — what is drawn, colors,
  layers, frustum culling.
- [Chunk Caching](baritone/caching) — the 2-bit chunk cache,
  packer queue, eviction.

### Reference

- [Settings](baritone/settings) — hub page linking every
  topic page's Settings Index.
- [Cookbook](baritone/cookbook) — task-oriented recipes
  (placeholder).
- [FAQ](baritone/faq) — common questions (placeholder).
