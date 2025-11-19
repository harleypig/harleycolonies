---
title: Mining & Resources
---

This document contains all commands related to mining & resources.

## Commands

### `blacklist`

**Description**: Blacklist closest block  

While going to a block this command blacklists the closest block so that Baritone won't attempt to get to it.

Usage:
> blacklist

---

### `find`

**Description**: Find positions of a certain block  

The find command searches through Baritone's cache and attempts to find the location of the block.
Tab completion will suggest only cached blocks and uncached blocks can not be found.

Usage:
> find <block> [...] - Try finding the listed blocks

---

### `mine`

**Description**: Mine some blocks  

The mine command allows you to tell Baritone to search for and mine individual blocks.

The specified blocks can be ores, or any other block.

Also see the legitMine settings (see #set l legitMine).

Usage:
> mine diamond_ore - Mines all diamonds it can find.

---

### `pickup`

**Description**: Pickup items  

Usage:
> pickup - Pickup anything
> pickup <item1> <item2> <...> - Pickup certain items

---


[← Back to Commands Index](baritone/COMMANDS)
