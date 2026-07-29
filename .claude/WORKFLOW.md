# HarleyColonies — Workflow

Agent-facing workflow. Procedures for the modpack tooling itself live in the
root [`WORKFLOW.md`](../WORKFLOW.md) — this file does not duplicate them.

## Where things live

| Path | What it is |
| --- | --- |
| `bin/modpack-manager` | CLI entry point (thin wrapper) |
| `bin/mpmanager/` | The Python package behind it — `cli.py`, `commands.py`, `data.py`, `packwiz.py`, `wiki.py` |
| `bin/tests/` | pytest suite for the above |
| `bin/backup-instance` | Backup script for a Minecraft instance |
| `moddata/mods.yaml` | Mod metadata — **the** source of truth for mods |
| `moddata/<mod-slug>/` | Per-mod custom `config/` and `wiki.md` |
| `harleycolonies-1.20.1-0.1.2/` | Packwiz pack — Forge 1.20.1 |
| `harleycolonies-1.21.1/` | Packwiz pack — NeoForge 1.21.1 |
| `pages/` | Gollum wiki source |
| `server/docker-compose.yml` | itzg server stack (RCON) |
| `archive/` | Retained historical config — not live |
| `docs/` | Server/infrastructure docs |

`moddata/` also holds a per-modpack state directory
(`moddata/harleycolonies-1.21.1/` — `info.yaml`, `mods.yaml`) that shares its
name with the real pack at the repo root. Same name, different thing: one is
the pack, the other is metadata about it.

## Branch and PR flow

Standard global flow, with this repo's specifics:

- Default branch is `master`, **protected**: PR required, force-push and
  deletion blocked, CI must pass.
- All branch work happens in a worktree off `origin/master`.
- `auto-merge: enabled`, so invoking **push-pr** carries through merge on
  green CI. Merge still obeys the ruleset.
- Head branches are deleted automatically on merge.

## Running the tooling

`bin/modpack-manager` needs `bin/requirements.txt` installed (`tomlkit`,
`pyyaml`, `pytest`, `jinja2`). A local `bin/venv/` is gitignored and is the
usual home for them.

Three command groups — `mod`, `modpack`, `wiki`. Run `--help` at any level;
the root `WORKFLOW.md` carries the worked examples.

**Destructive flag to know:** `wiki generate --all` clears `pages/mods/` and
removes `pages/mods.md` before regenerating. Do not reach for it when a
single `--mod <slug>` will do.

## Wiki conventions

`pages/` is rendered by Gollum:

- Every page opens with `--- title: ... ---` frontmatter.
- Intra-wiki links are page-relative and **extensionless** —
  `[Huts](style/huts)`, not `style/huts.md`.
- A page's directory of children mirrors its name (`style.md` +
  `style/*.md`).

Mod pages under `pages/mods/` are **generated** from `moddata/mods.yaml` and
the per-mod `wiki.md`; edit the source, not the generated page.

## Editing the packs

Prefer the tooling over hand-editing packwiz TOML — `modpack add`,
`modpack remove-mod`, `modpack sync` keep `moddata/mods.yaml` and the pack
in step. Direct `packwiz` calls bypass that bookkeeping and leave the two out
of sync.
