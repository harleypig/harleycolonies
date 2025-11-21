---
title: KleeSlabs
categories:
  - utility-qol
---

[Website](https://www.curseforge.com/minecraft/mc-mods/kleeslabs) | [Issues](https://github.com/ModdingForBlockheads/KleeSlabs/issues) | [Source](https://github.com/ModdingForBlockheads/KleeSlabs)

Client/Server: both

**KleeSlabs** allows players to break only half of a double slab block,
splitting it into two single slabs. This mod makes slab placement and
removal more intuitive by allowing players to break the top or bottom half
of a double slab independently. The mod includes configurable activation
modes and compatibility options for other mods.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `kleeslabs-common.toml`.

#### General Settings

- `mode` (default: `"ALWAYS"`)
  - Control whether KleeSlabs should trigger `ALWAYS`,
    `ONLY_WHEN_SNEAKING`, or `ONLY_WHEN_NOT_SNEAKING`. Allowed values:
    `ALWAYS`, `ONLY_WHEN_SNEAKING`, `ONLY_WHEN_NOT_SNEAKING`.

- `disabledCompat` (default: `[]`)
  - IDs of mods whose compatibility should be disabled. Enter mod IDs to
    disable compatibility with specific mods if conflicts occur.

- `dumpSlabs` (default: `false`)
  - Set to `true` to have KleeSlabs dump a list of items containing the
    word 'slab' in their name upon world load. This is useful for debugging
    and identifying which blocks are recognized as slabs.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.20.1-0.1.2
- harleycolonies-1.21.1

