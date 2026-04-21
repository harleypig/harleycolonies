---
title: Settings
---

Baritone has a large pool of settings that control pathfinding,
building, rendering, and everything in between. This page is a
hub: each topic page below owns the settings that belong to its
feature and discusses them in context. For the `#set` command
itself (reading, writing, toggling, resetting, saving, loading),
see [`set` in system](system#set-setting-settings).

## Where settings live

Settings are stored in `minecraft/baritone/settings.txt`, one
per line:

```
settingname value
```

For example:

```
allowBreak true
blockBreakSpeed 6
costHeuristic 3.563
```

Comments use `#` or `//`:

```
# this is a comment
allowBreak true
```

`#set save` writes the current in-memory values to that file;
`#set load [filename]` reads them back. The file is rewritten
wholesale on save, so hand-edited comments survive only until
the next `#set save`.

## Where settings are documented

Each topic page has a Settings Index near the top listing every
setting it owns, alphabetical, linked to a section that
discusses the setting in context rather than as an isolated
definition.

- [Pathfinding & Navigation](pathfinding) — movement rules, cost
  tuning, avoidance, fall safety, timeouts, path shape, goal
  behavior, A* internals.
- [Building & Schematics](building) — schematic loading, block
  substitution, builder pacing, scaffolding, map-art mode.
- [Mining](mining) — ore scanning, legit mode, branch mining,
  tunnel behavior, pickup.
- [Farming](farming) — crop detection, replanting, harvest
  passes, range centering.
- [Following](following) — follow distance, target selection,
  lost-target handling.
- [Exploration](exploration) — chunk scanning, exploration
  radius, explore filter.
- [Elytra](elytra) — takeoff, firework pacing, nether
  pathfinder cache, landing.
- [Rendering](rendering) — what is drawn, colors, layers,
  frustum culling.
- [Waypoints](waypoints) — automatic bed/death waypoints.
- [Chat & Control](chat) — prefix and chat-control settings,
  output channels, censoring, debug output.
- [Inventory](inventory) — moving items between inventory and
  hotbar, pacing, anticheat-safe swaps.
- [Tools & Item Handling](tools) — auto-tool, durability
  protection, silk touch preference, right-click rate.
- [Look & Rotation](look) — freeLook, block interactions,
  smoothing, jitter, anticheat rotation sync.
- [Chunk Caching](caching) — the 2-bit chunk cache, packer
  queue, eviction, sync.

## Setting types

Values in `settings.txt` and `#set` are parsed as:

- **Boolean** — `true` or `false`
- **Integer** — whole numbers (e.g., `5`, `100`)
- **Double / Float** — decimals (e.g., `3.563`, `0.5`)
- **Long** — whole numbers, larger range (used for time values)
- **String** — text (e.g., `"#"`, `schematic`)
- **List** — comma-separated (e.g.,
  `dirt,cobblestone,stone`)
- **Map** — key-value mappings (e.g.,
  `stone->cobblestone,andesite`)
- **Color** — RGB values or color names
- **Rotation / Mirror** — enum values (e.g., `NONE`,
  `CLOCKWISE_90`)

Setting names are case-insensitive when used via `#set`.

## Notes

- A few settings are marked `@JavaOnly` in the source and are
  not exposed to `#set`; they can only be changed
  programmatically via the API.
- Some settings gate others — for example, `allowParkourAscend`
  has no effect unless `allowParkour` is also on. The topic page
  that owns each setting calls out these dependencies.
- Default values are shown alongside each setting on its topic
  page.
