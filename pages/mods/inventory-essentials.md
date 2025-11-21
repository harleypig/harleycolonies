---
title: Inventory Essentials
---



Client/Server: both

**Inventory Essentials** enhances inventory management with various
quick-transfer features and bulk item movement options. The mod adds
keyboard shortcuts and mouse interactions to quickly move items between
inventories, transfer entire stacks or single items, and perform bulk
operations. This significantly speeds up inventory management, especially
when dealing with large inventories or storage systems.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `inventoryessentials-common.toml`.

#### Transfer Settings

- `enableShiftDrag` (default: `true`)
  - Should holding shift and moving your mouse over items quick-transfer
    them without requiring each to be clicked? When enabled, you can drag
    items while holding shift to quickly transfer them.

- `enableBulkTransferAll` (default: `true`)
  - Should space-clicking an item move all items from that inventory at
    once? When enabled, pressing space while clicking an item transfers all
    items of that type from the source inventory.

- `enableSingleTransfer` (default: `true`)
  - Should ctrl-clicking only move one item at a time instead of the full
    stack? When enabled, holding control while clicking moves only a single
    item rather than the entire stack.

- `allowBulkTransferAllOnEmptySlot` (default: `false`)
  - Should space-clicking move all items even if an empty slot was
    clicked? When enabled, space-clicking an empty slot transfers all items
    from the source inventory.

- `bulkTransferArmorSets` (default: `true`)
  - Should space-clicking armor in the inventory swap to all matching
    armor? When enabled, space-clicking armor pieces swaps all matching
    armor pieces at once.

- `enableBulkTransferSingle` (default: `true`)
  - Should control-space-clicking an item move one of each item from that
    inventory at once? When enabled, holding both control and space while
    clicking transfers one of each different item type.

- `enableBulkTransfer` (default: `true`)
  - Should shift-ctrl-clicking move all items of the same type at once?
    When enabled, holding both shift and control while clicking transfers all
    items matching the clicked item's type.

- `enableBulkDrop` (default: `true`)
  - Should shift-ctrl-drop-clicking drop all items of the same type at
    once? When enabled, holding shift and control while drop-clicking drops
    all items matching the clicked item's type.

#### Development Settings

- `forceClientImplementation` (default: `false`)
  - Use the client implementation even on servers that have the mod
    installed - only useful for development purposes. When enabled, forces
    client-side implementation even when server-side is available.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

