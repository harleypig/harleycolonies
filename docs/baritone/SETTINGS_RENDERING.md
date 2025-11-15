# Rendering & Visual

This document contains all settings related to rendering & visual.

## Settings

### `cachedChunksOpacity`

**Type**: `Float`  
**Default**: `0.5`  

0.0f = not visible, fully transparent (instead of setting this to 0, turn off renderCachedChunks) 1.0f = fully opaque

---

### `colorBlocksToBreak`

**Type**: `Color`  
**Default**: `RED`  

The color of the blocks to break

---

### `colorBlocksToPlace`

**Type**: `Color`  
**Default**: `GREEN`  

The color of the blocks to place

---

### `colorBlocksToWalkInto`

**Type**: `Color`  
**Default**: `MAGENTA`  

The color of the blocks to walk into

---

### `colorGoalBox`

**Type**: `Color`  
**Default**: `GREEN`  

The color of the goal box

---

### `colorInvertedGoalBox`

**Type**: `Color`  
**Default**: `RED`  

The color of the goal box when it's inverted

---

### `colorMostRecentConsidered`

**Type**: `Color`  
**Default**: `CYAN`  

The color of the path to the most recent considered node

---

### `colorSelection`

**Type**: `Color`  
**Default**: `CYAN`  

The color of all selections

---

### `colorSelectionPos1`

**Type**: `Color`  
**Default**: `BLACK`  

The color of the selection pos 1

---

### `colorSelectionPos2`

**Type**: `Color`  
**Default**: `ORANGE`  

The color of the selection pos 2

---

### `elytraRenderHitboxRaytraces`

**Type**: `Boolean`  
**Default**: `false`  

Renders the raytraces that are used in the hitbox part of the elytra fly calculation. Requires `elytraRenderRaytraces`.

---

### `elytraRenderRaytraces`

**Type**: `Boolean`  
**Default**: `false`  

Renders the raytraces that are performed by the elytra fly calculation.

---

### `elytraRenderSimulation`

**Type**: `Boolean`  
**Default**: `true`  

Renders the best elytra flight path that was simulated each tick.

---

### `goalRenderLineWidthPixels`

**Type**: `Float`  
**Default**: `3`  

Line width of the goal when rendered, in pixels

---

### `renderCachedChunks`

**Type**: `Boolean`  
**Default**: `false`  

😎 Render cached chunks as semitransparent. Doesn't work with OptiFine 😭 Rarely randomly crashes, see this issue.

Can be very useful on servers with low render distance. After enabling, you may need to reload the world in order for it to have an effect (e.g. disconnect and reconnect, enter then exit the nether, die and respawn, etc). This may literally kill your FPS and CPU because every chunk gets recompiled twice as much as normal, since the cached version comes into range, then the normal one comes from the server for real.

Note that flowing water is cached as AVOID, which is rendered as lava. As you get closer, you may therefore see lava falls being replaced with water falls.

SOLID is rendered as stone in the overworld, netherrack in the nether, and end stone in the end

---

### `renderGoal`

**Type**: `Boolean`  
**Default**: `true`  

Render the goal

---

### `renderGoalAnimated`

**Type**: `Boolean`  
**Default**: `true`  

Render the goal as a sick animated thingy instead of just a box (also controls animation of GoalXZ if `renderGoalXZBeacon` is enabled)

---

### `renderGoalXZBeacon`

**Type**: `Boolean`  
**Default**: `false`  

Renders X/Z type Goals with the vanilla beacon beam effect. Combining this with `renderGoalIgnoreDepth` will cause strange render clipping.

---

### `renderSelection`

**Type**: `Boolean`  
**Default**: `true`  

Render selections

---

### `renderSelectionBoxes`

**Type**: `Boolean`  
**Default**: `true`  

Render selection boxes

---

### `renderSelectionCorners`

**Type**: `Boolean`  
**Default**: `true`  

Render selection corners

---

### `selectionLineWidth`

**Type**: `Float`  
**Default**: `2`  

Line width of the goal when rendered, in pixels

---

### `selectionOpacity`

**Type**: `Float`  
**Default**: `.5`  

The opacity of the selection. 0 is completely transparent, 1 is completely opaque

---


[← Back to Settings Index](SETTINGS.md)
