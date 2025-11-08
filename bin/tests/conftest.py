"""
Pytest configuration and fixtures for mod-manager tests.
"""

import os
import shutil
import tempfile
from pathlib import Path

import pytest
import yaml


@pytest.fixture(autouse=True)
def temp_repo(tmp_path, monkeypatch):
    """Create a temporary repository structure for testing.
    
    This fixture runs automatically for all tests to ensure they don't
    modify real repository files.
    """
    repo = tmp_path / "test_repo"
    repo.mkdir()

    # Create directory structure
    (repo / "mods").mkdir()
    (repo / "pages" / "mods").mkdir(parents=True)
    (repo / "bin" / "mod_manager").mkdir(parents=True)
    (repo / "bin").mkdir(parents=True, exist_ok=True)
    
    # Create wiki template file
    template_file = repo / "bin" / "wiki-page-template.j2"
    template_file.write_text("""---
title: {{ name }}
---

## {{ name }}

{{ description }}

### Side

{{ side }}

### Modpacks

{% if installed_in %}
This mod is installed in the following modpacks:

{% for modpack in installed_in %}
- {{ modpack }}
{% endfor %}
{% else %}
This mod is not currently installed in any modpacks.
{% endif %}
""")
    
    # Create mods index template file
    index_template_file = repo / "bin" / "mods-index-template.j2"
    index_template_file.write_text("""# Mods

This page lists all mods across all modpacks in mods/mods.yaml, grouped by category.

{% for category in sorted_categories %}
## {{ category }}

{% for mod_slug, display_name in categorized_mods[category] -%}
- [{{ display_name }}](mods/{{ mod_slug }}.md)
{% endfor %}

{% endfor %}
{% if uncategorized_mods %}
## Uncategorized

{% for mod_slug, display_name in uncategorized_mods -%}
- [{{ display_name }}](mods/{{ mod_slug }}.md)
{% endfor %}

{% endif %}
""")

    # Create empty mods.yaml
    mods_yaml = repo / "mods" / "mods.yaml"
    with open(mods_yaml, "w") as f:
        yaml.dump({"mods": {}}, f)

    # Add mpmanager to path
    import sys
    # When running from bin/, mpmanager is in bin/mpmanager
    # When running from repo root, mpmanager is in bin/mpmanager
    source_modpack_manager = Path(__file__).parent.parent / "mpmanager"
    if not source_modpack_manager.exists():
        # Try from repo root
        source_modpack_manager = Path(__file__).parent.parent.parent / "bin" / "mpmanager"
    if str(source_modpack_manager) not in sys.path:
        sys.path.insert(0, str(source_modpack_manager))

    # Monkey patch get_repo_root functions
    # The patch must be applied before modules are imported to prevent
    # any module-level code from using the real get_repo_root
    def mock_get_repo_root():
        return repo

    # Import modules and patch immediately
    import mpmanager.data
    import mpmanager.packwiz
    import mpmanager.wiki

    # Patch the functions - this will override any calls to get_repo_root
    # The monkeypatch will ensure all calls to get_repo_root() use the mock
    monkeypatch.setattr(mpmanager.data, "get_repo_root", mock_get_repo_root)
    monkeypatch.setattr(mpmanager.packwiz, "get_repo_root", mock_get_repo_root)
    monkeypatch.setattr(mpmanager.wiki, "get_repo_root", mock_get_repo_root)

    yield repo


@pytest.fixture
def sample_mod_data():
    """Sample mod data for testing."""
    return {
        "name": "Test Mod",
        "description": "A test mod",
        "side": "both",
        "curseforge_id": 12345,
        "modpacks": {
            "installed_in": ["test-modpack-1.20.1"],
        },
    }


@pytest.fixture
def sample_modpack_dir(temp_repo):
    """Create a sample modpack directory."""
    modpack_dir = temp_repo / "test-modpack-1.20.1"
    modpack_dir.mkdir()
    (modpack_dir / "mods").mkdir()

    # Create pack.toml
    pack_toml = modpack_dir / "pack.toml"
    pack_toml.write_text("""name = "Test Modpack"
author = "Test"
version = "1.0.0"
pack-format = "packwiz:1.1.0"

[versions]
minecraft = "1.20.1"
forge = "47.2.0"
""")

    return modpack_dir


@pytest.fixture
def sample_mod_toml(temp_repo, sample_modpack_dir):
    """Create a sample mod .pw.toml file."""
    mod_toml = sample_modpack_dir / "mods" / "test-mod.pw.toml"
    mod_toml.write_text("""name = "Test Mod"
filename = "test-mod-1.20.1.jar"
side = "both"

[download]
hash-format = "sha1"
hash = "testhash"
mode = "metadata:curseforge"

[update]
[update.curseforge]
file-id = 12345
project-id = 12345

[metadata]
[metadata.curseforge]
website = "https://www.curseforge.com/minecraft/mc-mods/test-mod"
""")
    return mod_toml

