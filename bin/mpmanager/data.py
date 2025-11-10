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


def get_modpack_info_path(modpack_dir: str) -> Path:
    """Get path to per-modpack info.yaml."""
    return get_repo_root() / modpack_dir / "info.yaml"


def get_modpack_state_path(modpack_dir: str) -> Path:
    """Get path to per-modpack mods.yaml (state)."""
    return get_repo_root() / modpack_dir / "mods.yaml"


def load_modpack_info(modpack_dir: str) -> dict:
    """Load per-modpack info.yaml."""
    path = get_modpack_info_path(modpack_dir)
    if not path.exists():
        return {}
    with open(path, "r") as f:
        return yaml.safe_load(f) or {}


def save_modpack_info(modpack_dir: str, info: dict) -> None:
    """Save per-modpack info.yaml."""
    path = get_modpack_info_path(modpack_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        yaml.dump(info, f, default_flow_style=False, sort_keys=False)


def load_modpack_state(modpack_dir: str) -> dict:
    """Load per-modpack mods.yaml state: {mods: {slug: {status, reason?}}}."""
    path = get_modpack_state_path(modpack_dir)
    if not path.exists():
        return {"mods": {}}
    with open(path, "r") as f:
        data = yaml.safe_load(f) or {}
    if "mods" not in data or not isinstance(data["mods"], dict):
        data["mods"] = {}
    return data


def save_modpack_state(modpack_dir: str, state: dict) -> None:
    """Save per-modpack mods.yaml state."""
    path = get_modpack_state_path(modpack_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        yaml.dump(state, f, default_flow_style=False, sort_keys=False)


def set_mod_installed_in_modpack(mod_slug: str, modpack_dir: str) -> None:
    """Mark a mod as installed in a specific modpack."""
    state = load_modpack_state(modpack_dir)
    mods = state.setdefault("mods", {})
    entry = mods.get(mod_slug, {})
    entry["status"] = "installed"
    entry.pop("reason", None)
    mods[mod_slug] = entry
    save_modpack_state(modpack_dir, state)


def set_mod_rejected_in_modpack(mod_slug: str, modpack_dir: str, reason: str = "") -> None:
    """Mark a mod as rejected in a specific modpack with optional reason."""
    state = load_modpack_state(modpack_dir)
    mods = state.setdefault("mods", {})
    entry = mods.get(mod_slug, {})
    entry["status"] = "rejected"
    entry["reason"] = reason or ""
    mods[mod_slug] = entry
    save_modpack_state(modpack_dir, state)


def remove_mod_from_modpack_state(mod_slug: str, modpack_dir: str) -> bool:
    """Remove a mod from a modpack's installed/rejected lists."""
    state = load_modpack_state(modpack_dir)
    mods = state.get("mods", {})
    if mod_slug in mods:
        del mods[mod_slug]
        save_modpack_state(modpack_dir, state)
        return True
    return False


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
    """Get list (installed_in or rejected_in) for mod in modpack (compat shim)."""
    state = load_modpack_state(modpack_dir)
    entry = state.get("mods", {}).get(mod_slug)
    if not entry:
        return None
    status = entry.get("status")
    if status == "installed":
        return "installed_in"
    if status == "rejected":
        return "rejected_in"
    return None


def add_to_modpack(mod_slug, modpack_dir, list_type="installed_in", reason=None):
    """Add mod to modpack list (installed_in or rejected_in) in per-modpack state."""
    if list_type == "installed_in":
        set_mod_installed_in_modpack(mod_slug, modpack_dir)
    elif list_type == "rejected_in":
        set_mod_rejected_in_modpack(mod_slug, modpack_dir, reason or "")
    else:
        set_mod_installed_in_modpack(mod_slug, modpack_dir)


def remove_from_modpack(mod_slug, modpack_dir):
    """Remove mod from modpack (both installed and rejected) in per-modpack state."""
    return remove_mod_from_modpack_state(mod_slug, modpack_dir)


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
    not in the metadata dict.
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
    
    # Remove any stray 'side' from new_metadata; side is tracked via tags now
    if "side" in new_metadata:
        new_metadata.pop("side", None)
    
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


def _merge_string_lists(local_list, remote_list):
    """Union of two string lists preserving local order and uniqueness."""
    if not isinstance(local_list, list):
        local_list = []
    if not isinstance(remote_list, list):
        remote_list = []
    seen = set()
    merged = []
    # keep locals first
    for item in local_list:
        if isinstance(item, str):
            key = item
        else:
            key = str(item)
        if key not in seen:
            seen.add(key)
            merged.append(item)
    # add remotes not present
    for item in remote_list:
        if isinstance(item, str):
            key = item
        else:
            key = str(item)
        if key not in seen:
            seen.add(key)
            merged.append(item)
    return merged


def update_mod_from_remote(mod_slug, remote_metadata, modpack_dir, force_remote=False):
    """Update a mod's metadata from remotely retrieved values.
    
    Rules:
      - categories: overwrite canonical categories with remote (when present)
      - integrations: if provided remotely
          - default: union(local, remote)
          - force_remote: replace with remote
      - dependencies.{required, optional}: if provided remotely
          - default: union per-list
          - force_remote: replace with remote dict/lists
      - other metadata fields are merged using merge_metadata (version-aware)
    """
    mods_data = load_mods()
    if "mods" not in mods_data:
        mods_data["mods"] = {}
    if mod_slug not in mods_data["mods"]:
        mods_data["mods"][mod_slug] = {}
    mod = mods_data["mods"][mod_slug]
    if "metadata" not in mod:
        mod["metadata"] = {}
    metadata = mod["metadata"]

    # Handle categories: overwrite if present in remote
    if "categories" in remote_metadata:
        remote_categories = remote_metadata.get("categories") or []
        # Ensure list type
        if not isinstance(remote_categories, list):
            remote_categories = [remote_categories] if remote_categories else []
        metadata["categories"] = remote_categories
        # Remove from remote_metadata before delegating to merge_metadata
        remote_metadata = {k: v for k, v in remote_metadata.items() if k != "categories"}

    # Handle integrations (optional)
    if "integrations" in remote_metadata:
        remote_integrations = remote_metadata.get("integrations") or []
        local_integrations = metadata.get("integrations", [])
        if force_remote:
            metadata["integrations"] = remote_integrations
        else:
            metadata["integrations"] = _merge_string_lists(local_integrations, remote_integrations)
        # Remove from remote_metadata to avoid version-diff handling
        remote_metadata = {k: v for k, v in remote_metadata.items() if k != "integrations"}

    # Handle dependencies (optional)
    # Handle side from TOML into tags with precedence to existing entry
    if "side" in remote_metadata:
        remote_side = remote_metadata.get("side")
        # sanitize remote_side
        allowed_sides = {"client", "server", "both"}
        if isinstance(remote_side, str) and remote_side in allowed_sides:
            tags = metadata.get("tags", [])
            if not isinstance(tags, list):
                tags = []
            # check if local already has a side tag; if so, keep local (entry precedence)
            local_side = None
            for s in allowed_sides:
                if s in tags:
                    local_side = s
                    break
            if not local_side:
                # add remote side tag
                tags.append(remote_side)
                metadata["tags"] = tags
        # Remove from remote_metadata
        remote_metadata = {k: v for k, v in remote_metadata.items() if k != "side"}
    if "dependencies" in remote_metadata and isinstance(remote_metadata.get("dependencies"), dict):
        remote_deps = remote_metadata.get("dependencies") or {}
        local_deps = metadata.get("dependencies", {})
        if force_remote:
            metadata["dependencies"] = {
                "required": list(remote_deps.get("required", []) or []),
                "optional": list(remote_deps.get("optional", []) or []),
            }
        else:
            merged_required = _merge_string_lists(local_deps.get("required", []), remote_deps.get("required", []))
            merged_optional = _merge_string_lists(local_deps.get("optional", []), remote_deps.get("optional", []))
            if merged_required or "required" in local_deps:
                # preserve key presence if it existed
                local_deps["required"] = merged_required
            if merged_optional or "optional" in local_deps:
                local_deps["optional"] = merged_optional
            metadata["dependencies"] = local_deps
        # Remove from remote_metadata to avoid version-diff handling
        remote_metadata = {k: v for k, v in remote_metadata.items() if k != "dependencies"}

    # Delegate remaining fields (ids, side, website/wiki/issues/source, etc.)
    merge_metadata(mod_slug, dict(remote_metadata), modpack_dir)

    # Ensure our updates are persisted (merge_metadata saves, but we altered metadata above)
    # Reload and write back the updated mod metadata
    mods_data = load_mods()
    if "mods" not in mods_data:
        mods_data["mods"] = {}
    if mod_slug not in mods_data["mods"]:
        mods_data["mods"][mod_slug] = {}
    current = mods_data["mods"][mod_slug]
    current.setdefault("metadata", {})
    # sync categories/integrations/dependencies we may have changed
    for key in ("categories", "integrations", "dependencies"):
        if key in metadata:
            current["metadata"][key] = metadata[key]
    save_mods(mods_data)


def list_modpacks_with_mod(mod_slug: str) -> list:
    """Return list of modpack dirs that have this mod installed per state files."""
    root = get_repo_root()
    modpacks = []
    # Scan top-level directories only
    for child in root.iterdir():
        if not child.is_dir():
            continue
        # skip known non-modpack dirs
        if child.name in ("bin", "pages", "modpacks", ".git", ".venv"):
            continue
        state_path = child / "mods.yaml"
        if not state_path.exists():
            continue
        try:
            with open(state_path, "r") as f:
                state = yaml.safe_load(f) or {}
            mods = state.get("mods", {})
            entry = mods.get(mod_slug)
            if isinstance(entry, dict) and entry.get("status") == "installed":
                modpacks.append(child.name)
        except Exception:
            continue
    return sorted(modpacks)

