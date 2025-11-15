# System & Control

This document contains all commands related to system & control.

## Commands

### `cancel`, `c`, `stop`

**Description**: Cancel what Baritone is currently doing  

The cancel command tells Baritone to stop whatever it's currently doing.

Usage:
> cancel

---

### `click`

**Description**: Open click  

Opens click dude

Usage:
> click

---

### `eta`

**Description**: View the current ETA  

The ETA command provides information about the estimated time until the next segment.
and the goal

Be aware that the ETA to your goal is really unprecise

Usage:
> eta - View ETA, if present

---

### `forcecancel`

**Description**: Force cancel  

Like cancel, but more forceful.

Usage:
> forcecancel

---

### `gc`

**Description**: Call System.gc()  

Calls System.gc().

Usage:
> gc

---

### `help`, `?`

**Description**: View all commands or help on specific ones  

Using this command, you can view detailed help information on how to use certain commands of Baritone.

Usage:
> help - Lists all commands and their short descriptions.
> help <command> - Displays help information on a specific command.

---

### `invert`

**Description**: Run away from the current goal  

The invert command tells Baritone to head away from the current goal rather than towards it.

Usage:
> invert - Invert the current goal.

---

### `modified`, `mod`, `baritone`, `modifiedsettings`

**Type**: Alias → `set modified`  

**Description**: List modified settings  

This command is an alias, for: set modified ...

---

### `pause`, `p`, `paws`

**Description**: Pauses Baritone until you use resume  

The pause command tells Baritone to temporarily stop whatever it's doing.

This can be used to pause pathing, building, following, whatever. A single use of the resume command will start it right back up again!

Usage:
> pause

---

### `paused`

**Description**: Tells you if Baritone is paused  

The paused command tells you if Baritone is currently paused by use of the pause command.

Usage:
> paused

---

### `proc`

**Description**: View process state information  

The proc command provides miscellaneous information about the process currently controlling Baritone.

You are not expected to understand this if you aren't familiar with how Baritone works.

Usage:
> proc - View process information, if present

---

### `reloadall`

**Description**: Reloads Baritone's cache for this world  

The reloadall command reloads Baritone's world cache.

Usage:
> reloadall

---

### `repack`, `rescan`

**Description**: Re-cache chunks  

Repack chunks around you. This basically re-caches them.

Usage:
> repack - Repack chunks.

---

### `reset`

**Type**: Alias → `set reset`  

**Description**: Reset all settings or just one  

This command is an alias, for: set reset ...

---

### `resume`, `r`, `unpause`, `unpaws`

**Description**: Resumes Baritone after a pause  

The resume command tells Baritone to resume whatever it was doing when you last used pause.

Usage:
> resume

---

### `saveall`

**Description**: Saves Baritone's cache for this world  

The saveall command saves Baritone's world cache.

Usage:
> saveall

---

### `set`, `setting`, `settings`

**Description**: View or change settings  

Using the set command, you can manage all of Baritone's settings. Almost every aspect is controlled by these settings - go wild!

Usage:
> set - Same as `set list`
> set list [page] - View all settings
> set modified [page] - View modified settings
> set <setting> - View the current value of a setting
> set <setting> <value> - Set the value of a setting
> set reset all - Reset ALL SETTINGS to their defaults
> set reset <setting> - Reset a setting to its default
> set toggle <setting> - Toggle a boolean setting
> set save - Save all settings (this is automatic tho)
> set load - Load settings from settings.txt
> set load [filename] - Load settings from another file in your minecraft/baritone

---

### `version`

**Description**: View the Baritone version  

The version command prints the version of Baritone you're currently running.

Usage:
> version - View version information, if present

---


[← Back to Commands Index](COMMANDS.md)
