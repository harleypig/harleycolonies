---
title: Operating System and Server Software
---

This page documents research and decisions regarding server software
selection and architecture choices for the HarleyColonies modpack server.
Operational details such as server setup procedures, firewall
configuration, and access controls are documented separately in the
repository's private documentation.

## Server Architecture: Hybrid Server

The HarleyColonies modpack uses a hybrid server setup that combines
Spigot/Paper plugins with Forge/NeoForge mods. This architecture was
chosen for the following reasons:

### Why Hybrid?

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
   - **Spigot plugins**: For permissions management, server
     administration, and other server management features that are
     well-established in the plugin ecosystem

For more information about hybrid server types supported by the
itzg/minecraft-server Docker image, see the [Hybrids
documentation](https://docker-minecraft-server.readthedocs.io/en/latest/types-and-platforms/server-types/hybrids/).

## Server Software: Arclight

Arclight has been chosen as the hybrid server platform for the following
reasons:

1. **Stability and Performance**: Arclight is recognized for its
   stability and efficient performance, ensuring smooth operation even
   when running both plugins and mods concurrently.

2. **Active Development**: The Arclight project is actively maintained
   with regular updates and has a supportive community providing
   assistance and continuous improvements.

3. **Compatibility**: Arclight seamlessly integrates the Bukkit API into
   the modding environment, allowing Spigot/PaperMC plugins to operate
   alongside Forge/Fabric/NeoForge mods without conflicts.

4. **NeoForge Support**: Arclight supports NeoForge, which is required
   for the latest versions of the HarleyColonies modpack.

5. **Research Findings**: Based on searches and community feedback,
   Arclight appears to be the best choice among hybrid server options,
   with better stability and support compared to alternatives like Mohist.

### Alternative Options Considered

Other hybrid server options exist but were not chosen:

- **Mohist**: An alternative hybrid server that also supports
  NeoForge+Spigot, but has been noted for potential stability concerns in
  some reports.

- **Magma**: Discontinued as of November 15, 2023, so not a viable
  option.

- **SpongeForge**: Supports Sponge plugins (not Spigot plugins) with
  Forge mods, but has a smaller plugin ecosystem compared to
  Bukkit/Spigot.

## Version Information

- **Minecraft Version**: 1.21.1
- **Mod Loader**: NeoForge
- **NeoForge Version**: Managed via Arclight release (see server
  configuration)

## Containerization: Docker

The server runs using Docker with the `itzg/minecraft-server` image.
This approach provides:

- **Consistency**: Same server environment across development and
  production
- **Isolation**: Server processes isolated from host system
- **Ease of Management**: Simplified deployment and updates via Docker
  Compose
- **Portability**: Server can be easily moved between systems

## Plugin Categories

The hybrid server architecture allows the use of Spigot/Bukkit plugins
for server administration. Key plugin categories include:

- **Permissions**: LuckPerms for advanced permissions management
- **World Management**: Fast Chunk Pregenerator for world generation
- **Server Administration**: Various plugins for server management and
  player utilities

Specific plugin configuration and management details are documented
separately in the repository's private documentation.

## Operational Documentation

Operational details including server setup procedures, firewall
configuration, DNS setup, access controls, and deployment procedures are
documented separately in the repository's private documentation directory
(`server/`). This separation ensures sensitive operational information
remains private while making architectural decisions and research
findings publicly accessible.

