---
title: Minecraft Stuff
---

## Resources

- [Minecolonies Wiki](https://wiki.minecolonies.com)
- [Schematics](https://minecolonies.com/wiki/tutorials/schematics)
- [Datapacks](https://minecolonies.com/wiki/tutorials/datapacks)
- Use this [template
    world](https://www.planetminecraft.com/project/minecolonies-schematics-worlds/)
    to help with schematics.
- This [basic tutorial](https://www.youtube.com/watch?v=MDxCPKh6im0) might be
    helpful.

## Style

I want to create my own style for [Minecolonies](https://minecolonies.com). So
we need to start with a list of huts. This list is based off of the
[tutorial](https://minecolonies.com/wiki/tutorials/schematics) for creating
schematics.

A list of buildings is available on the wiki. Click on the `Buildings` menu item.

- [Alchemist's Laboratory](alchemist)
- [Apiary](apiary)
- [Archery](archery)
- [Bakery](baker)
- [Barracks](barracks)
- [Barracks Tower](barrackstower)
- [Blacksmith](blacksmith)
- [Builder](builder)
- [Chicken Farmer](chickenherder)
- [Combat Academy](combatacademy)
- [Composter](composter)
- [Concrete Mixer](concretemixer)
- [Cookery](cookery)
- [Courier](courier) (courier)
- [Cowhand](cowboy)
- [Crusher](crusher)
- [Dyer](dyer)
- [Enchanter's Tower](enchanter)
- [Farmer](farmer)
- [Fisherman](fisherman)
- [Fletcher](fletcher)
- [Flowershop](flowershop)
- [Forester](lumberjack)
- [Glassblower](glassblower)
- [Graveyard](graveyard)
- [Guard Tower](guardtower)
- [Hospital](hospital)
- [Library](library)
- [Mechanic](mechanic)
- [Mine](mine)
- [Mystical Site](mysticalsite)
- [Nether Mine](nethermine)
- [Plantation](plantation)
- [Quarry](quarry)
- [Rabbit Hutch](rabbithutch)
- [Residence](residence)
- [Sawmill](sawmill)
- [School](school)
- [Shepherd](shepherd)
- [Sifter](sifter)
- [Smeltery](smeltery)
- [Stonemason](stonemason)
- [Stone Smeltery](stonesmeltery)
- [Swineherd](swineherd)
- [Tavern](tavern)
- [Townhall](townhall)
- [University](university)
- [Warehouse](warehouse)

## Why?

I'm a minimalist. I want to standardize the hut layouts as much as possible,
to make creation of the various groupings as easy as possible.

I want to put huts underground that conceptually makes sense. Some groupings
will be all aboveground, or at least on the same level, some might be all
underground, some might be a mix.

For example:

- the farm/composter group would be on the same level, though it's possible
    fields might be scattered about
- the combat academy, archery, and barracks might be all underground
- one of the materials groups might be mixed (e.g., blacksmith above ground
    and the others below)

### Notes

- **Residence/Guardtower pairing**: These appear together throughout the
    document because they should be designed as paired buildings with
    [parent/child](https://minecolonies.com/wiki/tutorials/schematics#how-to-create-parentchild-buildings-or-decorations)
    relationships to enable auto-leveling.

- **Research and requirement notation**: `hutname (research branch level; building requirement)`
  - Example: `sawmill (technology 1; forester 3)` means the sawmill requires
      technology research level 1 AND a forester hut at level 3
  - If no research is needed (like forester), only the hut name is shown
  - See [research system](https://minecolonies.com/wiki/systems/research) for
      details
  - Physical requirements ('field blocks' for farmer, etc.) are listed as
      sub-bullets starting with 'requires ...'. See [hut
      requirements](https://minecolonies.com/wiki/tutorials/schematics#hut-requirements)

- Maybe make blueprints have road builtin?

- I don't like the quarry, I won't be using it.

## Style Packs

All schematics must be organized into style packs, which are similar to
resource packs or data packs. Each style pack contains:

### The pack.json File

Every style pack requires a `pack.json` file with metadata:

```json
{
  "version": 1,
  "pack-format": 1,
  "desc": "Description of your style pack",
  "authors": ["Your Name"],
  "mods": [],
  "name": "Your Style Name",
  "icon": "icon.png"
}
```

Key requirements:

- `version`: Start at 1, increase for each release
- `pack-format`: Must be 1 currently
- `desc`: Description visible in build tool
- `authors`: Array of creator names
- `mods`: Array of required mod IDs (empty if vanilla only)
- `name`: Style pack display name
- `icon`: Optional icon filename

### Folder Structure

Style packs use a specific folder structure in `*/blueprints/yourstylename/`:

- `fundamentals/` - Core buildings (townhall, builder, etc.)
- `infrastructure/` - Roads, bridges, mineshafts
- `civilian/` - Residential and civic buildings
- `craftsmanship/` - Production buildings
- `combat/` - Military buildings
- `decorations/` - Non-functional decorations
  - `decorations/supplies/` - Supply camps and ships

Each folder can have `icon.png` and `icon_disabled.png` for the build tool interface.

## Custom Supply Ships and Camps

Supply ships and camps have specific requirements:

### File Locations

- **Supply Camp**: `blueprints/yourstyle/decorations/supplies/supplycamp.blueprint`
- **Supply Ship**: `blueprints/yourstyle/decorations/supplies/supplyship.blueprint`
- **Nether Ship**: `blueprints/yourstyle/decorations/supplies/nethership.blueprint`

### Requirements

- Only one of each type per style pack (fixed filenames)
- Must include a `groundlevel` tag using the Tag Tool
- Should include builder huts and townhall
- Can include residence and guard tower if desired

### Design Considerations

- Include two builder huts and townhall for faster initial setup
- Consider including one or two residence/guard tower pairs
- Balance between useful starting resources and game balance

## Huts

- The huts in the **Initial** section below must be first.
- **Storage** and **Education** should be next.
- **Wood**, **Basic Materials**, **Cooking**, **Husbandry**, and **Growing
    Things** as you can.
- The rest, but as soon as you can.

### Parent/Child Building Implementation

Parent/child buildings allow embedding one building within another for automatic leveling and integrated designs. Key implementation details:

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

Special case buildings that should be designed as paired structures:

- residence (citizen in filenames)
- guardtower

Implementation options:
- Separate buildings with coordinated design
- Parent/child relationship for auto-leveling
- Shared access to above and below ground areas

Both should provide access to surface and underground areas regardless of implementation method.

## Possible Groupings

**Be careful of requirement loops**

### Initial

- townhall (required to be first)
- builder (required to be second)
  - requires minimum 1 rack per hut level
  - building aboveground, but storage space and access to belowground
  - residence/guardtower? Or separate hut for initial placement?

- tavern (strongly recommended)
  - requires 4 beds and a dining room
  - optionally include barrels for decoration
  - maybe link to restaurant?

### Wood

- residence/guardtower
- lumberjack
- sawmill (technology 1; forester 3)
- fletcher (technology 2; sawmill 1)

### Basic Materials

- residence/guardtower
  - maybe alternate guardtower since guard should be assigned to miner--can
      that be forced?
- mine
  - requires starting ladders tagged with `ladder` and `cobble` where the mineshaft will begin

### Storage

- residence/guardtower
- warehouse
  - requires at least 1 rack at first hut level, and minimum +1 rack for each
      hut level
- courier

### Education/Health

Maybe integrate these with townhall?

- university
  - requires bookshelves
- school (civilian 1; residence 3)
  - requires 2 carpet per hut level
- library (civilian 1; residence 3))
  - requires bookshelves
- hospital (civilian 1; none)
  - requires 1 bed per hut level

### Cooking

- residence/guardtower
- restaurant
  - requires 1 furnace per hut level
- cookery
- baker
  - requires 1 furnace

??? Make residence the parent, guardtower, cookery, and bakery child with
auto-leveling?

### Husbandry

???: Will putting all animals in the same pen cause confusion for the worker?

Even though I want these to have the same pen, they shouldn't be linked
because it may take longer to get one or more of them than others (i.e.,
rabbits don't appear in every biome and it may take some time to find them and
bring them home).

- chickenherder
- cowboy
- rabbithutch
- shepherd
- swineherd

### Growing Things

- residence/guardtower
- farmer
  - field of fields (5 fields max)
  - can I slave the fields to the farm hut so they level automatically?
  - Can make underground fields.
- composter (technology 1; farmer 3)
  - requires 1 composter barrel per hut level

--

- residence/guardtower
- fisherman
  - if including fishing pool: must be at least 7x7x2 unobstructed water blocks
  - unobstructed means no blocks above or within the water area
  - pool can potentially serve dual purpose for plantation water plants
- sifter (technology 2; fisher 3)

--

- plantation (technology 2; farmer 3)
  - requires 12 per hut level, 4 each sugar cane, cactus, bamboo
  - can handle up to 3 types of fields (depending on level and research) but
      can swith between multiple types of fields -- look into setting aside
      space for all types of fields?
  - can I make a fisherman's pool do double duty for water plants?

--

- residence/guardtower
- flowershop (technology 2; composter 3)
  - requires 4 composted dirt block per hut level
- dyer (technology 2; composter 3) (belowground)
  - requires 1 furnace

### WooWoo

- residence/guardtower
- enchanter
- mysticalsite (civilian 1; none)
- graveyard (civilian 1; townhall 2)
  - requires named graves: 14 at level 1, 18 at level 2, 27 at level 3, 36 at level 4, 50 at level 5
- alchemist (technology 3; none)
  - requires 1 brewing stand per hut level
  - requires 2 soul sand per hut level starting at level 2 (level 2 needs 4 soul
      sand)
  - requires leaves next to logs (i.e., trees)

### Materials

- residence/guardtower
- smeltery (technology 1; mine 2)
  - requires 1 furnace per hut level
- stonemason (technology 1; mine 3)
- blacksmith (technology 1; mine 3)

--

- residence/guardtower
- crusher (technology 2; stonemason 3)
- glassblower (technology 2; smeltery 3)
  - requires 1 furnace per hut level
- stonesmeltery (technology 2; stonemason 1)
  - requires 1 furnace per hut level

--

- residence/guardtower
- mechanic (technology 2; blacksmith 3)

--

- residence/guardtower
- concretemixer (technology 3; crusher 1)
  - requires 3 blocks of flowing water with solid blocks below and air blocks above
  - worker must be able to stand adjacent to the water blocks

--

- residence/guardtower
- nethermine (technology 2; none)
  - requires a nether portal and an enclosed 1x1x2 (2 deep) room

### Combat

- barracks (barrackstower) (combat 1; guardtower 3)
  - requires 1 barrackstower per hut level (up to 4)
  - requires 1 bed per hut level in barrackstower
- archery (combat 2; barracks 3)
  - requires 1 practice dummy (target block) per hut level
  - requires 1 bed per hut level
  - requires 1 standing position per hut level (glowstone block or block tagged with `work`)
- combatacademy (combat 2; barracks 3)
  - requires 1 practice dummy per hut level (carved pumpkin on hay bale)
  - requires 1 bed per hut level

NOTE: A barrackstower doesn't need to be a tower. It could be quonset hut.

### Mine Shaft

TBD

### Decorations

- roads should have both above and below ground stacked to make running
    tunnels easier.
  - use [upgradable
      decorations](https://minecolonies.com/wiki/tutorials/schematics#how-to-create-upgradable-decoration-schematics)
  - straight lengths of 11,7,5,3,1
  - intersections: 4 way, 3 way, corner
- parks
- what else?

## Datapacks

TBD

Customize [datapacks](https://minecolonies.com/wiki/tutorials/datapacks) such
as loot tables, recipes, research, tags ...
