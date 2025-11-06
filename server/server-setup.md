# Server Setup Documentation

This document explains the server configuration choices for the HarleyColonies
modpack server.

## Why a Hybrid Server?

The HarleyColonies modpack uses a hybrid server setup that combines
Spigot/Paper plugins with Forge/NeoForge mods. This is necessary because:

1. **MineColonies Requirement**: MineColonies is the core mod of this
   modpack and requires Forge or NeoForge to run. The modpack is designed
   around MineColonies functionality, so a Forge/NeoForge-compatible
   server is essential.

2. **Permissions Mods Limitation**: There are no decent permissions mods
   available for Forge/NeoForge. The Forge/NeoForge modding ecosystem
   lacks the mature permissions management systems that are available for
   Bukkit/Spigot/Paper servers.

3. **Best of Both Worlds**: By using a hybrid server, we can leverage:
   - **Forge/NeoForge mods**: Including MineColonies and all the other
     mods in the modpack
   - **Spigot plugins**: For permissions management, server administration,
     and other server management features that are well-established in the
     plugin ecosystem

For more information about hybrid server types supported by the
itzg/minecraft-server Docker image, see the [Hybrids
documentation](https://docker-minecraft-server.readthedocs.io/en/latest/types-and-platforms/server-types/hybrids/).

## Why Arclight?

Arclight has been chosen as the default hybrid server platform for the
following reasons:

1. **Stability and Performance**: Arclight is recognized for its stability
   and efficient performance, ensuring smooth operation even when running
   both plugins and mods concurrently.

2. **Active Development**: The Arclight project is actively maintained with
   regular updates and has a supportive community providing assistance and
   continuous improvements.

3. **Compatibility**: Arclight seamlessly integrates the Bukkit API into
   the modding environment, allowing Spigot/PaperMC plugins to operate
   alongside Forge/Fabric/NeoForge mods without conflicts.

4. **NeoForge Support**: Arclight supports NeoForge, which is required for
   the latest versions of the HarleyColonies modpack.

5. **Research Findings**: Based on searches and community feedback, Arclight
   appears to be the best choice among hybrid server options, with better
   stability and support compared to alternatives like Mohist.

## Alternative Options

Other hybrid server options exist but were not chosen:

- **Mohist**: An alternative hybrid server that also supports
  NeoForge+Spigot, but has been noted for potential stability concerns in
  some reports.

- **Magma**: Discontinued as of November 15, 2023, so not a viable option.

- **SpongeForge**: Supports Sponge plugins (not Spigot plugins) with Forge
  mods, but has a smaller plugin ecosystem compared to Bukkit/Spigot.

## Configuration

The server configuration can be adjusted in the `.env` file. The default
settings use Arclight with NeoForge support. See `env.template` for
documentation of all available configuration options.

## Data Directory Setup

The data directory is where the Minecraft server stores all its runtime data.
This includes world data, server configuration, mods, plugins, and logs. The
data directory path is configured via the `DATA_DIR` environment variable in
`.env`, which defaults to `./data` relative to the `server/` directory.

For detailed information about the data directory structure, see the
[data directory
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

### Volume Mounts

The docker-compose configuration mounts two directories:

1. **`${DATA_DIR}:/data`**: The main data directory containing world data,
   mods, plugins, and server files

2. **`./config:/config`**: A separate configuration directory (currently
   mounted but purpose to be determined - may be used for server-specific
   configs that differ from the modpack configs)

### Production Storage

For production deployments, consider using Linode Block Storage for the data
directory. Block storage provides persistent, high-performance storage that
can be detached and reattached to different Linodes, making it ideal for:

- **Data persistence**: World data and server configuration survive Linode
  rebuilds or migrations

- **Backup and recovery**: Block storage volumes can be easily backed up or
  duplicated for disaster recovery

- **Performance**: Block storage offers better I/O performance compared to
  local disk storage for database-like workloads (Minecraft world data)

- **Flexibility**: The storage volume can be resized or moved between Linodes
  as needed

To use Linode Block Storage, mount the block storage volume to your Linode
and set `DATA_DIR` in your `.env` file to point to the mount point. For
example, if the block storage is mounted at `/mnt/minecraft-data`, set
`DATA_DIR=/mnt/minecraft-data` in your production `.env` file.

### TODOs

The following configuration management questions need to be addressed:

1. **Mod/Plugin Configuration Management**: How will configuration files for
   mods and plugins be managed?
   - Should modpack config files from `config/` be automatically copied to
     `${DATA_DIR}/config/` on server setup?
   - How should server-specific overrides be handled?
   - Should we maintain a template or default config directory structure?

2. **Spigot Plugin Management**: How will Spigot plugins (especially
   permissions plugins like LuckPerms) be managed?
   - Where should plugin JAR files be stored (in the repo vs. manual
     installation)?
   - How should plugin configuration files be managed?
   - Should we document recommended plugins and their configuration?
   - How will plugin updates be handled?