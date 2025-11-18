# Building Hut Requirements

This document provides detailed building requirements and schematic
configurations for all huts in the custom Minecolonies style.

If you're new to this style, start with the [Getting Started](guides/getting-started)
guide, which provides a beginner-friendly build order and recommendations.

## Residence/Guard Tower

* 1 bed for guard Tower
* per level for residence:
  * 1 bed

**Possible Parent/Child Configuration:**
* Auto-leveling parent/child relationship
* Guard Tower bed is not functional, making auto-leveling viable
* Residence (parent) can have Guard Tower as auto-leveling child
* Residence can also have other huts with no functional requirements and no
  unlocking requirements as auto-leveling children (e.g., Forester's Hut)

## Town Hall

* Schematic with spaces for tavern and food huts?

**Possible Parent/Child Configuration:**
* Standalone building (no parent/child relationships)
* Or simple setup with tavern and food huts?

## Builder

!!! Because builder hut must be initially built first, either create a separate hut schematic for first time placement, or make special schematic.

* Residence/Guard Tower
* Builder's Hut
  * per level:
    * 1 rack

**Possible Parent/Child Configuration:**
* Simple parent/child OR decoration with locations
* Builder's Hut has functional racks per level (simple parent/child if
  embedding)
* Residence/Guard Tower combo has functional beds (auto-level viable for
  that relationship)
* Need to experiment: Builder could be decoration parent with embedded
  Residence/Guard Tower child, or separate placement
* If embedding Builder's Hut: use simple parent/child (level 0 method)

## Wood

*See [Getting Started Guide - Basic Resource Processing](getting-started.md#4-basic-resource-processing) for build order recommendations.*

* Residence/Guard Tower
* Forester's Hut
* Sawmill (Woodwork)
* Fletcher's Hut (Stringwork)

**Possible Parent/Child Configuration:**
* Residence (parent) with auto-leveling children:
  * Guard Tower (no functional requirements, no unlock requirements)
  * Forester's Hut (no functional requirements, no unlock requirements)
* If mixing auto-level and simple parent/child is supported:
  * Sawmill and Fletcher's Hut as simple children (have functional work blocks)
* Otherwise:
  * Sawmill and Fletcher's Hut marked as "place hut here" decoration markers
  * Decoration parent with separate hut placements for Sawmill and Fletcher

## Stone

*See [Getting Started Guide - Basic Resource Processing](getting-started.md#4-basic-resource-processing) for build order recommendations.*

* Residence/Guard Tower
* Mine
  * 3 ladders on blocks, with tags 'cobble' and 'ladder'
* Quarry
* Stonemason's Hut (Stone Cake)
* Crusher's Hut (Rocking Roll)
* Stone Smeltery (The Flintstones)
  * per level:
    * 1 furnace

**Possible Parent/Child Configuration:**
* Decoration with locations OR simple parent/child for some relationships
* Stone Smeltery has functional furnaces per level
* Mine has functional ladder requirements
* Residence/Guard Tower: auto-level relationship
* If embedding: use simple parent/child (level 0 method) due to functional
  blocks
* Recommend: Decoration parent with separate hut placements for flexibility

## Storage

*See [Getting Started Guide - Storage and Logistics](getting-started.md#1-storage-and-logistics) for build order recommendations.*

* Residence/Guard Tower
* Warehouse
  * racks - ALL THE RACKS!
* Courier's Hut (10)

**Possible Parent/Child Configuration:**
* Classic example: Warehouse (parent) with embedded Courier's Hut (child)
* Warehouse has functional racks - use simple parent/child (level 0 method)
* Courier's Hut can be embedded in Warehouse as child (common pattern)
* Residence/Guard Tower: auto-level relationship
* Recommended: Warehouse as parent with Courier child, OR decoration with
  locations if keeping separate for flexibility

## Feed the Masses

*See [Getting Started Guide - Food Processing](getting-started.md#3-food-processing) for build order recommendations.*

* Residence/Guard Tower
* Tavern
  * 4 beds and a dining room
  * (suggested) barrels - details?
* Restaurant
  * per level:
    * 1 furnace
* Cookery
* Bakery
  * a furnace

**Possible Parent/Child Configuration:**
* Decoration with locations OR simple parent/child for some relationships
* Tavern has functional beds and barrels
* Restaurant and Bakery have functional furnaces
* Residence/Guard Tower: auto-level relationship
* All have functional blocks - use simple parent/child (level 0 method) if
  embedding
* Recommend: Decoration parent with separate hut placements for flexibility

## Learning

* Residence/Guard Tower
* University
  * bookshelves
* School (Higher Learning)
  * per level:
    * 2 carpet (suggest 4? what does this mean?)
* Library (Keen)
  * bookshelves
* Hospital (Stamina)
  * per level:
    * 1 bed

**Possible Parent/Child Configuration:**
* Decoration with locations OR simple parent/child for some relationships
* Hospital has functional beds per level
* University and Library have functional bookshelves
* Residence/Guard Tower: auto-level relationship
* All have functional blocks - use simple parent/child (level 0 method) if
  embedding
* Recommend: Decoration parent with separate hut placements for flexibility

## Produce

*See [Getting Started Guide - Food Production](getting-started.md#2-food-production) for build order recommendations.*

* Residence/Guard Tower
* Farmer's Hut
* Composter's Hut (Biodegradable)
  * per level:
    * 1 composer barrel

**Possible Parent/Child Configuration:**
* Decoration with locations OR simple parent/child (Farmer/Composter combo)
* Composter's Hut has functional barrels per level
* Farmer's Hut has functional field/work block requirements
* Residence/Guard Tower: auto-level relationship
* If embedding: use simple parent/child (level 0 method) due to functional
  blocks
* Common pattern: Farmer's Hut parent with Composter child (fields embedded)

## Meat

*See [Getting Started Guide - Food Production](getting-started.md#2-food-production) for build order recommendations.*

* Residence/Guard Tower
* Chicken Farmer's Hut
* Cowhand's Hut
* Rabbit Hutch
* Shepherd's Hut
* Swineherd's Hut

**Possible Parent/Child Configuration:**
* Decoration with locations OR simple parent/child for some relationships
* All animal huts have functional work block requirements
* Residence/Guard Tower: auto-level relationship
* If embedding: use simple parent/child (level 0 method) due to functional
  blocks
* Recommend: Decoration parent with separate hut placements for flexibility
  (multiple animal types)

## Meat II

*See [Getting Started Guide - Food Production](getting-started.md#2-food-production) for build order recommendations.*

* Residence/Guard Tower
* Fisher's Hut
  * unobstructed body of water:
    * 7x7 blocks square
    * 2 blocks deep
* Sifter's Hut (Sieving) With Fisher?

**Possible Parent/Child Configuration:**
* Decoration with locations OR simple parent/child (Fisher/Sifter combo)
* Fisher's Hut requires specific water layout (likely decoration placement)
* Sifter's Hut has functional work block requirements
* Residence/Guard Tower: auto-level relationship
* If embedding: use simple parent/child (level 0 method) but Fisher's water
  requirement suggests decoration approach
* Recommend: Decoration parent with separate placements (water requirement
  constraints)

## Naming???

* Residence/Guard Tower
* Apiary
* Flowershop (Flower Power)
  * per level:
    * 4 compost (barrel or compost in a frame?)
* Dyer's Hut (Rainbow Heaven)
  * 1 furnace

**Possible Parent/Child Configuration:**
* Decoration with locations OR simple parent/child for some relationships
* Flowershop has functional compost per level
* Dyer's Hut has functional furnace
* Residence/Guard Tower: auto-level relationship
* If embedding: use simple parent/child (level 0 method) due to functional
  blocks
* Recommend: Decoration parent with separate hut placements for flexibility

## Metal/Creative/Tinkerer???

*See [Getting Started Guide - Basic Resource Processing](getting-started.md#4-basic-resource-processing) for build order recommendations.*

* Residence/Guard Tower
* Blacksmith's Hut (Hitting Iron!)
* Mechanic's Hut (What ya Need?)
* Smeltery (Hot!)
  * per level:
    * 1 furnace
* Glassblower's Hut (Those Lungs!)
  * per level:
    * 1 furnace
* Concrete Mixer's Hut (Pave the Road)
  * 3 blocks of flowing water
    * solid blocks below
    * air blocks above
    * work can stand next to flowing water

**Possible Parent/Child Configuration:**
* Decoration with locations OR simple parent/child for some relationships
* Multiple huts have functional furnaces per level
* Concrete Mixer requires specific water layout (likely decoration placement)
* Residence/Guard Tower: auto-level relationship
* If embedding: use simple parent/child (level 0 method) due to functional
  blocks
* Recommend: Decoration parent with separate placements (water and furnace
  constraints)

## Magic

* Residence/Guard Tower
* Enchanter's Tower
* Alchemist Laboratory (Magic Potions)
  * leaves next to logs (custom trees)
  * per level:
    * 1 brewing stand
    * 2 soul sand (starting at level 2, starts with 4)
* Nether Mine (Open the Nether)
  * nether portal
  * an enclosed 1x1 block, 2 high for worker to hide in

**Possible Parent/Child Configuration:**
* Decoration with locations OR simple parent/child for some relationships
* Alchemist Laboratory has functional brewing stands and soul sand per level
* Nether Mine requires nether portal (likely decoration placement)
* Residence/Guard Tower: auto-level relationship
* If embedding: use simple parent/child (level 0 method) but portal
  requirement suggests decoration approach
* Recommend: Decoration parent with separate placements (portal and brewing
  stand constraints)

## Spiritual

* Residence/Guard Tower
* Mystical Site (Ambition)
* Graveyard (Rememberance)
  * per level:
    * start with 14, but real requirements beyond that, other than increasing
      numbers for each level

**Possible Parent/Child Configuration:**
* Decoration with locations OR auto-leveling parent/child (if purely
  decorative)
* Mystical Site and Graveyard are primarily decorative (no functional blocks
  per level)
* Residence/Guard Tower: auto-level relationship
* Auto-leveling might work if both spiritual buildings are decorative
* Recommend: Decoration parent with separate placements, OR auto-leveling if
  confirmed decorative only

## Combat

* Barracks (Tactic Training)
  * per level:
    * Barracks Tower (total of 4)
      * per level:
        * 1 bed
* Combat Academy (Improved Swords)
  * per level:
    * 1 practice dummy
    * 1 bed
* Archery (Improved Bows)
  * per level:
    * 1 practice dummy per level
    * 1 bed per level
    * 1 standing position (glowstone block or block tagged with 'work')

**Possible Parent/Child Configuration:**
* Barracks (parent) with Barracks Towers (children) - EXISTING parent/child
  relationship
* Barracks Tower beds are functional per level - use simple parent/child
  (level 0 method)
* Combat Academy and Archery have functional beds and work blocks per level
* Recommend: Keep existing Barracks/Towers parent/child, separate placements
  for Combat Academy and Archery (decoration with locations)

## Plantations

* Residence/Guard Tower
* Plantation (Let It Grow)
  * per level:
    * 12 (blocks? need clarification):
      * 4 sugar cane
      * 4 cactus
      * 4 bamboo

**Possible Parent/Child Configuration:**
* Decoration with locations OR simple parent/child relationship
* Plantation has functional crop/block requirements per level
* Residence/Guard Tower: auto-level relationship
* If embedding: use simple parent/child (level 0 method) due to functional
  block requirements
* Recommend: Decoration parent with separate placement (crop space
  requirements)

---

## Basic Layout

See the various sections in the
[Schematics](https://minecolonies.com/wiki/tutorials/schematics) page in the
Minecolonies Wiki.

* Each grouping above (wood, stone, etc.), with some exceptions, will be based
  on an upgradable decoration schematic.
  * Will have access points both above and below ground.
  * Will be surrounded by a road at both ground level and underground.

### Residence/Guard Tower Blueprints

* parent/child
* auto level?
* guard tower will go much higher than residence

**Ground Floor:**
```
+------------+
|           S|
|           t|
+---        a|
|xx|        i|
|  |        r|
|dd|dd-------+
```

**Second/Third Floor:**
```
+------------+
|Bed        S|
|Bed        t|
+---        a|
|xx|        i|
|  |        r|
|--|---------+
```

**Basement Floor:**
```
+------------+
|Bed        S|
|           t|
+---        a|
|xx|        i|
|  |        r|
|--|---------+
```

---

## Notes

* Research Requirement in parens.

* 'per level' is usually a minimum.

* Combat grouping has no Residence or Guard Tower because of Barracks Towers.

### To be researched

* **Mixing relationship types:**
  * Can a parent building have both auto-leveling children and simple
    parent/child children at the same time?
* **Archery, Barracks Tower, and Combat Academy huts:**
  * Are practice dummies considered 'functional' for parent/child relationship?
  * Since beds are decorative, are they considered functional for parent/child
    relationship?
* **Graveyard hut and graves:**
  * Are graves considered 'functional' for parent/child relationship?

See [TODO.md](../../TODO.md) for questions and items to investigate.

