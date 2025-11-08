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
    return get_repo_root() / "mods" / "mods.yaml"


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

