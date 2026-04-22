---
title: Elytra
---

Baritone Elytra automatically flies your player to a goal in the Nether
using a vanilla elytra and fireworks. It is an experimental feature and
only works in the **Nether**. It relies on a bundled native library
(`nether-pathfinder`) that is only shipped for 64-bit x86 and 64-bit ARM
on Windows, Linux, and macOS.

## Settings Index

Alphabetical. Each link jumps to the section that discusses the setting.

- [elytraAllowEmergencyLand](#safety-and-landing)
- [elytraAllowLandOnNetherFortress](#safety-and-landing)
- [elytraAutoJump](#starting-flight)
- [elytraAutoSwap](#safety-and-landing)
- [elytraCacheCullDistance](#chunk-cache)
- [elytraChatSpam](#logging)
- [elytraConserveFireworks](#going-slower-and-saving-fireworks)
- [elytraFireworkSetbackUseDelay](#going-slower-and-saving-fireworks)
- [elytraFireworkSpeed](#going-slower-and-saving-fireworks)
- [elytraFreeLook](#rotation)
- [elytraMinFireworksBeforeLanding](#safety-and-landing)
- [elytraMinimumAvoidance](#pathfinding-tuning)
- [elytraMinimumDurability](#safety-and-landing)
- [elytraNetherSeed](#know-the-seed)
- [elytraPitchRange](#pathfinding-tuning)
- [elytraPredictTerrain](#know-the-seed)
- [elytraRenderHitboxRaytraces](#debug-rendering)
- [elytraRenderRaytraces](#debug-rendering)
- [elytraRenderSimulation](#debug-rendering)
- [elytraSimulationTicks](#pathfinding-tuning)
- [elytraSmoothLook](#rotation)
- [elytraTermsAccepted](#terms-acknowledgement)
- [elytraTimeBetweenCacheCullSecs](#chunk-cache)

## elytra

Fly to the current goal.

Preconditions:

- A goal must already be set (e.g. via `#goto`, `#goal`, `#wp goto …`).
- The player must be in the Nether (`Level.NETHER`).
- The native library must load on this OS/CPU — check with
  `elytra supported`.
- The player should be wearing an elytra and carrying fireworks.

Behavior with no subcommand:

- If `elytraTermsAccepted` is `false`, Baritone prints a long "gatekeep"
  message the first time explaining the feature, seed requirement, and
  relevant settings (see Best Practices below). Set it to `true` to
  silence the message.
- On 2b2t (detected by server IP containing `2b2t.org`), Baritone warns
  if `elytraNetherSeed` isn't one of the two known 2b2t seeds and
  suggests which to pick.
- Paths to the most recent goal from `customGoalProcess`.

### Subcommands

#### elytra reset

Resets the internal state of the elytra process but keeps flying to the
same goal. Use when the pather gets confused but the destination is
still correct.

#### elytra repack

Queues all chunks currently in render distance to be re-fed to the
native library. Useful after chunk updates or when the pather seems to
be pathing through blocks that have changed.

#### elytra supported

Prints `yes` if the native library loaded, otherwise prints the
unsupported-system message including your detected `os.arch` and
`os.name`. This is the one subcommand that works even when the native
library failed to load, so use it for diagnostics.

### Tab completion

`reset`, `repack`, `supported` — only offered as the first argument.
There are no further positional arguments.

## Best Practices

These come from the in-game "gatekeep" message, the 2b2t seed warning,
and the elytra-related settings.

### Know the seed

Baritone uses the world seed to predict Nether terrain beyond render
distance. Without the right seed it will frequently backtrack.

- `elytraNetherSeed` (Long, default `146008555100680` — 2b2t's newer
  nether seed) — the seed used to generate chunks for long-distance
  elytra path-finding. Set it with `#set elytraNetherSeed <seed>`.
- `elytraPredictTerrain` (Boolean, default `false`) — whether the
  nether-pathfinder generates terrain from `elytraNetherSeed`. When
  `false`, unloaded chunks are treated as air. If you don't know the
  seed, keep this `false` rather than guessing wrong.
- On 2b2t, Baritone ships two known seeds:
  - **Older seed** (`-4100785268875389365`) — for terrain generated on
    older versions; use near spawn / axes / highways and in older
    outer-ring terrain.
  - **Newer seed** (`146008555100680`, the default) — for terrain up
    through 1.12-era generation.
  - In **1.19+ custom generation** on 2b2t the terrain is unpredictable;
    turn `elytraPredictTerrain` off.
- Within a few hundred blocks of spawn on 2b2t, terrain is too
  fragmented to predict reliably — expect some backtracking regardless.

### Starting flight

Baritone does **not** take off from the ground by default. Either jump
off a ledge yourself, or let Baritone do it for you.

- `elytraAutoJump` (Boolean, default `false`) — automatically path to a
  ledge and jump off to initiate elytra flight when grounded. The
  gatekeep message warns against enabling this on laggy servers.

### Going slower and saving fireworks

- `elytraConserveFireworks` (Boolean, default `false`) — skips firework
  use while descending along the flight path.
- `elytraFireworkSpeed` (Double, default `1.2`, blocks/tick) — minimum
  speed before a firework is auto-deployed. Lower values mean fewer
  rockets fired and slower average flight.
- `elytraFireworkSetbackUseDelay` (Integer, default `15` ticks) — delay
  after the server rubberbands your position before another firework
  may be auto-deployed.

### Safety and landing

- `elytraAutoSwap` (Boolean, default `true`) — swap the current elytra
  for a fresh one from your inventory when durability gets too low.
- `elytraMinimumDurability` (Integer, default `5`) — durability
  threshold that triggers `elytraAutoSwap`.
- `elytraAllowEmergencyLand` (Boolean, default `true`) — land early
  when elytra durability or firework count is about to run out.
- `elytraMinFireworksBeforeLanding` (Integer, default `5`) — firework
  threshold used by the emergency-land logic.
- `elytraAllowLandOnNetherFortress` (Boolean, default `false`) —
  consider nether brick a valid landing block. Enable if you're OK
  setting down on fortress rooftops.

### Pathfinding tuning

- `elytraSimulationTicks` (Integer, default `20`) — ticks of elytra
  movement to simulate while firework boost is not active. Higher is
  more accurate but more expensive.
- `elytraPitchRange` (Integer, default `25`) — maximum pitch deviation
  from a direct line-of-sight to the flight target. Higher is more
  flexible but more expensive.
- `elytraMinimumAvoidance` (Double, default `0.2`) — the minimum
  padding value added to the player's hitbox when considering which
  point on the path to fly to. High values can rule out points that
  are otherwise safe; low values produce tighter paths with a risk of
  crashing into terrain.

### Rotation

- `elytraFreeLook` (Boolean, default `true`) — fly without forcing
  client-sided rotations. Analogous to `freeLook` for pathing.
- `elytraSmoothLook` (Boolean, default `false`) — smooth rotations
  while flying. Analogous to `smoothLook` for pathing.

### Debug rendering

- `elytraRenderRaytraces` (Boolean, default `false`) — render the
  raytraces performed by the elytra fly calculation.
- `elytraRenderHitboxRaytraces` (Boolean, default `false`) — render
  the hitbox raytraces. Requires `elytraRenderRaytraces`.
- `elytraRenderSimulation` (Boolean, default `true`) — render the best
  elytra flight path simulated each tick.

### Chunk cache

- `elytraTimeBetweenCacheCullSecs` (Long, default `180` — three
  minutes) — time between culling passes on the nether-pathfinder
  chunk cache.
- `elytraCacheCullDistance` (Integer, default `5000`) — maximum chunk
  distance before a chunk is culled from the cache.

### Logging

- `elytraChatSpam` (Boolean, default `false`) — verbose chat logging
  while in elytra mode.

### Terms acknowledgement

- `elytraTermsAccepted` (Boolean, default `false`) — set to `true`
  after you've read the in-game gatekeep message once to stop it
  reappearing. Purely a UX setting; does not change behavior.

## Notes and Limitations

- Only works in the Nether.
- Only works with **vanilla** firework boosting — no "hacks"/mods that
  grant non-vanilla boost.
- Requires the bundled native library. If `elytra supported` reports
  unsupported, the feature is unavailable on your system and there is
  no pure-Java fallback.
- The underlying pather lives in an external project,
  [`babbaj/nether-pathfinder`](https://github.com/babbaj/nether-pathfinder).
