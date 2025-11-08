#!/usr/bin/env python3
"""
Packwiz integration for modpack operations.
"""

import subprocess
import sys
from pathlib import Path
from tomlkit import parse, dumps


def _convert_tomlkit_to_primitive(value):
    """Convert tomlkit objects to plain Python primitives.
    
    Recursively processes dicts, lists, and tomlkit objects to ensure
    all values are plain Python types that can be safely serialized
    to YAML.
    """
    # Check if value is a tomlkit object (has unwrap method)
    if hasattr(value, "unwrap"):
        return _convert_tomlkit_to_primitive(value.unwrap())
    
    # Handle dicts
    if isinstance(value, dict):
        return {
            _convert_tomlkit_to_primitive(k): _convert_tomlkit_to_primitive(v)
            for k, v in value.items()
        }
    
    # Handle lists
    if isinstance(value, list):
        return [_convert_tomlkit_to_primitive(item) for item in value]
    
    # Return primitive types as-is
    return value


def get_repo_root():
    """Get repository root directory."""
    return Path(__file__).parent.parent.parent


def get_modpack_path(modpack_dir):
    """Get path to modpack directory."""
    return get_repo_root() / modpack_dir


def run_packwiz(command, modpack_dir, *args, check=True):
    """Run packwiz command in modpack directory."""
    modpack_path = get_modpack_path(modpack_dir)
    if not modpack_path.exists():
        raise FileNotFoundError(f"Modpack directory not found: {modpack_dir}")

    cmd = ["packwiz"] + command.split() + list(args)
    result = subprocess.run(
        cmd,
        cwd=str(modpack_path),
        capture_output=True,
        text=True,
        check=check,
    )
    return result


def install_mod(modpack_dir, mod_slug, source="curseforge", project_id=None):
    """Install mod using packwiz."""
    modpack_path = get_modpack_path(modpack_dir)

    if source == "curseforge":
        if not project_id:
            # Try to get from mods.yaml
            from mpmanager import data

            mod = data.get_mod(mod_slug)
            if mod and "curseforge_id" in mod:
                project_id = mod["curseforge_id"]
            else:
                # Try to search by name
                cmd = ["packwiz", "curseforge", "install", mod_slug]
                result = subprocess.run(
                    cmd,
                    cwd=str(modpack_path),
                    capture_output=True,
                    text=True,
                )
                return result
        cmd = ["packwiz", "curseforge", "install", str(project_id)]
    elif source == "modrinth":
        if not project_id:
            cmd = ["packwiz", "modrinth", "install", mod_slug]
        else:
            cmd = ["packwiz", "modrinth", "install", project_id]
    else:
        raise ValueError(f"Unknown source: {source}")

    result = subprocess.run(
        cmd,
        cwd=str(modpack_path),
        capture_output=True,
        text=True,
    )
    return result


def remove_mod(modpack_dir, mod_file):
    """Remove mod from modpack using packwiz."""
    modpack_path = get_modpack_path(modpack_dir)
    cmd = ["packwiz", "remove", mod_file]

    result = subprocess.run(
        cmd,
        cwd=str(modpack_path),
        capture_output=True,
        text=True,
    )
    return result


def export_modpack(modpack_dir):
    """Export modpack using packwiz."""
    modpack_path = get_modpack_path(modpack_dir)
    cmd = ["packwiz", "curseforge", "export"]

    result = subprocess.run(
        cmd,
        cwd=str(modpack_path),
        capture_output=True,
        text=True,
    )
    return result


def get_mod_side_from_packwiz(modpack_dir, mod_file):
    """Get mod side from packwiz .pw.toml file."""
    modpack_path = get_modpack_path(modpack_dir)
    mod_toml_path = modpack_path / "mods" / mod_file

    if not mod_toml_path.exists():
        return None

    try:
        with open(mod_toml_path, "r") as f:
            data = parse(f.read())
            side = data.get("side")
            return _convert_tomlkit_to_primitive(side) if side is not None else None
    except Exception:
        return None


def find_mod_file(modpack_dir, mod_slug):
    """Find packwiz .pw.toml file for mod in modpack."""
    modpack_path = get_modpack_path(modpack_dir)
    mods_dir = modpack_path / "mods"

    if not mods_dir.exists():
        return None

    # Try exact match first
    exact_match = mods_dir / f"{mod_slug}.pw.toml"
    if exact_match.exists():
        return exact_match.name

    # Search for files containing mod_slug
    for mod_file in mods_dir.glob("*.pw.toml"):
        if mod_slug.lower() in mod_file.stem.lower():
            return mod_file.name

    return None


def create_modpack(modpack_dir, mc_version, modloader, modloader_version=None):
    """Create new modpack using packwiz."""
    modpack_path = get_modpack_path(modpack_dir)
    modpack_path.mkdir(parents=True, exist_ok=True)

    # Initialize packwiz
    cmd = ["packwiz", "init", "--name", modpack_dir, "--author", "HarleyColonies"]
    result = subprocess.run(
        cmd,
        cwd=str(modpack_path),
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        return result

    # Update pack.toml with versions
    try:
        pack_toml = modpack_path / "pack.toml"
        with open(pack_toml, "r") as f:
            data = parse(f.read())

        if "versions" not in data:
            data["versions"] = {}

        data["versions"]["minecraft"] = mc_version
        data["versions"][modloader] = modloader_version or "latest"

        with open(pack_toml, "w") as f:
            f.write(dumps(data))
    except Exception as e:
        print(f"Warning: Could not update pack.toml: {e}")

    return result


def extract_metadata_from_toml(toml_data):
    """Extract metadata from packwiz TOML data.
    
    Returns a dict with extracted metadata fields:
    - curseforge_id: from update.curseforge.project-id
    - modrinth_id: from update.modrinth.project-id (if present)
    - side: from top-level 'side' field
    - website: from metadata.curseforge.website or metadata.modrinth.url
    - wiki: from metadata.curseforge.wiki
    - issues: from metadata.curseforge.issues
    - source: from metadata.curseforge.source
    - categories: from metadata.curseforge.categories
    """
    metadata = {}
    
    # Extract side (treat as metadata even though it's separate in TOML)
    side = toml_data.get("side")
    if side is not None:
        metadata["side"] = _convert_tomlkit_to_primitive(side)
    
    # Extract CurseForge project ID
    update_cf = toml_data.get("update", {}).get("curseforge", {})
    if update_cf:
        project_id = update_cf.get("project-id")
        if project_id is not None:
            metadata["curseforge_id"] = _convert_tomlkit_to_primitive(project_id)
    
    # Extract Modrinth project ID
    update_mr = toml_data.get("update", {}).get("modrinth", {})
    if update_mr:
        project_id = update_mr.get("project-id")
        if project_id is not None:
            metadata["modrinth_id"] = _convert_tomlkit_to_primitive(project_id)
    
    # Extract CurseForge metadata
    meta_cf = toml_data.get("metadata", {}).get("curseforge", {})
    if meta_cf:
        for key in ["website", "wiki", "issues", "source"]:
            value = meta_cf.get(key)
            if value is not None:
                metadata[key] = _convert_tomlkit_to_primitive(value)
        
        categories = meta_cf.get("categories")
        if categories is not None:
            metadata["categories"] = _convert_tomlkit_to_primitive(categories)
    
    # Extract Modrinth metadata
    meta_mr = toml_data.get("metadata", {}).get("modrinth", {})
    if meta_mr:
        # Modrinth uses "url" instead of "website"
        url = meta_mr.get("url")
        if url is not None and "website" not in metadata:
            metadata["website"] = _convert_tomlkit_to_primitive(url)
    
    return metadata


def update_mod_side_in_toml(modpack_dir, mod_file, new_side):
    """Update the 'side' field in a packwiz TOML file."""
    modpack_path = get_modpack_path(modpack_dir)
    mod_toml_path = modpack_path / "mods" / mod_file
    
    if not mod_toml_path.exists():
        return False
    
    try:
        with open(mod_toml_path, "r") as f:
            toml_data = parse(f.read())
        
        # Update the side field
        toml_data["side"] = new_side
        
        with open(mod_toml_path, "w") as f:
            f.write(dumps(toml_data))
        
        return True
    except Exception as e:
        print(f"Error updating TOML file {mod_file}: {e}", file=sys.stderr)
        return False


def get_mod_toml_data(modpack_dir, mod_file):
    """Get full TOML data for a mod file."""
    modpack_path = get_modpack_path(modpack_dir)
    mod_toml_path = modpack_path / "mods" / mod_file
    
    if not mod_toml_path.exists():
        return None
    
    try:
        with open(mod_toml_path, "r") as f:
            return parse(f.read())
    except Exception:
        return None


def get_all_mods_in_modpack(modpack_dir):
    """Get list of all mod files in modpack."""
    modpack_path = get_modpack_path(modpack_dir)
    mods_dir = modpack_path / "mods"

    if not mods_dir.exists():
        return []

    mod_files = []
    for mod_file in mods_dir.glob("*.pw.toml"):
        try:
            with open(mod_file, "r") as f:
                data = parse(f.read())
                mod_name = data.get("name", mod_file.stem)
                mod_side = data.get("side")
                mod_files.append({
                    "file": mod_file.name,
                    "name": _convert_tomlkit_to_primitive(mod_name),
                    "side": _convert_tomlkit_to_primitive(mod_side) if mod_side is not None else None,
                })
        except Exception:
            continue

    return mod_files

