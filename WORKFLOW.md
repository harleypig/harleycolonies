# Repository Workflow

This document defines repository-specific workflow rules and conventions for
the HarleyColonies modpack repository. These rules extend and complement the
general agent guidelines defined in `AGENTS.md`.

## Repository Structure

### Directory Organization

```
harleycolonies/
??? bin/                    # Helper scripts (gen-modlist, etc.)
??? docs/                   # Documentation
?   ??? guides/            # Player-facing guides
?   ??? mods/              # Mod-related documentation
?   ??? technical/         # Technical documentation
??? pages/                  # Wiki pages (Gollum)
??? archive/                # Historical/review files
??? harleycolonies-1.20.1-0.1.2/  # Active modpack directory
```

### Script Naming

- Scripts go in `bin/` directory (not `scripts/`)
- Use lowercase names with hyphens if needed
- Make scripts executable with shebang line

## Mod Manager

The `mod-manager` script provides a unified interface for managing mods,
generating modpacks, and creating wiki pages.

### Basic Usage

```bash
# Add a new mod
./bin/mod-manager add <mod-slug> [--curseforge-id ID] [--modrinth-id ID] [--side SIDE]

# Update mod information
./bin/mod-manager update <mod-slug> [--side SIDE]

# Remove a mod
./bin/mod-manager remove <mod-slug>

# List all mods
./bin/mod-manager list

# Show information for a specific mod
./bin/mod-manager list --mod <mod-slug>
```

### Modpack Operations

```bash
# Create a new modpack
./bin/mod-manager modpack create <modpack-dir> --mc-version VERSION --modloader LOADER [--modloader-version VERSION]

# Add mod to modpack
./bin/mod-manager modpack add <modpack-dir> <mod-slug>

# Remove mod from modpack
./bin/mod-manager modpack remove <modpack-dir> <mod-slug>

# Mark mod as rejected in modpack
./bin/mod-manager modpack reject <modpack-dir> <mod-slug> --reason "Reason"

# Sync modpack with mods.yaml (add/remove mods)
./bin/mod-manager modpack sync <modpack-dir>

# Export modpack
./bin/mod-manager modpack export <modpack-dir>

# List mods in a modpack
./bin/mod-manager list --modpack <modpack-dir>
```

### Wiki Generation

```bash
# Generate wiki page for a specific mod
./bin/mod-manager wiki --mod <mod-slug>

# Generate all wiki pages
./bin/mod-manager wiki
```

### Syncing from Existing Modpacks

```bash
# Import mods from an existing packwiz directory
./bin/mod-manager sync --from <modpack-dir>
```

### Mod Data Structure

Mod information is stored in `mods/mods.yaml` with the following structure:

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

Custom configuration files and wiki content can be stored in `mods/<mod-slug>/`:

- `mods/<mod-slug>/config/` - Custom config files (copied to modpack when generating)
- `mods/<mod-slug>/wiki.md` - Custom wiki page content (used instead of simple page)

## Packwiz Conventions

### Mod Addition Process (Legacy)

For manual packwiz operations:

1. Use `packwiz` commands to add mods:
   ```bash
   packwiz curseforge install <mod-name>
   packwiz modrinth install <mod-name>
   ```

2. Test the modpack after adding new mods

3. Update `docs/mods/confirmed-mods.md` with mod details

4. Regenerate mod list: `./bin/gen-modlist`

**Note:** It's recommended to use `mod-manager` instead for better tracking
and automation.

### Mod Removal Process (Legacy)

For manual packwiz operations:

1. Use `packwiz` commands to remove mods:
   ```bash
   packwiz remove <mod-file>.toml
   ```

2. Test the modpack after removal

3. Update documentation accordingly

**Note:** It's recommended to use `mod-manager modpack remove` instead.

### Mod Configuration

- Mod-specific configurations should be documented in `docs/mods/`
- Include configuration file locations when known
- Document any custom configurations or overrides
- Custom configs can be stored in `mods/<mod-slug>/config/` for automatic
  copying to modpacks

## Documentation Standards

### File Naming

- Use lowercase with hyphens: `example-file.md`
- Keep names descriptive and concise

### Markdown Formatting

- Word wrap at 78 columns in Markdown files and comments
- Use proper heading hierarchy (h1 for page title, h2 for sections, etc.)
- Include table of contents for longer documents

### Guide Organization

- Player guides go in `docs/guides/`
- Include practical examples
- Cross-reference related documentation

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

1. Before updating Journeymap, copy the `journeymap/` directory:
   ```bash
   cp -r journeymap/ journeymap-backup-$(date +%Y%m%d)/
   ```

2. Alternatively, backup specific files:
   - `journeymap/data/mp/<world-name>/waypoints.json` - Waypoints
   - `journeymap/data/mp/<world-name>/` - Map data

3. After updating, restore if needed:
   ```bash
   cp -r journeymap-backup-<date>/journeymap/* journeymap/
   ```

**Note:** The `journeymap/` directory is in `.gitignore` and should not be
committed to the repository as it contains user-specific world data.

## Git Workflow

### Branch Naming

Follow the conventions from `AGENTS.md`:
- `feature/` - New features or mod additions
- `bugfix/` - Bug fixes
- `refactor/` - Code or structure refactoring

### Commit Messages

- Use descriptive commit messages
- Reference issue numbers if applicable
- Follow conventional commit format when appropriate

### Modpack Versioning

- Current format: `harleycolonies-<mc-version>-<pack-version>`
- Example: `harleycolonies-1.20.1-0.1.2`
- Update version in `pack.toml` when making releases

## Testing Workflow

### Before Committing

1. Test modpack loading
2. Verify mod compatibility
3. Check for configuration errors
4. Validate packwiz format

### Before Pushing

1. Run `./bin/gen-modlist` to ensure mod list is current
2. Verify documentation is up to date
3. Ensure `.gitignore` excludes user-specific files

## Configuration Management

### User-Specific Files

These should be in `.gitignore`:
- `journeymap/` - User-specific map data
- `*.aider*` - Aider temporary files
- Other user-specific configs

### Modpack Configs

- Default configurations go in `config/` directory
- Document configuration file locations in `docs/mods/`
- Keep example configurations when helpful

## Wiki Pages

### Moving Documentation to Wiki

- Documentation in `pages/` is used by the Gollum wiki
- Consider moving relevant guides from `docs/guides/` to `pages/` for wiki
  integration
- Keep technical documentation in `docs/technical/`

## Resources

- [Packwiz Documentation](https://packwiz.infra.link/)
- [MineColonies Wiki](https://minecolonies.com/wiki/)
- See `docs/technical/resources.md` for additional development resources
