---
title: Performance & Caching (pending consolidation)
---

This file is a holding pen for performance/caching settings that
have not yet been moved to a topic page. Settings already
documented elsewhere (`elytraCacheCullDistance`,
`elytraTimeBetweenCacheCullSecs`, `extendCacheOnThreshold`,
`maxCachedWorldScanCount`) have been removed; see
[elytra](elytra) and [mining](mining) for those.

The settings below still need a home. They cluster around chunk
caching and the chunk packer queue.

## Settings

### `backfill`

**Type**: `Boolean`
**Default**: `false`

Fill in blocks behind you

---

### `cachedChunksExpirySeconds`

**Type**: `Long`
**Default**: `-1`

Cached chunks (regardless of if they're in RAM or saved to disk) expire and are deleted after this number of seconds -1 to disable

I would highly suggest leaving this setting disabled (-1).

The only valid reason I can think of enable this setting is if you are extremely low on disk space and you play on multiplayer, and can't take (average) 300kb saved for every 512x512 area. (note that more complicated terrain is less compressible and will take more space)

However, simply discarding old chunks because they are old is inadvisable. Baritone is extremely good at correcting itself and its paths as it learns new information, as new chunks load. There is no scenario in which having an incorrect cache can cause Baritone to get stuck, take damage, or perform any action it wouldn't otherwise, everything is rechecked once the real chunk is in range.

Having a robust cache greatly improves long distance pathfinding, as it's able to go around large scale obstacles before they're in render distance. In fact, when the chunkCaching setting is disabled and Baritone starts anew every time, or when you enter a completely new and very complicated area, it backtracks far more often because it has to build up that cache from scratch. But after it's gone through an area just once, the next time will have zero backtracking, since the entire area is now known and cached.

---

### `chunkCaching`

**Type**: `Boolean`
**Default**: `true`

The big one. Download all chunks in simplified 2-bit format and save them for better very-long-distance pathing.

---

### `chunkPackerQueueMaxSize`

**Type**: `Integer`
**Default**: `2000`

The chunk packer queue can never grow to larger than this, if it does, the oldest chunks are discarded

The newest chunks are kept, so that if you're moving in a straight line quickly then stop, your immediate render distance is still included

---

### `pruneRegionsFromRAM`

**Type**: `Boolean`
**Default**: `true`

On save, delete from RAM any cached regions that are more than 1024 blocks away from the player

Temporarily disabled

Temporarily reenabled @see Issue #248

---

### `repackOnAnyBlockChange`

**Type**: `Boolean`
**Default**: `true`

Whenever a block changes, repack the whole chunk that it's in
