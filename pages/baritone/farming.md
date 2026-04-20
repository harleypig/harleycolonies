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

- `farmMaxScanSize` (Integer, default `256`) — upper bound on the
  number of blocks the farming scan will consider. Raising it
  lets Baritone manage a bigger field in one command at the cost
  of longer scan ticks; lowering it tightens the working area and
  keeps scans cheap.

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
