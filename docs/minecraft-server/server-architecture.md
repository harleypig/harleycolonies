# Server Architecture Decisions

This document explains the architectural decisions made for the HarleyColonies
modpack server, including why a hybrid server was chosen and why Arclight was
selected as the platform.

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
itzg/minecraft-server Docker image, see the [itzg Docker Image
documentation](itzg-docker-image.md).

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
settings use Arclight with NeoForge support. See `server/env.template` for
documentation of all available configuration options.

