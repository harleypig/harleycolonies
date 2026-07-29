---
title: Better Ping Display
---

**Better Ping Display** enhances the player list interface by displaying
each player's ping as a numerical value, providing clearer visibility into
connection quality. This client-side mod replaces or supplements the default
Minecraft ping bars with customizable text displays that can be color-coded
based on latency. The mod offers flexible formatting options and can work
alongside or replace the vanilla ping bar display.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `betterpingdisplay-client.toml`.

#### Display Settings

- `textColor` (default: `"#A0A0A0"`)
  - The color of the ping display text, written in hex format. This setting
    has no effect if `autoColorText` is set to `true`. The default gray
    color (`#A0A0A0`) provides good visibility against most backgrounds.

- `textFormatString` (default: `"%dms"`)
  - Customizes the display text of the ping display. Must contain a `%d`,
    which will be replaced with the ping number. For example, `"%dms"` will
    transform into `"123ms"` if the player's ping is 123. You can customize
    this to show different formats like `"%d ms"` or `"Ping: %d"`.

- `autoColorText` (default: `true`)
  - Whether to color a player's ping based on their latency. When enabled,
    low latency displays as green and high latency displays as red, with
    colors transitioning based on ping value. If this setting is `true`, then
    the `textColor` setting is ignored.

#### Visual Options

- `renderPingBars` (default: `false`)
  - Whether to also draw the default Minecraft ping bars alongside the
    numerical ping display. When set to `true`, both the numerical ping and
    the traditional ping bars are shown. When set to `false`, only the
    numerical display is shown.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

