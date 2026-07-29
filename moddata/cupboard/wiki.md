---
title: Cupboard
---

**Cupboard** is a utility mod that provides various fixes and debugging
tools for Minecraft servers. It helps prevent crashes related to entity
loading, chunk loading, and command execution. The mod includes options
for debugging off-thread entity additions, preventing crashes on entity
load errors, and creating heap dumps for out-of-memory issues.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `cupboard.json`.

#### Error Handling

- `showCommandExecutionErrors` (default: `true`)
  - Whether to display errors during command execution. When enabled,
    errors that occur while executing commands are shown in the console,
    helping identify problematic commands or command handlers.

- `skipErrorOnEntityLoad` (default: `false`)
  - Prevent crashes on entity loading. When enabled, errors during entity
    loading are caught and logged instead of crashing the server. Use with
    caution as this may hide underlying issues.

#### Debug Settings

- `debugChunkloadAttempts` (default: `false`)
  - Enables debug logging of chunks being force-loaded on server thread by
    directly accessing an unloaded chunk, which stalls the server until the
    chunk finishes loading. Incompatible with Lithium and its forks. When
    enabled, logs when mods improperly access unloaded chunks, which can
    cause server lag.

- `logOffthreadEntityAdd` (default: `true`)
  - Entities should only be added on the server thread itself. Cupboard
    fixes the crashes caused by mods violating that. This option enables
    the logging of those violations. When enabled, logs when mods add
    entities from non-server threads, which can cause crashes.

- `forceHeapDumpOnOOM` (default: `false`)
  - Enables creating a heap dump automatically once the game crashes with
    an out of memory issue. Use with care as heap dumps take a lot of
    space. When enabled, a heap dump file is created when the server runs
    out of memory, which can be analyzed to identify memory leaks.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

