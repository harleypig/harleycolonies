---
title: HT's TreeChop
categories:
  - mc-miscellaneous
---

[Website](https://www.curseforge.com/minecraft/mc-mods/treechop) | [Issues](https://github.com/hammertater/treechop/issues) | [Source](https://github.com/hammertater/treechop)

Client/Server: both

**HT's TreeChop** modifies tree chopping mechanics by requiring multiple
chops to fell entire trees. Instead of breaking individual log blocks, the
mod allows players to chop trees progressively, eventually felling the
entire tree including leaves. The mod includes configurable chop counting
algorithms, tree detection settings, visual indicators, and compatibility
with various mods like Tinkers' Construct and Apotheosis.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config files.

#### Client Settings

These settings are configured in `treechop-client.toml`.

- `chopping.choppingEnabled` (default: `true`)
  - Default setting for whether or not the user wishes to chop (can be
    toggled in-game).

- `chopping.sneakBehavior` (default: `"INVERT_CHOPPING"`)
  - Default setting for the effect that sneaking has on chopping (can be
    cycled in-game). Allowed values: `NONE`, `INVERT_CHOPPING`.

- `chopping.treesMustHaveLeaves` (default: `true`)
  - Ignore trees without connected leaves (can be toggled in-game).

- `chopping.chopInCreativeMode` (default: `false`)
  - Enable chopping in creative mode (even when false, sneaking can still
    enable chopping) (can be toggled in-game).

- `visuals.removeBarkOnInteriorLogs` (default: `true`)
  - Visually replace the interior sides of logs with a chopped texture
    instead of bark.

- `visuals.choppingIndicator.enabled` (default: `true`)
  - Show an on-screen indicator when a block will be chopped instead of
    broken (can be toggled in-game).

- `visuals.choppingIndicator.xOffset` (default: `16`)
  - Horizontal location of the indicator relative to the player's
    crosshairs; positive values move the indicator to the right. Range: `-256`
    to `256`.

- `visuals.choppingIndicator.yOffset` (default: `0`)
  - Vertical location of the indicator relative to the player's crosshairs;
    positive values move the indicator down. Range: `-256` to `256`.

- `settingsScreen.showFeedbackMessages` (default: `true`)
  - Show chat confirmations when using hotkeys to change chop settings (can
    be toggled in-game).

- `settingsScreen.showTooltips` (default: `true`)
  - Show tooltips in the settings screen (can be toggled in-game).

#### Common Settings

These settings are configured in `treechop-common.toml`.

- `mod.enabled` (default: `true`)
  - Set to `false` to disable TreeChop without having to uninstall the
    mod.

- `mod.printDebugInfo` (default: `true`)
  - Let TreeChop print to the log.

- `general.dropLootForChoppedBlocks` (default: `true`)
  - If `false`, log items will be destroyed when chopping.

- `general.dropLootOnFirstChop` (default: `false`)
  - If `true`, chopped logs will drop a log item immediately instead of
    waiting for the tree to be felled, restoring legacy behavior. Does
    nothing if `dropLootForChoppedBlocks` is `false`.

- `treeDetection.maxTreeBlocks` (default: `1024`)
  - Maximum number of log blocks that can be detected to belong to one
    tree. Range: `1` to `8096`.

- `treeDetection.maxLeavesBlocks` (default: `1024`)
  - Maximum number of leaves blocks that can destroyed when a tree is
    felled. Range: `1` to `8096`.

- `treeDetection.breakOrDecayLeaves` (default: `"DECAY"`)
  - What to do with leaves blocks when a tree is felled. Allowed values:
    `IGNORE`, `BREAK`, `DECAY`.

- `treeDetection.fellCredit` (default: `"NONE"`)
  - Who to credit for breaking tree blocks (logs and leaves), which can
    change item drops, trigger enchantment effects, etc. Use with caution:
    may cause unexpected interactions with other mods. Allowed values:
    `NONE`, `PLAYER_NOT_TOOL`, `PLAYER_AND_TOOL`.

- `treeDetection.ignorePersistentLeaves` (default: `true`)
  - Non-decayable leaves are ignored when detecting leaves.

- `treeDetection.maxBreakLeavesDistance` (default: `7`)
  - Maximum distance from log blocks to destroy leaves blocks when
    felling. Range: `0` to `16`.

- `treeDetection.logs.blocks` (default: `["#treechop:choppables",
  "#minecraft:logs"]`)
  - Blocks that should be considered choppable. For block lists, specify
    using registry names (mod:block), tags (#mod:tag), namespaces (@mod),
    and Java-style regular expressions.

- `treeDetection.logs.exceptions` (default: `["minecraft:bamboo",
  "#dynamictrees:branches", "dynamictrees:trunk_shell"]`)
  - Blocks that should never be chopped, even if included in the list
    above.

- `treeDetection.leaves.blocks` (default: `["#treechop:leaves_like",
  "#minecraft:leaves", "pamhc2trees:pam[a-z]+"]`)
  - Blocks that should be considered leaves.

- `treeDetection.leaves.exceptions` (default: `[]`)
  - Blocks that should never be considered leaves, even if included in
    the list above.

- `chopCounting.algorithm` (default: `"LOGARITHMIC"`)
  - Method to use for computing the number of chops needed to fell a tree.
    Allowed values: `LINEAR`, `LOGARITHMIC`.

- `chopCounting.rounding` (default: `"NEAREST"`)
  - How to round the number of chops needed to fell a tree. Allowed
    values: `DOWN`, `NEAREST`, `UP`.

- `chopCounting.canRequireMoreChopsThanBlocks` (default: `false`)
  - Felling a tree can require more chops than the number of blocks in
    the tree.

- `chopCounting.logarithmic.a` (default: `10.0`)
  - Determines the number of chops required to fell a tree; higher values
    require more chops for bigger trees. Range: `0.0` to `10000.0`.

- `chopCounting.linear.chopsPerBlock` (default: `1.0`)
  - The number of chops per block required to fell a tree. Range: `0.0` to
    `7.0`.

- `chopCounting.linear.baseNumChops` (default: `0.0`)
  - The base number of chops required to fell a tree regardless of its
    size. Range: `-10000.0` to `10000.0`.

The mod also includes extensive compatibility settings for various mods
like Carry On, Project MMO, The One Probe, Terraformers mods, MultiMine,
Apotheosis, Silent Gear, and Tinkers' Construct. See the config file for
detailed compatibility options.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.20.1-0.1.2
- harleycolonies-1.21.1

