---
title: Shutdowner
categories:
  - server-utility
---

[Website](https://www.curseforge.com/minecraft/mc-mods/shutdowner)

Client/Server: server

**Shutdowner** provides automated server shutdown functionality with
configurable schedules, hang detection, and player notification messages.
The mod can automatically shut down the server at specified times, detect
when shutdowns hang, and send warning messages to players before shutdown.
This is useful for scheduled server restarts, maintenance windows, and
preventing server hangs during shutdown.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `shutdowner.json`.

#### Shutdown Settings

- `shouldAutoShutDown` (default: `true`)
  - Whether to use the timed shutdown. When enabled, the server will
    automatically shut down at the times specified in `shutdownTimes`.

- `shutdownTimes` (default: `["3:00", "11:00", "16:00"]`)
  - Shutdown timepoints, format: `["time1", "time2"]` e.g., `["18:00",
    "23:00"]`. Times are in 24-hour format. The server will shut down at
    each specified time.

- `shutdownMessages` (default: `["300;Server is restarting in 5min",
  "180;3 minutes till shutdown", "120;2 minutes till shutdown", "60;1
  minute till shutdown", "30;30 sec till shutdown", "10;10 sec till
  shuwdown", "9;9", "8;8", "7;7", "6;6", "5;5", "4;4", "3;3", "2;2",
  "1;1", "0;Shutting down now"]`)
  - Shutting down timed messages, format: `[secondsToShutdown;Message]`
    e.g., `["300;Server is restarting in 5min", "150;Server is
    restarting in 2.5min"]`. Messages are sent to players at the specified
    intervals before shutdown.

- `disconnectMessage` (default: `"Server shutting down"`)
  - Set the disconnect message for the players. This message is shown to
    players when they are disconnected during shutdown.

#### Hang Detection

- `shouldDetectShutDownHang` (default: `true`)
  - Whether to kill the server when shutdown takes too long. When enabled,
    if shutdown exceeds `maxShutDownTime`, the server process is forcefully
    terminated.

- `maxShutDownTime` (default: `120`)
  - The maximum time the shutdown is allowed to take, in seconds. If
    shutdown exceeds this time and `shouldDetectShutDownHang` is enabled,
    the server will be forcefully terminated.

- `shouldDetectHang` (default: `true`)
  - Whether to detect and close the server hang during runtime. When
    enabled, the mod monitors for server hangs and can take action to
    prevent the server from becoming unresponsive.

- `printThreads` (default: `true`)
  - Print remaining threads to log? When enabled, information about
    remaining threads is logged during shutdown, which can help identify
    what's preventing clean shutdown.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1
### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

