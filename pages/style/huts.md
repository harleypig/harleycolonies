---
title: Huts
---

## Huts

- The huts in the **Initial** section below must be first.
- **Storage** and **Education** should be next.
- **Wood**, **Basic Materials**, **Cooking**, **Husbandry**, and **Growing
    Things** as you can.
- The rest, but as soon as you can.

### Parent/Child Building Implementation

Parent/child buildings allow embedding one building within another for
automatic leveling and integrated designs. Key implementation details:

**Method 1: Level 0 Approach (Recommended)**

- Create a level 0 version of the child containing only the hut block
- Paste this level 0 into all levels of the parent schematic
- Child upgrades independently when player chooses

**Method 2: Auto-leveling**

- Paste matching child levels into parent levels (level 1 child → level 1 parent)
- Child upgrades automatically with parent
- Only use for decorative children without functional requirements

**Requirements:**

- Both buildings must be in the same folder
- Use placeholder blocks where parent/child overlap
- Explicitly set anchor block (main parent hut or Tag Anchor)
- Child hut must be placed with correct location and rotation
- Mark child-only versions as `invisible` using Tag Tool

### Residence/Guardtower Pairing

Special case buildings that should be designed as paired structures by default:

- residence (citizen in filenames)
- guardtower

Implementation options:

- Separate buildings with coordinated design
- Parent/child relationship for auto-leveling
- Shared access to above and below ground areas

Both should provide access to surface and underground areas regardless of
implementation method.

Groupings that have huts that don't require research should be considered for
pairing (e.g., forester, or the restaurant, cookery, and bakery).

Huts that require research and are part of a grouping should be accounted for
in the blueprint.

