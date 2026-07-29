# Repository Workflow

Repository-specific workflow and conventions for the HarleyColonies modpack
repository. Agent-facing configuration lives in `.claude/`.

## Repository Structure

```text
harleycolonies/
├── bin/                          # Helper scripts and the Python tooling
│   ├── modpack-manager           #   CLI entry point
│   ├── mpmanager/                #   the package behind it
│   ├── backup-instance           #   instance backup script
│   ├── mk-cf-modlist             #   CurseForge server modlist generator
│   ├── resources/                #   Jinja2 wiki templates
│   └── tests/                    #   pytest suite
├── modpacks/                     # Mod METADATA + per-mod wiki sources
│   ├── mods.yaml                 #   source of truth for mods
│   └── <mod-slug>/               #   custom config/ and wiki.md
├── harleycolonies-1.20.1-0.1.2/  # Packwiz pack — Forge 1.20.1
├── harleycolonies-1.21.1/        # Packwiz pack — NeoForge 1.21.1
├── pages/                        # Wiki (Gollum) — guides, mods, style, …
├── server/                       # Server stack (docker-compose, itzg)
├── docs/                         # Server/infrastructure documentation
├── config/                       # Default configurations
└── archive/                      # Historical/review files
```

**Naming trap:** `modpacks/` holds mod *metadata and wiki sources*, not
modpacks. The actual packs are the two `harleycolonies-*` directories.

### Script Naming

- Scripts go in `bin/` (not `scripts/`)
- Lowercase names with hyphens
- Executable, with a shebang line

## modpack-manager

`bin/modpack-manager` is the unified interface for managing mods, modpacks,
and wiki generation. It has three command groups — `mod`, `modpack`, and
`wiki`. Every level accepts `--help`.

It needs `bin/requirements.txt` installed (`tomlkit`, `pyyaml`, `pytest`,
`jinja2`); a gitignored `bin/venv/` is the usual home.

### Mod operations

```bash
# Create a mod entry and install it into a modpack via packwiz
./bin/modpack-manager mod create <mod-slug> --modpack <modpack-dir> \
    [--curseforge-id ID] [--category CATEGORY] [--file-id FILE_ID]

# List mods, optionally filtered
./bin/modpack-manager mod list [--slug SLUG] [--modpack MODPACK] \
    [--categories [CATEGORIES ...]] [--category-names]

# Refresh a mod's metadata from its packwiz TOML
./bin/modpack-manager mod refresh <mod-slug>

# Update mod information
./bin/modpack-manager mod update <mod-slug> [--side {client,server,both}] \
    [--curseforge-id ID] [--modrinth-id ID]

# Remove a mod
./bin/modpack-manager mod remove <mod-slug>

# Import mods from an existing packwiz directory
./bin/modpack-manager mod sync --from <modpack-dir> [--slug SLUG]
```

### Modpack operations

```bash
# Create a new modpack
./bin/modpack-manager modpack create <modpack-dir> [--mc-version VERSION] \
    [--modloader {forge,fabric,quilt}] [--modloader-version VERSION]

# List modpacks, or the mods in one
./bin/modpack-manager modpack list [--dir DIR]

# Update modpack metadata
./bin/modpack-manager modpack update <modpack-dir>

# Add / remove a mod
./bin/modpack-manager modpack add <modpack-dir> <mod-slug>
./bin/modpack-manager modpack remove-mod <modpack-dir> <mod-slug>

# Mark a mod as rejected for a modpack
./bin/modpack-manager modpack reject <modpack-dir> <mod-slug> --reason "..."

# Sync a modpack against mods.yaml
./bin/modpack-manager modpack sync <modpack-dir>

# Export via packwiz
./bin/modpack-manager modpack export <modpack-dir>

# Remove a modpack entirely
./bin/modpack-manager modpack remove <modpack-dir>
```

Note the asymmetry: `modpack remove` removes the **modpack**;
`modpack remove-mod` removes a **mod from** a modpack.

### Wiki generation

```bash
# Generate the page for one mod
./bin/modpack-manager wiki generate --mod <mod-slug>

# Regenerate the mods index
./bin/modpack-manager wiki generate --index

# Regenerate everything
./bin/modpack-manager wiki generate --all
```

**`--all` is destructive** — it clears `pages/mods/` and removes
`pages/mods.md` before regenerating. Prefer `--mod` for a single change.

### Mod Data Structure

Mod information lives in `modpacks/mods.yaml`:

```yaml
mods:
  <mod-slug>:
    name: "Display Name"  # Optional
    description: "Mod description"  # Optional
    side: "client" | "server" | "both"  # Auto-detected or manual
    curseforge_id: <project-id>  # Optional
    modrinth_id: <project-id>  # Optional
    modpacks:
      installed_in:
        - "harleycolonies-1.20.1-0.1.2"
      rejected_in:
        - modpack: "harleycolonies-1.20.1-0.1.2"
          reason: "Conflicts with other mods"
```

### Custom Mod Files

Per-mod custom content lives in `modpacks/<mod-slug>/`:

- `modpacks/<mod-slug>/config/` — custom config files, copied into the
  modpack when generating
- `modpacks/<mod-slug>/wiki.md` — custom wiki content, used instead of the
  simple generated page

## Packwiz Conventions

Prefer `modpack-manager` over raw `packwiz`: it keeps `modpacks/mods.yaml`
and the pack in step. Direct `packwiz` calls bypass that bookkeeping and
leave the two out of sync.

### Manual operations (legacy)

```bash
packwiz curseforge install <mod-name>
packwiz modrinth install <mod-name>
packwiz remove <mod-file>.toml
```

After any manual operation, test the modpack and reconcile the metadata with
`./bin/modpack-manager mod sync --from <modpack-dir>`.

### Server modlist

`bin/mk-cf-modlist` exports the server-side CurseForge modlist to
`server/extras/cf-modlist.txt`. Run it from within a pack directory.

## Documentation Standards

### File Naming

- Lowercase with hyphens: `example-file.md`
- Descriptive and concise

### Markdown Formatting

- Wrap prose at 78 columns in Markdown files and comments
- Proper heading hierarchy (h1 for page title, h2 for sections)
- Table of contents for longer documents
- Linted by markdownlint via pre-commit; see `.markdownlint.json`

### Wiki organization

Player-facing content lives in the Gollum wiki under `pages/`:

- `pages/guides/` — player guides
- `pages/mods/` — **generated** mod pages; edit the source in
  `modpacks/<mod-slug>/wiki.md`, not these
- `pages/style/` — the custom MineColonies style guide
- `pages/baritone/` — Baritone documentation
- `pages/technical/` — technical notes

`docs/` holds server and infrastructure documentation only.

Wiki links are page-relative and extensionless — `[Huts](style/huts)`, not
`style/huts.md`. Every page opens with `--- title: ... ---` frontmatter.

## Schematic and Blueprint Workflow

### Creating Schematics

1. Design the schematic in-game
2. Export using appropriate tools
3. Store schematics in designated location (TBD)
4. Document schematic requirements and usage

### Blueprint Management

- Document blueprint dependencies
- Note required materials and levels
- Include placement instructions

## Journeymap Configuration

### Backup Process

**Why backup Journeymap?**

Updating the Journeymap mod overwrites the entire `journeymap/` directory,
which can result in loss of:

- Custom waypoints
- Map exploration data
- Personal settings and configurations

**How to backup:**

Use `bin/backup-instance`, which captures the irreplaceable slice of an
instance — JourneyMap waypoints and config, blueprints, `options.txt`,
baritone settings, and `servers.dat` — while skipping regenerable data:

```bash
bin/backup-instance [--dest DIR] [--dry-run] <instance-path>
```

Destination precedence: `--dest` > `$MC_BACKUP_DIR` >
`~/projects/minecraft/backups`.

**Note:** `journeymap/` is gitignored and must not be committed — it holds
user-specific world data.

## Git Workflow

`master` is protected: PRs required, force-push and deletion blocked, CI must
pass. All branch work happens in a worktree.

### Branch Naming

- `feature/` — new features or mod additions
- `bugfix/` — bug fixes
- `docs/` — documentation only

### Commit Messages

Conventional Commits — `<type>(<scope>): <subject>`, imperative mood, subject
under 72 characters.

### Modpack Versioning

- Directory format: `harleycolonies-<mc-version>-<pack-version>`
- The authoritative version is the `version` field in each `pack.toml`
- Releases are tagged per pack (`<pack-dir>/vX.Y.Z`); see
  `.claude/CONVENTIONS.md`

## Testing Workflow

```bash
cd bin && python -m pytest tests/ -q
```

The suite currently has known pre-existing failures from fixture drift — see
`.claude/TESTS.md` before reading a red run as your own breakage.

### Before committing

1. Test modpack loading
2. Verify mod compatibility
3. Check for configuration errors
4. Validate packwiz format

## Configuration Management

### User-Specific Files

Gitignored:

- `journeymap/` — user-specific map data
- `*.aider*` — Aider temporary files
- `bin/venv/`, `work/`, `tmpconfig/`
- Exported packs (`*.zip`, `*.mrpack`) and mod jars

### Modpack Configs

- Default configurations go in `config/`
- Per-mod overrides go in `modpacks/<mod-slug>/config/`

## Resources

- [Packwiz Documentation](https://packwiz.infra.link/)
- [MineColonies Wiki](https://minecolonies.com/wiki/)
- `pages/technical/` — additional development resources
