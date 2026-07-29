---
title: Inventory
---

Baritone normally works with whatever you have on your hotbar
— the 9 slots it can switch between via `getInventory().selected`.
Turning on inventory management lets it reach into the main
inventory to pull tools, building blocks, and throwaway stacks
up to the hotbar when it needs them. This page covers the three
settings that control that behavior and its pacing.

There are no inventory-specific commands; everything happens
automatically under `InventoryBehavior`.

## Settings Index

Alphabetical. Each link jumps to the section that discusses the setting.

- [allowInventory](#turning-inventory-management-on)
- [inventoryMoveOnlyIfStationary](#anticheat-safe-pacing)
- [ticksBetweenInventoryMoves](#anticheat-safe-pacing)

## Best Practices

### Turning inventory management on

- `allowInventory` (Boolean, default `false`) — the master
  switch. With it off, Baritone never touches slots 9–35; it
  works with whatever you put on the hotbar. With it on,
  `InventoryBehavior` ticks every frame and can swap items
  between the main inventory and the hotbar.

Off by default because automated inventory moves look like
cheating on many servers. Two places in the code specifically
depend on it:

- `InventoryBehavior.throwaway` — finding a "free" hotbar slot
  to drop/swap items into. With `allowInventory` off, it only
  considers existing hotbar slots; with it on, it can pull a
  fresh item up from the main inventory.
- `BuilderProcess` — when a scaffold/target block isn't on the
  hotbar, it pulls the matching stack up so the builder has
  something to place.

Leave this off on servers that flag inventory manipulation.
Turn it on for singleplayer, long mining runs, or building
from a diverse block palette.

### Anticheat-safe pacing

Two settings slow inventory moves down so servers don't see a
burst of click-packets:

- `ticksBetweenInventoryMoves` (Integer, default `1`) —
  minimum tick gap between inventory-to-hotbar swaps. The
  default of 1 tick is "fast as practical". Raise it on
  strict-rate anticheats (2b2t-style) where rapid container
  clicks trigger a flag.
- `inventoryMoveOnlyIfStationary` (Boolean, default `false`) —
  pause movement before each swap. With it on,
  `InventoryBehavior.requestSwapWithHotBar` consults
  `InventoryPauserProcess.stationaryForInventoryMove()` and
  defers the swap until the player is stopped. The pauser
  process briefly halts movement, performs the click, then
  lets pathing resume. Turn this on if your anticheat flags
  container interactions while moving; expect slight pauses
  mid-path as the builder or miner restocks.

Both settings are independent. Together they give you:

- `ticksBetweenInventoryMoves=1`,
  `inventoryMoveOnlyIfStationary=false` — default, fastest.
- `ticksBetweenInventoryMoves=20`,
  `inventoryMoveOnlyIfStationary=true` — slowest, safest on
  strict servers.

Elytra behavior re-uses `ticksBetweenInventoryMoves` as a
firework-slot refill cooldown (`invTickCountdown` in
`ElytraBehavior`), so raising it affects how quickly the
elytra process can re-arm after firing a rocket.

## Notes and Limitations

- `allowInventory` is checked at the point of each action, not
  once at the start of a task. Toggling it mid-run takes
  effect immediately for the next inventory move.
- The debug log ("Inventory move requested but delaying …") is
  gated by `chatDebug`; see [chat](chat#verbose-and-debug-output)
  if you want to watch the pauser in action.
- `InventoryBehavior` writes through the normal container-
  click machinery, so any mod that hooks into inventory clicks
  (sorting mods, auto-ID) will see Baritone's moves.
