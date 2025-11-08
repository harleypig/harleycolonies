#!/usr/bin/env python3
"""
Validation functions for mod-manager.
"""

import shutil
import subprocess
import yaml
from pathlib import Path


def check_packwiz_available():
    """Check if packwiz command is available."""
    packwiz_path = shutil.which("packwiz")
    if not packwiz_path:
        return False, "packwiz command not found in PATH"
    return True, None


def validate_yaml_structure(data):
    """Validate YAML structure for mods.yaml."""
    if not isinstance(data, dict):
        return False, "Root must be a dictionary"
    if "mods" not in data:
        return False, "Missing 'mods' key"
    if not isinstance(data["mods"], dict):
        return False, "'mods' must be a dictionary"
    return True, None


def validate_mod_data(mod_data):
    """Validate mod data structure."""
    if not isinstance(mod_data, dict):
        return False, "Mod data must be a dictionary"

    # Check optional fields
    if "side" in mod_data:
        if mod_data["side"] not in ["client", "server", "both"]:
            return False, f"Invalid side value: {mod_data['side']}"

    if "modpacks" in mod_data:
        modpacks = mod_data["modpacks"]
        if not isinstance(modpacks, dict):
            return False, "'modpacks' must be a dictionary"

        if "installed_in" in modpacks:
            if not isinstance(modpacks["installed_in"], list):
                return False, "'installed_in' must be a list"

        if "rejected_in" in modpacks:
            if not isinstance(modpacks["rejected_in"], list):
                return False, "'rejected_in' must be a list"
            for rejected in modpacks["rejected_in"]:
                if isinstance(rejected, dict):
                    if "modpack" not in rejected:
                        return False, "Rejected entry must have 'modpack' key"

    return True, None


def validate_mod_id(mod_slug, project_id=None, source="curseforge"):
    """Validate mod ID before packwiz operations."""
    # Basic validation - could be enhanced to check against APIs
    if project_id:
        if source == "curseforge" and not isinstance(project_id, int):
            return False, "CurseForge ID must be an integer"
    return True, None

