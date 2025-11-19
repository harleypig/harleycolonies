---
title: Building & Schematics
---

This document contains all settings related to building & schematics.

## Settings

### `builderTickScanRadius`

**Type**: `Integer`  
**Default**: `5`  

Distance to scan every tick for updates. Expanding this beyond player reach distance (i.e. setting it to 6 or above) is only necessary in very large schematics where rescanning the whole thing is costly.

---

### `buildInLayers`

**Type**: `Boolean`  
**Default**: `false`  

Don't consider the next layer in builder until the current one is done

---

### `buildOnlySelection`

**Type**: `Boolean`  
**Default**: `false`  

Only build the selected part of schematics

---

### `buildRepeat`

**Type**: `Vec3i`  
**Default**: `Vec3i(0, 0, 0)`  

How far to move before repeating the build. 0 to disable repeating on a certain axis, 0,0,0 to disable entirely

---

### `buildRepeatCount`

**Type**: `Integer`  
**Default**: `-1`  

How many times to buildrepeat. -1 for infinite.

---

### `buildRepeatSneaky`

**Type**: `Boolean`  
**Default**: `true`  

Don't notify schematics that they are moved. e.g. replacing will replace the same spots for every repetition Mainly for backward compatibility.

---

### `buildSchematicMirror`

**Type**: `Mirror`  
**Default**: `Mirror.NONE`  

Mirrors the schematic before building it. Possible values are FRONT_BACK - mirror the schematic along its local x axis LEFT_RIGHT - mirror the schematic along its local z axis

---

### `buildSchematicRotation`

**Type**: `Rotation`  
**Default**: `Rotation.NONE`  

Rotates the schematic before building it. Possible values are NONE - No rotation CLOCKWISE_90 - Rotate 90° clockwise CLOCKWISE_180 - Rotate 180° clockwise COUNTERCLOCKWISE_90 - Rotate 270° clockwise

---

### `layerHeight`

**Type**: `Integer`  
**Default**: `1`  

How high should the individual layers be?

---

### `layerOrder`

**Type**: `Boolean`  
**Default**: `false`  

false = build from bottom to top

true = build from top to bottom

---

### `notificationOnBuildFinished`

**Type**: `Boolean`  
**Default**: `true`  

Desktop notification on build finished

---

### `okIfWater`

**Type**: `Boolean`  
**Default**: `false`  

Override builder's behavior to not attempt to correct blocks that are currently water

---

### `schematicOrientationX`

**Type**: `Boolean`  
**Default**: `false`  

When this setting is true, build a schematic with the highest X coordinate being the origin, instead of the lowest

---

### `schematicOrientationY`

**Type**: `Boolean`  
**Default**: `false`  

When this setting is true, build a schematic with the highest Y coordinate being the origin, instead of the lowest

---

### `schematicOrientationZ`

**Type**: `Boolean`  
**Default**: `false`  

When this setting is true, build a schematic with the highest Z coordinate being the origin, instead of the lowest

---

### `skipFailedLayers`

**Type**: `Boolean`  
**Default**: `false`  

If a layer is unable to be constructed, just skip it.

---

### `startAtLayer`

**Type**: `Integer`  
**Default**: `0`  

Start building the schematic at a specific layer. Can help on larger builds when schematic wants to break things its already built

---


[← Back to Settings Index](baritone/SETTINGS)
