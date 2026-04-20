---
title: Waypoints
---

Waypoints are named, tagged positions saved in Baritone's
per-world cache. They're how you bookmark places so you can
come back later — the world spawn, a diamond vein, a base
location — and they're also how a few other commands accept a
"go to here" target. Some tags populate automatically: Baritone
records your bed position when you interact with a bed and
your last death position when you die.

## Settings Index

Alphabetical. Each link jumps to the section that discusses the setting.

- [doBedWaypoints](#automatic-waypoints)
- [doDeathWaypoints](#automatic-waypoints)

## waypoints

Aliases: `waypoints`, `waypoint`, `wp`

Manage Baritone's waypoints. The command dispatches on a
subcommand (called an *action* in the source) that says what to
do — list, save, look up, delete, restore, wipe by tag, or set
a goal. If you run `wp` with no action at all, it defaults to
`list`.

Output is chat-rich: list entries are clickable to select,
info views are clickable to delete / set a goal / produce a
recreate command. The `restore` action leaves a clickable "undo"
on every `delete` and `clear`.

### Subcommands

Each subcommand has short aliases. The first name listed is the
canonical form.

#### waypoints list / get / l

List every waypoint. With a tag argument, list only waypoints
with that tag. Output is paginated.

Error: `No waypoints found` when unfiltered and empty;
`No waypoints found by that tag` when filtered and empty.

#### waypoints save / s

Create a new waypoint. All arguments are optional; omitted
arguments fall back to defaults.

- Tag defaults to `USER` when omitted.
- Name defaults to empty when omitted.
- Position defaults to your current feet position when omitted.

Full form: `wp save <tag> <name> <x> <y> <z>`. Coordinates
accept `~` relatives like regular Minecraft commands.

#### waypoints info / show / i

Show details for a single waypoint, selected by tag or name.
Prints location plus four clickable lines: delete, set goal,
show recreate command (populated in the chat box, not run), and
back to list.

If more than one waypoint matches the selector, a picker
paginated list is shown instead — click the one you want. You
can also disambiguate directly with `@ <timestamp>` appended to
the selector.

#### waypoints delete / d

Delete a single waypoint, same selector rules as `info`.
Baritone keeps the deletion in memory for this session, and
the confirmation message is clickable to restore.

#### waypoints restore

Undo recent deletions. Two forms:

- `wp restore <n>` — restore the last *n* waypoints deleted
  this session (most-recent first).
- `wp restore @ <timestamp> [<timestamp> ...]` — restore
  specific deletions by creation timestamp. This is the form
  the clickable undo messages use.

The deletion history is in-memory only (`private Map` on
`WaypointsCommand`), so restore works within the current
Minecraft session but not across restarts.

#### waypoints clear / c

Delete every waypoint with a given tag. Requires the tag
argument — the command does not default to `USER` here, so
there's no "clear everything" shortcut.

Error: `Invalid tag, "<name>"` when the argument isn't one of
the known tag names or aliases.

#### waypoints goal / g

Set Baritone's goal to a waypoint's position (as a `GoalBlock`)
without starting to path. Use `path` afterward to begin.

#### waypoints goto

Set the goal and start pathing immediately. The go-to-here
shortcut.

### Arguments

Positional arguments depend on the action. Shared patterns:

- Tag selector: one of `home` / `base`, `death`, `bed` /
  `spawn`, `user`. Case-insensitive.
- Name selector: free text.
- `@ <timestamp>` disambiguation: when a tag or name matches
  multiple waypoints, append a literal `@` and the creation
  timestamp to pick one. The timestamp is parsed strictly as a
  `long` (milliseconds since epoch) and matched by exact equality
  — no fuzzy parsing (`last week`, date strings, etc.) and no
  tolerance, so off-by-one fails. Get the exact value from the
  clickable chat output or from `wp info`.
- Position: coordinates in `x y z` form, accepting `~`
  relatives.

### Error states

- `No waypoints found` — `list` or multi-selector with no
  matches.
- `No waypoints found by that tag` — filtered list with no
  matches.
- `Invalid tag, "<name>"` — `clear` received a tag it doesn't
  recognize.
- `Timestamp was specified but no waypoint was found` — `@`
  disambiguation didn't match any waypoint.

### Tab completion

- First argument: all action names and aliases.
- After `list`, `save`, or `clear`: tag names.
- After `info`, `delete`, `goal`, or `goto`: waypoint selectors.
- Third argument after `save`: a `RelativeBlockPos` completer
  for coordinates.
- After `restore`: none (use the clickable chat messages).

## Tags

The four built-in tags, with their aliases:

- **HOME** — `home`, `base`. User-created, no automatic source.
- **DEATH** — `death`. Populated automatically when you die,
  gated by `doDeathWaypoints`.
- **BED** — `bed`, `spawn`. Populated automatically on bed
  interaction, gated by `doBedWaypoints`.
- **USER** — `user`. The default tag for manually-created
  waypoints when `save` is invoked without a tag argument.

Tags are enum values, not free-form strings. You cannot create
a new tag.

### Multiples per tag

A tag is a *label*, not a single-slot. Every tag holds a set of
waypoints, and there's no uniqueness constraint on name or
position. Running `sethome` from two different locations keeps
both; dying ten times creates ten `DEATH` entries; interacting
with two different beds creates two `BED` entries. The only
dedup is in `WaypointBehavior`, which skips a new `BED` entry
when one already exists at exactly the same block position.

This means you can treat tags as loose categories and keep the
name field for disambiguation:

```
wp s home mycolony
wp s home friendcolony
wp s bed remotecamp1
wp s bed remotecamp2
```

Both `home` entries coexist. `wp goto home` then shows the
standard picker so you can choose between `mycolony` and
`friendcolony` rather than silently grabbing one. The `home`
alias and `sethome` shortcut are thin wrappers around
`wp goto home` / `wp save home` and inherit this behavior —
they look single-slot but aren't.

## sethome

Aliases: `sethome`

Convenience alias for `waypoints save home`. Saves a waypoint
at your current position with the `HOME` tag and no name. Use
`sethome` from a repeat location (shelter, spawn, stash) that
you'll want to pair with `home` later.

## home

Aliases: `home`

Convenience alias for `waypoints goto home`. Sets a goal to
your most recent `HOME`-tagged waypoint and starts pathing.
If you have more than one `HOME` waypoint, the standard
disambiguation picker appears.

## Best Practices

Guidance comes from the `WaypointsCommand` implementation and
the settings around automatic waypoint creation.

### Automatic waypoints

Two waypoint tags populate themselves if you let them. Both
default to on.

- `doBedWaypoints` (Boolean, default `true`) — save a `BED`
  waypoint when you right-click a bed. Handy because it
  captures the actual bed block you interacted with, which is
  not necessarily where the game will spawn you.
- `doDeathWaypoints` (Boolean, default `true`) — save a
  `DEATH` waypoint at your position when you die. Pair with
  `wp goto death` to recover items.

Turn these off only if you don't want Baritone writing to the
waypoint cache on your behalf — e.g. on a server where you'd
rather manage bed positions manually, or if death waypoints
are polluting your list during testing.

## Notes & Limitations

- The restore history is in-memory and per-session. Closing
  Minecraft (or disconnecting and reconnecting) empties the
  undo buffer; a waypoint deleted last session cannot be
  restored this session.
- Waypoint storage is per-world, keyed by the world provider.
  Singleplayer worlds, each multiplayer server, and even each
  dimension on a server have their own separate waypoint
  files.
- The `save` command's interpretation of extra arguments is
  position-sensitive: with exactly one arg after the tag, the
  arg is a *name*; with exactly three args, they're the *pos*;
  with four, it's name followed by pos. Ambiguous mixes fall
  back to defaults rather than erroring, so double-check your
  `wp list` after a non-default save.
- Waypoints are also accepted by other commands that take a
  "where" argument — for example
  [`farm <range> <waypoint>`](farming#arguments) centers a
  farm on a saved waypoint instead of your current position.
