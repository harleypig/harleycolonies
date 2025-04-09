# Colony Rules

General rules for a colony layout.

This guide assumes the town hall placement has already been scouted, necessary
resources have been accounted for, etc.

## Guard Tower Coverage

Every hut block must be within 140 blocks of a guard tower’s hut block based
on the level 3 patrol radius of 140 blocks for full safety.

Early-game gaps in coverage at levels 1 (80-block radius) and 2 (110-block
radius) are acceptable, as colonists can manage until towers are upgraded to
level 3.

## Guard Tower Placement (Diamond Pattern)

Guard towers are arranged in a diamond pattern, spaced 280 blocks apart along
the vertical and horizontal axes (forming the vertexes of the diamond).

The Town Hall is at (0, 0). The first four guard towers are placed at (0,
140), (0, -140), (140, 0), and (-140, 0), forming the initial diamond ring
around the Town Hall.

Future towers are added in an alternating pattern as described below in the
`Other Intersections` section.

## Initial Hut Placement

The Town Hall is placed first at (0, 0), serving as the initial geographic
center of the colony.

The player will need to map out the roads and mark the areas where guard
towers will be created before beginning construction.

The Builder's hut must be placed and built first, as this is a requirement of
the mod. Place it within the planned 140-block radius of the Town Hall, ideally
close to where resources and construction will be needed.

After the Builder's hut is operational, the player may choose the sequence of
builds.  Generally, the Miner and Forester's huts should be built second and
third, but the order is up to the player. These should be placed within the
140-block radius of the planned guard towers, with their exact positions
determined based on terrain and resource availability (e.g., Forester near
trees, Miner near a hill).

After these initial buildings are established, the four guard towers should be
built at (0, 140), (140, 0), (0, -140), and (-140, 0) to establish the
cardinal pattern of protection.

The colony will generally start with 4 colonists total.  After assigning
colonists to the Builder, Miner, and Forester positions, you'll have one
unemployed colonist. Leaving this colonist unemployed is strategic - as each
guard tower is built, you can assign an unemployed colonist to it as a guard,
and a new colonist will automatically fill the empty slot without requiring
additional houses. This maximizes your early population efficiency.

A tavern should also be constructed during this phase of development. The tavern allows for recruiting additional colonists and serves as a social hub. The exact timing of the tavern construction is flexible and can be adjusted based on the player's priorities and resource availability.

Once the guard towers are in place, houses should be built for each worker to
ensure they have proper accommodations.

Once all these initial buildings are established, complete the road network.

## Road Layout

### Basic Road Structure

- All main roads follow a simple grid pattern, running only North-South or East-West
- Each road is 5 blocks wide (3 blocks of path with 1 block border on each side)
- Roads form the backbone of your colony's organization

### Town Hall Intersection

- The Town Hall sits at coordinates (0, 0)
- Roads surround the Town Hall on all four sides, creating a central plaza
- This forms a + shaped intersection with the Town Hall in the middle
- The central plaza is a 5×5 block area with the Town Hall at its center

### Other Intersections

All other road intersections follow a consistent pattern:

Initial guard towers are placed at the cardinal intersections (N, E, S, W) at
140 blocks from Town Hall

From there, intersections alternate between parks or gardens and guard towers.

### Visual Example

```
   |              |              |
---P--------------G--------------P---
   |              |              |
   |              |              |
   |              |              |
   |              |              |
   |              |              |
   |              |              |
   |              |              |
   |              |              |
   |              |              |
   |              |              |
   |              |              |
   |              |              |
   |              |              |
   |              |              |
---G--------------T--------------G---
   |              |              |
   |              |              |
   |              |              |
   |              |              |
   |              |              |
   |              |              |
   |              |              |
   |              |              |
   |              |              |
   |              |              |
   |              |              |
   |              |              |
   |              |              |
   |              |              |
---P--------------G--------------P---
   |              |              |
```

This is a 14:1 scale.

- T = Town Hall
- G = Guard Tower
- P = Park/Garden
- | and -- = Roads

## Colony Growth and Center Shift

The Town Hall starts as the geographic center at (0, 0), but the colony’s
center can shift as it grows (e.g., toward a mining area at (-200, 100)) to
accommodate resource needs or expansion.

New guard towers and huts are added organically, following the diamond pattern
for towers and placing huts within the 140-block radius of the nearest tower
at level 3.

## Aesthetic and Efficiency Balance

The diamond pattern for guard towers ensures the center (Town Hall) is covered
by all four towers, with an 82-block overlap between adjacent towers’ patrol
areas at level 3, minimizing overlap while maintaining full coverage.

Roads are N-S and E-W to avoid jagged diagonal paths, maintaining a clean,
grid-based aesthetic in Minecraft’s blocky environment.
