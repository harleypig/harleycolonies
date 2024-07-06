---
title: Minecraft Stuff
---

I want to create my own style for [Minecolonies](https://minecolonies.com). So
we need to start with a list of huts. This list is based off of the
[tutorial](https://minecolonies.com/wiki/tutorials/schematics) for creating
schematics.

* [archery](archery)
* [alchemist](alchemist)
* [baker](baker)
* [barracks](barracks)
* [barrackstower](barrackstower)
* [beekeeper](beekeeper)
* [blacksmith](blacksmith)
* [builder](builder)
* [chickenherder](chickenherder)
* [citizen](citizen)
* [combatacademy](combatacademy)
* [composter](composter)
* [concretemixer](concretemixer)
* [cook](cook)
* [cowboy](cowboy)
* [crusher](crusher)
* [deliveryman](deliveryman) (courier)
* [dyer](dyer)
* [enchanter](enchanter)
* [farmer](farmer)
* [fisherman](fisherman)
* [fletcher](fletcher)
* [florist](florist)
* [glassblower](glassblower)
* [graveyard](graveyard)
* [guardtower](guardtower)
* [hospital](hospital)
* [library](library)
* [lumberjack](lumberjack)
* [mechanic](mechanic)
* [miner](miner)
* [mysticalsite](mysticalsite)
* [netherworker](netherworker)
* [plantation](plantation)
* [rabbithutch](rabbithutch)
* [sawmill](sawmill)
* [school](school)
* [shepherd](shepherd)
* [sifter](sifter)
* [smeltery](smeltery)
* [stonemason](stonemason)
* [stonesmeltery](stonesmeltery)
* [swineherder](swineherder)
* [tavern](tavern)
* [townhall](townhall)
* [university](university)
* [warehouse](warehouse)

## Why?

I'm a minimalist. I want to make as much of the work huts the same layout as
possible. I also want to put them out of site, so most of those work huts will
be belowground.

* Some aboveground huts will extend to the belowground level to allow for
  easier access (e.g., guardtower, citizen maybe).

* Huts in parens after another hut means they are paired, or
  [parent/child](https://minecolonies.com/wiki/tutorials/schematics#how-to-create-parentchild-buildings-or-decorations).
  The goal is to make them autolevel if possible.

* hutname (name #; requirement) - the name in parens is the research branch,
  the number is the level). (see
  [research](https://minecolonies.com/wiki/systems/research))

* Maybe make blueprints have road builtin?

* Maybe create citizen (with guardtower as autolevel child) and also create
  a grouped citizen/guardtower with each of the beekeeper, cowboy,
  rabbithutch, shepherd, swineherder, and chickenherder huts.

## Custom supply ship/camp

TBD

* Include two builder huts and townhall.
* Maybe include citizen hut or two?

## Huts

* builder (building aboveground, but storage space and access to belowground)

* beekeeper
* citizen (guardtower (invisible)) (access to belowground)
* tavern
* townhall (access to belowground)
* warehouse (deliveryman) (belowground)

## Possible grouping

**Be careful of loops**

### Husbandry

???: Will putting all animals in the same pen cause confusion for the worker?

No loops for husbandry.

* cowboy
* rabbithutch
* shepherd
* swineherder
* chickenherder

### Education/Health

* university
* school (civilian 1; residence 3)
* library (civilian 1; residence 3))
* hospital (civilian 1; none)

### Growing Things

* farmer (composter: technology 1; farmer 3)
* plantation (technology 2; farmer 3)
* florist (technology 2; composter 3)
* dyer (technology 2; composter 3) (belowground)

* fisherman
* sifter (technology 2; fisher 3) (belowground?)

### WooWoo

* mysticalsite (civilian 1; none)
* graveyard (civilian 1; townhall 2)

### Wood

* lumberjack
* sawmill (technology 1; lumberjack 3)
* fletcher (technology 2; sawmill 1)

### Cooking

* cook (access to belowground?)
* baker

### Materials

* miner

* smeltery (technology 1; mine 2)
* stonemason (technology 1; mine 3)
* blacksmith (technology 1; mine 3)

* crusher (technology 2; stonemason 3)
* glassblower (technology 2; smeltery 3)
* stonesmeltery (technology 2; stonemason 1)
* mechanic (technology 2; blacksmith 3)

* concretemixer (technology 3; crusher 1)

### Combat

* barracks (barrackstower) (combat 1; guardtower 3)
* archery (combat 2; barracks 3)
* combatacademy (combat 2; barracks 3)

### Undecided

* enchanter
* alchemist (technology 3; none)
* netherworker (technology 2; none)
