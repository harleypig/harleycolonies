#!/usr/bin/env python3
"""
Data management for mods.yaml.
"""

import yaml
from pathlib import Path


def get_repo_root():
    """Get repository root directory."""
    # bin/mod_manager/data.py -> repo root
    return Path(__file__).parent.parent.parent


def get_mods_yaml_path():
    """Get path to mods.yaml file."""
    return get_repo_root() / "modpacks" / "mods.yaml"


def load_mods():
    """Load mods from mods.yaml."""
    mods_path = get_mods_yaml_path()
    if not mods_path.exists():
        return {"mods": {}}

    with open(mods_path, "r") as f:
        return yaml.safe_load(f) or {"mods": {}}


def save_mods(data):
    """Save mods to mods.yaml."""
    mods_path = get_mods_yaml_path()
    mods_path.parent.mkdir(parents=True, exist_ok=True)

    with open(mods_path, "w") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False)


def get_mod(mod_slug):
    """Get mod by slug."""
    mods_data = load_mods()
    return mods_data.get("mods", {}).get(mod_slug)


def set_mod(mod_slug, mod_data):
    """Set mod data."""
    mods_data = load_mods()
    if "mods" not in mods_data:
        mods_data["mods"] = {}
    mods_data["mods"][mod_slug] = mod_data
    save_mods(mods_data)


def remove_mod(mod_slug):
    """Remove mod from mods.yaml."""
    mods_data = load_mods()
    if mod_slug in mods_data.get("mods", {}):
        del mods_data["mods"][mod_slug]
        save_mods(mods_data)
        return True
    return False


def get_modpack_list(mod_slug, modpack_dir):
    """Get list (installed_in or rejected_in) for mod in modpack."""
    mod = get_mod(mod_slug)
    if not mod:
        return None

    modpacks = mod.get("modpacks", {})
    if modpack_dir in modpacks.get("installed_in", []):
        return "installed_in"
    for rejected in modpacks.get("rejected_in", []):
        if isinstance(rejected, dict) and rejected.get("modpack") == modpack_dir:
            return "rejected_in"
    return None


def add_to_modpack(mod_slug, modpack_dir, list_type="installed_in", reason=None):
    """Add mod to modpack list (installed_in or rejected_in)."""
    mods_data = load_mods()
    if "mods" not in mods_data:
        mods_data["mods"] = {}

    if mod_slug not in mods_data["mods"]:
        mods_data["mods"][mod_slug] = {}

    mod = mods_data["mods"][mod_slug]
    if "modpacks" not in mod:
        mod["modpacks"] = {}

    modpacks = mod["modpacks"]

    if list_type == "installed_in":
        if "installed_in" not in modpacks:
            modpacks["installed_in"] = []
        if modpack_dir not in modpacks["installed_in"]:
            modpacks["installed_in"].append(modpack_dir)
        # Remove from rejected_in if present
        if "rejected_in" in modpacks:
            modpacks["rejected_in"] = [
                r
                for r in modpacks["rejected_in"]
                if not (
                    isinstance(r, dict) and r.get("modpack") == modpack_dir
                )
            ]
    elif list_type == "rejected_in":
        if "rejected_in" not in modpacks:
            modpacks["rejected_in"] = []
        # Check if already rejected
        existing = [
            r
            for r in modpacks["rejected_in"]
            if isinstance(r, dict) and r.get("modpack") == modpack_dir
        ]
        if not existing:
            modpacks["rejected_in"].append({
                "modpack": modpack_dir,
                "reason": reason or ""
            })
        elif reason:
            # Update reason if provided
            for r in modpacks["rejected_in"]:
                if isinstance(r, dict) and r.get("modpack") == modpack_dir:
                    r["reason"] = reason
        # Remove from installed_in if present
        if "installed_in" in modpacks:
            modpacks["installed_in"] = [
                d for d in modpacks["installed_in"] if d != modpack_dir
            ]

    save_mods(mods_data)


def remove_from_modpack(mod_slug, modpack_dir):
    """Remove mod from modpack (both installed_in and rejected_in)."""
    mods_data = load_mods()
    mod = mods_data.get("mods", {}).get(mod_slug)
    if not mod:
        return False

    modpacks = mod.get("modpacks", {})
    changed = False

    if "installed_in" in modpacks and modpack_dir in modpacks["installed_in"]:
        modpacks["installed_in"].remove(modpack_dir)
        changed = True

    if "rejected_in" in modpacks:
        original_len = len(modpacks["rejected_in"])
        modpacks["rejected_in"] = [
            r
            for r in modpacks["rejected_in"]
            if not (isinstance(r, dict) and r.get("modpack") == modpack_dir)
        ]
        if len(modpacks["rejected_in"]) < original_len:
            changed = True

    if changed:
        save_mods(mods_data)

    return changed


def _deep_compare_dicts(dict1, dict2):
    """Compare two dicts and return only fields that differ.
    
    Returns a dict with only the keys that have different values.
    For nested dicts, recursively compares and returns differences.
    """
    differences = {}
    
    # Check all keys in dict2
    for key, value2 in dict2.items():
        value1 = dict1.get(key)
        
        if isinstance(value2, dict) and isinstance(value1, dict):
            # Recursively compare nested dicts
            nested_diff = _deep_compare_dicts(value1, value2)
            if nested_diff:
                differences[key] = nested_diff
        elif value1 != value2:
            # Values differ, include in differences
            differences[key] = value2
    
    return differences


def merge_metadata(mod_slug, new_metadata, modpack_dir):
    """Merge metadata for a mod, storing canonical or version-specific.
    
    If mod has no existing metadata, store in modpacks/<mod-slug>/metadata.
    If mod has existing metadata, compare and store differences in
    modpacks/<mod-slug>/versions/<modpack-dir>/metadata.
    
    Note: curseforge_id and modrinth_id are stored at the top level,
    not in the metadata dict. 'side' is also stored at top level but
    treated as metadata for comparison purposes.
    """
    mods_data = load_mods()
    if "mods" not in mods_data:
        mods_data["mods"] = {}
    
    if mod_slug not in mods_data["mods"]:
        mods_data["mods"][mod_slug] = {}
    
    mod = mods_data["mods"][mod_slug]
    
    # Handle curseforge_id and modrinth_id at top level
    for id_key in ["curseforge_id", "modrinth_id"]:
        if id_key in new_metadata:
            new_id = new_metadata.pop(id_key)
            existing_id = mod.get(id_key)
            if not existing_id:
                # First time - store at top level
                mod[id_key] = new_id
            elif existing_id != new_id:
                # Different ID - store in version-specific
                if "versions" not in mod:
                    mod["versions"] = {}
                if modpack_dir not in mod["versions"]:
                    mod["versions"][modpack_dir] = {}
                if "metadata" not in mod["versions"][modpack_dir]:
                    mod["versions"][modpack_dir]["metadata"] = {}
                mod["versions"][modpack_dir]["metadata"][id_key] = new_id
    
    # Handle 'side' at top level (but treat as metadata for comparison)
    if "side" in new_metadata:
        new_side = new_metadata.pop("side")
        existing_side = mod.get("side")
        if not existing_side:
            # First time - store at top level
            mod["side"] = new_side
        elif existing_side != new_side:
            # Different side - store in version-specific
            if "versions" not in mod:
                mod["versions"] = {}
            if modpack_dir not in mod["versions"]:
                mod["versions"][modpack_dir] = {}
            if "metadata" not in mod["versions"][modpack_dir]:
                mod["versions"][modpack_dir]["metadata"] = {}
            mod["versions"][modpack_dir]["metadata"]["side"] = new_side
    
    # Handle remaining metadata fields
    existing_metadata = mod.get("metadata", {})
    
    if not existing_metadata and new_metadata:
        # First time seeing this mod - store as canonical metadata
        mod["metadata"] = new_metadata
        print(f"  Stored canonical metadata for {mod_slug}")
    elif new_metadata:
        # Compare with existing metadata
        differences = _deep_compare_dicts(existing_metadata, new_metadata)
        if differences:
            # Store differences in versions/<modpack-dir>/metadata
            if "versions" not in mod:
                mod["versions"] = {}
            if modpack_dir not in mod["versions"]:
                mod["versions"][modpack_dir] = {}
            if "metadata" not in mod["versions"][modpack_dir]:
                mod["versions"][modpack_dir]["metadata"] = {}
            # Merge differences into existing version metadata
            mod["versions"][modpack_dir]["metadata"].update(differences)
            print(f"  Stored version-specific metadata for {mod_slug} in {modpack_dir}")
    
    save_mods(mods_data)

