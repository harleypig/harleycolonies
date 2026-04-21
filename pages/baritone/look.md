---
title: Look & Rotation
---

Baritone controls two separate rotation states: the **server-
sided** rotation (what the server thinks your head is pointing
at) and the **client-sided** rotation (what your camera
actually shows on screen). Vanilla Minecraft always keeps them
in sync — your camera direction is what the server sees. Baritone
can decouple them, so the camera stays still while Baritone
independently tells the server to aim at blocks it needs to
break or place.

This decoupling is what the `freeLook` family of settings
controls, along with jitter, smoothing, and anticheat tweaks
that make the server-sided rotation look more human.

There are no look-specific commands. All the logic lives in
`LookBehavior` and `RotationUtils`.

## Settings Index

Alphabetical. Each link jumps to the section that discusses the setting.

- [antiCheatCompatibility](#anticheat-compatibility)
- [blockFreeLook](#free-look)
- [freeLook](#free-look)
- [randomLooking](#randomization)
- [randomLooking113](#randomization)
- [remainWithExistingLookDirection](#sticky-look-direction)
- [smoothLook](#smoothing)
- [smoothLookTicks](#smoothing)

`elytraFreeLook` and `elytraSmoothLook` are the flight-mode
analogues; see [elytra](elytra#rotation).

## How rotation routing works

`LookBehavior` decides each tick whether to set the player's
client-sided rotation (camera) based on three conditions, in
order:

1. If the player is elytra-flying, `elytraFreeLook` decides.
2. Otherwise, if `freeLook` is on: a block interaction request
   checks `blockFreeLook` (on → server only; off → force
   client); any other aim request routes to server only.
3. If `freeLook` is off, client rotations are always forced.

The upshot: `freeLook` is the top-level gate; `blockFreeLook`
is a narrower override for block-breaking and block-placing
rotations specifically.

## Best Practices

### Free look

- `freeLook` (Boolean, default `true`) — move without having
  to force client-sided rotations. With it on, your camera
  stays pointed wherever you're looking while Baritone sends
  a separate "I'm looking at block X" rotation to the server
  for pathing aim.
- `blockFreeLook` (Boolean, default `false`) — break and
  place blocks without forcing client-sided rotations.
  Requires `freeLook`; with `freeLook` off this setting does
  nothing. Off by default because some anticheats check that
  your camera is pointed at the block you're breaking.

Rule of thumb:

- **Singleplayer / relaxed servers** — `freeLook=true`,
  `blockFreeLook=true`. Your camera never gets yanked around;
  Baritone handles all rotations server-side.
- **Strict anticheats (NCP, etc.)** — `freeLook=true`,
  `blockFreeLook=false`. Pathing aim stays server-only (free
  to point anywhere), but when Baritone actually breaks or
  places a block, the camera briefly snaps to match so the
  server sees consistent look+interaction.
- **Debugging what Baritone sees** — `freeLook=false`. Every
  rotation Baritone requests forces the camera to match.
  Useful for watching exactly where it's aiming.

### Smoothing

- `smoothLook` (Boolean, default `false`) — average the
  client-sided yaw and pitch over the last N ticks of server-
  sided rotations, so forced camera movements look less
  robotic.
- `smoothLookTicks` (Integer, default `5`) — the averaging
  window. Higher values smooth more but lag more.

`LookBehavior` keeps a `smoothYawBuffer` and `smoothPitchBuffer`
(ArrayDeque of recent rotations) and truncates them to
`smoothLookTicks` entries. When `smoothLook` is on, the client
rotation is set to the mean of the buffer instead of the
current target rotation directly. Only kicks in when client
rotations are being forced — if `freeLook` is on and Baritone
isn't forcing the camera, smoothing has nothing to smooth.

Starting point: leave smoothing off unless the "camera
snaps" look bothers you. If it does, `smoothLook=true`,
`smoothLookTicks=5` is the default and looks natural; `10`
makes rotations feel sluggish; `15+` is noticeable lag.

### Sticky look direction

- `remainWithExistingLookDirection` (Boolean, default `true`)
  — when a reachable target can be hit from the player's
  current look direction, don't recompute a rotation.

Checked in `RotationUtils.reachable`: if the player is already
looking at the target, the existing rotation is reused. This
cuts down on rotation churn (every hit causing a tiny re-aim)
and keeps the camera more stable under `freeLook=false`.

Occasionally, the "existing" direction can technically reach
the block but happens to aim at a spot where the next path
step is blocked — the player gets stuck repeatedly hitting the
wrong face. Turning this off forces fresh rotation computation
every tick, trading stability for correctness.

### Randomization

Two settings jitter the server-sided rotation every tick to
look less bot-like:

- `randomLooking` (Double, default `0.01`) — maximum pitch/yaw
  offset in degrees applied uniformly each tick. Tiny; meant
  to defeat pattern detection on naïve heuristics.
- `randomLooking113` (Double, default `2`) — yaw-only jitter
  for 1.13+ anticheats that look at sub-tick rotations. Much
  larger than `randomLooking` because 1.13 sends per-tick
  micro-rotations that modern anticheats sample statistically;
  2 degrees of noise blends in.

Both offsets compose: the final yaw offset is
`(randomLooking jitter) + (randomLooking113 jitter)`. Set
either to `0` to disable that layer.

Lower these only if you need *deterministic* rotations for
recording or testing. Raising `randomLooking` much above `1`
makes aim visibly jittery in first-person; raising
`randomLooking113` past `5` starts affecting block-reach
reliability.

### Anticheat compatibility

- `antiCheatCompatibility` (Boolean, default `true`) —
  silently synchronize the client-sided rotation with
  Baritone's server-sided rotation when under `freeLook`, so
  the server doesn't see a player "sprinting sideways."

Default on because it's cheap and catches a common tell:
vanilla sends the client's current look direction alongside
the `isSprinting` packet; with `freeLook` on, that direction
stays pinned to the camera instead of tracking movement,
which naïve-to-moderate anticheats flag as movement-look
mismatch. AAC is known to catch this; NCP is not. The tweak
only affects what gets sent, not what's rendered — your camera
doesn't move, but the server sees consistent look+movement.

Turn off only if you're instrumenting rotations for testing
and want the unmodified server-sided rotation to come through.

## Notes & Limitations

- `blockFreeLook` without `freeLook` is a no-op: the outer
  `freeLook` gate must be open for the inner check to fire.
- `smoothLook` is client-side only: the server never sees the
  smoothed values. The buffer filling happens with or without
  `smoothLook` on; the setting only controls whether the
  averaged value is *applied* to the client rotation.
- The elytra-flight path uses `elytraSmoothLook` and
  `elytraFreeLook` instead of the non-elytra variants; see
  [elytra](elytra#rotation). `smoothLookTicks` is shared
  between the two modes.
- `randomLooking` has been in Baritone since before 1.13.
  `randomLooking113` was added because anticheats evolved to
  sample 1.13+'s per-tick rotation stream; one is not a
  replacement for the other.
- If you're writing an API consumer, see
  `ILookBehavior.getAimProcessor()` — the exact rotations
  produced by `LookBehavior` differ from the values passed in
  by callers because of `randomLooking` offsets. Read
  rotations through the aim processor if you need the exact
  values the server sees.
