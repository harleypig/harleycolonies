---
title: Lazybones Style
---

## Lazybones Style

A MineColonies style built to minimize the number of buildings the player
has to place, move, and manage. It crosses two existing ideas:

- **Barebones** — very small footprints (1x1 and 5x5 builds).
- **Old English** — multiple huts embedded in a single build (residence +
  guard tower, builder + sawmill).

Lazybones takes the density of Old English and the compactness of
Barebones and applies both at the *district* level: the player places a
handful of large, self-contained complexes instead of dozens of
individual huts.

> **Status:** design phase. Nothing is built yet. Sections below are
> marked **Decided** or **Open**; [Open questions](#open-questions) is
> the working list, ordered by what blocks what.

### Design principles

These are the load-bearing rules. Everything else in this document is
derived from them, so a change here ripples.

- **P1 — Density over count.** Every hut that can reasonably share a
  complex with related huts does. The player manages districts, not
  buildings.
- **P2 — Claim-aware modularity.** Layout is modular in the spirit of
  Fortress, but no single schematic may exceed the colony's *current*
  claim. A complex that cannot be placed is worse than one that is
  slightly less dense.
- **P3 — Uniform districts.** Every functional district (the Wall is the
  sole exception) shares one square footprint with identical connector
  points on all four sides, so orientation never matters and any district
  can abut any other.
- **P4 — Chunk alignment is the author's convenience, not the player's.**
  Schematics may be designed on chunk boundaries to make scanning and
  alignment easier. The end user must never need to think about chunks to
  place one.
- **P5 — Self-sufficient districts.** Each district carries its own
  builder, housing, and defense, so bringing a district online does not
  depend on another district's spare capacity.
- **P6 — Research-gated huts ship embedded.** A hut behind research is
  built into the complex from the start. It simply cannot be built until
  the research completes, and upgrades independently afterward.

### Constraints

- **No custom supply camp or ship.** The target server does not permit
  one, so the style cannot rely on a Lazybones-specific starting
  structure. See [Custom Supply Ships and Camps](supply-ships-camps) for
  what a custom supply structure would normally provide. This constraint
  is what drives the two-permanent-Builders decision below.
- **First-builder problem.** The first Builder's Hut is placed before the
  Town Hall Complex exists, so it will usually land somewhere that
  conflicts with the complex. Mitigation: the Town Hall Complex embeds
  **two permanent Builder's Huts**, and the player relocates the initial
  hut into one of those slots once the complex is up.
- **Claim size gates footprint.** The Town Hall Complex must fit inside
  the claim the colony has when it is first placed; later districts must
  fit the claim available when *they* are placed. This is the hard
  ceiling on the district square — see
  [Open questions](#open-questions).
- **Parent/child depth is one level.** Children cannot nest inside
  children, so a district cannot be the parent of a hut that is itself a
  parent. See [Parent/Child Buildings](parent-child).

### The district model

#### District contract

Every functional district must satisfy all of the following. This is the
contract that makes districts interchangeable.

| Requirement | Rule |
| --- | --- |
| Footprint | Identical square, size `S` (see Open questions) |
| Connectors | Identical connector points on **all four** sides |
| Orientation | Placeable in any of the four rotations |
| Builder | Embeds its own Builder's Hut |
| Housing | Embeds Residence(s) sufficient for its workers |
| Defense | Embeds a Guard Tower grid per the coverage rule below |
| Food | *Optional* small Dining Hall / Restaurant |

A district is a **thematic grouping** — organized by what its buildings
do, not by when they unlock.

#### Connector points

Because all four sides carry the same connectors, districts tile in any
arrangement without special corner or edge variants.

The connector spec itself is still open. At minimum it must define the
road/tunnel entry position along each edge, and whether the above-ground
and below-ground road layers both connect — the existing
[groupings](groupings) notes call for roads stacked above and below
ground to make tunnelling easier, which implies two connector planes
rather than one.

#### District catalog

| District | Contents | Status |
| --- | --- | --- |
| Town Hall Complex | Colony center — see below | **Decided** (contents) |
| Husbandry | All animal huts | **Decided** (scope) |
| Agriculture | Crop and plant huts | **Decided** (scope) |
| Mining / Smelting | Extra mines + ore processing | **Open** |
| Forestry / Wood | Extra foresters + wood processing | **Open** |
| Military | Barracks, archery, combat academy | **Open** |
| Crafting / Industry | Blacksmith, mechanic, glassblower, … | **Open** |
| Wall | Perimeter defense — **exempt from the contract** | **Open** |

[Possible Groupings](groupings) is the existing per-hut grouping work and
is the natural source for filling in the open districts, alongside each
hut's physical requirements in [Hut Requirements](huts).

### Town Hall Complex

The functional center of the colony. It holds everything that needs no
research, plus the critical early-game buildings, so a new colony is
fully operational from one placement.

| Building | Notes |
| --- | --- |
| Town Hall | Parent structure |
| Builder's Hut ×2 | Both permanent; see the first-builder constraint |
| Warehouse | Preferably in the basement |
| Courier | Child of the Warehouse, basement |
| University | Parent for Library and School |
| Library | Embedded child, research-gated |
| School | Embedded child, research-gated |
| Hospital | |
| Tavern | For visitors |
| Residence(s) | Count driven by the workers above |
| Fisher's Hut | Starter copy; a dedicated district may hold more |
| Forester's Hut | Starter copy; Forestry district may hold more |
| Mine | Starter copy; Mining district may hold more |
| Dining Hall / Restaurant | |
| Guard Towers | Grid per the coverage rule |

Notes:

- **Starter vs. dedicated.** Fisher, Forester, and Mine appear here as
  single starter copies. Additional copies and their downstream
  processing huts (sawmill, smeltery, sifter, …) belong to the dedicated
  Forestry and Mining districts.
- **Animals are excluded on purpose.** All animal huts live in the
  Husbandry district, never in the Town Hall Complex.
- **Research-gated children.** Library and School are embedded from the
  start per P6. Watch for research dependency loops when wiring the
  parent/child relationships — see the warning in [Parent/Child
  Buildings](parent-child).

### Defined districts

#### Husbandry

All animal buildings: Shepherd, Cowhand, Chicken Farmer, Swineherd,
Rabbit Hutch, and any later additions. Explicitly kept out of the Town
Hall Complex.

The existing [groupings](groupings) note applies here: these huts should
share pen infrastructure but should **not** be linked as parent/child,
because the player may acquire the animals at very different times (a
biome without rabbits can delay the Rabbit Hutch indefinitely).

#### Agriculture

Crop and plant-related buildings: Farmer, Composter, Florist, and
related.

Field placement is the complication — the farmer needs field blocks, the
plantation needs its own field types, and a fisher needs an unobstructed
water volume. Whether fields sit inside the district square or spill
outside it is open, and it is the question most likely to force `S`
upward.

### Wall District

The Wall is the **one exception** to the district contract. It is neither
square nor a fixed size.

- Modular sections placed at the edge of the colony claim, intended for
  late game when the claim is large.
- Creates a **killing field** — open ground in front of the wall.
- Integrates Guard Towers, and possibly Barracks Towers, to give level-5
  coverage along the perimeter.
- Section length and killing-field depth are undetermined.

Because the claim grows over the life of a colony, wall sections must be
placeable incrementally rather than as one perimeter.

### Guard Tower coverage

Every functional district embeds Guard Towers in a grid, sized so that
**coverage is complete at level 5**. Gaps at lower levels are expected
and acceptable — the grid is designed for the end state, not the start.

The geometry, so spacing can be derived once the range is confirmed:

- Let `R` be the effective guard coverage radius at level 5. The source
  brief states 200 blocks; **this needs verifying in-game** before any
  grid is committed.
- For a square grid of towers spaced `G` apart, the worst-case point is
  the center of a cell, at distance `G·√2 / 2` from the nearest tower.
- Full coverage therefore requires `G·√2 / 2 ≤ R`, i.e. **`G ≤ R·√2`**.
- At `R = 200` that gives `G ≤ 283` blocks — comfortably larger than any
  plausible district square, which implies **one tower per district may
  suffice for coverage**, and further towers become a defense-depth
  choice rather than a coverage requirement.

That last point is worth testing early: if it holds, the tower grid stops
constraining the district square and becomes a tuning knob instead.

### Open questions

Ordered by dependency — the earlier ones block the later ones.

1. **What is the district square size `S`?** The keystone. Bounded above
   by the colony claim at the time a district is placed (P2), and bounded
   below by the densest district's contents. Resolving it means measuring
   the claim available at the town hall levels where each district
   realistically comes online.
2. **What is the connector spec?** Edge entry position, above-ground and
   below-ground road layers, and whether tunnels connect at a fixed
   depth.
3. **What is the real level-5 guard coverage radius?** Confirms or
   invalidates the one-tower-per-district conclusion above.
4. **Do Agriculture fields live inside the square or outside it?** Same
   question for the fisher's water volume.
5. **What are the remaining district rosters?** Mining/Smelting,
   Forestry/Wood, Military, Crafting/Industry — populate from
   [groupings](groupings).
6. **Wall section length and killing-field depth.**
7. **Which starting style supplies the supply camp,** and what does the
   handoff to Lazybones look like in practice?
8. **Above-ground vs. below-ground split per district.** The existing
   style notes favour putting huts underground where it makes conceptual
   sense; Lazybones needs a per-district call.

### Build order

A workable sequence once question 1 is answered:

1. Fix `S` and the connector spec.
2. Build the Town Hall Complex first — it is the largest and most
   constrained, so it proves whether `S` is viable at all.
3. Build one simple district (Husbandry is the best candidate — few
   dependencies, no research gating) to validate that the contract and
   the connectors actually tile.
4. Build Agriculture, which stresses the field-placement question.
5. Fill in the remaining districts.
6. Wall sections last — late-game content, and exempt from the contract
   anyway.

### Related pages

- [Style Packs](style-packs) — pack structure and `pack.json`
- [Possible Groupings](groupings) — per-hut grouping and research gates
- [Hut Requirements](huts) — physical requirements per hut
- [Parent/Child Buildings](parent-child) — embedding mechanics
- [Custom Supply Ships and Camps](supply-ships-camps) — what a custom
  supply structure would provide
- [Tag Tool Usage](tag-tool) — tagging for schematic requirements
