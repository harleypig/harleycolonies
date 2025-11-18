# Exploration

This document contains all commands related to exploration.

## Commands

### `explore`

**Description**: Explore things  

Tell Baritone to explore randomly. If you used explorefilter before this, it will be applied.

Usage:
> explore - Explore from your current position.
> explore <x> <z> - Explore from the specified X and Z position.

---

### `explorefilter`

**Description**: Explore chunks from a json  

Apply an explore filter before using explore, which tells the explore process which chunks have been explored/not explored.

The JSON file will follow this format: [{\
:0,\
:0},...]

If 'invert' is specified, the chunks listed will be considered NOT explored, rather than explored.

Usage:
> explorefilter <path> [invert] - Load the JSON file referenced by the specified path. If invert is specified, it must be the literal word 'invert'.

---


[← Back to Commands Index](COMMANDS.md)
