---
title: Chunk Caching
---

Baritone keeps its own simplified copy of the world on disk so
that long-distance pathing isn't limited to render distance.
Every chunk Minecraft shows gets queued into a background
packer thread, converted to a compact 2-bit-per-block format
(walkable / passable / solid / avoid), and stored in 512×512
block regions under `.minecraft/baritone/<world-key>/`. The
next time pathing runs through an area it's already cached,
the planner sees the whole area, backtracks far less, and can
plan around large-scale obstacles long before they enter
render distance.

This page covers the five settings that control that cache
lifecycle. There's no cache-specific command; the cache ticks
along under the various `baritone.cache.*` classes behind the
scenes. Use [`reloadall`](system#reloadall) and
[`saveall`](system#saveall) from the system command if you
need to force a reload/save.

## Settings Index

Alphabetical. Each link jumps to the section that discusses the setting.

- [cachedChunksExpirySeconds](#eviction)
- [chunkCaching](#enabling-the-cache)
- [chunkPackerQueueMaxSize](#packer-backpressure)
- [pruneRegionsFromRAM](#eviction)
- [repackOnAnyBlockChange](#keeping-the-cache-in-sync)

## How the cache is built

Two sources feed the background packer queue:

1. **Chunk load** — every chunk that loads (post-populate or
   pre-unload) gets enqueued via `queueForPacking`.
2. **Block change** — when `repackOnAnyBlockChange` is on and
   the block that changed is one of a small set of "tracked"
   blocks (chests, furnaces, shulkers, portals, observers,
   hoppers, spawners, barriers), the containing chunk is
   re-enqueued.

A single `PackerThread` drains the queue. For each chunk it
runs `ChunkPacker.pack` (Minecraft's full block state →
2-bit classification) and stores the result in a
`CachedRegion`. Regions are the persistence unit on disk:
32×32 chunks (512×512 blocks) per region file.

## Best Practices

### Enabling the cache

- `chunkCaching` (Boolean, default `true`) — the master gate.
  When on, `CachedWorld.save` serializes every in-memory
  region to disk. When off, save is a no-op (it still runs
  `removeExpired` and `prune` on the in-memory copy, but
  nothing hits disk).

On by default and generally should stay on. Turn it off only
if you specifically don't want Baritone touching disk — e.g.,
on a strict shared host where you don't want extra writes,
or if disk I/O is measurably hurting your tick times.

Cost estimate from the original docs: an average 512×512 area
is about 300 KB on disk. More complex terrain compresses
worse and takes more. A long-traveled world cache accumulates
over time but there's no cap — if disk footprint matters, see
eviction below.

### Eviction

Two separate mechanisms evict cached regions. Both fire on the
save path (`CachedWorld.save` → `removeExpired` → `prune`):

- `cachedChunksExpirySeconds` (Long, default `-1`) — age-
  based expiry, per-chunk. `-1` disables entirely; any
  non-negative value removes chunks that haven't been
  re-packed within that many seconds. Check runs per-region
  during save and also when a region loads from disk.
- `pruneRegionsFromRAM` (Boolean, default `true`) —
  distance-based eviction, per-region, RAM-only. On save,
  any region whose center is more than 1024 blocks from the
  player is dropped from the in-memory region map. The disk
  file stays; the region just gets reloaded next time it's
  needed.

The defaults intentionally lean on `pruneRegionsFromRAM` (keep
RAM bounded) and leave `cachedChunksExpirySeconds` off (disk
is cheap, stale data is self-correcting).

The original source notes strongly advise leaving
`cachedChunksExpirySeconds=-1` because the cache is self-
correcting: Baritone re-verifies everything it sees in render
distance, so an "old" cache entry never causes wrong
behavior — it just means long-distance pathing temporarily
has less info until the real chunks come into view. Discarding
old chunks purely because they're old throws away the exact
thing the cache is for (avoiding backtracking in areas you've
already explored).

Turn `cachedChunksExpirySeconds` on only when you're on
multiplayer, extremely disk-constrained, and willing to trade
pathing quality for storage.

### Packer backpressure

- `chunkPackerQueueMaxSize` (Integer, default `2000`) — upper
  bound on the chunk packer queue. When the queue grows
  beyond this, the packer thread drops chunks off the head
  instead of processing them until the queue shrinks.

This is the "moving fast through fresh terrain" safety valve.
When render distance is churning faster than the packer can
keep up (typical when flying or when a lot of chunks load at
once during a server transition), something has to give —
the packer sheds the oldest unprocessed work and keeps up
with new arrivals. The effect: your immediate vicinity stays
cached; the trail behind you may have gaps. Those gaps fill
back in when you slow down or return to the area and the
chunks load again.

Raising the limit lets the queue buffer more work before
shedding, at the cost of RAM. Lowering it makes the packer
shed sooner. Tuning isn't usually needed; the default handles
most workloads.

### Keeping the cache in sync

- `repackOnAnyBlockChange` (Boolean, default `true`) — when a
  tracked block updates, re-queue the containing chunk for
  packing.

"Any block change" in the setting name is slightly misleading:
the event fires for every block update, but the repack only
triggers when the changed block is in
`CachedChunk.BLOCKS_TO_KEEP_TRACK_OF` — a small set of
navigationally-interesting blocks:

- Storage: chest, trapped chest, ender chest, shulker boxes
  (all colors), hopper, furnace.
- Structural: spawner, barrier, observer.
- Portals: nether portal, end portal, end portal frame.

Mining stone or placing dirt doesn't trigger a repack;
breaking into a chest or opening a portal does. Leave this on
unless you're profiling pack-thread overhead — turning it off
saves packer work at the cost of stale "where is the chest"
info for those block categories.

## Notes and Limitations

- Region storage is keyed by world — singleplayer worlds,
  each multiplayer server, and each dimension on a server
  all cache to separate files under
  `.minecraft/baritone/<world-key>/`. Dimensions don't share
  caches.
- [`reloadall`](system#reloadall) force-loads every in-memory
  region from disk (discarding unsaved in-RAM state);
  [`saveall`](system#saveall) force-saves in the other
  direction. Normally the cache saves automatically via game
  hooks and you don't need to call these.
- The packer is a single background thread. On hosts with
  lots of cores this isn't parallel; it just means the cache
  will never peg more than one core.
- The 1024-block prune radius in `pruneRegionsFromRAM` is a
  hardcoded constant, not a setting. The 512-block region
  size means a region roughly two regions away from you is
  the cutoff.
- `cachedChunksExpirySeconds` is measured against a chunk's
  `cacheTimestamp`, which is updated every time the chunk is
  re-packed. Entering render distance of a cached area and
  loading its chunks re-triggers packing and refreshes the
  timestamp, so routine travel resets the expiry clock.
