# Server TODO

## Configuration

- Determine the optimal value for the `MEMORY` variable for the server
  - Currently set to 2G in env.template
  - Consider factors such as:
    - Number of expected concurrent players
    - Modpack size and mod count
    - World size and complexity
    - Server performance requirements
    - Available system resources
  - Test different memory allocations and monitor performance
  - Document recommended values for different server sizes
  - Determine if we need to manage init (`-Xms`) and max (`-Xmx`) memory
    variables separately
    - The `MEMORY` variable in itzg/minecraft-server sets both -Xms and
      -Xmx to the same value
    - Consider if separate init (INIT_MEMORY) and max memory (MAX_MEMORY) settings are needed
    - Typically recommended to set both to the same value for consistent
      performance

- Evaluate which environment variables from itzg/minecraft-server should be
  used
  - Review available variables from [variables
    documentation](https://docker-minecraft-server.readthedocs.io/en/latest/variables/)
  - Determine which variables are relevant for this server setup:
    - General options (MEMORY, TZ, USE_AIKAR_FLAGS, etc.)
    - Server settings (MAX_PLAYERS, DIFFICULTY, etc.)
    - RCON configuration (already configured)
    - JVM options (JVM_OPTS, JVM_XX_OPTS, etc.)
    - Other relevant categories
  - Evaluate whether variables should be:
    - Set as environment variables in docker-compose.yml/.env
    - Managed in configuration files (server.properties, bukkit.yml,
      spigot.yml, etc.)
    - Not used at all (rely on defaults)
  - Consider separation of concerns:
    - Environment variables for server-level configuration
    - Configuration files for game/server-specific settings
    - Document which variables are essential vs. optional
  - Update env.template and docker-compose.yml based on findings

- We're using arclight hybrid for spigot/neoforge. Do we need to modify data/arclight.conf?

- Comprehensive audit of all non-mod configuration files and settings
  - Review and document all configuration files that need management,
    even if defaults are acceptable. Document findings in
    `docs/minecraft-server/` directory.
  - **Docker and Infrastructure Configuration:**
    - `docker-compose.yml`: Review service definitions, port mappings,
      environment variables, volume mounts, container settings (tty,
      stdin_open, restart policy, pull_policy)
    - `env.template` and `.env`: Review all environment variables from
      itzg/minecraft-server, including:
      - Memory settings (MEMORY, potentially INIT_MEMORY/MAX_MEMORY)
      - Server type (TYPE, ARCLIGHT_TYPE, ARCLIGHT_RELEASE)
      - Version settings (VERSION, NEOFORGE_VERSION)
      - RCON configuration (ENABLE_RCON, RCON_PASSWORD, RCON_PORT)
      - Mod/plugin management (REMOVE_OLD_MODS, SPIGET_RESOURCES,
        PLUGINS_FILE, CURSEFORGE_FILES, CF_API_KEY)
      - Timezone (TZ)
      - JVM flags (USE_AIKAR_FLAGS, JVM_OPTS, JVM_XX_OPTS)
      - Other variables from [itzg/minecraft-server
        documentation](https://docker-minecraft-server.readthedocs.io/en/latest/variables/)
    - `extras/` directory: Review plugin and mod list files
      (spiget-plugins.txt, CF_MODLIST, PLUGINS_FILE)
  - **Core Server Configuration Files (in ${DATA_DIR}):**
    - `server.properties`: Review all vanilla Minecraft server
      properties including:
      - Server port, IP binding
      - Game mode, difficulty
      - Max players, view distance
      - Online mode, whitelist, enforce whitelist
      - MOTD, server name
      - PvP, spawn protection
      - Resource pack settings
      - Network compression, max tick time
      - All other vanilla server properties
    - `eula.txt`: Verify EULA acceptance (auto-generated but needs
      verification)
  - **Player Management Files (in ${DATA_DIR}):**
    - `ops.json`: Review operator management and permission levels
    - `whitelist.json`: Review whitelist management
    - `banned-players.json`: Review banned players list
    - `banned-ips.json`: Review banned IP addresses list
    - `usercache.json`: Document player cache (auto-managed)
  - **Arclight/Bukkit/Spigot Configuration Files (in ${DATA_DIR}):**
    - `arclight.conf`: Review Arclight-specific settings, hybrid server
      configuration, mod/plugin compatibility settings
    - `bukkit.yml`: Review Bukkit API settings, plugin loading
      configuration, warning settings
    - `spigot.yml`: Review Spigot performance settings, entity
      activation ranges, chunk loading settings, player settings
      (moved-too-quickly, etc.), world settings (mob-spawn-range,
      etc.)
    - `paper.yml`: Review Paper-specific optimizations if applicable
      (anti-xray, chunk system, performance tuning)
    - `help.yml`: Review help command customization
    - `commands.yml`: Review command aliases and shortcuts
    - `permissions.yml`: Review default permission groups and nodes
  - **Logging Configuration:**
    - `log4j2.xml`: Review logging levels, appenders, log file
      rotation settings, console output formatting
  - **Runtime Data (Documentation Only):**
    - `logs/` directory: Document log file management, rotation, and
      retention policies
    - `world/` directories: Document backup strategy (not managed but
      needs backup plan)
  - **Documentation Requirements:**
    - Create documentation structure in `docs/minecraft-server/`
    - Document each configuration file category with:
      - Purpose and location
      - Key settings and their effects
      - Default values and when to change them
      - Best practices for management
      - Relationship to environment variables vs. config files
    - Even if defaults are acceptable, document that they were
      reviewed and found suitable
    - Consider which settings should be templated vs. manually
      configured
    - Document separation of concerns: environment variables for
      server-level config, files for game/server-specific settings