# Advanced/Internal

This document contains all settings related to advanced/internal.

## Settings

### `cutoffAtLoadBoundary`

**Type**: `Boolean`  
**Default**: `false`  

After calculating a path (potentially through cached chunks), artificially cut it off to just the part that is entirely within currently loaded chunks. Improves path safety because cached chunks are heavily simplified.

This is much safer to leave off now, and makes pathing more efficient. More explanation in the issue. @see Issue #114

---

### `mapArtMode`

**Type**: `Boolean`  
**Default**: `false`  

Build in map art mode, which makes baritone only care about the top block in each column

---

### `minimumImprovementRepropagation`

**Type**: `Boolean`  
**Default**: `true`  

Don't repropagate cost improvements below 0.01 ticks. They're all just floating point inaccuracies, and there's no point.

---

### `planningTickLookahead`

**Type**: `Integer`  
**Default**: `150`  

Start planning the next path once the remaining movements tick estimates sum up to less than this value

---


[← Back to Settings Index](SETTINGS.md)
