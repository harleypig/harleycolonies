---
title: Bad Wither No Cookie - Reloaded
---



Client/Server: both

**Bad Wither No Cookie - Reloaded** silences global broadcast sounds in
Minecraft, reducing audio spam from server-wide events. This lightweight mod
is particularly useful on servers where spawners or farms are used for mobs
like Withers or Ender Dragons, as it prevents their death and spawn sounds
from playing globally. The mod provides configurable sound silencing with
support for custom sound events and includes a command utility to help
identify sounds for advanced customization.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `bwncr-common.toml`.

#### General Settings

- `general.silenceWither` (default: `true`)
  - Silence the server-wide Wither spawn and death broadcast sounds. When
    enabled, players will not hear Wither spawn or death sounds from
    anywhere on the server, reducing audio spam from Wither farms.

- `general.silenceTrader` (default: `true`)
  - Silence the wandering trader's ambient sound. When enabled, the
    wandering trader's ambient sound effects are muted, reducing noise
    pollution.

- `general.silenceDragon` (default: `true`)
  - Silence the server-wide Ender Dragon Death broadcast sound. When
    enabled, players will not hear the Ender Dragon death sound from
    anywhere on the server, useful for Ender Dragon farms.

- `general.silenceLightning` (default: `true`)
  - Silence the server-wide Thunder broadcast sound caused by the Lightning
    event. When enabled, thunder sounds from lightning strikes are muted,
    reducing audio spam during storms or lightning farms.

- `general.silenceUs` (default: `[""]`)
  - A list of custom sounds to silence, discoverable with the toggle command
    `/listen`. Enter one sound event per line with no commas. This allows
    you to silence any sound from any mod or vanilla Minecraft by specifying
    its sound event name. Use the `/listen` command to identify sound event
    names while playing.

- `general.debugMode` (default: `false`)
  - If enabled, the console will display spam showing what sounds are being
    received and whether or not they are being canceled. This is useful for
    troubleshooting and identifying sound event names, but should be kept
    disabled during normal gameplay to avoid console spam.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

