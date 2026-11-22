# Public Server Management

## Goal

Use the same packwiz definition and itzg image for the long-running public
server that players connect to, with a clear promotion path from "tested
in ephemeral container" to "live".

## Leveraging What Already Exists

- `server/docker-compose.yml` and the env templates already target the
  itzg image.
- `bin/mk-cf-modlist` produces the server-side CurseForge list.
- Packwiz's server-side filtering (`-s server`) is already what the itzg
  image uses when given `PACKWIZ_URL`.

## Promotion Flow

1. A pack version passes the testing environment (previous plan).
2. The corresponding packwiz directory (or a tagged release) is made
   available at a stable URL.
3. Update the public server's `PACKWIZ_URL` (or the compose env) and
   restart (or use a blue/green pair of containers behind a proxy if
   zero-downtime becomes important).
4. RCON or the itzg console confirms the new mods loaded.
5. Optional: announce via Discord or in-game.

## Ongoing Management Tasks (agent- or script-friendly)

- Tail logs and alert on exceptions or TPS drops.
- Periodic backups of the world volume.
- Whitelist / op management via RCON.
- MotD or server-icon updates.
- "Is the current live pack still the one we tested?" checksum or git
  SHA check.

## Safety

- Never auto-promote without an explicit approval step (human or a
  recorded "tests passed" artifact).
- Keep the public server's data volume separate from ephemeral test
  volumes.
- Document the exact `PACKWIZ_URL` and pack git SHA that is live.
