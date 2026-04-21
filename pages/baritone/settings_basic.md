---
title: Basic Permissions & Actions (pending consolidation)
---

This file is a holding pen for settings that the auto-generator
grouped under "basic permissions & actions" but that have not yet
been moved to a topic page. Settings already documented on topic
pages (`allowBreak`, `allowSprint`, `allowPlace`, `axisHeight`,
etc.) have been removed; see [pathfinding](pathfinding),
[building](building), [mining](mining), [rendering](rendering),
[waypoints](waypoints), and [elytra](elytra) for those.

The settings below still need a home. They split roughly into
inventory/tool handling, chat-adjacent behavior, and
look/rotation controls.

## Settings

### `allowInventory`

**Type**: `Boolean`
**Default**: `false`

Allow Baritone to move items in your inventory to your hotbar

---

### `antiCheatCompatibility`

**Type**: `Boolean`
**Default**: `true`

Will cause some minor behavioral differences to ensure that Baritone works on anticheats.

At the moment this will silently set the player's rotations when using freeLook so you're not sprinting in directions other than forward, which is picken up by more "advanced" anticheats like AAC, but not NCP.

---

### `assumeExternalAutoTool`

**Type**: `Boolean`
**Default**: `false`

Disable baritone's auto-tool at runtime, but still assume that another mod will provide auto tool functionality

Specifically, path calculation will still assume that an auto tool will run at execution time, even though Baritone itself will not do that.

---

### `autoTool`

**Type**: `Boolean`
**Default**: `true`

Automatically select the best available tool

---

### `blockFreeLook`

**Type**: `Boolean`
**Default**: `false`

Break and place blocks without having to force the client-sided rotations. Requires `freeLook`.

---

### `inventoryMoveOnlyIfStationary`

**Type**: `Boolean`
**Default**: `false`

Come to a halt before doing any inventory moves. Intended for anticheat such as 2b2t

---

### `itemSaver`

**Type**: `Boolean`
**Default**: `false`

Stop using tools just before they are going to break.

---

### `itemSaverThreshold`

**Type**: `Integer`
**Default**: `10`

Durability to leave on the tool when using itemSaver

---

### `preferSilkTouch`

**Type**: `Boolean`
**Default**: `false`

Always prefer silk touch tools over regular tools. This will not sacrifice speed, but it will always prefer silk touch tools over other tools of the same speed. This includes always choosing ANY silk touch tool over your hand.

---

### `randomLooking`

**Type**: `Double`
**Default**: `0.01`

How many degrees to randomize the pitch and yaw every tick. Set to 0 to disable

---

### `randomLooking113`

**Type**: `Double`
**Default**: `2`

How many degrees to randomize the yaw every tick. Set to 0 to disable

---

### `remainWithExistingLookDirection`

**Type**: `Boolean`
**Default**: `true`

When true, the player will remain with its existing look direction as often as possible. Although, in some cases this can get it stuck, hence this setting to disable that behavior.

---

### `repackOnAnyBlockChange`

**Type**: `Boolean`
**Default**: `true`

Whenever a block changes, repack the whole chunk that it's in

---

### `rightClickSpeed`

**Type**: `Integer`
**Default**: `4`

How many ticks between right clicks are allowed. Default in game is 4

---

### `smoothLookTicks`

**Type**: `Integer`
**Default**: `5`

The number of ticks to average across for `smoothLook`;

---

### `ticksBetweenInventoryMoves`

**Type**: `Integer`
**Default**: `1`

Wait this many ticks between InventoryBehavior moving inventory items

---

### `useMessageTag`

**Type**: `Boolean`
**Default**: `false`

Use a modern message tag instead of a prefix when logging to chat
