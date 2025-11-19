# Pathfinding & Navigation

This document contains all commands related to pathfinding & navigation.

## Commands

### `axis`, `highway`

**Description**: Set a goal to the axes  

The axis command sets a goal that tells Baritone to head towards the nearest axis. That is, X=0 or Z=0.

Usage:
> axis

---

### `come`

**Description**: Start heading towards your camera  

The come command tells Baritone to head towards your camera.

This can be useful in hacked clients where freecam doesn't move your player position.

Usage:
> come

---

### `goal`

**Description**: Set or clear the goal  

The goal command allows you to set or clear Baritone's goal.

Wherever a coordinate is expected, you can use ~ just like in regular Minecraft commands. Or, you can just use regular numbers.

Usage:
> goal - Set the goal to your current position
> goal <reset/clear/none> - Erase the goal
> goal <y> - Set the goal to a Y level
> goal <x> <z> - Set the goal to an X,Z position
> goal <x> <y> <z> - Set the goal to an X,Y,Z position

---

### `goto`

**Description**: Go to a coordinate or block  

The goto command tells Baritone to head towards a given goal or block.

Wherever a coordinate is expected, you can use ~ just like in regular Minecraft commands. Or, you can just use regular numbers.

Usage:
> goto <block> - Go to a block, wherever it is in the world
> goto <y> - Go to a Y level
> goto <x> <z> - Go to an X,Z position
> goto <x> <y> <z> - Go to an X,Y,Z position

---

### `path`

**Description**: Start heading towards the goal  

The path command tells Baritone to head towards the current goal.

Usage:
> path - Start the pathing.

---

### `surface`, `top`

**Description**: Used to get out of caves, mines, ...  

The surface/top command tells Baritone to head towards the closest surface-like area.

This can be the surface or the highest available air space, depending on circumstances.

Usage:
> surface - Used to get out of caves, mines, ...
> top - Used to get out of caves, mines, ...

---

### `thisway`, `forward`

**Description**: Travel in your current direction  

Creates a GoalXZ some amount of blocks in the direction you're currently looking

Usage:
> thisway <distance> - makes a GoalXZ distance blocks in front of you

---


[← Back to Commands Index](baritone/COMMANDS)
