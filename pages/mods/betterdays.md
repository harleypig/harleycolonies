---
title: Better Days
categories:
  - utility-qol
  - server-utility
---

[Website](https://www.curseforge.com/minecraft/mc-mods/betterdays) | [Issues](https://github.com/wendall911/BetterDays/issues) | [Source](https://github.com/wendall911/BetterDays)

Client/Server: both

**Better Days** enhances Minecraft's time and sleep mechanics by allowing
configurable time speeds for day and night cycles, improved sleep
functionality, and synchronized effects. The mod provides flexible control
over how time passes, with options to set day and night speeds using ratios,
real-world minutes, or real-time settings. Better Days includes features
like accelerated sleep time, configurable sleep requirements, weather and
random tick synchronization, and a customizable bed clock interface. The
mod supports both single-player and multiplayer servers, with different
time speeds based on the number of sleeping players.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config files.

#### GUI Settings

These settings control the bed clock display and are configured in
`betterdays-client.toml`.

- `gui.clockAlignment` (default: `"TOP_RIGHT"`)
  - Sets the screen alignment of the bed clock. Allowed values:
    `TOP_LEFT`, `TOP_CENTER`, `TOP_RIGHT`, `CENTER_LEFT`, `CENTER_CENTER`,
    `CENTER_RIGHT`, `BOTTOM_LEFT`, `BOTTOM_CENTER`, `BOTTOM_RIGHT`.

- `gui.clockScale` (default: `64`)
  - Sets the scale of the bed clock. Range: greater than `1`.

- `gui.clockMargin` (default: `16`)
  - Sets the distance between the clock and the edge of the screen. Unused
    if `clockAlignment` is `CENTER_CENTER`. Range: greater than `0`.

- `gui.preventClockWobble` (default: `true`)
  - Prevents clock wobble when getting in bed by updating the clock's
    position every tick. As a side-effect, the clock won't wobble when
    first viewed as it does in vanilla. This setting is unused if
    `displayBedClock` is `false`.

- `gui.blacklistDimensions` (default: `["aether:the_aether"]`)
  - Blacklists sky rendering for specific dimensions. This prevents sky
    jittering when using `/time set` command in certain dimensions like
    the Aether.

#### Time Settings

These settings are configured in `betterdays-common.toml`.

- `time.speedMethod` (default: `"RATIO"`)
  - Determines which method is used to set day and night speed. Allowed
    values: `RATIO` (uses `daySpeed` and `nightSpeed`), `MINUTES` (uses
    `daySpeedMinutes` and `nightSpeedMinutes`), `REALTIME` (sets day and
    night to 12 real-world hours each).

- `time.daySpeed` (default: `1.0`)
  - The speed at which time passes during the day. This is the ratio of
    time passing relative to vanilla (vanilla speed: `1.0`). Day is
    defined as any time between `dayStart` and `nightStart` the next day.
    Range: `0.0` to `24000.0`.

- `time.nightSpeed` (default: `1.0`)
  - The speed at which time passes during the night. This is the ratio of
    time passing relative to vanilla (vanilla speed: `1.0`). Night is
    defined as any time between `dayStart` and `nightStart`. Range: `0.0`
    to `24000.0`.

- `time.daySpeedMinutes` (default: `10.0`)
  - An alternative way to set day speed. This setting defines the length
    of the day in real-world minutes (vanilla length: `10.0` minutes).
    Mutually exclusive with `daySpeed`; `speedMethod` determines which is
    used. Range: `0.1` to `10000.0`.

- `time.nightSpeedMinutes` (default: `10.0`)
  - An alternative way to set night speed. This setting defines the length
    of the night in real-world minutes (vanilla length: `10.0` minutes).
    Mutually exclusive with `nightSpeed`; `speedMethod` determines which
    is used. Range: `0.1` to `10000.0`.

- `time.dayStart` (default: `23500.0`)
  - The time to start day. This is configurable within the time the sun
    appears and day starts. Range: `22300.0` to `24000.0`.

- `time.nightStart` (default: `12500.0`)
  - The time to start night. This is configurable within the time sunset
    starts and night starts. Range: `12000.0` to `13000.0`.

- `time.enableInterpolatedTime` (default: `false`)
  - Enables setting an infinite amount of time speeds defined as pairs in
    the form `(currentTick, desiredSpeed)` where between each value bezier
    spline interpolation is performed for smooth transitioning. The two
    default pairs at `0` and `24000` are necessary as bounds, but their
    time speed values can be freely modified.

- `time.interpolatedTimeSmoothingFactor` (default: `0.25`)
  - Determines the smoothing factor in the interpolation algorithm. A
    high value makes the interpolation softer and curvier; a low value
    makes it closer to a piecewise function. Range: `0.0` to `10.0`.

- `time.interpolatedTimeList` (default: `["0,1.0", "24000,1.0"]`)
  - These are the pairs that define what speed time should run at at the
    specified day/night tick. The two default pairs need to exist, but
    their time speed values can be modified.

#### Time Effects

These settings are configured in `betterdays-common.toml`.

- `time.effects.weatherEffect` (default: `"SLEEPING"`)
  - When applied, syncs the passage of weather with the current speed of
    time. As time moves faster, rain stops faster. Clear weather is not
    affected. When set to `SLEEPING`, this effect only applies when at
    least one player is sleeping in a dimension. Note: On NeoForge 1.21.1+
    this is already handled by the platform. This setting is not applicable
    if game rule `doWeatherCycle` is `false`. Allowed values: `NEVER`,
    `ALWAYS`, `SLEEPING`.

- `time.effects.randomTickEffect` (default: `"NEVER"`)
  - When applied, syncs the random tick speed with the current speed of
    time, forcing crop, tree, and grass growth to occur at
    `baseRandomTickSpeed` multiplied by the current time-speed. When set to
    `SLEEPING`, `randomTickSpeed` is set to `baseRandomTickSpeed` unless
    at least one player is sleeping in a dimension. WARNING: This setting
    overwrites the `randomTickSpeed` game rule. This effect has a minimum
    `randomTickSpeed` of `1` if time speed is less than `1.0`. Allowed
    values: `NEVER`, `ALWAYS`, `SLEEPING`.

- `time.effects.baseRandomTickSpeed` (default: `3`)
  - The base random tick speed used by the `randomTickEffect` time effect.
    Range: greater than `0`.

- `time.effects.potionEffect` (default: `"NEVER"`)
  - When applied, progresses potion effects to match the rate of the
    current time-speed. This effect does not apply if time speed is `1.0`
    or less. WARNING: This may have a negative impact on performance in
    servers with many players. When set to `ALWAYS`, this effect applies
    to all players in the dimension, day or night. When set to `SLEEPING`,
    this effect only applies to players who are sleeping. Allowed values:
    `NEVER`, `ALWAYS`, `SLEEPING`.

- `time.effects.hungerEffect` (default: `"NEVER"`)
  - When applied, progresses player hunger effects to match the rate of
    the current time-speed. This results in faster healing when food level
    is full, and faster harm when food level is too low. This effect does
    not apply if time speed is `1.0` or less. When set to `ALWAYS`, this
    effect applies to all players in the dimension, day or night. Not
    recommended on higher difficulty settings. When set to `SLEEPING`, this
    effect only applies to players who are sleeping. Allowed values:
    `NEVER`, `ALWAYS`, `SLEEPING`.

- `time.effects.blockEntityEffect` (default: `"NEVER"`)
  - When applied, progresses block entities like furnaces, hoppers, and
    spawners to match the rate of the current time-speed. WARNING: This
    time-effect has a significant impact on performance. This effect does
    not apply if time speed is `1.0` or less. When set to `SLEEPING`, this
    effect only applies when at least one player is sleeping in a
    dimension. Allowed values: `NEVER`, `ALWAYS`, `SLEEPING`.

#### Sleep Settings

These settings are configured in `betterdays-common.toml`.

- `sleep.enableSleepFeature` (default: `true`)
  - Enables or disables the sleep feature of this mod. Enabling this
    setting will modify the vanilla sleep functionality and may conflict
    with other sleep mods. If disabled, all settings in the sleep section
    will not apply.

- `sleep.sleepSpeedMax` (default: `110.0`)
  - The maximum speed at which time passes when all players are sleeping.
    This setting defines the sleep time-speed in single-player games. A
    value of `110` is nearly equal to the time it takes to sleep in
    vanilla. Range: `0.0` to `24000.0`.

- `sleep.sleepSpeedMin` (default: `1.0`)
  - The minimum speed at which time passes when only 1 player is sleeping
    in a full server. Range: `0.0` to `24000.0`.

- `sleep.sleepSpeedAll` (default: `-1.0`)
  - The speed at which time passes when all players are sleeping. Set to
    `-1` to disable this feature (`sleepSpeedMax` will be used when all
    players are sleeping). Range: `-1.0` to `24000.0`.

- `sleep.sleepSpeedCurve` (default: `0.3`)
  - Defines the curvature of the interpolation function that translates
    the sleeping player percentage into time-speed. The function used is a
    Normalized Tunable Sigmoid Function. A value of `0.5` represents a
    linear relationship. Smaller values bend the curve toward the X axis,
    while greater values bend it toward the Y axis. Range: `0.0` to `1.0`.

- `sleep.clearWeatherOnWake` (default: `true`)
  - Set to `true` for the weather to clear when players wake up in the
    morning as it does in vanilla. Set to `false` to force weather to pass
    naturally. Adds realism when `accelerateWeather` is enabled. Note:
    This setting is ignored if game rule `doWeatherCycle` is `false`.

- `sleep.allowDaySleep` (default: `false`)
  - When `true`, players are allowed to sleep at all times of day in
    dimensions controlled by Better Days. Note: Other mods may override
    this ability.

- `sleep.displayBedClock` (default: `true`)
  - When `true`, a clock is displayed in the sleep interface.

- `sleep.ratioPlayersForSleep` (default: `0.0`)
  - The ratio of players in a dimension that must be sleeping to skip to
    morning. A value of `1` means all players must be sleeping, `0.5`
    means half the players must be sleeping, etc. A value of `0`
    effectively disables this feature. Range: `0.0` to `1.0`.

#### Sleep Messages

These settings are configured in `betterdays-common.toml`. Sleep messages
support Minecraft formatting codes and variables that can be inserted using
`${variableName}` format. Any message can be disabled by setting it to an
empty string.

- `sleep.messages.morning.message` (default: `"§e§oTempus fugit!"`)
  - This message is sent after a sleep cycle has completed. Available
    variables: `sleepingPlayers`, `totalPlayers`, `sleepingPercentage`.

- `sleep.messages.morning.type` (default: `"GAME_INFO"`)
  - Sets where this message appears. Allowed values: `SYSTEM` (appears as
    a message in the chat), `GAME_INFO` (game information that appears
    above the hotbar).

- `sleep.messages.morning.target` (default: `"DIMENSION"`)
  - Sets to whom this message is sent. A target of `SLEEPING` will send
    the message to all players who just woke up. Allowed values: `ALL`,
    `DIMENSION`, `SLEEPING`.

- `sleep.messages.enterBed.message` (default: `"${player} is now sleeping. [${sleepingPlayers}/${totalPlayers}]"`)
  - This message is sent when a player enters their bed. Available
    variables: `player`, `sleepingPlayers`, `totalPlayers`,
    `sleepingPercentage`.

- `sleep.messages.enterBed.type` (default: `"GAME_INFO"`)
  - Sets where this message appears. Allowed values: `SYSTEM`, `GAME_INFO`.

- `sleep.messages.enterBed.target` (default: `"DIMENSION"`)
  - Sets to whom this message is sent. Allowed values: `ALL`, `DIMENSION`,
    `SLEEPING`.

- `sleep.messages.leaveBed.message` (default: `"${player} has left their bed. [${sleepingPlayers}/${totalPlayers}]"`)
  - This message is sent when a player leaves their bed (without being
    woken up naturally by morning). Available variables: `player`,
    `sleepingPlayers`, `totalPlayers`, `sleepingPercentage`.

- `sleep.messages.leaveBed.type` (default: `"GAME_INFO"`)
  - Sets where this message appears. Allowed values: `SYSTEM`, `GAME_INFO`.

- `sleep.messages.leaveBed.target` (default: `"DIMENSION"`)
  - Sets to whom this message is sent. Allowed values: `ALL`, `DIMENSION`,
    `SLEEPING`.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.20.1-0.1.2
- harleycolonies-1.21.1

