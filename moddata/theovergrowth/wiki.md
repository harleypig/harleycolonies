---
title: TheOvergrowth
---

**TheOvergrowth** adds natural world decay and transformation mechanics to
Minecraft. The mod causes various blocks and structures to degrade over
time, including torches going out, farmland degrading, paths decaying,
mossy blocks forming, mud spreading, and various other natural processes.
This adds realism and encourages active maintenance of builds.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `overgrowth-server.toml`.

#### Global Settings

- `main.globalspeed` (default: `80`)
  - Global update rate. In general how often the individual handlers are
    ticked. `0` to turn it off. Range: `0` to `1000`.

#### Feature Handlers

Each handler controls how often a specific decay/transformation feature is
processed. Higher values mean more frequent updates. Set to `0` to disable
a feature.

- `main.byetorch` (default: `19`)
  - Torch falling handling. The amount of times at a global rate this is
    ticked. Range: `0` to `1000`.

- `main.coastdecline` (default: `18`)
  - Coast decline handling. Range: `0` to `1000`.

- `main.lavadegration` (default: `17`)
  - Lava degradation handling. Range: `0` to `1000`.

- `main.farmlanddegration` (default: `16`)
  - Farmland degradation handling. Range: `0` to `1000`.

- `main.mushrooms` (default: `23`)
  - Mushroom handling. Range: `0` to `1000`.

- `main.growplants` (default: `16`)
  - Plants growing on grass handling. Range: `0` to `1000`.

- `main.underwaterplants` (default: `15`)
  - Underwater plant handling. Range: `0` to `1000`.

- `main.drylava` (default: `17`)
  - Lava drying handling. Range: `0` to `1000`.

- `main.mossyblocks` (default: `14`)
  - Mossy blocks handling. Range: `0` to `1000`.

- `main.drymud` (default: `7`)
  - Mud dry handling. Range: `0` to `1000`.

- `main.spreadmud` (default: `64`)
  - Mud during rain spread handling. Range: `0` to `1000`.

- `main.byecampfire` (default: `11`)
  - Campfire going out handling. Range: `0` to `1000`.

- `main.anvilsand` (default: `13`)
  - Anvil on sand to sandstone handling. Range: `0` to `1000`.

- `main.spiderwebs` (default: `15`)
  - Spiderweb handling. Range: `0` to `1000`.

- `main.byepath` (default: `29`)
  - Grass path decay handling. Range: `0` to `1000`.

- `main.entityspawn` (default: `23`)
  - Entity spawning handling. Range: `0` to `1000`.

- `main.spreadnylium` (default: `24`)
  - Nylium spread handling. Range: `0` to `1000`.

- `main.createpath` (default: `100`)
  - Entities leaving handling (creates paths). Range: `0` to `1000`.

- `main.caveentities` (default: `false`)
  - Allow neutral animals to spawn in caves. When enabled, neutral mobs can
    spawn in cave biomes.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

