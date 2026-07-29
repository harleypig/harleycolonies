---
title: FerriteCore ((Neo)Forge)
---

**FerriteCore** is a performance optimization mod that reduces memory usage
by deduplicating block state data, model data, and other game objects. The
mod uses various memory optimization techniques including caching,
deduplication, and compact data structures to significantly reduce RAM
usage, especially in modded environments with many blocks and items.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `ferritecore-mixin.toml`.

#### Memory Optimization Settings

- `compactFastMap` (default: `false`)
  - Use a slightly more compact, but also slightly slower representation
    for block states. When enabled, uses less memory but may have a small
    performance impact.

- `useSmallThreadingDetector` (default: `false`)
  - Replace objects used to detect multi-threaded access to chunks by a
    much smaller field. This option is disabled by default due to very rare
    and very hard-to-reproduce crashes, use at your own risk!

- `cacheMultipartPredicates` (default: `true`)
  - Cache the predicate instances used in multipart models. When enabled,
    reduces memory usage by caching model predicates.

- `multipartDeduplication` (default: `true`)
  - Do not create a new MultipartBakedModel instance for each block state
    using the same multipart model. Requires `cacheMultipartPredicates` to
    be enabled. When enabled, deduplicates multipart models.

- `blockstateCacheDeduplication` (default: `true`)
  - Deduplicate cached data for blockstates, most importantly collision
    and render shapes. When enabled, significantly reduces memory usage by
    sharing blockstate data.

- `modelResourceLocations` (default: `true`)
  - Avoid creation of new strings when creating ModelResourceLocations.
    When enabled, reuses string instances to reduce memory.

- `modelSides` (default: `true`)
  - Use smaller data structures for "simple" models, especially models
    with few side-specific faces. When enabled, optimizes memory for simple
    models.

- `replaceNeighborLookup` (default: `true`)
  - Replace the blockstate neighbor table. When enabled, uses a more
    memory-efficient neighbor lookup system.

- `populateNeighborTable` (default: `false`)
  - Populate the neighbor table used by vanilla. Enabling this slightly
    increases memory usage, but can help with issues in the rare case where
    mods access it directly.

- `replacePropertyMap` (default: `true`)
  - Do not store the properties of a state explicitly and read them from
    the replace neighbor table instead. Requires `replaceNeighborLookup` to
    be enabled. When enabled, further reduces memory usage.

- `bakedQuadDeduplication` (default: `true`)
  - Deduplicate vertex data of baked quads in the basic model
    implementations. When enabled, shares vertex data between identical
    quads.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

