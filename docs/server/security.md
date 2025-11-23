# Server Security Configuration

This document covers security configuration including firewall rules, access
controls, and security best practices. This is sensitive operational
documentation.

## Firewall Configuration

### UFW (Uncomplicated Firewall)

```bash
# Enable UFW
sudo ufw enable

# Allow SSH (adjust port if using non-standard)
sudo ufw allow 22/tcp

# Allow Minecraft server port
sudo ufw allow 25565/tcp

# Allow RCON port (restrict to specific IPs if possible)
sudo ufw allow from <admin-ip> to any port 25575

# Deny all other incoming by default
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

### Firewall Rules Summary

- **Port 22 (SSH)**: Allow from trusted IPs only (consider VPN)
- **Port 25565 (Minecraft)**: Allow from anywhere (or restrict to specific
  regions)
- **Port 25575 (RCON)**: Restrict to admin IPs only
- **All other ports**: Deny by default

### Advanced Firewall (iptables)

If using iptables directly:

```bash
# Allow established connections
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Allow SSH (from specific IP if possible)
iptables -A INPUT -p tcp --dport 22 -s <admin-ip> -j ACCEPT

# Allow Minecraft
iptables -A INPUT -p tcp --dport 25565 -j ACCEPT

# Allow RCON (restricted)
iptables -A INPUT -p tcp --dport 25575 -s <admin-ip> -j ACCEPT

# Default deny
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT
```

## SSH Security

### Key-Based Authentication

```bash
# Generate SSH key pair (on local machine)
ssh-keygen -t ed25519 -C "your-email@example.com"

# Copy public key to server
ssh-copy-id user@server-ip

# Disable password authentication (after verifying key works)
sudo nano /etc/ssh/sshd_config
# Set: PasswordAuthentication no
# Set: PubkeyAuthentication yes
sudo systemctl restart sshd
```

### SSH Hardening

Edit `/etc/ssh/sshd_config`:

```
# Disable root login
PermitRootLogin no

# Use key authentication only
PasswordAuthentication no
PubkeyAuthentication yes

# Change default port (optional)
Port 2222

# Limit login attempts
MaxAuthTries 3

# Disable empty passwords
PermitEmptyPasswords no

# Use only strong ciphers
Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com
```

Restart SSH: `sudo systemctl restart sshd`

## Access Controls

### Server Operator Management

Manage operators via `ops.json` in data directory:

```json
[
  {
    "uuid": "player-uuid",
    "name": "PlayerName",
    "level": 4,
    "bypassesPlayerLimit": false
  }
]
```

Operator levels:
- Level 1: Can use basic commands
- Level 2: Can use moderation commands
- Level 3: Can use server management commands
- Level 4: Full access (use sparingly)

### Whitelist Management

Enable whitelist in `server.properties`:
```
white-list=true
```

Manage whitelist via `whitelist.json`:
```json
[
  {
    "uuid": "player-uuid",
    "name": "PlayerName"
  }
]
```

### RCON Access Control

- Use strong password (set in `.env` as `RCON_PASSWORD`)
- Restrict firewall to admin IPs only
- Consider using VPN for RCON access
- Rotate password regularly

### File Permissions

```bash
# Set proper permissions on server directory
chmod 700 /path/to/harleycolonies/server
chmod 600 server/.env
chmod 644 server/docker-compose.yml

# Data directory permissions
chmod 755 $DATA_DIR
chmod 644 $DATA_DIR/server.properties
```

## Docker Security

### Non-Root User

Run Docker containers as non-root user:

```yaml
# In docker-compose.yml
services:
  mc:
    user: "${UID}:${GID}"
```

### Resource Limits

Set resource limits to prevent resource exhaustion:

```yaml
services:
  mc:
    deploy:
      resources:
        limits:
          memory: 4G
        reservations:
          memory: 2G
```

### Network Isolation

Consider using Docker networks for isolation:

```yaml
services:
  mc:
    networks:
      - minecraft-net

networks:
  minecraft-net:
    driver: bridge
```

## Application Security

### RCON Password

- Use strong, randomly generated password
- Store in `.env` file (not committed to repository)
- Rotate regularly
- Use different password than SSH/other services

### API Keys

- Store CurseForge API key in `.env`
- Never commit API keys to repository
- Rotate keys if exposed
- Use least-privilege API keys when possible

### Plugin Security

- Only install plugins from trusted sources
- Keep plugins updated
- Review plugin permissions
- Remove unused plugins

### Mod Security

- Only use mods from trusted sources (CurseForge, Modrinth)
- Verify mod checksums when possible
- Keep mods updated
- Review mod permissions and capabilities

## Monitoring and Logging

### Log Monitoring

Monitor server logs for suspicious activity:

```bash
# Watch for failed login attempts
tail -f $DATA_DIR/logs/latest.log | grep "Failed to login"

# Monitor RCON access
tail -f $DATA_DIR/logs/latest.log | grep "RCON"
```

### Access Logs

Review SSH access logs:
```bash
sudo tail -f /var/log/auth.log
```

### Intrusion Detection

Consider setting up:
- Fail2ban for SSH protection
- Log monitoring tools
- Alert systems for suspicious activity

## Backup Security

- Encrypt backups containing sensitive data
- Store backups securely (encrypted storage)
- Limit backup access to authorized personnel
- Test backup restoration regularly

## Incident Response

If security incident occurs:

1. **Immediate Actions**
   - Isolate affected systems
   - Change all passwords and keys
   - Review access logs
   - Document incident

2. **Investigation**
   - Identify attack vector
   - Assess damage
   - Review security controls

3. **Remediation**
   - Patch vulnerabilities
   - Strengthen security controls
   - Restore from clean backup if needed

4. **Prevention**
   - Update security procedures
   - Improve monitoring
   - Conduct security review

## Security Checklist

- [ ] Firewall configured and enabled
- [ ] SSH key authentication enabled
- [ ] Password authentication disabled
- [ ] Strong RCON password set
- [ ] API keys secured in `.env`
- [ ] File permissions set correctly
- [ ] Regular security updates applied
- [ ] Backups encrypted and secured
- [ ] Monitoring and logging configured
- [ ] Access controls documented
- [ ] Incident response plan documented

## Regular Security Tasks

- **Weekly**: Review access logs
- **Monthly**: Rotate passwords and keys
- **Quarterly**: Security audit and review
- **Annually**: Full security assessment

