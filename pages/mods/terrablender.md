---
title: TerraBlender (Forge)
categories:
  - world-biomes
  - library-api
  - world-gen
---

[Website](https://www.curseforge.com/minecraft/mc-mods/terrablender) | [Issues](https://github.com/Glitchfiend/TerraBlender/) | [Source](https://github.com/Glitchfiend/TerraBlender/)

Client/Server: both

**TerraBlender** is a library mod that provides biome generation
infrastructure for mods that add custom biomes. The mod manages biome
region sizes, weights, and distribution across different dimensions. It
allows multiple biome mods to work together by organizing biomes into
regions and controlling how they interact with vanilla biomes.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `terrablender.toml`.

#### General Settings

- `general.overworld_region_size` (default: `3`)
  - The size of overworld biome regions from each mod that uses
    TerraBlender. Larger values create larger biome regions, making biomes
    more spread out.

- `general.vanilla_overworld_region_weight` (default: `10`)
  - The weighting of vanilla biome regions in the overworld. Higher values
    make vanilla biomes more common relative to modded biomes.

- `general.nether_region_size` (default: `2`)
  - The size of nether biome regions from each mod that uses TerraBlender.
    Larger values create larger biome regions.

- `general.vanilla_nether_region_weight` (default: `10`)
  - The weighting of vanilla biome regions in the nether. Higher values
    make vanilla nether biomes more common.

#### End Settings

- `end.edge_biome_size` (default: `3`)
  - The size of edge end biomes. Controls how large edge biomes are in the
    End dimension.

- `end.highlands_biome_size` (default: `4`)
  - The size of highlands end biomes. Controls how large highlands biomes
    are in the End.

- `end.vanilla_end_barrens_weight` (default: `10`)
  - The weight of Vanilla end barrens biomes. Higher values make vanilla
    end barrens more common.

- `end.island_biome_size` (default: `2`)
  - The size of island end biomes. Controls how large island biomes are in
    the End.

- `end.vanilla_end_highlands_weight` (default: `10`)
  - The weight of Vanilla end highlands biomes. Higher values make vanilla
    end highlands more common.

- `end.vanilla_end_midlands_weight` (default: `10`)
  - The weight of Vanilla end midlands biomes. Higher values make vanilla
    end midlands more common.

- `end.midlands_biome_size` (default: `4`)
  - The size of midlands end biomes. Controls how large midlands biomes
    are in the End.

- `end.vanilla_small_end_islands_weight` (default: `10`)
  - The weight of Vanilla small end islands biomes. Higher values make
    vanilla small end islands more common.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1
- harleycolonies-1.20.1-0.1.2

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.20.1-0.1.2

