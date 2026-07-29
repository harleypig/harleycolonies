---
title: Tools and Item Handling
---

Baritone's auto-tool picks the best tool in your inventory for
the block it's about to break, and factors that choice into
path cost calculations so it can plan routes that rely on
having the right pick or axe. This page covers the settings
that control which tool it picks, when it refuses to pick a
tool (durability protection), and the rate limit on
right-click interactions.

There are no tool-specific commands; all of this runs inside
`ToolSet`, `MovementHelper.switchToBestToolFor`, and
`BlockPlaceHelper`.

## Settings Index

Alphabetical. Each link jumps to the section that discusses the setting.

- [assumeExternalAutoTool](#auto-tool)
- [autoTool](#auto-tool)
- [itemSaver](#durability-protection)
- [itemSaverThreshold](#durability-protection)
- [preferSilkTouch](#silk-touch-preference)
- [rightClickSpeed](#right-click-rate)

## Best Practices

### Auto-tool

- `autoTool` (Boolean, default `true`) — let Baritone switch
  to the best tool for each block before breaking. When off,
  whatever is in the currently-selected hotbar slot gets used.
- `assumeExternalAutoTool` (Boolean, default `false`) — run
  path calculations *as if* auto-tool were on, but leave the
  actual runtime switching to another mod.

The two interact in `MovementHelper.switchToBestToolFor`:

```
if (autoTool && !assumeExternalAutoTool) {
    // actually switch slot
}
```

Both gates must agree before Baritone touches your hotbar.
`ToolSet.getBestSlot` also short-circuits to the current slot
when `!autoTool` during path-cost calculation, so turning
`autoTool` off makes the planner pessimistic — it assumes you
won't switch and prices long breaks accordingly.

The three useful combinations:

- `autoTool=true`, `assumeExternalAutoTool=false` — default.
  Baritone both plans for and performs tool switching.
- `autoTool=true`, `assumeExternalAutoTool=true` — plan for
  fast breaks, but let another mod do the actual switching.
  Use when a companion mod (e.g., an inventory-management
  mod) already handles auto-tool and you want to avoid
  double-switching.
- `autoTool=false` — don't switch, and price breaks
  accordingly. The planner will often prefer routes that
  avoid swinging through bedrock-grade blocks with your hand.

The fourth combination (`autoTool=false`,
`assumeExternalAutoTool=true`) means "I lied to the planner;
please don't actually switch, but optimize as if you would" —
it plans fast routes but executes slowly. Not recommended.

### Silk touch preference

- `preferSilkTouch` (Boolean, default `false`) — in tie-break
  situations, prefer a silk touch tool over a regular tool of
  equivalent mining speed.

`ToolSet.getBestSlot` always picks the fastest tool first. With
this setting on, the tie-breaker between two tools of equal
speed goes to the silk touch one, even if that means picking
"any silk touch tool over your hand" when the hand is also
speed-zero. Useful when mining blocks you want to preserve
(glass, ice, spawners) — but note it only affects tie-breaks,
not the primary ordering, so a regular iron pickaxe still beats
a silk-touch wooden pickaxe on stone.

### Durability protection

- `itemSaver` (Boolean, default `false`) — refuse to use a
  tool whose durability is within the threshold of breaking.
- `itemSaverThreshold` (Integer, default `10`) — how much
  durability to leave on the tool.

The check runs in two places:

- `ToolSet.getBestSlot` — tools with
  `damageValue + itemSaverThreshold >= maxDamage` are skipped
  over during selection. The next-best (non-exhausted) tool
  wins. If every candidate is exhausted, the `else` branch
  falls through to whatever is currently selected.
- `InventoryBehavior.throwaway` — the same exhausted tools are
  skipped when choosing a free hotbar slot to drop into.

The check requires `maxDamage > 1`, so un-damageable items
(nametags, blocks) are always fair game. The threshold is an
absolute durability count, not a percentage: at the default
10, a diamond pickaxe (1561 max) is retired with 10 uses left,
and a wooden pickaxe (59 max) is retired with 10 uses left. For
short-lived tools the default can be aggressive; raise
`itemSaverThreshold` only if you want a larger safety margin,
and keep in mind it shrinks the effective pool of usable tools.

### Right-click rate

- `rightClickSpeed` (Integer, default `4`) — ticks between
  right-click interactions (block placement, bucket use,
  etc.).

Minecraft's own game loop rate-limits right-clicks at 4 ticks,
so the default matches vanilla. `BlockPlaceHelper` subtracts
`BASE_PLACE_DELAY = 1` internally, so the effective timer is
`rightClickSpeed - 1`. Lowering to `1` or `0` makes Baritone
right-click as fast as possible; raising it slows placement
and can help on servers that flag rapid block placement.

## Notes and Limitations

- Auto-tool only triggers on the *break* path. Tool choice for
  right-click interactions (hoe on grass for farming, bucket
  swaps, etc.) is managed by individual processes and ignores
  `autoTool` / `assumeExternalAutoTool`.
- `itemSaver` doesn't prevent you from picking up a nearly-
  broken tool onto the hotbar via `allowInventory` — see
  [inventory](inventory). It only prevents Baritone from
  *selecting* an exhausted tool for use. The tool stays in
  place; your next activity just gets the next-best option.
- `preferSilkTouch` is a tie-breaker only. For strict silk-
  touch mining (refuse to mine with non-silk), combine this
  with [mining settings](mining) that restrict which blocks
  are targeted in the first place.
- The rate-limit timer is per-process, so pacing from
  `rightClickSpeed` doesn't coordinate with other mods that
  also send click packets.
