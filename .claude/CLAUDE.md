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

## Migration checklist — rescue from the stale clone

Assets that currently exist ONLY in `~/projects/harleycolonies` (all
untracked there). Move/handle each, then tick it off:

- [ ] `client-side-only/United Colonies/` — 2.1 GB Minecraft instance.
      Don't move wholesale; run `bin/backup-instance` against it to
      capture the irreplaceable slice, then decide what (if anything)
      else to keep.
- [ ] `client-side-only/minecolonies-blueprints/` — a **nested git
      repo** (has its own `.git`). Decide: standalone repo, submodule,
      or copy of blueprints only.
- [ ] `client-side-only/ClientSideMods/` — 112 MB of mods/resourcepacks.
      Likely re-downloadable; keep the *list* (`MyCSOMods.txt`), not the
      binaries.
- [ ] `client-side-only/MyCSOMods.txt` — the actual client-side-only mod
      *documentation*. This is the real CSO project content; bring it in
      and track it.
- [ ] zips/jars in `client-side-only/` (schematic worlds, resource
      packs, baritone jar) — `*.zip` is gitignored; keep them as local
      assets or external storage, not in git.

## Open cleanup items (from the repo scan — verify against THIS clone)

- [ ] `WORKFLOW.md` is stale: documents a non-existent `bin/mod-manager`
      (real entry points are `bin/modpack-manager` + the `bin/mpmanager`
      package) and refers to `mods/mods.yaml` when the dir is `modpacks/`.
- [ ] `.gitignore` doesn't cover the instance dir, jars, or baritone
      `.bcr` caches — only `*.zip`/`*.mrpack`. Harden it so a stray add
      can't pull in gigabytes.
- [ ] `modpacks/` is misleadingly named — it's the mod metadata + wiki
      store (`modpacks/mods.yaml`, per-mod `wiki.md`), not modpacks. The
      actual packs are `harleycolonies-1.20.1-0.1.2/` and
      `harleycolonies-1.21.1/`.
- [ ] `AGENTS.md` is generic multi-agent boilerplate, largely unrelated
      to this Minecraft repo — candidate for trimming to what applies.

## Quick reference

- Packs: `harleycolonies-1.20.1-0.1.2/` (Forge 1.20.1),
  `harleycolonies-1.21.1/` (NeoForge 1.21.1).
- Tooling: `bin/modpack-manager` + `bin/mpmanager/` (Python; tests in
  `bin/tests/`). Mod data: `modpacks/mods.yaml`.
- Server: `server/docker-compose.yml` (itzg, ARCLIGHT/NeoForge, RCON).
- Wiki (Gollum): `pages/`.
- Branches present: `master`, `docs/baritone` (current),
  `feature/docker-config-audit`.
