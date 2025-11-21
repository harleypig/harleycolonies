---
title: Hud Compass
---



Client/Server: both

**Hud Compass** displays a compass overlay on the HUD showing cardinal
directions, waypoints, and player locations. The mod integrates with
vanilla maps, Journeymap waypoints, and team systems to provide a
comprehensive navigation aid. The compass can be configured to show
different information based on conditions like holding a compass or
sneaking, making it flexible for various gameplay styles.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config files.

#### Display Settings

These settings are configured in `hudcompass-client.toml`.

- `display.alwaysShowLabels` (default: `false`)
  - If set to `true`, the labels on the compass will always be visible.
    If `false` (default), only the closest to the center of the compass
    will show the name.

- `display.alwaysShowFocusedLabel` (default: `true`)
  - If set to `false`, the closest waypoint to the center of the compass
    will not show the label, and sneak will be required to display it.

- `display.showAllLabelsOnSneak` (default: `true`)
  - If set to `false`, sneaking will only show the closest waypoint to the
    center of the compass.

- `display.animateLabels` (default: `true`)
  - If set to `false`, support for sewing recipes will not be enabled
    regardless of the mod's presence. This controls label animation
    effects.

- `display.displayWhen` (default: `"HOLDING_COMPASS"`)
  - Choose when the compass is visible. Allowed values: `NEVER` (don't
    display the compass, the mod remains active, just doesn't render),
    `HAS_COMPASS` (only display HUD if a compass is in the inventory),
    `HOLDING_COMPASS` (only display HUD if a compass is in the hand),
    `ALWAYS` (always display the compass).

- `display.enableJourneymapIntegration` (default: `true`)
  - If set to `false`, Journeymap waypoints won't be displayed in the
    compass.

- `display.waypointFadeDistance` (default: `195.0`)
  - Sets the distance at which waypoints start to fade, in blocks.
    Meaningless if `waypointViewDistance` is `0`. If this value is >=
    `waypointViewDistance`, it will never fade. Range: `0.0` to
    `1.7976931348623157E308`.

- `display.waypointViewDistance` (default: `200.0`)
  - Sets the distance at which waypoints stop drawing, in blocks. If set
    to `0`, waypoints will never disappear. Range: `0.0` to
    `1.7976931348623157E308`.

#### General Settings

These settings are configured in `hudcompass-common.toml`.

- `general.enableVanillaMapIntegration` (default: `true`)
  - If set to `false`, vanilla map waypoints won't be displayed in the
    compass.

- `general.enableSpawnPointWaypoint` (default: `true`)
  - If set to `false`, the spawn point location will not be shown.

- `general.disableServerHello` (default: `false`)
  - If set to `true`, the server will not advertise itself to the
    clients, making them work in client-only mode.

- `general.playerDisplay` (default: `"TEAM"`)
  - Choose how the compass shows other players. Allowed values: `NONE`
    (don't display other players, ever), `TEAM` (only display players that
    are in the same team), `ALL` (display all players).

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

