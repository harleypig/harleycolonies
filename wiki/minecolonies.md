---
title: Minecraft Stuff
---

## Resources

* [Minecolonies Wiki](https://wiki.minecolonies.com)
* [Schematics](https://minecolonies.com/wiki/tutorials/schematics)
* [Datapacks](https://minecolonies.com/wiki/tutorials/datapacks)

## Style

I want to create my own style for [Minecolonies](https://minecolonies.com). So
we need to start with a list of huts. This list is based off of the
[tutorial](https://minecolonies.com/wiki/tutorials/schematics) for creating
schematics.

A list of buildings is available on the wiki. Click on the `Buildings` menu item.

* [Alchemist's Laboratory](alchemist)
* [Apiary](apiary)
* [Archery](archery)
* [Bakerey](bakerery)
* [Barracks](barracks)
* [Barracks Tower](barrackstower)
* [Blacksmith](blacksmith)
* [Builder](builder)
* [Chicken Farmer](chickenfarmer)
* [Combat Academy](combatacademy)
* [Composter](composter)
* [Concrete Mixer](concretemixer)
* [Cookery](cookery)
* [Courier](courier) (courier)
* [Cowhand](cowhand)
* [Crusher](crusher)
* [Dyer](dyer)
* [Enchanter's Tower](enchanter)
* [Farmer](farmer)
* [Fisherman](fisherman)
* [Fletcher](fletcher)
* [Flowershop](flowershop)
* [Forester](forester)
* [Glassblower](glassblower)
* [Graveyard](graveyard)
* [Guard Tower](guardtower)
* [Hospital](hospital)
* [Library](library)
* [Mechanic](mechanic)
* [Mine](mine)
* [Mystical Site](mysticalsite)
* [Nether Mine](nethermine)
* [Plantation](plantation)
* [Quarry](quarry)
* [Rabbit Hutch](rabbithutch)
* [Residence](residence)
* [Sawmill](sawmill)
* [School](school)
* [Shepherd](shepherd)
* [Sifter](sifter)
* [Smeltery](smeltery)
* [Stonemason](stonemason)
* [Stone Smeltery](stonesmeltery)
* [Swineherd](swineherd)
* [Tavern](tavern)
* [Townhall](townhall)
* [University](university)
* [Warehouse](warehouse)

## Why?

I'm a minimalist. I want to make as much of the work huts the same layout as
possible. I also want to put them out of site, so most of those work huts will
be belowground.

### Notes

* Some aboveground huts will extend to the belowground level to allow for
    easier access (e.g., guardtower, resident maybe).

* Huts in parens after another hut means they are paired, or
    [parent/child](https://minecolonies.com/wiki/tutorials/schematics#how-to-create-parentchild-buildings-or-decorations).
    The goal is to make them autolevel if possible.

* hutname (name #; requirement)
  - the name in parens is the research branch,
      the number is the level). (see
      [research](https://minecolonies.com/wiki/systems/research))
  - If a hut has requirements ('field block' for farmer) it will have sub
      bullets starting with 'requires ...'. (see [hut
      requirements](https://minecolonies.com/wiki/tutorials/schematics#hut-requirements))

* Maybe make blueprints have road builtin?

* Maybe create resident (with guardtower as autolevel child) and also create
    a grouped resident/guardtower with each of the beekeeper, cowhand,
    rabbithutch, shepherd, swineherd, and chickenfarmer huts.

* I don't like the quarry, I won't be using it.

## Template World

Use this [template
world](https://www.planetminecraft.com/project/minecolonies-schematics-worlds/)
to help with schematics.

Also, this [basic tutorial](https://www.youtube.com/watch?v=MDxCPKh6im0).

## Custom supply ship/camp

TBD

* Include two builder huts and townhall.
* Maybe include one or two resident hut and/or guard tower?
* Or just flat out cheat and give myself whatever I want ...

## Huts

* The huts in the **Initial** section below must be first.
* **Storage** and **Education** should be next.
* **Wood**, **Basic Materials**, **Cooking**, **Husbandry**, and **Growing
    Things** as you can.
* The rest, but as soon as you can.

### Resident

Special case. Should have guardtower linked, as in note above.

* resident (guardtower (invisible)) (access to belowground)

## Possible Groupings

**Be careful of requirement loops**

### Initial

* townhall (required to be first)
* builder (required to be second)
  - requires minimum 1 rack per hut level
  - building aboveground, but storage space and access to belowground
  - residence/guardtower? Or separate hut for initial placement?

* tavern (strongly recommended)

### Wood

* forester
  - residence/guardtower
* sawmill (technology 1; forester 3)
* fletcher (technology 2; sawmill 1)

### Basic Materials

* mine
  - residence/guardtower (maybe alternate guardtower since guard should be
      assigned to miner--can that be forced?)

### Storage

* warehouse
  - residence/guardtower
  - courier (integrated into warehouse, row of small rooms?)

### Education/Health

Maybe integrate these with townhall?

* university
* school (civilian 1; residence 3)
* library (civilian 1; residence 3))
* hospital (civilian 1; none)

### Cooking

* restaurant (access to belowground?)
  - residence/guardtower
* cookery (access to belowground?)
* bakery (access to belowground?)
  - requires 1 furnace

### Husbandry

???: Will putting all animals in the same pen cause confusion for the worker?

Even though I want these to have the same pen, they shouldn't be linked
because it may take longer to get one or more of them than others (i.e.,
rabbits don't appear in every biome and it may take some time to find them and
bring them home).

* chickenfarmer
* cowhand
* rabbithutch
* shepherd
* swineherd

### Growing Things

* farmer
  - field of fields (5 fields max)
  - can I slave the fields to the farm hut so they level automatically?
  - Can make underground fields.
  - residence/guardtower
* composter (technology 1; farmer 3)
  - requires 1 composter barrel per hut level

--

* fisherman
  - residence/guardtower
  - if including fishing pool in blueprint, the pool must be 7x7x2
      unobstructed blocks of water (2 deep)
  - does unobstructed mean no plants?
  - can I make the pool do double duty for a plantation?
* sifter (technology 2; fisher 3) (belowground?)
  - incorporated into fisherman building?

--

* plantation (technology 2; farmer 3)
  - residence/guardtower
  - can handle up to 3 types of fields (depending on level and research) but
      can swith between multiple types of fields -- look into setting aside
      space for all types of fields?
  - can I make a fisherman's pool do double duty for water plants?

--

* flowershop (technology 2; composter 3)
  - residence/guardtower
  - requires 4 composted dirt block per hut level
* dyer (technology 2; composter 3) (belowground)
  - requires 1 furnace

### WooWoo

* enchanter
  - residence/guardtower
* mysticalsite (civilian 1; none)
* graveyard (civilian 1; townhall 2)
  - requires named graves, more each level (see note in hut requirements link)
* alchemist (technology 3; none)
  - requires 1 brewing stand per level
  - requires 2 soul sand per level starting at level 2 (level 2 needs 4 soul
      sand)
  - requires leaves next to logs (i.e., trees)

### Materials

* smeltery (technology 1; mine 2)
  - residence/guardtower
* stonemason (technology 1; mine 3)
* blacksmith (technology 1; mine 3)

--

* crusher (technology 2; stonemason 3)
  - residence/guardtower
* glassblower (technology 2; smeltery 3)
  - requires 1 furnace per level
* stonesmeltery (technology 2; stonemason 1)

--

* mechanic (technology 2; blacksmith 3)
  - residence/guardtower

--

* concretemixer (technology 3; crusher 1)
  - requires 3 blocks flowing water with solid blocks below, air blocks above,
      and space for the worker to stand next to the water
  - residence/guardtower

--

* nethermine (technology 2; none)
  - residence/guardtower

### Combat

* barracks (barrackstower) (combat 1; guardtower 3)
  - requires 1 barrackstower per level (up to 4)
  - requires 1 bed per level in barrackstower
* archery (combat 2; barracks 3)
  - requires 1 practice dummy (per hut level?)
  - requires 1 bed per hut level level
  - requires 1 standing position per hut level (see requirement link for details)
* combatacademy (combat 2; barracks 3)
  - requires 1 practice dummy per hut level
  - requires 1 bed per hut level

NOTE: A barrackstower doesn't need to be a tower. It could be quonset hut.

## Datapacks

TBD

Customize [datapacks](https://minecolonies.com/wiki/tutorials/datapacks) such
as loot tables, recipes, research, tags ...
