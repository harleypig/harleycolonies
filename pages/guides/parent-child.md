# Simple Parent/Child Instructions

*(Instructions for designing a building where one structure is embedded inside another — e.g., courier inside warehouse.)*

**Purpose:** Use this when you want a child building to physically exist inside a parent building or decoration.

### Key Concepts

* The **parent** contains the child.
* Both schematics must use **Placeholders** to indicate where blocks from the other schematic should appear.
* The **child hut block** must appear in the correct place and rotation inside **every** level of the parent.
* The child **cannot be upgraded to a higher level than the parent** (unless the parent is a non-upgradeable decoration).

### Required Setup

* Parent and child schematics **must be located in the same folder**.
* The parent must have a **clear anchor block** selected — otherwise, placement breaks due to multiple hut blocks.
* Avoid **research dependency loops** (don’t make unlocking one require the other in a circular way).

### Recommended Build Workflow

1. Build both parent and child together temporarily in-world to align positioning.
2. Scan the child separately.
3. Paste the child’s hut block into **every** level** of the parent.
4. Ensure the child’s orientation matches your intended final rotation.
5. Do **not** nest children inside children — only one parent layer is supported.

### Level 0 Child-Block Method (Preferred)

* Create **level 0** of the child containing **only the hut block** (placeholders optional).
* Paste that into each level of the parent.
* After embedding, **remove the level 0 blueprint** from your final release.

---

# Auto-Leveling Parent/Child Instructions

*(Instructions for when the child automatically upgrades whenever the parent upgrades.)*

**Purpose:** Useful when the child is purely decorative or has no level-dependent functional blocks.

### How It Works

* Embed **the matching child level** in **each corresponding parent level** (level 1 child in level 1 parent, level 2 child in level 2 parent, etc.).
* During upgrades, the builder upgrades both **parent and child together**.

### Pros

* No need for the player to manage two upgrade paths.

### Cons & Warnings

* **Do not use** auto-leveling for children that require functional blocks (such as beds, furnaces, racks, etc.).
* **Avoid** when the child's unlock is behind research unless you are certain there is no research dependency loop.
* May require manual cleanup of overlapping blocks after pasting.

---

# Common Instructions

### Supported Structure

* One parent may contain **multiple** children.
* Children **cannot** have children of their own.

### Orientation Matters

* The child’s hut must be pasted with the **exact rotation** intended for final gameplay.

### Folder Layout

* The child’s blueprint used as the embedded version must be **in the same folder as the parent**.
* Standalone alternates may exist in separate folders if desired.

### Visibility Tagging

* Mark any blueprint intended **only** for use as a child as **invisible** (via the Tag Tool), so players don’t try to build it standalone.

---

---

# Examples

### Parent/Child Example (Manual Embedding)

**Scenario:** Embedding a Courier inside a Warehouse.

* Build a warehouse and place space blocks where the courier hut will sit.
* In the courier schematic, mark blocks that overlap with the warehouse as **Placeholders**.
* In the warehouse schematic, paste the courier **hut block** at the matching location.
* Fill all overlapping child spaces in the warehouse with **Placeholders**.
* Result: The courier is treated as a functional child building *inside* the warehouse structure.

### Auto-Leveling Example

**Scenario:** Warehouse with an embedded Courier (auto-leveling variant).

* Paste **Warehouse Level 1**.
* Paste **Courier Level 1** into the designated alcove/cut-out in the warehouse; align rotation exactly.
* Repeat for **Warehouse Level 2 + Courier Level 2**, **Warehouse Level 3 + Courier Level 3**, etc.
* When the Warehouse upgrades, the Courier upgrades **automatically** in lockstep.

**Caveats:** This demonstrates auto-leveling with a *functional* child (Courier) and therefore is **not generally recommended**. Expect to resolve overlapping blocks after pasting levels and watch for functional-block transitions (e.g., racks). If players may not have Courier research unlocked at the time the Warehouse is available, prefer the **Level 0 Child-Block** method instead.

---

# Scanning & Embedding Checklist

**Use this list while preparing scans and blueprints:**

1. **Confirm building folders:** Parent and child blueprints must be in the **same folder**.
2. **Decide embedding type:**

   * If child has required furniture → **use Parent/Child** method.
   * If child is decorative → **Auto-Leveling is possible**.
3. **Check for research dependencies** — ensure no unlock loops.
4. **Place the child hut block** into the correct orientation relative to parent.
5. **Use Placeholders** wherever one blueprint’s blocks overlap the other.
6. **Confirm anchor:** Select **main parent hut block** as anchor.
7. **Scan only from your style pack**, *not* your scan folder.
8. **Test upgrade:** Move one level up to ensure child doesn’t exceed parent.

**Differences:**

* Parent/Child → Use **Level 0 child hut** and paste into every parent level.
* Auto-Leveling → Paste **matching-level child** into matching-level parent.

---

# Troubleshooting

### ❗ Anchor Ambiguous

**Issue:** More than one hut block is present.
**Fix:** Manually set the parent’s **main hut block** as the anchor.

### ❗ Child Does Not Appear In-Game

**Likely Cause:** Child blueprint is in a different folder than parent.
**Fix:** Ensure both are in **the same folder**.

### ❗ Child Upgrades Past Parent

**Cause:** Parent missing child hut in higher levels.
**Fix:** Include the **child hut in every level** of the parent.

### ❗ Research Loop Problem

**Cause:** Child requires research that parent also gates.
**Fix:** Provide either:

* A standalone alternate child, **or**
* Reorder research unlock tiers.

### ❗ Auto-Leveling Breaks Storage/Work Blocks

**Cause:** Child blueprint has functional blocks.
**Fix:** Use **manual Parent/Child** method instead.

---
