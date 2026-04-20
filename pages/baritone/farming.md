---
title: Farming
---

Farming commands tell Baritone to walk a bounded area and automate
crop harvest and replant. The `FarmProcess` scans within a spherical
radius around a chosen center, harvests ripe crops, picks up the
drops, applies bonemeal when it has some, and replants where
allowed by the replant settings.

## Settings Index

Alphabetical. Each link jumps to the section that discusses the setting.

- [farmMaxScanSize](#scan-range-and-scale)
- [notificationOnFarmFail](#completion-and-notifications)
- [replantCrops](#replanting)
- [replantNetherWart](#replanting)

## farm

Aliases: `farm`

Start farming nearby crops. Baritone picks a center and a cubic
scan range, then iterates: locate harvestable crops inside the
range, path to them, harvest, pick up drops, and (if enabled)
replant.

### Arguments

- `[<range>]` — optional integer radius (in blocks) measured from
  the center point as a Euclidean distance. Reachable blocks are
  those where `distance(block, center) ≤ range`, so doubling the
  argument roughly octuples the scan volume. When omitted, range
  is unbounded and only `farmMaxScanSize` caps the work.
- `[<waypoint>]` — optional waypoint that overrides the default
  center. Resolved through `ForWaypoints`, so tab completion
  offers your existing waypoint tags/names. Only valid when a
  `<range>` is also given.

When no `<waypoint>` is supplied, the center is your position at
the moment the command runs.

### Error states

- `No waypoints found` — the waypoint argument did not match any
  stored waypoint.
- `Multiple waypoints were found` — the waypoint argument matched
  more than one stored waypoint; disambiguate by tag or name.

### Tab completion

Waypoint completion for the second argument once a `<range>` is
present. No completion for the first argument.

## Harvest behavior

`FarmProcess` decides what counts as "ripe" per crop type. Some
of this is surprising, so it's worth knowing up front:

- **Wheat, carrots, potatoes, beetroot** — harvested at max age
  (standard `CropBlock` behavior).
- **Pumpkin, melon** — always harvestable once the block exists.
- **Nether wart** — harvested at age ≥ 3.
- **Cocoa** — harvested at age ≥ 2.
- **Sugar cane, bamboo, cactus** — behavior depends on
  `replantCrops`:
  - `replantCrops = true` (default): only the upper segments are
    harvested, leaving the base block to regrow.
  - `replantCrops = false`: every segment is harvested, including
    the base, so the column has to be replanted manually.

Baritone also picks up drops inside the scan area (seeds, produce,
sugar cane, bamboo, cactus items) and will use bonemeal on
bonemealable crops when it finds some in inventory.

## Best Practices

Guidance comes from setting defaults and the `FarmProcess`
implementation.

### Scan range and scale

- `farmMaxScanSize` (Integer, default `256`) — cap on the number
  of candidate blocks returned by the world scan, not a distance.
  The scan itself always walks out to 10 chunks around the center
  and stops once this many matching blocks have been collected.
  Raising it lets Baritone track more crops at once (useful for
  dense megafields); lowering it keeps scans cheap at the cost of
  only seeing the closest matches.

### Replanting

Replanting is two-layered: the master switch covers normal crops,
and a separate opt-in covers nether wart.

- `replantCrops` (Boolean, default `true`) — replant wheat,
  carrots, potatoes, beetroot, melon seeds, pumpkin seeds once
  harvested. When enabled, sugar cane, bamboo, and cactus are
  also left to regrow from their base block. Turn this off only
  if you want a clean sweep with no replanting.
- `replantNetherWart` (Boolean, default `false`) — also replant
  nether wart. No effect unless `replantCrops` is also true.
  Nether wart is opt-in because soul sand is scarce enough that
  you may want the drops without spending the stock on replant.

Replanting is re-evaluated every scan: empty farmland (and soul
sand, when enabled) stays in the replant queue until inventory
has a matching seed item, so starting the run with no seeds is
fine — the first wave of harvests won't replant, but every pass
after that will, once drops are picked up.

Baritone does not craft. It can only replant whatever vanilla
drops land directly in inventory:

- Wheat and beetroot crops drop their seeds on harvest, so they
  self-sustain.
- Carrots and potatoes are their own "seed," so they self-sustain
  too.
- Pumpkin and melon work differently — `FarmProcess` only
  targets the fruit blocks (`Blocks.PUMPKIN`, `Blocks.MELON`),
  never the stem. The stem stays intact and regrows a fruit on
  its own, so there is nothing to replant. Do **not** stock
  pumpkin or melon seeds for a farm run: if Baritone happens to
  have seeds on hand it will plant them on the freshly-empty
  farmland tile beside the existing stem, ending up with a
  redundant new stem instead of just letting the original regrow.

### Completion and notifications

- `notificationOnFarmFail` (Boolean, default `true`) — desktop
  notification when farming fails (e.g., no harvestable crops in
  range, or pathing to them is impossible).

## Notes & Limitations

- The reachable area is a sphere around the center, not a cube
  or square; if your field is a long strip, pick a center in the
  middle so both ends fall inside the radius rather than placing
  the center at one end.
- Replanting requires the matching seed/item in your inventory.
  Baritone will skip replants it can't fulfill; that's the most
  common cause of a partially-replanted field.
- Farming will path into lit farmland and harvest at night if
  movement settings allow it — combine with your usual safety
  settings (sprint/parkour/etc.) rather than relying on farming
  to avoid hazards.
- Only the eleven crops above are recognized. The harvest list,
  the plantable list, and the pickup list are all hardcoded to
  vanilla `Blocks.*` / `Items.*` references with identity
  comparisons — no tag lookup and no registry hook. That means
  several other vanilla plants are also invisible to
  `FarmProcess`, not just modded ones:
  - **Vanilla, but unsupported**: sweet berry bushes, glow
    berries / cave vines, chorus fruit, kelp, red and brown
    mushrooms, crimson/warped fungi and nylium, twisting and
    weeping vines, torchflower, pitcher crop.
  - **Modded crops** (Farmer's Delight tomatoes/cabbages/rice/
    onions, Croptopia, Pam's HarvestCraft, etc.) are invisible
    for the same reason.
  In every case the crop is not harvested, not replanted, and
  the farmland beneath it is never flagged as empty because a
  growing crop block is not air.
  Expanding the list has been requested upstream —
  [cabaletta/baritone#896](https://github.com/cabaletta/baritone/issues/896)
  ("Add berry bushes to #farm") has been open since September
  2019, so don't hold your breath.
