# bin/ - Helper Scripts

This directory contains helper scripts and utilities for managing the modpack.

## Scripts

### gen-modlist

Generates a markdown mod list from the packwiz `.toml` files in the modpack
directory.

**Usage:**

```bash
./bin/gen-modlist
```

This script scans all `.toml` files in the modpack directory (excluding
`pack.toml` and `index.toml`) and generates a `modlist.md` file organized by
mod class and category.

## mod-manager

The mod-manager script provides a unified interface for managing mods,
generating modpacks, and creating wiki pages.

### Features

- **Mod Management**: Add, update, and remove mods in `mods/mods.yaml`
- **Modpack Operations**: Create, sync, add/remove mods from modpacks
- **Wiki Generation**: Generate vimwiki markdown pages for mods
- **Client-Side Detection**: Auto-detect mod side from packwiz files
- **Custom Configs**: Copy custom config files from `mods/<mod-slug>/config/` to modpacks

### Usage Examples

```bash
# Add a mod
./bin/mod-manager add jei --curseforge-id 238222 --side both

# Add mod to modpack
./bin/mod-manager modpack add harleycolonies-1.20.1-0.1.2 jei

# Sync modpack with mods.yaml
./bin/mod-manager modpack sync harleycolonies-1.20.1-0.1.2

# Generate wiki pages
./bin/mod-manager wiki

# Import from existing modpack
./bin/mod-manager sync --from-dir harleycolonies-1.20.1-0.1.2
```

See `WORKFLOW.md` for detailed documentation.
