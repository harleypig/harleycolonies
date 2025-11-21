---
title: Compact Help Command
categories:
  - server-utility
  - map-information
  - cosmetic
  - mc-miscellaneous
---

[Website](https://www.curseforge.com/minecraft/mc-mods/compact-help-command) | [Issues](https://github.com/Serilum/.issue-tracker/labels/Mod: Compact Help Command) | [Source](https://github.com/Serilum/Compact-Help-Command)

Client/Server: both

**Compact Help Command** enhances the `/help` command by providing a more
organized and customizable display of available commands. The mod allows
server administrators to configure the appearance of command listings,
including colors, spacing, and pagination. This makes it easier for players
to navigate and understand available commands, especially on servers with
many mods that add numerous commands.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `compacthelpcommand.json5`.

#### Display Settings

- `addVerticalBarSpacing` (default: `true`)
  - When enabled, adds a space in front and behind a vertical bar in the
    subcommands. This improves readability of command listings by adding
    visual spacing around separators.

- `amountCommandsPerPage` (default: `8`)
  - The number of commands displayed per page in the `/help` command output.
    This setting controls pagination, making it easier to browse through
    command lists. Range: `1` to `50`.

#### Color Settings

- `commandColour` (default: `2`)
  - The colour of the command in `/help`. The possible values are: `0`:
    black, `1`: dark_blue, `2`: dark_green, `3`: dark_aqua, `4`:
    dark_red, `5`: dark_purple, `6`: gold, `7`: gray, `8`: dark_gray, `9`:
    blue, `10`: green, `11`: aqua, `12`: red, `13`: light_purple, `14`:
    yellow, `15`: white. Range: `0` to `15`.

- `subcommandColour` (default: `7`)
  - The colour of the subcommand in `/help`. Uses the same color values as
    `commandColour`. This allows you to differentiate between main commands
    and their subcommands visually. Range: `0` to `15`.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1
- harleycolonies-1.20.1-0.1.2

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.20.1-0.1.2
- harleycolonies-1.21.1

