---
title: Client-Side-Only Mods
---

Mods and resource packs that run **client-side only**, so they can be
installed when connecting to any server that allows them. This is a general
"things I can always run client-side" catalogue — separate from the
HarleyColonies pack's own mod list, though some appear in both.

Rescued from a stale working clone where it was the only copy. It is the seed
for a proper generated catalogue; until then it is maintained by hand.

## Launcher setup

Set RAM to **8192 MB**.

Additional JVM arguments:

```text
-XX:+UseZGC -XX:+ZGenerational -XX:+AlwaysPreTouch -XX:+DisableExplicitGC -XX:+UseDynamicNumberOfGCThreads -XX:+PerfDisableSharedMem
```

## Baritone

- 1.21.1 NeoForge: `baritone-api-neoforge-1.11.2.jar`

See [Baritone](baritone) for settings and commands.

## Resource Packs

- Better Lanterns
- CLEAN WATER
- Clear Glass with Connected Textures!
- Fast Better Grass
- Fresh Animations
- Fresh Animations: Extensions (load **above** Fresh Animations)
- Fresh Animations: Objects
- HD Font - Inconsolata
- Lower Shield - Enhanced Combat Visibility
- Low On Fire
- Motschen's Better Leaves
- Xray Ultimate

## Mods

### JourneyMap

- JourneyMap
- JourneyMap Integration
- Compass to Map: JourneyMap & Explorer's Compass & Nature's Compass, and
  possibly others — the source list trailed off here, so treat this entry as
  incomplete

Unverified:

- JourneyMap Extra InfoSlots

### Just Enough Items (JEI)

- JEI Enhancements
- JEI Integration: Reborn
- JER Integration
- Just Enough Advancements (JEA)
- Just Enough Beacons Reforged
- Just Enough Breeding (JEBr)
- Just Enough Crafting Tree (JECT)
- Just Enough Effect Descriptions (JEED)
- Just Enough Markers (JEM)
- Just Enough Resources (JER)
- Smithing Template Viewer for JEI/EMI

### Tooltips

- Durability Tooltip
- Durability Viewer
- Enchantment Descriptions
- Food Effect Tooltips (Forge)
- Held Item Tooltips
- Mod Name Tooltip

### Other

- Automatic ToolSwap
- Better Ping Display
- Catalogue
- Compact Help Command
- Ding (Forge)
- Distant Horizons: A Level of Detail mod
- Inventory Sorter
- Just Zoom
- AutoTorch (also seen as "Auto Torch")
- Forgematica
- Sounds Be Gone!

## Known issues

- **Configured** — version mismatch with JEI for Minecolonies Official.
  JEI `19.21.2.313` installed; Configured wants `>= 19.25.0.322`.
- **Equipment Compare** — version mismatch with Curios for Minecolonies
  Official. Curios `9.0.15+1.21.1` installed; Equipment Compare wants
  `>= 9.3.0`.

## Last known installed set

The list above is the **curated** catalogue. This section records what was
actually installed in the rescued instance — the binaries themselves are not
tracked (they are re-downloadable), only the list.

The two do **not** match, and the gaps are informative rather than errors.

### Mods installed

| File | Catalogued above? |
| --- | --- |
| `amecsneoforge-v1.jar` | **no** — Amecs is not in the list |
| `autotorchset-neoforge-1.0.0-1.21.1.jar` | yes — AutoTorch |
| `baritone-api-neoforge-1.11.2.jar` | yes |
| `DistantHorizons-3.0.2-b-1.21.1-fabric-neoforge.jar` | yes |
| `durabilitytooltip-1.1.6-neoforge-mc1.21.jar` | yes |
| `durabilityviewer-1.1.2-neoforge-1.21.8.jar` | yes |
| `forgematica-0.4.1+mc1.21.1.jar` | yes |
| `soundsbegone-neoforge-1.5.1+mc1.21.jar` | yes |

Everything in the catalogue's JourneyMap, JEI, and Tooltips sections is
absent from this instance — those come from the modpack itself rather than
being installed client-side.

### Resource packs installed

| File | Catalogued above? |
| --- | --- |
| `Better-Leaves-9.5.zip` | yes — Motschen's Better Leaves |
| `Inconsolata+120.zip` | yes — HD Font - Inconsolata |
| `XRAY-texture-pack-java.zip` | yes — Xray Ultimate |
| `FreshAnimations_v1.10.4.zip.disabled` | yes, but **disabled** |
| `Better_Farm_Animals_v0.08.zip` | **no** |
| `Faithful 32x - 1.21.1.zip` | **no** |
| `Faithful 64x - Release 6.zip` | **no** |
| `Ozocraft Remix 1.21+ [R15].zip` | **no** |
| `Quark Programmer Art.zip` | **no** |
| `Realistic Animals - 4.0.zip` | **no** |

Catalogued but not installed here: Better Lanterns, CLEAN WATER, Clear Glass
with Connected Textures!, Fast Better Grass, Fresh Animations Extensions and
Objects, Lower Shield, Low On Fire.

Note the overlap between **Fresh Animations** (disabled), **Better Farm
Animals**, and **Realistic Animals** — three packs covering similar ground,
which is likely why one is switched off.
