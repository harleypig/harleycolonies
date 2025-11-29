# Environment Variables Evaluation

This document evaluates which environment variables from itzg/minecraft-server
should be used for the HarleyColonies modpack server, and determines whether
they should be set as environment variables or managed in configuration files.

## Evaluation Criteria

- **Environment Variables**: Used for server-level configuration that affects
  Docker container behavior, JVM settings, or server initialization
- **Configuration Files**: Used for game/server-specific settings that can be
  changed without restarting the container
- **Defaults**: Acceptable when the default behavior is suitable for our use
  case

## Currently Configured Variables

### Core Server Settings

- **VERSION** (`1.21.1`)
  - **Status**: Configured
  - **Recommendation**: Keep - Essential for specifying Minecraft version
  - **Location**: env.template

- **NEOFORGE_VERSION** (empty)
  - **Status**: Configured
  - **Recommendation**: Keep - Required for NeoForge modpack
  - **Location**: env.template
  - **Note**: Should be set to specific version for reproducibility

- **MEMORY** (`2G`)
  - **Status**: Configured
  - **Recommendation**: Keep - Essential for JVM memory allocation
  - **Location**: env.template
  - **Note**: See TODO.md for optimization task

- **TYPE** (`ARCLIGHT`)
  - **Status**: Hardcoded in docker-compose.yml
  - **Recommendation**: Keep hardcoded - Server type is fixed
  - **Location**: docker-compose.yml

- **ARCLIGHT_TYPE** (`NEOFORGE`)
  - **Status**: Hardcoded in docker-compose.yml
  - **Recommendation**: Keep hardcoded - Arclight variant is fixed
  - **Location**: docker-compose.yml

- **ARCLIGHT_RELEASE** (empty)
  - **Status**: Configured
  - **Recommendation**: Keep - Should specify Arclight release version
  - **Location**: env.template
  - **Note**: Should be set to specific version for reproducibility

### RCON Configuration

- **ENABLE_RCON** (`true`)
  - **Status**: Configured
  - **Recommendation**: Keep - Essential for server management
  - **Location**: env.template

- **RCON_PASSWORD** (empty)
  - **Status**: Configured
  - **Recommendation**: Keep - Required when RCON is enabled
  - **Location**: env.template
  - **Note**: Must be set in production .env file

- **RCON_PORT** (`25575`)
  - **Status**: Configured
  - **Recommendation**: Keep - Allows customization of RCON port
  - **Location**: env.template

### Mod and Plugin Management

- **REMOVE_OLD_MODS** (`false`)
  - **Status**: Configured
  - **Recommendation**: Keep - Useful for modpack updates
  - **Location**: env.template

- **SPIGET_RESOURCES** (mapped from `SPIGET_PLUGINS`)
  - **Status**: Configured
  - **Recommendation**: Keep - Allows plugin installation via Spiget
  - **Location**: env.template (as SPIGET_PLUGINS)

- **PLUGINS_FILE** (`/extras/$PLUGINS_FILE`)
  - **Status**: Configured
  - **Recommendation**: Keep - Allows plugin installation from file
  - **Location**: env.template

- **USES_PLUGINS** (`true`)
  - **Status**: Hardcoded in docker-compose.yml
  - **Recommendation**: Keep hardcoded - Always using plugins
  - **Location**: docker-compose.yml

- **CF_API_KEY** (empty)
  - **Status**: Configured
  - **Recommendation**: Keep - Required for CurseForge mod downloads
  - **Location**: env.template
  - **Note**: Must be set in production .env file

- **CURSEFORGE_FILES** (`@/extras/$CF_MODLIST`)
  - **Status**: Configured
  - **Recommendation**: Keep - Allows modpack installation from CurseForge
  - **Location**: env.template (as CF_MODLIST)

### Infrastructure

- **SERVER_PORT** (`25565`)
  - **Status**: Configured
  - **Recommendation**: Keep - Allows port customization
  - **Location**: env.template

- **DATA_DIR** (`./data`)
  - **Status**: Configured
  - **Recommendation**: Keep - Essential for data directory location
  - **Location**: env.template

- **EULA** (`true`)
  - **Status**: Hardcoded in docker-compose.yml
  - **Recommendation**: Keep hardcoded - Always accept EULA
  - **Location**: docker-compose.yml

## Recommended Additional Variables

### General Options

- **TZ** (Timezone)
  - **Status**: Not configured
  - **Recommendation**: Add - Important for log timestamps and server time
  - **Default**: System timezone
  - **Suggested**: `America/New_York` or appropriate timezone
  - **Location**: env.template

- **USE_AIKAR_FLAGS** (`true`)
  - **Status**: Not configured
  - **Recommendation**: Add - Recommended JVM flags for Minecraft servers
  - **Default**: `false`
  - **Suggested**: `true` for better performance
  - **Location**: env.template

### JVM Options

- **JVM_OPTS** (Additional JVM options)
  - **Status**: Not configured
  - **Recommendation**: Optional - Add if custom JVM tuning needed
  - **Default**: None
  - **Suggested**: Leave empty unless specific tuning required
  - **Location**: env.template (commented out)

- **JVM_XX_OPTS** (Additional JVM -XX options)
  - **Status**: Not configured
  - **Recommendation**: Optional - Add if custom JVM tuning needed
  - **Default**: None
  - **Suggested**: Leave empty unless specific tuning required
  - **Location**: env.template (commented out)

### Server Settings (Should Use Configuration Files)

These settings are better managed in `server.properties` rather than
environment variables:

- **MAX_PLAYERS**: Should be in server.properties
- **DIFFICULTY**: Should be in server.properties
- **MOTD**: Should be in server.properties
- **GAMEMODE**: Should be in server.properties
- **ONLINE_MODE**: Should be in server.properties
- **WHITELIST**: Should be in server.properties

**Rationale**: These are game settings that may need to change without
restarting the container. Managing them in server.properties allows for
runtime changes and better separation of concerns.

## Variables to Avoid

- **INIT_MEMORY** / **MAX_MEMORY**: Not needed - MEMORY sets both -Xms and
  -Xmx to the same value, which is recommended for consistent performance
- **OVERRIDE_SERVER_PROPERTIES**: Not recommended - Better to manage
  server.properties directly
- **OVERRIDE_*_CONFIG**: Not recommended - Better to manage config files
  directly

## Summary

### Essential Variables (Keep)
- VERSION
- NEOFORGE_VERSION
- MEMORY
- ARCLIGHT_RELEASE
- ENABLE_RCON
- RCON_PASSWORD
- RCON_PORT
- REMOVE_OLD_MODS
- SPIGET_PLUGINS
- PLUGINS_FILE
- CF_API_KEY
- CF_MODLIST
- SERVER_PORT
- DATA_DIR

### Recommended Additions
- TZ (timezone)
- USE_AIKAR_FLAGS

### Optional Additions
- JVM_OPTS (if custom tuning needed)
- JVM_XX_OPTS (if custom tuning needed)

### Hardcoded (Keep as-is)
- EULA: true
- TYPE: ARCLIGHT
- ARCLIGHT_TYPE: NEOFORGE
- USES_PLUGINS: true

## Implementation Plan

1. Add TZ and USE_AIKAR_FLAGS to env.template
2. Add optional JVM_OPTS and JVM_XX_OPTS (commented) to env.template
3. Update docker-compose.yml to use TZ from environment
4. Document which settings belong in server.properties vs environment
  variables
5. Ensure all required variables are documented in env.template

