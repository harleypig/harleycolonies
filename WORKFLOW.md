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

## Packwiz Conventions

### Mod Addition Process

1. Use `packwiz` commands to add mods:
   ```bash
   packwiz curseforge install <mod-name>
   packwiz modrinth install <mod-name>
   ```

2. Test the modpack after adding new mods

3. Update `docs/mods/confirmed-mods.md` with mod details

4. Regenerate mod list: `./bin/gen-modlist`

### Mod Removal Process

1. Use `packwiz` commands to remove mods:
   ```bash
   packwiz remove <mod-file>.toml
   ```

2. Test the modpack after removal

3. Update documentation accordingly

### Mod Configuration

- Mod-specific configurations should be documented in `docs/mods/`
- Include configuration file locations when known
- Document any custom configurations or overrides

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
