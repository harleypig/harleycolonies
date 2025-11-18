# Mining

This document contains all settings related to mining.

## Settings

### `allowOnlyExposedOres`

**Type**: `Boolean`  
**Default**: `false`  

This will only allow baritone to mine exposed ores, can be used to stop ore obfuscators on servers that use them.

---

### `allowOnlyExposedOresDistance`

**Type**: `Integer`  
**Default**: `1`  

When allowOnlyExposedOres is enabled this is the distance around to search.

It is recommended to keep this value low, as it dramatically increases calculation times.

---

### `buildIgnoreDirection`

**Type**: `Boolean`  
**Default**: `false`  

If this is true, the builder will ignore directionality of certain blocks like glazed terracotta.

---

### `buildIgnoreExisting`

**Type**: `Boolean`  
**Default**: `false`  

If this is true, the builder will treat all non-air blocks as correct. It will only place new blocks.

---

### `elytraMinFireworksBeforeLanding`

**Type**: `Integer`  
**Default**: `5`  

The minimum fireworks before landing early for safety

---

### `exploreChunkSetMinimumSize`

**Type**: `Integer`  
**Default**: `10`  

Take the 10 closest chunks, even if they aren't strictly tied for distance metric from origin.

---

### `exploreForBlocks`

**Type**: `Boolean`  
**Default**: `true`  

When GetToBlock or non-legit Mine doesn't know any locations for the desired block, explore randomly instead of giving up.

---

### `exploreMaintainY`

**Type**: `Integer`  
**Default**: `64`  

Attempt to maintain Y coordinate while exploring

-1 to disable

---

### `forceInternalMining`

**Type**: `Boolean`  
**Default**: `true`  

When mining block of a certain type, try to mine two at once instead of one. If the block above is also a goal block, set GoalBlock instead of GoalTwoBlocks If the block below is also a goal block, set GoalBlock to the position one down instead of GoalTwoBlocks

---

### `internalMiningAirException`

**Type**: `Boolean`  
**Default**: `true`  

Modification to the previous setting, only has effect if forceInternalMining is true If true, only apply the previous setting if the block adjacent to the goal isn't air.

---

### `legitMine`

**Type**: `Boolean`  
**Default**: `false`  

Disallow MineBehavior from using X-Ray to see where the ores are. Turn this option on to force it to mine "legit" where it will only mine an ore once it can actually see it, so it won't do or know anything that a normal player couldn't. If you don't want it to look like you're X-Raying, turn this on This will always explore, regardless of exploreForBlocks

---

### `legitMineIncludeDiagonals`

**Type**: `Boolean`  
**Default**: `false`  

Magically see ores that are separated diagonally from existing ores. Basically like mining around the ores that it finds in case there's one there touching it diagonally, except it checks it un-legit-ly without having the mine blocks to see it. You can decide whether this looks plausible or not.

This is disabled because it results in some weird behavior. For example, it can """see""" the top block of a vein of iron_ore through a lava lake. This isn't an issue normally since it won't consider anything touching lava, so it just ignores it. However, this setting expands that and allows it to see the entire vein so it'll mine under the lava lake to get the iron that it can reach without mining blocks adjacent to lava. This really defeats the purpose of legitMine since a player could never do that lol, so thats one reason why its disabled

---

### `legitMineYLevel`

**Type**: `Integer`  
**Default**: `-59`  

What Y level to go to for legit strip mining

---

### `mineDropLoiterDurationMSThanksLouca`

**Type**: `Long`  
**Default**: `250`  

While mining, wait this number of milliseconds after mining an ore to see if it will drop an item instead of immediately going onto the next one

Thanks Louca

---

### `mineGoalUpdateInterval`

**Type**: `Integer`  
**Default**: `5`  

Rescan for the goal once every 5 ticks. Set to 0 to disable.

---

### `mineMaxOreLocationsCount`

**Type**: `Integer`  
**Default**: `64`  

Mine will not scan for or remember more than this many target locations. Note that the number of locations retrieved from cache is additionaly limited by `maxCachedWorldScanCount`.

---

### `mineScanDroppedItems`

**Type**: `Boolean`  
**Default**: `true`  

While mining, should it also consider dropped items of the correct type as a pathing destination (as well as ore blocks)?

---

### `notificationOnExploreFinished`

**Type**: `Boolean`  
**Default**: `true`  

Desktop notification on explore finished

---

### `notificationOnMineFail`

**Type**: `Boolean`  
**Default**: `true`  

Desktop notification on mine fail

---

### `renderGoalIgnoreDepth`

**Type**: `Boolean`  
**Default**: `true`  

Ignore depth when rendering the goal

---

### `renderSelectionBoxesIgnoreDepth`

**Type**: `Boolean`  
**Default**: `true`  

Ignore depth when rendering the selection boxes (to break, to place, to walk into)

---

### `renderSelectionIgnoreDepth`

**Type**: `Boolean`  
**Default**: `true`  

Ignore depth when rendering selections

---

### `useSwordToMine`

**Type**: `Boolean`  
**Default**: `true`  

Use sword to mine.

---


[← Back to Settings Index](baritone/SETTINGS)
