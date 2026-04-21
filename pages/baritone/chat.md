---
title: Chat & Control
---

Baritone's chat integration does two separate jobs: it reads
your outgoing chat messages to decide whether a line is a
command or actual chat, and it writes status/debug output back
to you through one of several channels (chat, toast, desktop
notification). This page groups the settings that steer both
halves.

The command that runs settings themselves — reading, writing,
toggling, resetting, saving, loading — is
[`set`](system#set-setting-settings), documented on the system
page. Nothing on this page is a command; chat control has no
dedicated subcommand tree.

## Settings Index

Alphabetical. Each link jumps to the section that discusses the setting.

- [censorCoordinates](#censoring)
- [censorRanCommands](#censoring)
- [chatControl](#turning-chat-control-on-and-off)
- [chatControlAnyway](#turning-chat-control-on-and-off)
- [chatDebug](#verbose-and-debug-output)
- [desktopNotifications](#output-channels)
- [echoCommands](#echo-and-command-history)
- [logAsToast](#output-channels)
- [prefix](#turning-chat-control-on-and-off)
- [prefixControl](#turning-chat-control-on-and-off)
- [shortBaritonePrefix](#chat-tag-and-prefix)
- [toastTimer](#output-channels)
- [useMessageTag](#chat-tag-and-prefix)
- [verboseCommandExceptions](#verbose-and-debug-output)

`elytraChatSpam` is also a chat-output toggle but is scoped
to one behavior; it lives on [elytra](elytra#logging).

## How chat is intercepted

Every outgoing chat message passes through
`ExampleBaritoneControl.onSendChatMessage`. It decides whether
the message is a Baritone command in one of two ways, in this
order:

1. **Prefix form.** If `prefixControl` is on and the message
   starts with the current `prefix` (default `#`), the prefix
   is stripped, the rest is treated as a command, and the chat
   event is cancelled so the message never hits the server.
2. **Prefix-less form.** Otherwise, if either `chatControl` or
   `chatControlAnyway` is on, the whole message is speculatively
   parsed as a command. If it matches, it runs and the chat event
   is cancelled; if it doesn't match, the message passes through
   to the server unchanged.

These two paths are independent. You can run prefix-only (typed
commands always start with `#`, raw chat is never interpreted),
prefix-less only (every message is tried as a command first),
or both. Both off means Baritone has no chat surface at all and
can only be driven programmatically.

## Best Practices

### Turning chat control on and off

Four settings gate command input. The safe default leaves all
of them where they are:

- `prefixControl` (Boolean, default `true`) — honor the
  `prefix` as a command marker. This is the setting most users
  leave alone; disabling it makes `#goto …` fall through as
  literal chat.
- `prefix` (String, default `"#"`) — the prefix string itself.
  Change when `#` conflicts with another mod's chat prefix.
  Any non-empty string works; there's no validation for
  collisions.
- `chatControl` (Boolean, default `true`) — interpret prefix-
  less chat as commands. Leave on for in-game typing
  convenience; turn off if you ever want to say the word
  `goto` in chat without triggering a path.
- `chatControlAnyway` (Boolean, default `false`) — a second
  copy of `chatControl` for clients (like Impact) that force
  `chatControl` off. If you're on such a client, flipping this
  restores prefix-less control.

The `set` command's revert-click output has a safety net for
the combinations that leave you stranded: turning off both
`chatControl` and `chatControlAnyway` simultaneously, or
turning off `prefixControl`, prints a red warning and leaves
the click-to-revert line usable. See
[`set`](system#set-setting-settings) for the exact warning
wording and how to back out.

Force-run prefix: the clickable "rerun" on echoed commands
uses an internal UUID-wrapped prefix
(`IBaritoneChatControl.FORCE_COMMAND_PREFIX`) that bypasses
both `prefixControl` and `chatControl`. Users never type it
manually — it's how Baritone talks to itself through the chat
box.

### Output channels

Every outgoing Baritone message goes through `Helper.logDirect`.
That function picks between three destinations:

- **Chat** — the default. Output prefixed with `[Baritone]`
  (see [Chat tag and prefix](#chat-tag-and-prefix)).
- **Toast** — Minecraft's achievement-style pop-up in the
  upper-right. Less intrusive, easier to miss.
- **Desktop notification** — OS-level notification outside
  Minecraft. Reserved for a small set of messages that go out
  through `logNotification` in addition to the regular chat log.

Three settings steer the channel:

- `logAsToast` (Boolean, default `false`) — route the regular
  `logDirect` stream through toasts instead of chat. Affects
  most Baritone output, not just one category.
- `toastTimer` (Long, default `5000`, ms) — how long each
  toast stays on screen. Values below `1000` are effectively
  invisible; the setting's javadoc suggests disabling toasts
  entirely rather than going that low.
- `desktopNotifications` (Boolean, default `false`) — allow
  `logNotification(…)` to surface OS notifications. The
  Baritone-critical variant (`logNotificationDirect`) ignores
  this gate; everything else respects it.

### Chat tag and prefix

When output goes to chat, two settings affect how it's labeled:

- `shortBaritonePrefix` (Boolean, default `false`) — render the
  in-chat label as `[B]` instead of `[Baritone]`. Nothing
  functional depends on the length; it's pure screen real
  estate.
- `useMessageTag` (Boolean, default `false`) — use Minecraft's
  newer `GuiMessageTag` API to mark Baritone messages instead
  of prepending `[Baritone]` text. With this on, the prefix
  disappears from the visible message body and is replaced by
  the native tag affordance (colored side-bar, hover tooltip).
  Toasts ignore this setting — their title always shows the
  prefix.

### Echo and command history

- `echoCommands` (Boolean, default `true`) — when a command
  runs, echo `> <command>` back to chat with a click-to-rerun
  affordance (hover: "Click to rerun command"). Turning this
  off makes command execution silent. Affects both prefix and
  prefix-less paths.
- `censorRanCommands` (Boolean, default `false`) — redact
  arguments from the echoed line, rendering `> goto …` instead
  of `> goto 150 64 -2000`. Useful on streams or during
  screen-shares. The click-to-rerun still replays the real
  command.

### Verbose and debug output

Three settings open up extra output that is silent by default:

- `chatDebug` (Boolean, default `false`) — enable
  `Helper.logDebug`. A lot of internal status messages
  funnel through this gate, so flipping it on is the standard
  "why is nothing happening" diagnostic.
- `verboseCommandExceptions` (Boolean, default `false`) —
  print full stack traces to stdout for every command parse
  error, including routine syntax mistakes. Chat still gets
  the short human-readable message either way; this only
  affects the game log.
- `elytraChatSpam` — verbose chat logging in elytra mode;
  see [elytra#logging](elytra#logging) for details.

### Censoring

Two independent toggles redact coordinate values from output:

- `censorCoordinates` (Boolean, default `false`) — replace
  coordinates inside goal descriptions and block-position
  strings with `<censored>`. Implemented in
  `SettingsUtil.maybeCensor`; it only affects text that
  routes through that helper, so hand-formatted log lines in
  third-party code might leak coordinates anyway.
- `censorRanCommands` — described above under echo; it
  collapses command arguments to `…` and is a superset of
  coordinate censoring for the `echoCommands` path.

Turn both on together when recording or streaming with
coordinate-sensitive content.

## Notes & Limitations

- All the "permissive" chat-control settings (`chatControl`,
  `chatControlAnyway`, `prefixControl`) default to on. Baritone
  is intentionally easy to drive; the lockdown combinations
  exist for embedders and for quiet streams, not as a security
  model.
- `chatControl` treats *any* matching command name as a
  command, including single-word settings. Typing `allowbreak`
  in chat with `chatControl` on and no prefix will toggle
  `allowBreak`. This is why `echoCommands` defaults on — the
  click-to-revert line is often the only hint that a chat
  message was intercepted.
- The `set` command auto-saves on most write paths, so setting
  changes made via chat persist immediately. See
  [`set`](system#set-setting-settings) for the save/load
  workflow.
- Output-channel settings interact: turning on `logAsToast`
  and `useMessageTag` means chat output becomes toasts (no
  tag applied) while anything that specifically calls
  `logDirect(false, …)` still hits chat with the tag style.
  The two settings aren't either/or — they control different
  branches in `Helper.logDirect`.
