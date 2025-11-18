# Pathfinding & Movement

This document contains all settings related to pathfinding & movement.

## Settings

### `allowDiagonalAscend`

**Type**: `Boolean`  
**Default**: `false`  

Allow diagonal ascending

Actually pretty safe, much safer than diagonal descend tbh

---

### `allowDiagonalDescend`

**Type**: `Boolean`  
**Default**: `false`  

Allow descending diagonally

Safer than allowParkour yet still slightly unsafe, can make contact with unchecked adjacent blocks, so it's unsafe in the nether.

For a generic "take some risks" mode I'd turn on this one, parkour, and parkour place.

---

### `allowDownward`

**Type**: `Boolean`  
**Default**: `true`  

Allow mining the block directly beneath its feet

Turn this off to force it to make more staircases and less shafts

---

### `allowJumpAtBuildLimit`

**Type**: `Boolean`  
**Default**: `false`  

If true, parkour is allowed to make jumps when standing on blocks at the maximum height, so player feet is y=256

Defaults to false because this fails on constantiam. Please let me know if this is ever disabled. Please.

---

### `allowOvershootDiagonalDescend`

**Type**: `Boolean`  
**Default**: `true`  

Is it okay to sprint through a descend followed by a diagonal? The player overshoots the landing, but not enough to fall off. And the diagonal ensures that there isn't lava or anything that's !canWalkInto in that space, so it's technically safe, just a little sketchy.

Note: this is *not* related to the allowDiagonalDescend setting, that is a completely different thing.

---

### `allowParkour`

**Type**: `Boolean`  
**Default**: `false`  

You know what it is

But it's very unreliable and falls off when cornering like all the time so.

It also overshoots the landing pretty much always (making contact with the next block over), so be careful

---

### `allowParkourAscend`

**Type**: `Boolean`  
**Default**: `true`  

This should be monetized it's so good

Defaults to true, but only actually takes effect if allowParkour is also true

---

### `allowVines`

**Type**: `Boolean`  
**Default**: `false`  

Enables some more advanced vine features. They're honestly just gimmicks and won't ever be needed in real pathing scenarios. And they can cause Baritone to get trapped indefinitely in a strange scenario.

Almost never turn this on lol

---

### `allowWalkOnBottomSlab`

**Type**: `Boolean`  
**Default**: `true`  

Slab behavior is complicated, disable this for higher path reliability. Leave enabled if you have bottom slabs everywhere in your base.

---

### `allowWaterBucketFall`

**Type**: `Boolean`  
**Default**: `true`  

Allow Baritone to fall arbitrary distances and place a water bucket beneath it. Reliability: questionable.

---

### `assumeSafeWalk`

**Type**: `Boolean`  
**Default**: `false`  

Assume safe walk functionality; don't sneak on a backplace traverse.

Warning: if you do something janky like sneak-backplace from an ender chest, if this is true it won't sneak right click, it'll just right click, which means it'll open the chest instead of placing against it. That's why this defaults to off.

---

### `assumeStep`

**Type**: `Boolean`  
**Default**: `false`  

Assume step functionality; don't jump on an Ascend.

---

### `assumeWalkOnLava`

**Type**: `Boolean`  
**Default**: `false`  

If you have Fire Resistance and Jesus then I guess you could turn this on lol

---

### `assumeWalkOnWater`

**Type**: `Boolean`  
**Default**: `false`  

Allow Baritone to assume it can walk on still water just like any other block. This functionality is assumed to be provided by a separate library that might have imported Baritone.

Note: This will prevent some usage of the frostwalker enchantment, like pillaring up from water.

---

### `avoidance`

**Type**: `Boolean`  
**Default**: `false`  

Toggle the following 4 settings

They have a noticeable performance impact, so they default off

Specifically, building up the avoidance map on the main thread before pathing starts actually takes a noticeable amount of time, especially when there are a lot of mobs around, and your game jitters for like 200ms while doing so

---

### `avoidBreakingMultiplier`

**Type**: `Double`  
**Default**: `.1`  

this multiplies the break speed, if set above 1 it's "encourage breaking" instead

---

### `avoidUpdatingFallingBlocks`

**Type**: `Boolean`  
**Default**: `true`  

If this setting is true, Baritone will never break a block that is adjacent to an unsupported falling block.

I.E. it will never trigger cascading sand / gravel falls

---

### `backtrackCostFavoringCoefficient`

**Type**: `Double`  
**Default**: `0.5`  

Set to 1.0 to effectively disable this feature @see Issue #18

---

### `blockBreakAdditionalPenalty`

**Type**: `Double`  
**Default**: `2`  

This is just a tiebreaker to make it less likely to break blocks if it can avoid it. For example, fire has a break cost of 0, this makes it nonzero, so all else being equal it will take an otherwise equivalent route that doesn't require it to put out fire.

---

### `blockPlacementPenalty`

**Type**: `Double`  
**Default**: `20`  

It doesn't actually take twenty ticks to place a block, this cost is so high because we want to generally conserve blocks which might be limited.

Decrease to make Baritone more often consider paths that would require placing blocks

---

### `breakCorrectBlockPenaltyMultiplier`

**Type**: `Double`  
**Default**: `10`  

Multiply the cost of breaking a block that's correct in the builder's schematic by this coefficient

---

### `colorBestPathSoFar`

**Type**: `Color`  
**Default**: `BLUE`  

The color of the best path so far

---

### `colorCurrentPath`

**Type**: `Color`  
**Default**: `RED`  

The color of the current path

---

### `colorNextPath`

**Type**: `Color`  
**Default**: `MAGENTA`  

The color of the next path

---

### `costHeuristic`

**Type**: `Double`  
**Default**: `3.563`  

This is the big A* setting. As long as your cost heuristic is an *underestimate*, it's guaranteed to find you the best path. 3.5 is always an underestimate, even if you are sprinting. If you're walking only (with allowSprint off) 4.6 is safe. Any value below 3.5 is never worth it. It's just more computation to find the same path, guaranteed. (specifically, it needs to be strictly slightly less than ActionCosts.WALK_ONE_BLOCK_COST, which is about 3.56)

Setting it at 3.57 or above with sprinting, or to 4.64 or above without sprinting, will result in faster computation, at the cost of a suboptimal path. Any value above the walk / sprint cost will result in it going straight at its goal, and not investigating alternatives, because the combined cost / heuristic metric gets better and better with each block, instead of slightly worse.

Finding the optimal path is worth it, so it's the default.

---

### `costVerificationLookahead`

**Type**: `Integer`  
**Default**: `5`  

Stop 5 movements before anything that made the path COST_INF. For example, if lava has spread across the path, don't walk right up to it then recalculate, it might still be spreading lol

---

### `elytraAutoJump`

**Type**: `Boolean`  
**Default**: `false`  

Automatically path to and jump off of ledges to initiate elytra flight when grounded.

---

### `fadePath`

**Type**: `Boolean`  
**Default**: `false`  

Start fading out the path at 20 movements ahead, and stop rendering it entirely 30 movements ahead. Improves FPS.

---

### `failureTimeoutMS`

**Type**: `Long`  
**Default**: `2000`  

Pathing can never take longer than this, even if that means failing to find any path at all

---

### `followOffsetDirection`

**Type**: `Float`  
**Default**: `0`  

The actual GoalNear is set in this direction from the entity you're following. This value is in degrees.

---

### `followOffsetDistance`

**Type**: `Double`  
**Default**: `0`  

The actual GoalNear is set this distance away from the entity you're following

For example, set followOffsetDistance to 5 and followRadius to 0 to always stay precisely 5 blocks north of your follow target.

---

### `followRadius`

**Type**: `Integer`  
**Default**: `3`  

The radius (for the GoalNear) of how close to your target position you actually have to be

---

### `followTargetMaxDistance`

**Type**: `Integer`  
**Default**: `0`  

The maximum distance to the entity you're following

---

### `jumpPenalty`

**Type**: `Double`  
**Default**: `2`  

Additional penalty for hitting the space bar (ascend, pillar, or parkour) because it uses hunger

---

### `maxCostIncrease`

**Type**: `Double`  
**Default**: `10`  

If a movement's cost increases by more than this amount between calculation and execution (due to changes in the environment / world), cancel and recalculate

---

### `maxFallHeightBucket`

**Type**: `Integer`  
**Default**: `20`  

How far are you allowed to fall onto solid ground (with a water bucket)? It's not that reliable, so I've set it below what would kill an unarmored player (23)

---

### `maxFallHeightNoWater`

**Type**: `Integer`  
**Default**: `3`  

How far are you allowed to fall onto solid ground (without a water bucket)? 3 won't deal any damage. But if you just want to get down the mountain quickly and you have Feather Falling IV, you might set it a bit higher, like 4 or 5.

---

### `maxPathHistoryLength`

**Type**: `Integer`  
**Default**: `300`  

If we are more than 300 movements into the current path, discard the oldest segments, as they are no longer useful

---

### `mobAvoidanceCoefficient`

**Type**: `Double`  
**Default**: `1.5`  

Set to 1.0 to effectively disable this feature

Set below 1.0 to go out of your way to walk near mobs

---

### `mobAvoidanceRadius`

**Type**: `Integer`  
**Default**: `8`  

Distance to avoid mobs.

---

### `mobSpawnerAvoidanceCoefficient`

**Type**: `Double`  
**Default**: `2.0`  

Set to 1.0 to effectively disable this feature

Set below 1.0 to go out of your way to walk near mob spawners

---

### `mobSpawnerAvoidanceRadius`

**Type**: `Integer`  
**Default**: `16`  

Distance to avoid mob spawners.

---

### `movementTimeoutTicks`

**Type**: `Integer`  
**Default**: `100`  

If a movement takes this many ticks more than its initial cost estimate, cancel it

---

### `notificationOnPathComplete`

**Type**: `Boolean`  
**Default**: `true`  

Desktop notification on path complete

---

### `pathCutoffFactor`

**Type**: `Double`  
**Default**: `0.9`  

Static cutoff factor. 0.9 means cut off the last 10% of all paths, regardless of chunk load state

---

### `pathCutoffMinimumLength`

**Type**: `Integer`  
**Default**: `30`  

Only apply static cutoff for paths of at least this length (in terms of number of movements)

---

### `pathHistoryCutoffAmount`

**Type**: `Integer`  
**Default**: `50`  

If the current path is too long, cut off this many movements from the beginning.

---

### `pathingMapDefaultSize`

**Type**: `Integer`  
**Default**: `1024`  

Default size of the Long2ObjectOpenHashMap used in pathing

---

### `pathingMapLoadFactor`

**Type**: `Float`  
**Default**: `0.75`  

Load factor coefficient for the Long2ObjectOpenHashMap used in pathing

Decrease for faster map operations, but higher memory usage

---

### `pathingMaxChunkBorderFetch`

**Type**: `Integer`  
**Default**: `50`  

The maximum number of times it will fetch outside loaded or cached chunks before assuming that pathing has reached the end of the known area, and should therefore stop.

---

### `pathRenderLineWidthPixels`

**Type**: `Float`  
**Default**: `5`  

Line width of the path when rendered, in pixels

---

### `pathThroughCachedOnly`

**Type**: `Boolean`  
**Default**: `false`  

Exclusively use cached chunks for pathing

Never turn this on

---

### `pauseMiningForFallingBlocks`

**Type**: `Boolean`  
**Default**: `true`  

When breaking blocks for a movement, wait until all falling blocks have settled before continuing

---

### `placeIncorrectBlockPenaltyMultiplier`

**Type**: `Double`  
**Default**: `2`  

Multiply the cost of placing a block that's incorrect in the builder's schematic by this coefficient

---

### `planAheadFailureTimeoutMS`

**Type**: `Long`  
**Default**: `5000`  

Planning ahead while executing a segment can never take longer than this, even if that means failing to find any path at all

---

### `planAheadPrimaryTimeoutMS`

**Type**: `Long`  
**Default**: `4000`  

Planning ahead while executing a segment ends after this amount of time, but only if a path has been found

If no valid path (length above the minimum) has been found, pathing continues up until the failure timeout

---

### `primaryTimeoutMS`

**Type**: `Long`  
**Default**: `500`  

Pathing ends after this amount of time, but only if a path has been found

If no valid path (length above the minimum) has been found, pathing continues up until the failure timeout

---

### `renderPath`

**Type**: `Boolean`  
**Default**: `true`  

Render the path

---

### `renderPathAsLine`

**Type**: `Boolean`  
**Default**: `false`  

Render the path as a line instead of a frickin thingy

---

### `renderPathIgnoreDepth`

**Type**: `Boolean`  
**Default**: `true`  

Ignore depth when rendering the path

---

### `schematicFallbackExtension`

**Type**: `String`  
**Default**: `"schematic"`  

The fallback used by the build command when no extension is specified. This may be useful if schematics of a particular format are used often, and the user does not wish to have to specify the extension with every usage.

---

### `slowPath`

**Type**: `Boolean`  
**Default**: `false`  

For debugging, consider nodes much much slower

---

### `slowPathTimeDelayMS`

**Type**: `Long`  
**Default**: `100`  

Milliseconds between each node

---

### `slowPathTimeoutMS`

**Type**: `Long`  
**Default**: `40000`  

The alternative timeout number when slowPath is on

---

### `splicePath`

**Type**: `Boolean`  
**Default**: `true`  

When a new segment is calculated that doesn't overlap with the current one, but simply begins where the current segment ends, splice it on and make a longer combined path. If this setting is off, any planned segment will not be spliced and will instead be the "next path" in PathingBehavior, and will only start after this one ends. Turning this off hurts planning ahead, because the next segment will exist even if it's very short. See `planningTickLookahead`

---

### `walkOnWaterOnePenalty`

**Type**: `Double`  
**Default**: `3`  

Walking on water uses up hunger really quick, so penalize it

---


[← Back to Settings Index](baritone/SETTINGS)
