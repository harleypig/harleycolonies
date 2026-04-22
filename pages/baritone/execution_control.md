---
title: Execution Control
---

The execution-control commands start, stop, suspend, and resume whatever
Baritone is currently doing — pathing, building, following, mining,
elytra flight, any of it. They take no arguments and have no tab
completions.

These are meant for human use in chat. Internally, Baritone processes
coordinate pause/cancel via `PathingCommandType.REQUEST_PAUSE` rather
than by invoking these commands, and the pause/resume wiring is
deliberately sealed off from reflection so other code can't grab it.

## pause

Aliases: `pause`, `p`, `paws`

Pauses Baritone until you use `resume`. Temporarily stops pathing,
building, following, elytra — whatever is running. A single `resume`
picks it right back up.

Error states:

- `Already paused` — running `pause` while already paused.

## resume

Aliases: `resume`, `r`, `unpause`, `unpaws`

Resumes whatever Baritone was doing when you last ran `pause`. Also
resumes the builder process explicitly (in case it stashed state
separately from the pause flag).

Error states:

- `Not paused` — running `resume` when Baritone isn't paused.

## paused

Aliases: `paused`

Reports whether Baritone is currently paused. Prints either
`Baritone is paused` or `Baritone is not paused`.

## cancel

Aliases: `cancel`, `c`, `stop`

Tells Baritone to stop whatever it's doing. Cancels all processes and
calls `PathingBehavior.cancelEverything()`. If Baritone was paused,
`cancel` also clears the paused state — so you don't need to `resume`
before issuing the next command.

Note from the source: all *processes* are guaranteed to be cancelled,
but `PathingBehavior` itself may be mid-way through an un-cancellable
action (for example, a parkour jump) and will finish it before
actually stopping.

## forcecancel

Aliases: `forcecancel`

Like `cancel`, but more forceful. Calls `cancelEverything()` and then
`forceCancel()`. The `forceCancel()` method is explicitly annotated
"PLEASE never call this" in the source — the Javadoc describes the
difference as:

> If `cancelEverything` was like `kill`, this is `sudo kill -9`. Or
> shutting off your computer.

Use `cancel` by default. Reach for `forcecancel` only when `cancel`
isn't actually stopping things — for example, if Baritone seems stuck
in an un-cancellable action.

## Notes and Limitations

- All five commands take zero positional arguments. Passing any
  argument produces an argument-count error from the command parser.
- Tab completion is empty for all five.
- `pause`, `resume`, and `paused` coordinate through a single internal
  boolean flag. `cancel` clears it. `forcecancel` clears it by way of
  `cancelEverything()`, the same path `cancel` uses.
- Mods or custom processes that want to pause/resume Baritone should
  implement an `IBaritoneProcess` returning `REQUEST_PAUSE`, not call
  these commands. The underlying fields are intentionally hidden from
  reflection for this reason.
