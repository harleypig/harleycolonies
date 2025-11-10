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

    # Check optional fields (top-level 'side' deprecated; no longer validated)

    # Validate metadata structure if present
    if "metadata" in mod_data:
        metadata = mod_data["metadata"]
        if not isinstance(metadata, dict):
            return False, "'metadata' must be a dictionary"
        # categories: list[str]
        if "categories" in metadata:
            categories = metadata["categories"]
            if not isinstance(categories, list) or not all(isinstance(c, str) for c in categories):
                return False, "'metadata.categories' must be a list of strings"
        # tags: list[str]; recommended to include exactly one of client/server/both
        if "tags" in metadata:
            tags = metadata["tags"]
            if not isinstance(tags, list) or not all(isinstance(t, str) for t in tags):
                return False, "'metadata.tags' must be a list of strings"
        # integrations: list[str]
        if "integrations" in metadata:
            integrations = metadata["integrations"]
            if not isinstance(integrations, list) or not all(isinstance(i, str) for i in integrations):
                return False, "'metadata.integrations' must be a list of strings"
        # dependencies: {required?: list[str], optional?: list[str]}
        if "dependencies" in metadata:
            deps = metadata["dependencies"]
            if not isinstance(deps, dict):
                return False, "'metadata.dependencies' must be a dictionary"
            if "required" in deps:
                req = deps["required"]
                if not isinstance(req, list) or not all(isinstance(i, str) for i in req):
                    return False, "'metadata.dependencies.required' must be a list of strings"
            if "optional" in deps:
                opt = deps["optional"]
                if not isinstance(opt, list) or not all(isinstance(i, str) for i in opt):
                    return False, "'metadata.dependencies.optional' must be a list of strings"

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

