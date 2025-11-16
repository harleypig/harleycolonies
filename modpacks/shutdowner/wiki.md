**Shutdowner** is a lightweight server utility mod that enables
scheduled automatic shutdowns or restarts of your Minecraft server. It can
detect when the server hangs during runtime or shutdown and force a shutdown
to prevent prolonged downtime. The mod supports customizable shutdown
timepoints, warning messages, and disconnect reasons.

### Configuration

Below are the available options and their defaults. Paths and lists use the
same names as in the mod's config file.

#### General

- `shouldAutoShutDown` (default: `true`)
  - Enables scheduled automatic shutdowns at configured timepoints.

- `shutdownTimes` (default: `[]`)
  - List of timepoints when the server should automatically shut down.  
  - Format: `["HH:mm", "HH:mm", ...]` (24-hour format)  
  - Examples:
    - `["3:00", "11:00", "19:00"]`
    - `["00:00"]`

- `shutdownMessages` (default: `[]`)
  - Warning messages sent to players before shutdown.  
  - Format: `["seconds;Message", "seconds;Message", ...]`  
  - Messages are sent when the specified number of seconds remain before
    shutdown.  
  - Examples:
    - `["300;Server is restarting in 5 minutes"]`
    - `["60;1 minute till shutdown", "30;30 seconds till shutdown"]`

- `disconnectMessage` (default: `"Server shutting down"`)
  - Message shown to players when they are disconnected during shutdown.

#### Hang Detection

- `shouldDetectHang` (default: `true`)
  - If `true`, detects when the server hangs during normal runtime and
    forces a shutdown.

- `shouldDetectShutDownHang` (default: `true`)
  - If `true`, detects when shutdown takes too long and kills the server
    process.

- `maxShutDownTime` (default: `120`)
  - Maximum time (in seconds) the shutdown process is allowed to take
    before being killed. Used when `shouldDetectShutDownHang = true`.

- `printThreads` (default: `true`)
  - If `true`, prints remaining threads to the log when hang detection
    triggers.

