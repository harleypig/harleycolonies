# HarleyColonies — Session Memory & Handoff

This file is the working memory for Claude Code sessions in this repo. It
records what has been done, what we are trying to do, and what still needs
to be migrated out of the *other* clone. Update it as items get done — tick
the checklists and move finished work out of "In progress".

## Where you are (read this first)

- **This is the ACTIVE clone:** `~/projects/minecraft/harleycolonies`
  (the user keeps all Minecraft repos under `~/projects/minecraft/`:
  baritone, packwiz, docker-minecraft-server, journeymap-api,
  journeymap-waypoint-manager, MDK templates). **All work happens here.**
- **Stale asset-stash clone:** `~/projects/harleycolonies` — an old
  `master`@`wip` checkout that became a dumping ground for ~2.3 GB of
  **untracked** binary assets under `client-side-only/`. It is in sync
  with origin on tracked files. Treat it as a *read-only asset stash*,
  not a working repo. **Never `git add -A` there.** Pull assets *from*
  it as needed (see Migration checklist), then it can eventually be
  deleted once everything useful is rescued.

## How this came about

A new session was started in the stale clone, scanned the repo, and
discovered the dual-clone situation. The user wants Minecraft work to
live in `~/projects/minecraft/`, so we are consolidating here. A new
session will be started in this directory to continue.

## Done

- **`bin/backup-instance`** — backup script for a Minecraft instance.
  Written, executable, shellcheck-clean, tested against the United
  Colonies instance (2.1 GB instance → 1.3 MB tarball, 666 entries).
  **Committed** on the `fix-dual-repo` branch (`9bf9f46`) and pushed.
  - Captures the irreplaceable ~MB slice only:
    `journeymap/data/**/waypoints/` (raw `WaypointData.dat`),
    `journeymap/config/` (JourneyMap settings — **no mod API exists for
    these, so the file copy is the only backup**), `blueprints/`,
    `options.txt`, `baritone/settings.txt`, `servers.dat`, and
    `jm_waypoint_manager/` if present.
  - Excludes regenerable data: mods, Distant Horizons data, map tiles,
    baritone `.bcr` caches.
  - Usage: `bin/backup-instance [--dest DIR] [--dry-run] <instance-path>`
  - Destination precedence: `--dest` > `$MC_BACKUP_DIR` > default
    `~/projects/minecraft/backups`.
  - When `journeymap-waypoint-manager`'s `/wm export` ships, its JSON
    lands in `jm_waypoint_manager/` and the script picks it up
    automatically; the raw-file copy stays as the settings backup.

## In progress / goals

- Establish a real workflow for the United Colonies instance backup
  (when to run it, where backups live, rotation/retention).

## Migrated to issues

The migration checklist and cleanup list that used to live here are now
tracked as GitHub issues — this file no longer duplicates them:

| Was | Now |
| --- | --- |
| Rescue assets from the stale clone | [#6](https://github.com/harleypig/harleycolonies/issues/6) |
| `modpacks/` is misleadingly named | **done** — renamed to `moddata/` in #7 |
| Stale `WORKFLOW.md` | **done** — corrected in #3 |
| `.gitignore` too narrow | **done** — hardened in #3 |
| `AGENTS.md` is generic boilerplate | **done** — deleted in #3 |

Surfaced while onboarding, also tracked:
[#4](https://github.com/harleypig/harleycolonies/issues/4) (red test suite),
[#5](https://github.com/harleypig/harleycolonies/issues/5) (markdownlint
backlog), [#8](https://github.com/harleypig/harleycolonies/issues/8)
(pre-commit phase 2).

## Quick reference

- Packs: `harleycolonies-1.20.1-0.1.2/` (Forge 1.20.1),
  `harleycolonies-1.21.1/` (NeoForge 1.21.1).
- Tooling: `bin/modpack-manager` + `bin/mpmanager/` (Python; tests in
  `bin/tests/`). Mod data: `moddata/mods.yaml`.
- Server: `server/docker-compose.yml` (itzg, ARCLIGHT/NeoForge, RCON).
- Wiki (Gollum): `pages/`.
- Branches present: `master`, `docs/baritone` (merged, deletable),
  `feature/docker-config-audit`.
