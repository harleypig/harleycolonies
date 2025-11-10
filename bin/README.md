# bin/ - Helper Scripts

This directory contains helper scripts and utilities for managing the modpack.

## Scripts

## modpack-manager

The `modpack-manager` script provides a unified interface for managing mods,
generating modpacks, and creating wiki pages.

### Features

- **Mod Management**: Create, update, remove, list, and sync mods in `modpacks/mods.yaml`
- **Modpack Operations**: Create, update, remove, sync, add/remove mods from modpacks
- **Wiki Generation**: Generate wiki markdown pages for mods using Jinja2
  templates
- **Metadata Management**: Two-tier metadata system (canonical and
  version-specific)
- **Side Management**: Update mod side (client/server/both) via tags with
  automatic TOML updates
- **Automatic Dependency Checking**: Automatically installs missing
  dependencies from `requirements.txt`
- **Client-Side Detection**: Auto-detect mod side from packwiz files
- **Custom Configs**: Copy custom config files from `modpacks/<mod-slug>/config/`
  to modpacks
- **Packwiz Integration**: Uses Packwiz for mod installation and management
- **Error Handling**: Automatically marks mods as rejected when no matching file found

### Commands

#### Testing

```bash
# Run all tests
bin/modpack-manager pytest

# Run tests with pytest options
bin/modpack-manager pytest -v
bin/modpack-manager pytest tests/test_wiki.py
bin/modpack-manager pytest -k test_generate
```

The `pytest` command creates a temporary test virtual environment, installs
dependencies, runs tests, and cleans up automatically. This bypasses all
other setup in the script.

#### Mod Commands

```bash
# Create a new mod entry and install using Packwiz
bin/modpack-manager mod create <mod-slug> --modpack <modpack-dir> [--curseforge-id ID] [--category CATEGORY] [--file-id FILE_ID]

# List mods
bin/modpack-manager mod list [--slug <mod-slug>] [--modpack <modpack-dir>] [--categories ...] [--category-names]

# Update mod information
bin/modpack-manager mod update <mod-slug> [--side SIDE] [--curseforge-id ID] [--modrinth-id ID]

# Remove a mod (from modpack or from modpacks directory)
bin/modpack-manager mod remove <mod-slug> [--from-modpack <modpack-dir>]

# Sync mod(s) from modpack TOML to modpacks/mods.yaml
bin/modpack-manager mod sync --from <modpack-dir> [--slug <mod-slug>]

# Refresh a mod's metadata from packwiz TOML
bin/modpack-manager mod refresh <mod-slug> [--modpack <modpack-dir>] [--force-remote]
```

**Note**: `mod create` requires `--modpack` and the modpack directory must exist. The command uses `packwiz curseforge add` to install the mod. If the mod exists but no matching file is found for the modpack, it will automatically be marked as rejected in `modpacks/mods.yaml`.

#### Modpack Commands

```bash
# Create a new modpack
bin/modpack-manager modpack create <modpack-dir> --mc-version VERSION --modloader LOADER [--modloader-version VERSION]

# List modpacks or mods in modpack
bin/modpack-manager modpack list [--dir <modpack-dir>]

# Update modpack metadata
bin/modpack-manager modpack update <modpack-dir> [--mc-version VERSION] [--modloader LOADER]

# Remove modpack (from tracking or from filesystem)
bin/modpack-manager modpack remove <modpack-dir> [--from-filesystem]

# Sync modpack TO match per-modpack state (installs/removes mods)
bin/modpack-manager modpack sync <modpack-dir>

# Sync modpacks/mods.yaml FROM modpack (imports all mods)
bin/modpack-manager modpack sync --from <modpack-dir>

# Migrate central modpack state to per-modpack files
bin/modpack-manager modpack migrate-state

# Add mod to modpack
bin/modpack-manager modpack add <modpack-dir> <mod-slug>

# Remove mod from modpack
bin/modpack-manager modpack remove-mod <modpack-dir> <mod-slug>

# Mark mod as rejected in modpack
bin/modpack-manager modpack reject <modpack-dir> <mod-slug> --reason "Reason"

# Export modpack using packwiz
bin/modpack-manager modpack export <modpack-dir>
```

#### Wiki Commands

```bash
# Generate wiki page for a specific mod
bin/modpack-manager wiki generate --mod <mod-slug>

# Generate all wiki pages
bin/modpack-manager wiki generate

# Generate all wiki pages (destructive: clears pages/mods and removes pages/mods.md)
bin/modpack-manager wiki generate --all

# Generate mods index page (pages/mods.md)
bin/modpack-manager wiki generate --index
```

### Usage Examples

```bash
# Create a mod entry and install using Packwiz
bin/modpack-manager mod create jei --modpack harleycolonies-1.21.1 --curseforge-id 238222

# Create a mod with category and file-id options
bin/modpack-manager mod create minecolonies --modpack harleycolonies-1.21.1 --curseforge-id 245211 --category mods

# Create a new modpack
bin/modpack-manager modpack create harleycolonies-1.21.1 --mc-version 1.21.1 --modloader forge

# Add mod to modpack
bin/modpack-manager modpack add harleycolonies-1.20.1-0.1.2 jei

# Sync modpack TO match modpacks/mods.yaml
bin/modpack-manager modpack sync harleycolonies-1.20.1-0.1.2

# Sync modpacks/mods.yaml FROM modpack (import all mods)
bin/modpack-manager modpack sync --from harleycolonies-1.20.1-0.1.2

# Sync single mod from modpack
bin/modpack-manager mod sync --from harleycolonies-1.20.1-0.1.2 --slug jei

# Update mod side
bin/modpack-manager mod update minecolonies --side both

# Update mod curseforge_id
bin/modpack-manager mod update jei --curseforge-id 238222

# Remove mod from modpack only
bin/modpack-manager mod remove jei --from-modpack harleycolonies-1.20.1-0.1.2

# Remove mod from modpacks directory entirely
bin/modpack-manager mod remove jei

# Generate wiki page for a mod
bin/modpack-manager wiki generate --mod jei

# Generate all wiki pages (destructive)
bin/modpack-manager wiki generate --all

# Generate mods index page
bin/modpack-manager wiki generate --index

# List all mods
bin/modpack-manager mod list

# List mods in a modpack
bin/modpack-manager mod list --modpack harleycolonies-1.20.1-0.1.2

# Show categorized list of all mods
bin/modpack-manager mod list --categories

# Show categorized list for specific categories
bin/modpack-manager mod list --categories adventure-rpg,library-api

# Show available category names
bin/modpack-manager mod list --category-names
```

### Metadata System

The modpack-manager uses a two-tier metadata system:

- **Canonical Metadata**: Stored in `modpacks/<mod-slug>/metadata` - the first
  metadata seen for a mod
- **Version-Specific Metadata**: Stored in
  `modpacks/<mod-slug>/versions/<modpack-dir>/metadata` - only differences from
  canonical metadata

This allows tracking metadata differences between modpack versions while
keeping a single source of truth for the canonical metadata.

#### Metadata fields

`modpacks/mods.yaml` stores canonical metadata under each mod entry. Relevant
fields for this workflow:

```yaml
mods:
  some-mod:
    name: Some Mod
    side: both
    curseforge_id: 12345
    modrinth_id: abcdef
    metadata:
      # Categories are remote-sourced (CurseForge/packwiz) and refreshed
      # via the CLI; treat as read-only in the CLI.
      categories: [utility-qol, ui]

      # Optional, user-maintained or inferred
      integrations: [jei]

      # Optional. Use 'required' for true hard dependencies, 'optional' for
      # soft deps that enhance features.
      dependencies:
        required: [fabric-api]
        optional: [jei]
```

#### Refresh and merge rules

- `mod refresh` pulls metadata from the mod's packwiz `.pw.toml`.
- Categories are always overwritten by remote values when present.
- Integrations and dependencies are merged by default (union with local
  values preserved). Use `--force-remote` to replace locals entirely with
  remote values.
- `mods.yaml` remains the source of truth; manual additions persist unless
  `--force-remote` is specified.

**Note**: The `mods/` directory has been renamed to `modpacks/` to avoid
confusion with modpack directories. All mod metadata is now stored in
`modpacks/mods.yaml` and `modpacks/<mod-slug>/`.

### Automatic Dependency Management

The script automatically checks for required dependencies and installs them
from `requirements.txt` if missing. This ensures the script works correctly
even after cloning the repository on a new system.

### Relationship with Packwiz

`modpack-manager` is designed to **supplement** packwiz, not replace it.
Packwiz handles the core modpack management, while `modpack-manager` adds
additional features like versioning, metadata management, and wiki
generation.

#### What Packwiz Handles

- **Mod File Management**: Downloads and manages mod `.jar` files
- **Mod Metadata Storage**: Stores mod information in `.pw.toml` files
- **Mod Versioning**: Tracks mod versions within a single modpack
- **Mod Dependencies**: Manages mod dependencies and conflicts
- **Pack Metadata**: Manages pack information (Minecraft version, modloader,
  etc.) in `pack.toml`
- **Mod Side Settings**: Stores mod side (client/server/both) in TOML files
- **Export Functionality**: Exports modpacks for distribution
- **Update Management**: Handles mod updates from CurseForge/Modrinth

#### What modpack-manager Handles

- **Mod Metadata Centralization**: Stores canonical mod metadata in
  `modpacks/mods.yaml`
- **Modpack Versioning**: Manages multiple modpack versions with different
  mod versions
- **Version-Specific Metadata**: Tracks metadata differences between
  modpack versions
- **Wiki Generation**: Generates wiki pages from templates
- **Mod Categorization**: Organizes mods by categories for documentation
- **Side Overrides**: Can override packwiz side settings (as tags) and update
  TOML files
- **Metadata Extraction**: Extracts metadata from packwiz TOML files and
  stores in YAML format
- **Mod Creation with Packwiz**: Uses `packwiz curseforge add` to install mods
- **Error Handling**: Automatically marks mods as rejected when no matching file found
- **Dependency Detection**: Detects when Packwiz installs dependencies (handling TBD)

### Per‑modpack Files

Each modpack directory (e.g., `harleycolonies-1.21.1/`) now contains its own
state/config files:

```yaml
# harleycolonies-1.21.1/info.yaml
name: harleycolonies-1.21.1
author: HarleyColonies
# Optional fields used to replay `packwiz init` and pack settings:
mc_version: 1.21.1
modloader: forge            # forge | fabric | quilt | neoforge
modloader_version: latest   # or an explicit loader version
version: 0.1.0              # pack.toml 'version'
index_file: index.toml      # pack.toml 'index'
hash_format: sha256         # pack.toml 'hash-format'
```

```yaml
# harleycolonies-1.21.1/mods.yaml
mods:
  jei:
    status: installed
  some-mod:
    status: rejected
    reason: No matching file found
```

- `modpack-manager modpack create <dir>` will read missing versions/loader
  from `<dir>/info.yaml` when not provided as flags.
- `modpack-manager modpack sync <dir>` installs/removes mods to match
  `<dir>/mods.yaml`.

Use `modpack-manager modpack migrate-state` once to migrate existing central
`modpacks/mods.yaml` modpack references to the new per‑modpack files.

#### Where They Overlap

- **Mod Side Management**: Both handle mod side settings. `modpack-manager`
  can override packwiz side settings and automatically update the TOML
  files.
- **Mod Metadata**: Packwiz stores metadata in TOML, while
  `modpack-manager` extracts and stores it in YAML. The YAML format is
  used for wiki generation and cross-modpack analysis.
- **Modpack Structure**: `modpack-manager` works with packwiz modpack
  directories and respects packwiz's file structure.

#### Workflow Integration

The typical workflow is:
1. Use `modpack-manager modpack create` to create a new modpack
2. Use `modpack-manager mod create` to create mod entries and install mods
   using Packwiz
3. Use `modpack-manager modpack sync --from` to extract metadata from packwiz
   TOML files into the centralized YAML format
4. Use `modpack-manager mod` commands to manage mod metadata across multiple
   modpack versions
5. Use `modpack-manager wiki generate` to generate documentation from the
   centralized metadata
6. Use `modpack-manager modpack export` to export modpacks for distribution

### Wiki Templates

Wiki pages are generated using Jinja2 templates. The template files are
located in `bin/resources/`:

- **`mod-page.template.j2`** - Jinja2 template for individual mod wiki pages
  - Generates pages in `pages/mods/<mod-slug>.md`
  - Variables: `name`, `description`, `side`, `installed_in`

- **`mods-index-template.j2`** - Jinja2 template for the mods index page
  - Generates `pages/mods.md` with all mods grouped by category
  - Variables: `sorted_categories`, `categorized_mods`, `uncategorized_mods`

These templates can be customized as needed. The templates use Jinja2
syntax for dynamic content generation.

See `WORKFLOW.md` for detailed documentation.
