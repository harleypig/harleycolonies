---
title: Connectivity[Forge/Fabric]
categories:
  - technology-player-transport
  - map-information
  - server-utility
---

[Website](https://www.curseforge.com/minecraft/mc-mods/connectivity) | [Issues](https://github.com/someaddons/connectivity/issues) | [Source](https://github.com/someaddons/connectivity)

Client/Server: both

**Connectivity** enhances Minecraft's networking capabilities by removing
or adjusting packet size limits and improving connection stability. The mod
helps prevent disconnections caused by oversized packets, particularly
useful on servers with many mods that may send large amounts of data. It
provides configurable timeout settings and debugging options to help
identify and resolve networking issues.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `connectivity.json`.

#### Packet Limits

- `disableLoginLimits` (default: `true`)
  - Should login packet size limits be disabled? This prevents errors like
    "Payload may not be larger than 1048576 bytes" during login. When
    enabled, larger login packets are allowed, which can help prevent
    connection issues with modded servers.

- `disablePacketLimits` (default: `true`)
  - Should play packet size limits be disabled? This prevents errors like
    "Badly compressed packet" during gameplay. When enabled, larger packets
    are allowed, which can help prevent disconnections on modded servers.

#### Chat Settings

- `disableChatVerificationDisconnect` (default: `true`)
  - (Client-side) Disables players disconnecting on chat message
    verification problems. Enable `debugPrintMessages` to see the message
    causing issues. When enabled, players won't be kicked for chat
    verification failures, improving connection stability.

#### Timeout Settings

- `logintimeout` (default: `120`)
  - Set the max login timeout in seconds. This determines how long the
    server will wait for a player to complete the login process before
    timing out. Increase this value if players frequently timeout during
    login, especially on slower connections or heavily modded servers.

- `disconnectTimeout` (default: `60`)
  - Set the in-game disconnect timeout for disconnecting players in
    seconds. This determines how long the server waits before forcefully
    disconnecting a player who is no longer responding.

#### Debug Settings

- `debugPrintMessages` (default: `false`)
  - Enable additional debug logging for networking errors. When enabled,
    detailed information about network packet issues is logged, which can
    help identify problems causing disconnections or connection issues.

- `packetHistoryMinutes` (default: `5`)
  - Set the amount of minutes for which network packet history data is
    saved. This history can be useful for debugging network issues. Range:
    `1` to `60`.

- `showFullResourceLocationException` (default: `false`)
  - Enable to see the full log output for all resource location exceptions.
    When enabled, complete error messages are shown for resource location
    issues, which can help identify mod conflicts or missing resources.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1
- harleycolonies-1.20.1-0.1.2

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.20.1-0.1.2
- harleycolonies-1.21.1

