---
title: Dynamic View[Forge]
---



Client/Server: both

**Dynamic View** automatically adjusts chunk view distance and simulation
distance based on server performance. The mod monitors server tick time
and dynamically increases or decreases render distances to maintain optimal
performance. This helps prevent lag spikes and maintains consistent TPS
(ticks per second) by balancing visual quality with server load.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `dynamicview.json`.

#### View Distance Settings

- `minChunkViewDist` (default: `10`)
  - The minimum chunk view distance allowed to use. This is the lowest
    view distance the mod will set, even if server performance is good.
    Range: `3` to `200`.

- `maxChunkViewDist` (default: `10`)
  - The maximum chunk view distance allowed to use. Set to the max a
    player could benefit from. This is the highest view distance the mod
    will set, even if server performance is excellent. Range: `3` to
    `200`.

#### Performance Settings

- `meanAvgTickTime` (default: `45`)
  - The average tick time to stabilize the distances around, in
    milliseconds. Setting it higher than 50ms is not advised, as after 50ms
    the TPS will go below 20. The mod adjusts view distance to try to keep
    tick time around this value. Range: `10` to `100`.

- `viewDistanceUpdateRate` (default: `60`)
  - The change frequency of distances in seconds. This determines how often
    the mod recalculates and adjusts view distance. Lower values mean more
    frequent adjustments but more calculations. Range: `1` to `1000`.

#### Simulation Distance Settings

- `minSimulationDist` (default: `4`)
  - The minimum simulation distance allowed to use. This is the lowest
    simulation distance the mod will set. Range: `1` to `200`.

- `maxSimulationDist` (default: `10`)
  - The maximum simulation distance allowed to use. This is the highest
    simulation distance the mod will set. Range: `1` to `200`.

- `adjustSimulationDistance` (default: `true`)
  - Enables automatic simulation distance adjustment. When enabled, the
    mod automatically adjusts simulation distance along with view distance
    to optimize performance.

#### Debug Settings

- `logMessages` (default: `false`)
  - Whether to output log messages for actions done. This can be helpful
    to balance the other settings nicely. When enabled, logs view distance
    changes and performance metrics.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

