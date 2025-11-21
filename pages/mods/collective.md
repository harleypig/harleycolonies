---
title: Collective
categories:
  - library-api
---

[Website](https://www.curseforge.com/minecraft/mc-mods/collective) | [Issues](https://github.com/Serilum/.issue-tracker/labels/Library: Collective) | [Source](https://github.com/Serilum/Collective)

Client/Server: both

**Collective** is a library mod that provides shared functionality for
other mods by the same developer. It includes utilities for entity
replacement, item transfer, procedural drop generation, and block detection
around entities. The mod is designed to be a dependency for other mods
rather than a standalone feature mod.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `collective.json5`.

#### Entity Settings

- `transferItemsBetweenReplacedEntities` (default: `true`)
  - When enabled, transfer the held items and armour from replaced entities
    by any of the Entity Spawn mods which depend on Collective. This
    ensures that items and equipment are preserved when entities are
    replaced.

- `loopsAmountUsedToGetAllEntityDrops` (default: `100`)
  - The amount of times Collective loops through possible mob drops to get
    them all procedurally. Drops are only generated when a dependent mod
    uses them. Lowering this can increase world load time but decrease
    accuracy. Range: `1` to `500`.

- `findABlockCheckAroundEntitiesDelayMs` (default: `30000`)
  - The delay of the is-there-a-block-around-check around entities in
    milliseconds. Used in mods which depend on a specific blockstate in the
    world. Increasing this number can increase TPS if needed. Range: `0` to
    `3600000`.

- `enablePatronPets` (default: `true`)
  - Enables pets for Patrons. Will be added in a future release.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.20.1-0.1.2
- harleycolonies-1.21.1

