# Server Deployment and Updates

This document covers procedures for deploying updates, managing server
lifecycle, and performing maintenance tasks.

## Server Lifecycle Management

### Starting the Server

```bash
cd /path/to/harleycolonies/server
docker-compose up -d
```

### Stopping the Server

```bash
# Graceful shutdown (saves world)
docker-compose stop mc

# Or use server console command
docker-compose exec mc rcon-cli stop
```

### Restarting the Server

```bash
docker-compose restart mc
```

### Viewing Server Console

```bash
# Follow logs
docker-compose logs -f mc

# Access interactive console
docker-compose exec -it mc rcon-cli
```

## Updating the Server

### Update Procedure

1. **Backup Current State**
   ```bash
   # Backup data directory
   tar -czf backup-$(date +%Y%m%d-%H%M%S).tar.gz $DATA_DIR
   ```

2. **Stop Server**
   ```bash
   docker-compose stop mc
   ```

3. **Update Docker Image**
   ```bash
   docker-compose pull
   ```

4. **Update Configuration**
   - Review `env.template` for new variables
   - Update `.env` if needed
   - Update `docker-compose.yml` if needed

5. **Update Modpack**
   - Update mod files in modpack directory
   - Update `CF_MODLIST` if mod list changed
   - Copy updated mods to `${DATA_DIR}/mods/` or let Docker handle it

6. **Update Plugins**
   - Update plugin list in `SPIGET_PLUGINS` if needed
   - Or manually update plugin JARs in `${DATA_DIR}/plugins/`

7. **Start Server**
   ```bash
   docker-compose up -d
   ```

8. **Verify**
   - Check logs for errors
   - Test server connectivity
   - Verify mods/plugins loaded correctly

### Modpack Updates

When updating the modpack:

1. Update modpack files in repository
2. Export modpack using `modpack-manager modpack export`
3. Copy mods to server `extras/` directory
4. Update `CF_MODLIST` file if mod list changed
5. Follow update procedure above

### Minecraft Version Updates

When updating Minecraft version:

1. **Check Compatibility**
   - Verify Arclight supports new version
   - Check mod compatibility
   - Review NeoForge version requirements

2. **Update Configuration**
   - Update `VERSION` in `.env`
   - Update `NEOFORGE_VERSION` if needed
   - Update `ARCLIGHT_RELEASE` if needed

3. **Test in Development**
   - Test modpack with new version locally
   - Verify all mods load correctly

4. **Production Update**
   - Follow standard update procedure
   - May require world migration (backup first!)

## Backup Procedures

### Automated Backups

Set up automated backups using cron:

```bash
# Add to crontab
0 2 * * * /path/to/backup-script.sh
```

Example backup script:
```bash
#!/bin/bash
BACKUP_DIR="/backups/minecraft"
DATA_DIR="/mnt/minecraft-data"
DATE=$(date +%Y%m%d-%H%M%S)

# Stop server
cd /path/to/harleycolonies/server
docker-compose stop mc

# Create backup
tar -czf "$BACKUP_DIR/backup-$DATE.tar.gz" "$DATA_DIR"

# Start server
docker-compose start mc

# Remove backups older than 30 days
find "$BACKUP_DIR" -name "backup-*.tar.gz" -mtime +30 -delete
```

### Manual Backups

```bash
# Full backup
tar -czf backup-$(date +%Y%m%d).tar.gz $DATA_DIR

# World-only backup
tar -czf world-backup-$(date +%Y%m%d).tar.gz $DATA_DIR/world*
```

### Backup Storage

- Store backups on separate storage volume
- Consider off-site backup storage
- Test backup restoration periodically

## Maintenance Tasks

### Regular Maintenance

- **Daily**: Check server logs for errors
- **Weekly**: Review server performance metrics
- **Monthly**: Update plugins and mods
- **Quarterly**: Review and optimize server configuration

### Log Management

```bash
# View recent logs
docker-compose logs --tail=100 mc

# Clear old logs (server manages this, but can manually clean)
# Logs are in ${DATA_DIR}/logs/
```

### Performance Monitoring

- Monitor memory usage: `docker stats mc`
- Check disk usage: `df -h $DATA_DIR`
- Review server TPS (Ticks Per Second) via server console

### Configuration Updates

When updating server configuration:

1. Stop server
2. Edit configuration files in `${DATA_DIR}/`
3. Restart server
4. Verify changes took effect

Common configuration files:
- `server.properties` - Server settings
- `bukkit.yml` - Bukkit settings
- `spigot.yml` - Spigot settings
- `config/` - Mod and plugin configs

## Rollback Procedures

If an update causes issues:

1. **Stop Server**
   ```bash
   docker-compose stop mc
   ```

2. **Restore Backup**
   ```bash
   # Restore data directory
   tar -xzf backup-YYYYMMDD.tar.gz -C /
   ```

3. **Revert Configuration**
   - Restore previous `.env` if needed
   - Restore previous `docker-compose.yml` if needed

4. **Start Server**
   ```bash
   docker-compose up -d
   ```

5. **Verify**
   - Check logs
   - Test functionality
   - Document issues encountered

## Emergency Procedures

### Server Crashes

1. Check logs: `docker-compose logs mc`
2. Review crash reports in `${DATA_DIR}/crash-reports/`
3. Check system resources: `docker stats`, `df -h`, `free -h`
4. Restart if needed: `docker-compose restart mc`

### Data Corruption

1. Stop server immediately
2. Restore from most recent backup
3. Investigate cause (disk issues, power failure, etc.)
4. Implement preventive measures

### Security Incident

1. Stop server immediately
2. Review access logs
3. Change all passwords and keys
4. Review firewall rules
5. Restore from clean backup if compromised
6. See `security.md` for security procedures

