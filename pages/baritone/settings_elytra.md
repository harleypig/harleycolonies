---
title: Elytra
---

This document contains all settings related to elytra.

## Settings

### `elytraAllowEmergencyLand`

**Type**: `Boolean`  
**Default**: `true`  

Automatically land when elytra is almost out of durability, or almost out of fireworks

---

### `elytraAllowLandOnNetherFortress`

**Type**: `Boolean`  
**Default**: `false`  

Should elytra consider nether brick a valid landing block

---

### `elytraAutoSwap`

**Type**: `Boolean`  
**Default**: `true`  

Automatically swap the current elytra with a new one when the durability gets too low

---

### `elytraConserveFireworks`

**Type**: `Boolean`  
**Default**: `false`  

If enabled, avoids using fireworks when descending along the flight path.

---

### `elytraFireworkSetbackUseDelay`

**Type**: `Integer`  
**Default**: `15`  

The delay after the player's position is set-back by the server that a firework may be automatically deployed. Value is in ticks.

---

### `elytraFireworkSpeed`

**Type**: `Double`  
**Default**: `1.2`  

The minimum speed that the player can drop to (in blocks/tick) before a firework is automatically deployed.

---

### `elytraFreeLook`

**Type**: `Boolean`  
**Default**: `true`  

Automatically elytra fly without having to force the client-sided rotations.

---

### `elytraMinimumAvoidance`

**Type**: `Double`  
**Default**: `0.2`  

The minimum padding value that is added to the player's hitbox when considering which point to fly to on the path. High values can result in points not being considered which are otherwise safe to fly to. Low values can result in flight paths which are extremely tight, and there's the possibility of crashing due to getting too low to the ground.

---

### `elytraMinimumDurability`

**Type**: `Integer`  
**Default**: `5`  

The minimum durability an elytra can have before being swapped

---

### `elytraNetherSeed`

**Type**: `Long`  
**Default**: `146008555100680`  

The seed used to generate chunks for long distance elytra path-finding in the nether. Defaults to 2b2t's nether seed.

---

### `elytraPitchRange`

**Type**: `Integer`  
**Default**: `25`  

The maximum allowed deviation in pitch from a direct line-of-sight to the flight target. Higher values are computationally more expensive.

---

### `elytraPredictTerrain`

**Type**: `Boolean`  
**Default**: `false`  

Whether nether-pathfinder should generate terrain based on `elytraNetherSeed`. If false all chunks that haven't been loaded are assumed to be air.

---

### `elytraSimulationTicks`

**Type**: `Integer`  
**Default**: `20`  

The number of ticks of elytra movement to simulate while firework boost is not active. Higher values are computationally more expensive.

---

### `elytraSmoothLook`

**Type**: `Boolean`  
**Default**: `false`  

Same as `smoothLook` but for elytra flying.

---

### `elytraTermsAccepted`

**Type**: `Boolean`  
**Default**: `false`  

Has the user read and understood the elytra terms and conditions

---


[← Back to Settings Index](baritone/SETTINGS)
