# Waypoints

This document contains all commands related to waypoints.

## Commands

### `home`

**Type**: Alias → `waypoints goto home`  

**Description**: Path to your home waypoint  

This command is an alias, for: waypoints goto home ...

---

### `sethome`

**Type**: Alias → `waypoints save home`  

**Description**: Sets your home waypoint  

This command is an alias, for: waypoints save home ...

---

### `waypoints`, `waypoint`, `wp`

**Description**: Manage waypoints  

The waypoint command allows you to manage Baritone's waypoints.

Waypoints can be used to mark positions for later. Waypoints are each given a tag and an optional name.

Note that the info, delete, and goal commands let you specify a waypoint by tag. If there is more than one waypoint with a certain tag, then they will let you select which waypoint you mean.

Missing arguments for the save command use the USER tag, creating an unnamed waypoint and your current position as defaults.

Usage:
> wp [l/list] - List all waypoints.
> wp <l/list> <tag> - List all waypoints by tag.
> wp <s/save> - Save an unnamed USER waypoint at your current position
> wp <s/save> [tag] [name] [pos] - Save a waypoint with the specified tag, name and position.
> wp <i/info/show> <tag/name> - Show info on a waypoint by tag or name.
> wp <d/delete> <tag/name> - Delete a waypoint by tag or name.
> wp <restore> <n> - Restore the last n deleted waypoints.
> wp <c/clear> <tag> - Delete all waypoints with the specified tag.
> wp <g/goal> <tag/name> - Set a goal to a waypoint by tag or name.
> wp <goto> <tag/name> - Set a goal to a waypoint by tag or name and start pathing.

---


[← Back to Commands Index](COMMANDS.md)
