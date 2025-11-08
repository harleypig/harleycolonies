#!/usr/bin/env python3
"""
Command implementations for mod-manager.
"""

import shutil
import sys
from pathlib import Path

from mod_manager import data, packwiz, wiki, validation


def add_mod(mod_slug, curseforge_id=None, modrinth_id=None, side=None):
    """Add a new mod to mods.yaml."""
    print(f"Adding mod: {mod_slug}")

    # Check if mod already exists
    existing_mod = data.get_mod(mod_slug)
    if existing_mod is not None:
        print(f"Error: Mod {mod_slug} already exists")
        return 1

    # Validate mod IDs
    if curseforge_id:
        valid, error = validation.validate_mod_id(mod_slug, curseforge_id, "curseforge")
        if not valid:
            print(f"Error: {error}")
            return 1

    if modrinth_id:
        valid, error = validation.validate_mod_id(mod_slug, modrinth_id, "modrinth")
        if not valid:
            print(f"Error: {error}")
            return 1

    # Create new mod entry
    mod_data = {}
    if curseforge_id:
        mod_data["curseforge_id"] = curseforge_id
    if modrinth_id:
        mod_data["modrinth_id"] = modrinth_id
    if side:
        mod_data["side"] = side

    # Validate mod data
    valid, error = validation.validate_mod_data(mod_data)
    if not valid:
        print(f"Error: {error}")
        return 1

    data.set_mod(mod_slug, mod_data)
    print(f"Added mod: {mod_slug}")
    return 0


def update_mod(mod_slug, side=None):
    """Update mod information."""
    print(f"Updating mod: {mod_slug}")

    mod = data.get_mod(mod_slug)
    if mod is None:
        print(f"Error: Mod {mod_slug} not found")
        return 1

    if side:
        mod["side"] = side
        data.set_mod(mod_slug, mod)
        print(f"Updated side for {mod_slug} to {side}")

    return 0


def remove_mod(mod_slug):
    """Remove a mod from mods.yaml."""
    print(f"Removing mod: {mod_slug}")

    if not data.remove_mod(mod_slug):
        print(f"Error: Mod {mod_slug} not found")
        return 1

    print(f"Removed mod: {mod_slug}")
    return 0


def modpack_add(modpack_dir, mod_slug):
    """Add mod to modpack."""
    print(f"Adding {mod_slug} to modpack {modpack_dir}")

    # Check packwiz availability
    available, error = validation.check_packwiz_available()
    if not available:
        print(f"Error: {error}")
        return 1

    # Check if mod exists
    mod = data.get_mod(mod_slug)
    if mod is None:
        print(f"Error: Mod {mod_slug} not found. Add it first with 'mod-manager add'")
        return 1

    # Check if modpack exists
    modpack_path = packwiz.get_modpack_path(modpack_dir)
    if not modpack_path.exists():
        print(f"Error: Modpack directory {modpack_dir} not found")
        return 1

    # Install mod using packwiz
    source = "curseforge"  # Default, could be determined from mod data
    project_id = mod.get("curseforge_id")
    if not project_id:
        # Try modrinth
        source = "modrinth"
        project_id = mod.get("modrinth_id")

    result = packwiz.install_mod(modpack_dir, mod_slug, source, project_id)
    if result.returncode != 0:
        print(f"Error installing mod: {result.stderr}")
        return 1

    # Auto-detect side from packwiz file if not already set
    mod_file = packwiz.find_mod_file(modpack_dir, mod_slug)
    if mod_file:
        detected_side = packwiz.get_mod_side_from_packwiz(modpack_dir, mod_file)
        if detected_side and not mod.get("side"):
            # Update mod with detected side
            mod["side"] = detected_side
            data.set_mod(mod_slug, mod)
            print(f"  Auto-detected side: {detected_side}")

    # Update mods.yaml
    data.add_to_modpack(mod_slug, modpack_dir, "installed_in")

    # Copy custom configs if they exist
    copy_custom_configs(mod_slug, modpack_dir)

    print(f"Added {mod_slug} to {modpack_dir}")
    return 0


def modpack_remove(modpack_dir, mod_slug):
    """Remove mod from modpack."""
    print(f"Removing {mod_slug} from modpack {modpack_dir}")

    # Find mod file in modpack
    mod_file = packwiz.find_mod_file(modpack_dir, mod_slug)
    if not mod_file:
        print(f"Error: Mod {mod_slug} not found in modpack {modpack_dir}")
        return 1

    # Remove using packwiz
    result = packwiz.remove_mod(modpack_dir, mod_file)
    if result.returncode != 0:
        print(f"Error removing mod: {result.stderr}")
        return 1

    # Update mods.yaml
    data.remove_from_modpack(mod_slug, modpack_dir)

    print(f"Removed {mod_slug} from {modpack_dir}")
    return 0


def modpack_reject(modpack_dir, mod_slug, reason):
    """Mark mod as rejected in modpack."""
    print(f"Rejecting {mod_slug} from modpack {modpack_dir}: {reason}")

    # Check if mod exists
    mod = data.get_mod(mod_slug)
    if mod is None:
        print(f"Error: Mod {mod_slug} not found. Add it first with 'mod-manager add'")
        return 1

    # Update mods.yaml
    data.add_to_modpack(mod_slug, modpack_dir, "rejected_in", reason)

    print(f"Marked {mod_slug} as rejected in {modpack_dir}")
    return 0


def modpack_sync(modpack_dir):
    """Sync modpack with mods.yaml."""
    print(f"Syncing modpack {modpack_dir}")

    modpack_path = packwiz.get_modpack_path(modpack_dir)
    if not modpack_path.exists():
        print(f"Error: Modpack directory {modpack_dir} not found")
        return 1

    # Get all mods that should be installed
    mods_data = data.load_mods()
    mods_to_install = []
    for mod_slug, mod_info in mods_data.get("mods", {}).items():
        modpacks = mod_info.get("modpacks", {})
        if modpack_dir in modpacks.get("installed_in", []):
            mods_to_install.append(mod_slug)

    # Get all mods currently in modpack
    current_mods = packwiz.get_all_mods_in_modpack(modpack_dir)
    current_mod_slugs = set()
    for mod_info in current_mods:
        # Try to match by file name or mod name
        mod_file = mod_info["file"]
        # Extract potential slug from filename
        potential_slug = mod_file.replace(".pw.toml", "").lower()
        current_mod_slugs.add(potential_slug)

    # Add missing mods
    for mod_slug in mods_to_install:
        # Check if already installed (rough match)
        installed = any(
            mod_slug.lower() in slug or slug in mod_slug.lower()
            for slug in current_mod_slugs
        )
        if not installed:
            print(f"  Adding {mod_slug}...")
            modpack_add(modpack_dir, mod_slug)

    # Remove mods not in installed_in
    for mod_info in current_mods:
        mod_file = mod_info["file"]
        potential_slug = mod_file.replace(".pw.toml", "").lower()
        # Check if this mod should be removed
        should_remove = True
        for mod_slug in mods_to_install:
            if mod_slug.lower() in potential_slug or potential_slug in mod_slug.lower():
                should_remove = False
                break

        if should_remove:
            print(f"  Removing {mod_file}...")
            packwiz.remove_mod(modpack_dir, mod_file)

    print(f"Synced modpack {modpack_dir}")
    return 0


def modpack_create(modpack_dir, mc_version, modloader, modloader_version=None):
    """Create new modpack."""
    print(f"Creating modpack {modpack_dir} for {mc_version} {modloader}")

    # Check packwiz availability
    available, error = validation.check_packwiz_available()
    if not available:
        print(f"Error: {error}")
        return 1

    result = packwiz.create_modpack(modpack_dir, mc_version, modloader, modloader_version)
    if result.returncode != 0:
        print(f"Error creating modpack: {result.stderr}")
        return 1

    print(f"Created modpack {modpack_dir}")
    return 0


def modpack_export(modpack_dir):
    """Export modpack using packwiz."""
    print(f"Exporting modpack {modpack_dir}")

    result = packwiz.export_modpack(modpack_dir)
    if result.returncode != 0:
        print(f"Error exporting modpack: {result.stderr}")
        return 1

    print(f"Exported modpack {modpack_dir}")
    return 0


def generate_wiki(regenerate=False, mod_slug=None):
    """Generate wiki pages."""
    if mod_slug:
        print(f"Generating wiki page for {mod_slug}")
        mod = data.get_mod(mod_slug)
        if mod is None:
            print(f"Error: Mod {mod_slug} not found")
            return 1
        wiki.generate_wiki_page(mod_slug, mod)
        print(f"Generated wiki page for {mod_slug}")
    else:
        print("Generating all wiki pages")
        generated = wiki.generate_all_wiki_pages()
        print(f"Generated {len(generated)} wiki pages")
    return 0


def list_mods(modpack=None, mod_slug=None):
    """List mods or modpack information."""
    if modpack:
        print(f"Mods in modpack: {modpack}")
        mods_data = data.load_mods()
        mods_in_pack = []
        for slug, mod_info in mods_data.get("mods", {}).items():
            modpacks = mod_info.get("modpacks", {})
            if modpack in modpacks.get("installed_in", []):
                mods_in_pack.append((slug, mod_info))
        for slug, mod_info in mods_in_pack:
            name = mod_info.get("name", slug)
            side = mod_info.get("side", "unknown")
            print(f"  - {name} ({slug}) - {side}")
    elif mod_slug:
        print(f"Information for mod: {mod_slug}")
        mod = data.get_mod(mod_slug)
        if mod is None:
            print(f"Error: Mod {mod_slug} not found")
            return 1
        name = mod.get("name", mod_slug)
        description = mod.get("description", "")
        side = mod.get("side", "unknown")
        modpacks = mod.get("modpacks", {})
        installed_in = modpacks.get("installed_in", [])
        rejected_in = modpacks.get("rejected_in", [])

        print(f"Name: {name}")
        print(f"Description: {description}")
        print(f"Side: {side}")
        if installed_in:
            print(f"Installed in: {', '.join(installed_in)}")
        if rejected_in:
            print("Rejected in:")
            for r in rejected_in:
                if isinstance(r, dict):
                    print(f"  - {r.get('modpack')}: {r.get('reason', 'No reason')}")
    else:
        print("All mods:")
        mods_data = data.load_mods()
        for slug, mod_info in mods_data.get("mods", {}).items():
            name = mod_info.get("name", slug)
            side = mod_info.get("side", "unknown")
            print(f"  - {name} ({slug}) - {side}")
    return 0


def sync_from_modpack(modpack_dir):
    """Import from existing packwiz directory."""
    print(f"Syncing from modpack directory: {modpack_dir}")

    modpack_path = packwiz.get_modpack_path(modpack_dir)
    if not modpack_path.exists():
        print(f"Error: Modpack directory {modpack_dir} not found")
        return 1

    # Get all mods in modpack
    mod_files = packwiz.get_all_mods_in_modpack(modpack_dir)

    for mod_info in mod_files:
        mod_file = mod_info["file"]
        mod_name = mod_info["name"]
        mod_side = mod_info["side"]

        # Extract slug from filename
        mod_slug = mod_file.replace(".pw.toml", "").lower()

        # Check if mod exists in mods.yaml
        mod = data.get_mod(mod_slug)
        if not mod:
            # Create new mod entry
            mod_data = {
                "name": mod_name,
            }
            # Only set side if detected from packwiz
            if mod_side:
                mod_data["side"] = mod_side
            data.set_mod(mod_slug, mod_data)
            print(f"  Added new mod: {mod_slug} (side: {mod_side or 'unknown'})")
        else:
            # Update side if not already set (preserve manual settings)
            if not mod.get("side") and mod_side:
                mod["side"] = mod_side
                data.set_mod(mod_slug, mod)
                print(f"  Updated side for {mod_slug} to {mod_side}")
            elif mod.get("side") and mod_side:
                # Side already exists, don't overwrite (respects manual settings)
                pass

        # Add to installed_in
        data.add_to_modpack(mod_slug, modpack_dir, "installed_in")

    print(f"Synced {len(mod_files)} mods from {modpack_dir}")
    return 0


def copy_custom_configs(mod_slug, modpack_dir):
    """Copy custom config files from mods/<mod-slug>/config/ to modpack."""
    mod_dir = wiki.get_mod_dir(mod_slug)
    config_dir = mod_dir / "config"

    if not config_dir.exists():
        return

    modpack_path = packwiz.get_modpack_path(modpack_dir)
    modpack_config_dir = modpack_path / "config"
    modpack_config_dir.mkdir(parents=True, exist_ok=True)

    # Copy all files from mod config to modpack config
    for config_file in config_dir.iterdir():
        if config_file.is_file():
            dest_file = modpack_config_dir / config_file.name
            shutil.copy2(config_file, dest_file)
            print(f"  Copied config: {config_file.name}")

