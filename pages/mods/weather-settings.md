---
title: Weather settings[Forge/Fabric]
---



Client/Server: both

**Weather settings** provides configurable weather control for Minecraft
servers, allowing administrators to set custom weather patterns, durations,
and weights. The mod can skip weather after sleeping and provides commands
for weather control. Weather entries can be configured per dimension with
custom durations and weights for rain and thunder.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `weathersettings.json`.

#### General Settings

- `skipWeatherOnSleep` (default: `false`)
  - Whether to skip weather after sleeping. When enabled, weather is
    cleared after players sleep through the night.

- `clearWeatherCommand` (default: `"weather clear"`)
  - Command for clean weather. This is the command executed when weather
    should be cleared.

#### Weather Entries

- `weatherEntries` (default: `[{"world": "minecraft:overworld", "rain":
  {"command": "weather rain", "weight": 100, "duration": 300,
  "clearDuration": 3600}, "thunder": {"command": "weather thunder",
  "weight": 20, "duration": 200, "clearDuration": 3600}}]`)
  - Weather entries, duration in seconds. Weight is the chance to be
    chosen out of the sum of all weights. Each entry specifies a world
    (dimension), rain settings, and thunder settings. For each weather
    type:
    - `command`: The weather command to execute
    - `weight`: Relative chance for this weather type to be chosen
    - `duration`: How long the weather lasts in seconds
    - `clearDuration`: How long clear weather lasts after this weather type
      ends

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

