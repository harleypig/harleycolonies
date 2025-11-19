# Building

This document contains all commands related to building.

## Commands

### `build`

**Description**: Build a schematic  

Build a schematic from a file.

Usage:
> build <filename> - Loads and builds '<filename>.schematic'
> build <filename> <x> <y> <z> - Custom position

---

### `sel`, `selection`, `s`

**Description**: WorldEdit-like commands  

The sel command allows you to manipulate Baritone's selections, similarly to WorldEdit.

Using these selections, you can clear areas, fill them with blocks, or something else.

The expand/contract/shift commands use a kind of selector to choose which selections to target. Supported ones are a/all, n/newest, and o/oldest.

Usage:
> sel pos1/p1/1 - Set position 1 to your current position.
> sel pos1/p1/1 <x> <y> <z> - Set position 1 to a relative position.
> sel pos2/p2/2 - Set position 2 to your current position.
> sel pos2/p2/2 <x> <y> <z> - Set position 2 to a relative position.

> sel clear/c - Clear the selection.
> sel undo/u - Undo the last action (setting positions, creating selections, etc.)
> sel set/fill/s/f [block] - Completely fill all selections with a block.
> sel walls/w [block] - Fill in the walls of the selection with a specified block.
> sel shell/shl [block] - The same as walls, but fills in a ceiling and floor too.
> sel sphere/sph [block] - Fills the selection with a sphere bounded by the sides.
> sel hsphere/hsph [block] - The same as sphere, but hollow.
> sel cylinder/cyl [block] <axis> - Fills the selection with a cylinder bounded by the sides, oriented about the given axis. (default=y)
> sel hcylinder/hcyl [block] <axis> - The same as cylinder, but hollow.
> sel cleararea/ca - Basically 'set air'.
> sel replace/r <blocks...> <with> - Replaces blocks with another block.
> sel copy/cp <x> <y> <z> - Copy the selected area relative to the specified or your position.
> sel paste/p <x> <y> <z> - Build the copied area relative to the specified or your position.

> sel expand <target> <direction> <blocks> - Expand the targets.
> sel contract <target> <direction> <blocks> - Contract the targets.
> sel shift <target> <direction> <blocks> - Shift the targets (does not resize).

---

### `tunnel`

**Description**: Set a goal to tunnel in your current direction  

The tunnel command sets a goal that tells Baritone to mine completely straight in the direction that you're facing.

Usage:
> tunnel - No arguments, mines in a 1x2 radius.
> tunnel <height> <width> <depth> - Tunnels in a user defined height, width and depth.

---


[← Back to Commands Index](baritone/COMMANDS)
