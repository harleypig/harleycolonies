# Server Infrastructure and Networking

This document covers hosting provider configuration, DNS setup, networking,
and infrastructure management. This is operational documentation.

## Hosting Provider: Linode

### Instance Selection

Considerations for instance selection:
- Expected player count
- Modpack size and complexity
- World size and generation requirements
- Budget constraints

Recommended starting points:
- **Small (2-5 players)**: Shared CPU, 4GB RAM, 2 vCPU
- **Medium (5-15 players)**: Dedicated CPU, 8GB RAM, 4 vCPU
- **Large (15+ players)**: Dedicated CPU, 16GB+ RAM, 8+ vCPU

### Instance Setup

1. **Create Linode Instance**
   - Select distribution (Ubuntu LTS recommended)
   - Choose instance type
   - Select region (closest to majority of players)
   - Set root password or SSH key

2. **Initial Configuration**
   - Configure hostname
   - Set timezone
   - Update system packages
   - Install Docker and Docker Compose

3. **Network Configuration**
   - Configure static IP (if needed)
   - Set up firewall rules
   - Configure reverse DNS (PTR record)

## Storage Configuration

### Linode Block Storage

For production deployments, use Linode Block Storage for data directory:

1. **Create Block Storage Volume**
   - Size: Start with 100GB, scale as needed
   - Label: `minecraft-data`

2. **Attach to Linode**
   - Attach volume in Linode dashboard
   - Note device path (e.g., `/dev/disk/by-id/...`)

3. **Format and Mount**
   ```bash
   # Format (first time only)
   sudo mkfs.ext4 /dev/disk/by-id/...

   # Create mount point
   sudo mkdir -p /mnt/minecraft-data

   # Mount
   sudo mount /dev/disk/by-id/... /mnt/minecraft-data

   # Set permissions
   sudo chown -R $USER:$USER /mnt/minecraft-data
   ```

4. **Persistent Mount**
   Add to `/etc/fstab`:
   ```
   /dev/disk/by-id/... /mnt/minecraft-data ext4 defaults,noatime 0 2
   ```

5. **Configure Server**
   Set `DATA_DIR=/mnt/minecraft-data` in `.env`

### Storage Management

- Monitor disk usage: `df -h /mnt/minecraft-data`
- Set up alerts for disk usage > 80%
- Plan for storage growth (world expansion)
- Consider backup storage volume

## DNS Configuration

### Domain Setup

1. **Purchase Domain** (if not already owned)
   - Use reputable registrar
   - Enable domain privacy if desired

2. **Configure DNS Records**

   **A Record** (IPv4):
   ```
   Type: A
   Name: @ (or subdomain like mc)
   Value: <Linode IP address>
   TTL: 3600
   ```

   **AAAA Record** (IPv6, if available):
   ```
   Type: AAAA
   Name: @ (or subdomain)
   Value: <Linode IPv6 address>
   TTL: 3600
   ```

   **SRV Record** (for Minecraft):
   ```
   Type: SRV
   Name: _minecraft._tcp
   Priority: 5
   Weight: 0
   Port: 25565
   Target: mc.example.com
   TTL: 3600
   ```

3. **Reverse DNS (PTR)**
   - Configure in Linode dashboard
   - Set PTR record to domain name
   - Improves server reputation

### DNS Propagation

- DNS changes can take 24-48 hours to propagate
- Use `dig` or `nslookup` to verify DNS records
- Test connectivity: `ping mc.example.com`

## Networking

### Port Configuration

Standard ports:
- **25565**: Minecraft server (TCP)
- **25575**: RCON (TCP, restrict access)
- **22**: SSH (TCP, restrict access)

### Network Security

- Configure firewall (see `security.md`)
- Use VPN for administrative access when possible
- Restrict RCON port to admin IPs
- Consider DDoS protection if needed

### IPv6 Configuration

If using IPv6:
- Configure IPv6 address in Linode
- Add AAAA DNS record
- Update firewall rules for IPv6
- Test IPv6 connectivity

## Backup Infrastructure

### Backup Storage

Options for backup storage:
- **Linode Object Storage**: S3-compatible object storage
- **Linode Block Storage**: Additional volume for backups
- **External Storage**: AWS S3, Backblaze B2, etc.

### Backup Strategy

1. **Full Backups**: Daily, keep for 7 days
2. **Weekly Backups**: Keep for 4 weeks
3. **Monthly Backups**: Keep for 12 months

### Backup Automation

Set up automated backups:
- Use cron for scheduled backups
- Upload to object storage
- Rotate old backups automatically
- Test restoration regularly

## Monitoring and Alerting

### System Monitoring

Monitor:
- CPU usage
- Memory usage
- Disk usage
- Network traffic
- Server uptime

### Application Monitoring

Monitor:
- Server TPS (Ticks Per Second)
- Player count
- Memory usage (JVM)
- Error rates in logs
- Plugin/mod loading issues

### Alerting

Set up alerts for:
- High CPU/memory usage
- Disk usage > 80%
- Server crashes
- Failed backups
- Unusual network traffic

### Monitoring Tools

Consider using:
- Linode Longview (built-in monitoring)
- Prometheus + Grafana
- Custom monitoring scripts
- Log aggregation tools

## Scaling Considerations

### Vertical Scaling

- Upgrade Linode instance size
- Increase memory allocation
- Add CPU cores
- Upgrade storage volume

### Horizontal Scaling

- Consider multiple servers for different purposes
- Load balancing (if applicable)
- Separate development/staging servers

### Performance Optimization

- Tune JVM settings (see server configuration)
- Optimize world generation settings
- Configure chunk loading limits
- Use performance mods/plugins

## Disaster Recovery

### Recovery Procedures

1. **Server Failure**
   - Restore from backup
   - Recreate instance if needed
   - Restore data from block storage

2. **Data Loss**
   - Restore from most recent backup
   - Investigate cause
   - Implement preventive measures

3. **Network Issues**
   - Check DNS configuration
   - Verify firewall rules
   - Test connectivity
   - Contact hosting provider if needed

### Recovery Testing

- Test backup restoration quarterly
- Document recovery procedures
- Maintain recovery runbook
- Train team on recovery procedures

## Cost Management

### Cost Optimization

- Right-size instance (don't over-provision)
- Use block storage efficiently
- Monitor and optimize resource usage
- Consider reserved instances for long-term use

### Budget Planning

- Estimate monthly costs
- Plan for growth
- Budget for backups and storage
- Consider cost alerts

## Infrastructure Checklist

- [ ] Linode instance provisioned and configured
- [ ] Block storage created and mounted
- [ ] DNS records configured
- [ ] Reverse DNS (PTR) set
- [ ] Firewall rules configured
- [ ] Backup storage configured
- [ ] Monitoring set up
- [ ] Alerting configured
- [ ] Documentation updated
- [ ] Access controls documented

