---
title: System & Control
---

System commands cover the meta-layer: command discovery, settings,
Baritone's own state, the world-chunk cache, and a click-driven
goal picker. Nothing here pathfinds, builds, or mines by itself —
these are the tools you use to inspect, configure, and nudge
Baritone rather than to tell it where to go.

There are no system-specific settings. Almost everything
configurable lives on a topic page (see [settings](settings)) —
this page only documents the `set` command itself.

## Commands

### help / ?

Aliases: `help`, `?`

Browse Baritone's command registry or view the long description
for one specific command.

- `help` with no argument prints a paginated, clickable list of
  every non-hidden command. Each entry hovers to show its names,
  short description, and a "Click to view full help" hint; left-
  clicking runs `help <command>`.
- `help <command>` prints that command's names, short
  description, full long description, and a clickable "return to
  the help menu" line at the end.

#### Arguments

- `[<command>]` — optional command name. If omitted, lists all
  commands.
- `[<page>]` — optional integer page number when listing.

#### Error states

- `Unknown command: <name>` — `help <command>` didn't resolve.

#### Tab completion

Command name for the first argument. No completion for the page
number.

### version

Aliases: `version`

Print the version string from the jar's manifest
(`getClass().getPackage().getImplementationVersion()`).

#### Error states

- `Null version (this is normal in a dev environment)` — no
  manifest version is present. Happens in dev builds where the
  jar hasn't been assembled with a populated `Implementation-
  Version` entry.

### proc

Aliases: `proc`

Dump the process currently in control of Baritone:

- Class (e.g. `baritone.process.MineProcess`)
- Priority (float)
- Temporary (boolean — whether the process auto-yields control
  when idle)
- Display name
- Last `PathingCommand` the process issued (or `None`)

Useful when you're not sure what Baritone is currently trying to
do, or when two processes are fighting for control and you want
to know which one won the last tick.

#### Error states

- `No process in control` — no process has claimed Baritone yet
  this session.

### eta

Aliases: `eta`

Estimated time remaining on the current path. Prints two values:
ticks to the end of the currently-executing segment, and ticks to
the final goal. Both are also converted to seconds assuming 20
TPS — the code explicitly doesn't measure real TPS, so on a
laggy server the seconds figure is optimistic.

ETA to the goal is also genuinely imprecise: the source comment
("really unprecise") reflects that the estimate is based on the
path the planner has extended so far, not on a full route.

#### Error states

- `No process in control` — nothing is pathing, so there's
  nothing to estimate.

### set / setting / settings

Aliases: `set`, `setting`, `settings`

The one-and-only settings command. Every configurable value in
Baritone is read and written through here. The action is the
first argument (or the setting name, for the shorthand forms);
the setting name is the second argument where applicable.

#### Subcommands

- `set` — same as `set list`.
- `set list [<search>] [<page>]` — paginated list of all
  non-Java-only settings. A non-numeric first argument is treated
  as a substring filter.
- `set modified [<search>] [<page>]` — same, but only settings
  whose values differ from the default.
- `set <setting>` — print the current value of one setting.
- `set <setting> <value>` — parse and apply a new value. Type
  checking happens in `SettingsUtil.parseAndApply`.
- `set reset all` — reset every modified setting to its default.
  The bare `set reset` does **not** do this — it prints a
  confirmation prompt reminding you to type `all` explicitly, so
  you can't nuke your config by fat-fingering.
- `set reset <setting>` — reset one setting.
- `set toggle <setting>` — flip a boolean setting. Errors if the
  setting isn't boolean.
- `set save` / `set s` — explicitly save `settings.txt`.
  Normally unnecessary because `set <setting> <value>`,
  `set reset`, and `set toggle` all auto-save.
- `set load` / `set ld [<filename>]` — reset everything to
  defaults and then re-load from `settings.txt` (or the named
  file, relative to `.minecraft/baritone/`). The reset step is
  deliberate — it means `load` produces the same state as if
  you'd started Minecraft with that settings file.

#### Aliases

Two common actions have top-level aliases in `DefaultCommands`:

- `modified`, `mod`, `baritone`, `modifiedsettings` → `set modified`.
  Named `baritone` because it's the fastest way to ask a support
  channel "what have you changed?" — one word.
- `reset` → `set reset`. Bare `reset` inherits the same
  "type `all` to confirm" guard as `set reset`.

#### Output

- List and modified views are paginated and clickable. Each
  setting shows its name, its type in gray parens, and hovering
  shows current value, default value, and type. Clicking
  populates `<prefix>set <name> ` in the chat box for you to
  finish.
- Writing a value logs the old value as a clickable "click to
  revert" line, so undoing a single setting change is one click.
- Turning off [`chatControl`](chat#turning-chat-control-on-and-off)
  while [`chatControlAnyway`](chat#turning-chat-control-on-and-off)
  is already off (or vice versa) prints a red warning that "Chat
  commands will no longer work." Turning off
  [`prefixControl`](chat#turning-chat-control-on-and-off) always
  prints a red warning that "Prefixed commands will no longer
  work." In both cases the clickable-revert line on the previous
  output line lets you back out without restarting, and the other
  control path (if it's still on) remains usable. See
  [Chat & Control](chat) for how these settings interact.

#### Error states

- `a valid setting` (type error) — the setting name didn't
  match anything.
- `Setting <name> can only be used via the api.` — the setting
  is marked Java-only and isn't exposed to chat.
- `a valid value` (type error) — the new value failed to parse
  for the setting's type. Underlying parse exception is printed
  to the game log.
- `a toggleable setting` (type error) — `set toggle` was used
  on a non-Boolean setting.

#### Tab completion

- First argument: settings subcommand names (`list`, `modified`,
  `reset`, `toggle`, `save`, `load`) followed by every setting
  name.
- Second argument: for `reset`, modified-settings names plus
  `all`; for `toggle`, toggleable settings; for `load`, a file
  completer rooted at `.minecraft/baritone/`; for a setting
  name, the current value (and for Booleans, the opposite value
  first so tab-completing is equivalent to toggling).

### click

Aliases: `click`

Open a mouse-driven goal picker. Opens a pause-less screen (game
keeps running) where your cursor ray-casts onto blocks through
the viewport and the block under the crosshair is highlighted
in cyan.

- **Left-click a block** — set a `GoalBlock` to that block and
  start pathing.
- **Left-click-drag** — create a
  [selection](building#sel-selection-s) between the two block
  positions. Replaces any existing selections. Prints a clickable
  `help sel` so you can see what you can do with it.
- **Right-click a block** — set a `GoalBlock` to the block
  *above* the clicked one and start pathing. Useful for standing
  on top of a block instead of inside it.

Drops you back to the game when you close the screen.

#### Tab completion

None.

### reloadall

Aliases: `reloadall`

Discard Baritone's in-memory chunk cache and re-read it from
disk (`ctx.worldData().getCachedWorld().reloadAllFromDisk()`).
Useful after you've edited the cache files externally, or when
the cache seems desynced from what's actually on disk.

This doesn't repull anything from the server — it's a
disk → memory reload, not a world re-scan.

### saveall

Aliases: `saveall`

Flush Baritone's chunk cache to disk
(`ctx.worldData().getCachedWorld().save()`). Normally runs
automatically — you'd only call it manually before a shutdown
you're worried about, or after running `repack` on a huge area
that you want persisted before moving on.

### repack / rescan

Aliases: `repack`, `rescan`

Re-cache every chunk in range around you. Baritone's
`WorldScanner.repack(ctx)` walks the loaded chunks, queues each
for a fresh scan, and reports the count that got queued. Use
this after you've modified a lot of terrain (building, mining,
TNT) and want the cache to reflect current reality before a
`mine`, `goto`, or `find` run.

`rescan` is an alternate name for the same command; nothing
structurally different.

### gc

Aliases: `gc`

Calls `System.gc()` and prints `ok called System.gc()`. This is
a hint to the JVM, not a command — the VM is free to ignore it.
Mostly useful as a "clear anything you can" nudge after a long
session where memory has grown; modern JVMs rarely benefit from
it, so treat this as a debug tool rather than routine
housekeeping.

## Notes & Limitations

- `help` filters on `hiddenFromHelp()`, a per-command override
  that defaults to `false`. No command currently overrides it,
  so every registered command appears in the listing — the
  filter exists for future use.
- `set save` is almost never needed because the individual
  mutating subcommands save automatically. The only time you
  benefit from it is after a script or API caller has set a
  value without going through the `set` command.
- `set load` always resets to defaults first, so it's a
  replace-all operation, not a merge. If you want to layer
  settings from multiple files, you have to write a single
  combined file.
- `click` uses the raw OpenGL projection-view matrix to turn
  mouse coordinates back into world rays, and will hit-test
  against block outlines only (`ClipContext.Block.OUTLINE`,
  `ClipContext.Fluid.NONE`). Fluids and entities are passed
  through, so clicking "on" water selects the block behind it.
- `reloadall` / `saveall` act on the *cache*, not on world
  files owned by the game. They don't touch Minecraft's own
  `level.dat`, region files, or player data.
- `gc` can cause a brief freeze when the JVM actually honors the
  hint. If FPS matters, don't run it mid-movement.
