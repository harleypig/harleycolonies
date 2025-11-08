# bin/ - Helper Scripts

This directory contains helper scripts and utilities for managing the modpack.

## Scripts

### gen-modlist

**Note:** This script is deprecated. Use `bin/modpack-manager list --categories`
instead, which provides the same functionality using centralized metadata from
`mods/mods.yaml`.

Generates a markdown mod list from the packwiz `.toml` files in the modpack
directory.

**Usage:**

```bash
bin/gen-modlist
```

This script scans all `.toml` files in the modpack directory (excluding
`pack.toml` and `index.toml`) and generates a `modlist.md` file organized by
mod class and category.

**Replacement:**

```bash
# Generate categorized mod list (prints to stdout)
bin/modpack-manager list --categories

# Save to file
bin/modpack-manager list --categories > docs/mods/modlist.md
```

The `modpack-manager list --categories` command provides the same output format
but uses centralized metadata from `mods/mods.yaml` instead of scanning TOML
files directly.

## modpack-manager

The `modpack-manager` script provides a unified interface for managing mods,
generating modpacks, and creating wiki pages.

### Features

- **Mod Management**: Add, update, and remove mods in `mods/mods.yaml`
- **Modpack Operations**: Create, sync, add/remove mods from modpacks
- **Wiki Generation**: Generate wiki markdown pages for mods using Jinja2
  templates
- **Metadata Management**: Two-tier metadata system (canonical and
  version-specific)
- **Side Management**: Update mod side (client/server/both) with automatic TOML
  updates
- **Automatic Dependency Checking**: Automatically installs missing
  dependencies from `requirements.txt`
- **Client-Side Detection**: Auto-detect mod side from packwiz files
- **Custom Configs**: Copy custom config files from `mods/<mod-slug>/config/`
  to modpacks

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

#### Mod Management

```bash
# Add a new mod
bin/modpack-manager add <mod-slug> [--curseforge-id ID] [--modrinth-id ID] [--side SIDE]

# Update mod information
bin/modpack-manager update <mod-slug> [--side SIDE]

# Remove a mod
bin/modpack-manager remove <mod-slug>

# List all mods or show specific mod information
bin/modpack-manager list [--modpack <modpack-dir>] [--mod <mod-slug>]

# Show categorized list (all categories)
bin/modpack-manager list --categories

# Show categorized list for specific categories
bin/modpack-manager list --categories adventure-rpg library-api
bin/modpack-manager list --categories adventure-rpg,library-api

# Show alphabetized list of all category names
bin/modpack-manager list --category-names

# Update mod side (canonical or version-specific)
bin/modpack-manager side <mod-slug> <new-side> [--modpack <modpack-dir>]
```

#### Modpack Operations

```bash
# Create a new modpack
bin/modpack-manager modpack create <modpack-dir> --mc-version VERSION --modloader LOADER [--modloader-version VERSION]

# Add mod to modpack
bin/modpack-manager modpack add <modpack-dir> <mod-slug>

# Remove mod from modpack
bin/modpack-manager modpack remove <modpack-dir> <mod-slug>

# Mark mod as rejected in modpack
bin/modpack-manager modpack reject <modpack-dir> <mod-slug> --reason "Reason"

# Sync modpack with mods.yaml (add/remove mods)
bin/modpack-manager modpack sync <modpack-dir>

# Export modpack using packwiz
bin/modpack-manager modpack export <modpack-dir>
```

#### Wiki Generation

```bash
# Generate wiki page for a specific mod
bin/modpack-manager wiki --mod <mod-slug>

# Generate all wiki pages
bin/modpack-manager wiki

# Generate all wiki pages (destructive: clears pages/mods and removes pages/mods.md)
bin/modpack-manager wiki --generate

# Generate mods index page (pages/mods.md)
bin/modpack-manager wiki --index
```

#### Syncing from Existing Modpacks

```bash
# Import mods from an existing packwiz directory
bin/modpack-manager sync --from <modpack-dir>
```

This command will:
- Extract metadata from packwiz TOML files
- Store canonical metadata in `mods/<mod-slug>/metadata`
- Store version-specific differences in
  `mods/<mod-slug>/versions/<modpack-dir>/metadata`
- Automatically handle side differences between modpacks

### Usage Examples

```bash
# Add a mod with CurseForge ID and side
bin/modpack-manager add jei --curseforge-id 238222 --side both

# Create a new modpack
bin/modpack-manager modpack create harleycolonies-1.21.1 --mc-version 1.21.1 --modloader forge

# Add mod to modpack
bin/modpack-manager modpack add harleycolonies-1.20.1-0.1.2 jei

# Sync modpack with mods.yaml
bin/modpack-manager modpack sync harleycolonies-1.20.1-0.1.2

# Import from existing modpack
bin/modpack-manager sync --from harleycolonies-1.20.1-0.1.2

# Update mod side for specific modpack
bin/modpack-manager side minecolonies both --modpack harleycolonies-1.20.1-0.1.2

# Generate wiki page for a mod
bin/modpack-manager wiki --mod jei

# Generate mods index page
bin/modpack-manager wiki --index

# List all mods
bin/modpack-manager list

# List mods in a modpack
bin/modpack-manager list --modpack harleycolonies-1.20.1-0.1.2

# Show categorized list of all mods
bin/modpack-manager list --categories

# Show categorized list for specific categories
bin/modpack-manager list --categories adventure-rpg,library-api

# Show available category names
bin/modpack-manager list --category-names
```

### Metadata System

The modpack-manager uses a two-tier metadata system:

- **Canonical Metadata**: Stored in `mods/<mod-slug>/metadata` - the first
  metadata seen for a mod
- **Version-Specific Metadata**: Stored in
  `mods/<mod-slug>/versions/<modpack-dir>/metadata` - only differences from
  canonical metadata

This allows tracking metadata differences between modpack versions while
keeping a single source of truth for the canonical metadata.

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
  `mods/mods.yaml`
- **Modpack Versioning**: Manages multiple modpack versions with different
  mod versions
- **Version-Specific Metadata**: Tracks metadata differences between
  modpack versions
- **Wiki Generation**: Generates wiki pages from templates
- **Mod Categorization**: Organizes mods by categories for documentation
- **Side Overrides**: Can override packwiz side settings and update TOML
  files
- **Metadata Extraction**: Extracts metadata from packwiz TOML files and
  stores in YAML format

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
1. Use packwiz to manage mod files, versions, and dependencies within a
   modpack
2. Use `modpack-manager sync --from` to extract metadata from packwiz TOML
   files into the centralized YAML format
3. Use `modpack-manager` to manage mod metadata across multiple modpack
   versions
4. Use `modpack-manager wiki` to generate documentation from the
   centralized metadata
5. Use packwiz to export modpacks for distribution

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
