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
