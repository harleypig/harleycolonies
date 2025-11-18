# Basic Permissions & Actions

This document contains all settings related to basic permissions & actions.

## Settings

### `allowBreak`

**Type**: `Boolean`  
**Default**: `true`  

Allow Baritone to break blocks

---

### `allowInventory`

**Type**: `Boolean`  
**Default**: `false`  

Allow Baritone to move items in your inventory to your hotbar

---

### `allowParkourPlace`

**Type**: `Boolean`  
**Default**: `false`  

Actually pretty reliable.

Doesn't make it any more dangerous compared to just normal allowParkour th

---

### `allowPlace`

**Type**: `Boolean`  
**Default**: `true`  

Allow Baritone to place blocks

---

### `allowPlaceInFluidsFlow`

**Type**: `Boolean`  
**Default**: `true`  

Allow Baritone to place blocks in flowing fluid

---

### `allowPlaceInFluidsSource`

**Type**: `Boolean`  
**Default**: `true`  

Allow Baritone to place blocks in fluid source blocks

---

### `allowSprint`

**Type**: `Boolean`  
**Default**: `true`  

Allow Baritone to sprint

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

### `axisHeight`

**Type**: `Integer`  
**Default**: `120`  

The "axis" command (aka GoalAxis) will go to a axis, or diagonal axis, at this Y level.

---

### `blacklistClosestOnFailure`

**Type**: `Boolean`  
**Default**: `true`  

When GetToBlockProcess or MineProcess fails to calculate a path, instead of just giving up, mark the closest instance of that block as "unreachable" and go towards the next closest. GetToBlock expands this search to the whole "vein"; MineProcess does not. This is because MineProcess finds individual impossible blocks (like one block in a vein that has gravel on top then lava, so it can't break) Whereas GetToBlock should blacklist the whole "vein" if it can't get to any of them.

---

### `blockBreakSpeed`

**Type**: `Integer`  
**Default**: `6`  

How many ticks between breaking a block and starting to break the next block. Default in game is 6 ticks. Values under 1 will be clamped. The delay only applies to non-instant (1-tick) breaks.

---

### `blockFreeLook`

**Type**: `Boolean`  
**Default**: `false`  

Break and place blocks without having to force the client-sided rotations. Requires `freeLook`.

---

### `blockReachDistance`

**Type**: `Float`  
**Default**: `4.5`  

Block reach distance

---

### `breakFromAbove`

**Type**: `Boolean`  
**Default**: `false`  

Allow standing above a block while mining it, in BuilderProcess

Experimental

---

### `cancelOnGoalInvalidation`

**Type**: `Boolean`  
**Default**: `true`  

Cancel the current path if the goal has changed, and the path originally ended in the goal but doesn't anymore.

Currently only runs when either MineBehavior or FollowBehavior is active.

For example, if Baritone is doing "mine iron_ore", the instant it breaks the ore (and it becomes air), that location is no longer a goal. This means that if this setting is true, it will stop there. If this setting were off, it would continue with its path, and walk into that location. The tradeoff is if this setting is true, it mines ores much faster since it doesn't waste any time getting into locations that no longer contain ores, but on the other hand, it misses some drops, and continues on without ever picking them up.

Also on cosmic prisons this should be set to true since you don't actually mine the ore it just gets replaced with stone.

---

### `considerPotionEffects`

**Type**: `Boolean`  
**Default**: `true`  

For example, if you have Mining Fatigue or Haste, adjust the costs of breaking blocks accordingly.

---

### `disableCompletionCheck`

**Type**: `Boolean`  
**Default**: `false`  

Turn this on if your exploration filter is enormous, you don't want it to check if it's done, and you are just fine with it just hanging on completion

---

### `disconnectOnArrival`

**Type**: `Boolean`  
**Default**: `false`  

Disconnect from the server upon arriving at your goal

---

### `distanceTrim`

**Type**: `Boolean`  
**Default**: `true`  

Trim incorrect positions too far away, helps performance but hurts reliability in very large schematics

---

### `doBedWaypoints`

**Type**: `Boolean`  
**Default**: `true`  

allows baritone to save bed waypoints when interacting with beds

---

### `doDeathWaypoints`

**Type**: `Boolean`  
**Default**: `true`  

allows baritone to save death waypoints

---

### `enterPortal`

**Type**: `Boolean`  
**Default**: `true`  

When running a goto towards a nether portal block, walk all the way into the portal instead of stopping one block before.

---

### `freeLook`

**Type**: `Boolean`  
**Default**: `true`  

Move without having to force the client-sided rotations

---

### `goalBreakFromAbove`

**Type**: `Boolean`  
**Default**: `false`  

As well as breaking from above, set a goal to up and to the side of all blocks to break.

Never turn this on without also turning on breakFromAbove.

---

### `incorrectSize`

**Type**: `Integer`  
**Default**: `100`  

The set of incorrect blocks can never grow beyond this size

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

### `maxYLevelWhileMining`

**Type**: `Integer`  
**Default**: `2031`  

Sets the maximum y level to mine ores at.

---

### `minYLevelWhileMining`

**Type**: `Integer`  
**Default**: `0`  

Sets the minimum y level whilst mining - set to 0 to turn off. if world has negative y values, subtract the min world height to get the value to put here

---

### `overshootTraverse`

**Type**: `Boolean`  
**Default**: `true`  

If we overshoot a traverse and end up one block beyond the destination, mark it as successful anyway.

This helps with speed exceeding 20m/s

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

### `rightClickContainerOnArrival`

**Type**: `Boolean`  
**Default**: `true`  

When running a goto towards a container block (chest, ender chest, furnace, etc), right click and open it once you arrive.

---

### `rightClickSpeed`

**Type**: `Integer`  
**Default**: `4`  

How many ticks between right clicks are allowed. Default in game is 4

---

### `simplifyUnloadedYCoord`

**Type**: `Boolean`  
**Default**: `true`  

If your goal is a GoalBlock in an unloaded chunk, assume it's far enough away that the Y coord doesn't matter yet, and replace it with a GoalXZ to the same place before calculating a path. Once a segment ends within chunk load range of the GoalBlock, it will go back to normal behavior of considering the Y coord. The reasoning is that if your X and Z are 10,000 blocks away, your Y coordinate's accuracy doesn't matter at all until you get much much closer.

---

### `smoothLook`

**Type**: `Boolean`  
**Default**: `false`  

Forces the client-sided yaw rotation to an average of the last `smoothLookTicks` of server-sided rotations.

---

### `smoothLookTicks`

**Type**: `Integer`  
**Default**: `5`  

The number of ticks to average across for `smoothLook`;

---

### `sprintAscends`

**Type**: `Boolean`  
**Default**: `true`  

Sprint and jump a block early on ascends wherever possible

---

### `sprintInWater`

**Type**: `Boolean`  
**Default**: `true`  

Continue sprinting while in water

---

### `strictLiquidCheck`

**Type**: `Boolean`  
**Default**: `false`  

Don't allow breaking blocks next to liquids.

Enable if you have mods adding custom fluid physics.

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

---

### `walkWhileBreaking`

**Type**: `Boolean`  
**Default**: `true`  

Don't stop walking forward when you need to break blocks in your way

---

### `yLevelBoxSize`

**Type**: `Double`  
**Default**: `15`  

The size of the box that is rendered when the current goal is a GoalYLevel

---


[← Back to Settings Index](baritone/SETTINGS)
