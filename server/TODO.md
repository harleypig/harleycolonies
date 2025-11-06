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