# Server Setup Procedures

This document provides step-by-step procedures for initial server setup and
configuration. This is operational documentation and should not be made
publicly accessible.

## Prerequisites

- Hosting provider account (e.g., Linode)
- SSH access to server
- Docker and Docker Compose installed
- Basic Linux administration knowledge

## Initial Server Setup

### 1. Provision Server Instance

- [ ] Select appropriate instance type based on expected player count
- [ ] Choose Linux distribution (Ubuntu LTS recommended)
- [ ] Configure initial SSH keys
- [ ] Set up basic firewall rules (see `security.md`)

### 2. Install Docker and Docker Compose

```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Install Docker Compose
sudo apt-get update
sudo apt-get install docker-compose-plugin

# Add user to docker group (if needed)
sudo usermod -aG docker $USER
```

### 3. Clone Repository

```bash
# Clone the repository
git clone <repository-url> harleycolonies
cd harleycolonies/server
```

### 4. Configure Environment Variables

```bash
# Copy template
cp env.template .env

# Edit .env with production values
nano .env
```

Required configuration:
- `VERSION`: Minecraft version (e.g., `1.21.1`)
- `NEOFORGE_VERSION`: NeoForge version (if specific version needed)
- `MEMORY`: JVM memory allocation (start with `2G`, adjust based on testing)
- `SERVER_PORT`: Server port (default `25565`)
- `DATA_DIR`: Path to data directory (use absolute path for production)
- `ARCLIGHT_RELEASE`: Arclight release version
- `RCON_PASSWORD`: Strong password for RCON access
- `CF_API_KEY`: CurseForge API key (if using CurseForge mod downloads)
- `CF_MODLIST`: Filename of mod list in `extras/` directory
- `SPIGET_PLUGINS`: Comma-separated list of Spigot plugin resource IDs

### 5. Set Up Data Directory

```bash
# Create data directory (or use Linode Block Storage mount point)
mkdir -p $DATA_DIR

# Set appropriate permissions
chown -R $USER:$USER $DATA_DIR
```

For production, consider using Linode Block Storage:
- Create block storage volume in Linode dashboard
- Attach volume to Linode instance
- Mount volume: `sudo mount /dev/disk/by-id/... /mnt/minecraft-data`
- Set `DATA_DIR=/mnt/minecraft-data` in `.env`
- Add to `/etc/fstab` for persistent mounting

### 6. Prepare Modpack Files

```bash
# Copy modpack files to extras directory
# Ensure CF_MODLIST file exists in server/extras/
# Ensure PLUGINS_FILE exists if using plugin file list
```

### 7. Start Server

```bash
# Start server in detached mode
docker-compose up -d

# View logs
docker-compose logs -f mc
```

### 8. Initial Configuration

- [ ] Accept EULA (auto-generated if `EULA=true` in environment)
- [ ] Configure `server.properties` in data directory
- [ ] Set up operator permissions (`ops.json`)
- [ ] Configure whitelist if needed (`whitelist.json`)
- [ ] Copy modpack config files to `${DATA_DIR}/config/`

## Post-Setup Tasks

- [ ] Configure DNS records (see `infrastructure.md`)
- [ ] Set up firewall rules (see `security.md`)
- [ ] Configure backup procedures
- [ ] Set up monitoring and alerting
- [ ] Document server access procedures
- [ ] Test server connectivity and functionality

## Troubleshooting

### Server Won't Start

- Check Docker logs: `docker-compose logs mc`
- Verify environment variables: `docker-compose config`
- Check data directory permissions
- Verify port availability: `netstat -tuln | grep 25565`

### Mods Not Loading

- Verify mod files are in `${DATA_DIR}/mods/`
- Check mod compatibility with Minecraft/NeoForge version
- Review server logs for mod loading errors
- Ensure `CF_MODLIST` file format is correct

### Plugins Not Loading

- Verify plugin files are in `${DATA_DIR}/plugins/`
- Check plugin compatibility with Arclight version
- Review server logs for plugin errors
- Ensure `SPIGET_PLUGINS` resource IDs are correct

## Next Steps

- See `deployment.md` for update and maintenance procedures
- See `security.md` for security configuration
- See `infrastructure.md` for networking and DNS setup

