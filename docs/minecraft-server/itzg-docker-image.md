# itzg/minecraft-server Docker Image

This document covers documentation specific to the `itzg/minecraft-server`
Docker image used for running the Minecraft server.

## Hybrid Server Support

For more information about hybrid server types supported by the
itzg/minecraft-server Docker image, see the [Hybrids
documentation](https://docker-minecraft-server.readthedocs.io/en/latest/types-and-platforms/server-types/hybrids/).

## Data Directory Structure

The data directory is where the Minecraft server stores all its runtime data.
This includes world data, server configuration, mods, plugins, and logs. The
data directory path is configured via the `DATA_DIR` environment variable in
`.env`, which defaults to `./data` relative to the `server/` directory.

For detailed information about the data directory structure, see the [data
directory
documentation](https://docker-minecraft-server.readthedocs.io/en/latest/data-directory/).

### Directory Structure

The `itzg/minecraft-server` image stores all server data in `/data` within the
container, which is mounted from `${DATA_DIR}` on the host. The typical
structure includes:

```
${DATA_DIR}/
  server.properties          # Server configuration
  eula.txt                   # EULA acceptance (auto-generated)
  logs/                       # Server logs
  mods/                       # NeoForge/Forge mods
  plugins/                    # Spigot/Bukkit plugins
  config/                     # Mod and plugin configuration files
  world/                      # Main world data
  world_nether/               # Nether dimension data
  world_the_end/              # End dimension data
  usercache.json              # Player cache
  banned-players.json         # Banned players list
  ops.json                    # Operator list
  whitelist.json              # Whitelist
```

### Files Managed by the Repository

These files should be copied from the repository to the server data directory:

- **`server.properties`**: Server configuration file (port, difficulty,
  gamemode, etc.) - should be created from a template or copied from the repo
  if we maintain a server-specific version

- **Mod configuration files**: Configuration files for mods in the modpack
  (from `config/` in the modpack directory) - these should be copied to
  `${DATA_DIR}/config/` to ensure consistent mod behavior across server
  instances

### Files Managed by Minecraft Server

These files are automatically created and managed by the Minecraft server:

- **World data** (`world/`, `world_nether/`, `world_the_end/`): All chunk
  data, player data, and world state

- **Server logs** (`logs/`): Server console output and log files

- **Player data** (`usercache.json`, `banned-players.json`, `ops.json`,
  `whitelist.json`): Player-related server data

- **`eula.txt`**: EULA acceptance (auto-generated when `EULA=TRUE` is set)

### Files Installed by Users/Administrators

These files will be installed into the server data directory:

- **Mods** (`mods/`): NeoForge/Forge mods from the modpack. These should be
  installed from the modpack distribution (e.g., using packwiz or copying
  from the modpack's `mods/` directory)

- **Plugins** (`plugins/`): Spigot/Bukkit plugins for server administration,
  including:
  - Permissions plugins (e.g., LuckPerms)
  - Economy plugins
  - Protection/claiming plugins
  - Other server management plugins

## Volume Mounts

The docker-compose configuration mounts two directories:

1. **`${DATA_DIR}:/data`**: The main data directory containing world data,
   mods, plugins, and server files

2. **`./config:/config`**: A separate configuration directory (currently
   mounted but purpose to be determined - may be used for server-specific
   configs that differ from the modpack configs)

## References

- [itzg/minecraft-server Documentation](https://docker-minecraft-server.readthedocs.io/)
- [Environment Variables](https://docker-minecraft-server.readthedocs.io/en/latest/variables/)
- [Data Directory](https://docker-minecraft-server.readthedocs.io/en/latest/data-directory/)
- [Hybrid Server Types](https://docker-minecraft-server.readthedocs.io/en/latest/types-and-platforms/server-types/hybrids/)

