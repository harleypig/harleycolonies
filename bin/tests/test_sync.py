"""
Tests for sync functionality.
"""

from unittest.mock import MagicMock, patch

import pytest

from mpmanager import commands, data, packwiz


@patch("mpmanager.commands.packwiz")
def test_sync_from_modpack(temp_repo, sample_modpack_dir, sample_mod_toml):
    """Test syncing from existing modpack."""
    import mpmanager.commands as cmd_module
    cmd_module.packwiz.get_modpack_path = lambda d: temp_repo / d

    cmd_module.packwiz.get_all_mods_in_modpack.return_value = [
        {
            "file": "test-mod.pw.toml",
            "name": "Test Mod",
            "side": "both",
        }
    ]
    
    # Mock TOML data and metadata extraction
    cmd_module.packwiz.get_mod_toml_data.return_value = {
        "name": "Test Mod",
        "side": "both",
        "update": {
            "curseforge": {
                "project-id": 12345
            }
        },
        "metadata": {
            "curseforge": {
                "website": "https://www.curseforge.com/minecraft/mc-mods/test-mod"
            }
        }
    }
    cmd_module.packwiz.extract_metadata_from_toml.return_value = {
        "curseforge_id": 12345,
        "side": "both",
        "website": "https://www.curseforge.com/minecraft/mc-mods/test-mod"
    }

    result = commands.sync_from_modpack("test-modpack-1.20.1")
    assert result == 0

    # Check that mod was added
    mod = data.get_mod("test-mod")
    assert mod is not None
    assert mod["name"] == "Test Mod"
    assert mod["side"] == "both"

    # Check that mod was added to installed_in
    assert "test-modpack-1.20.1" in mod["modpacks"]["installed_in"]
    
    # Check that metadata was extracted
    assert mod.get("curseforge_id") == 12345
    assert "metadata" in mod


@patch("mpmanager.commands.packwiz")
def test_sync_from_modpack_preserves_side(temp_repo, sample_modpack_dir):
    """Test that sync preserves existing side setting."""
    import mpmanager.commands as cmd_module
    cmd_module.packwiz.get_modpack_path = lambda d: temp_repo / d

    # Add mod with manual side setting
    commands.add_mod("test-mod", side="client")

    cmd_module.packwiz.get_all_mods_in_modpack.return_value = [
        {
            "file": "test-mod.pw.toml",
            "name": "Test Mod",
            "side": "both",  # Different from manual setting
        }
    ]
    
    # Mock TOML data
    cmd_module.packwiz.get_mod_toml_data.return_value = {
        "name": "Test Mod",
        "side": "both"
    }
    cmd_module.packwiz.extract_metadata_from_toml.return_value = {
        "side": "both"
    }

    result = commands.sync_from_modpack("test-modpack-1.20.1")
    assert result == 0

    # Check that side was preserved (not overwritten)
    mod = data.get_mod("test-mod")
    assert mod["side"] == "client"  # Should not be overwritten
    
    # Check that version-specific side was stored
    assert "versions" in mod
    assert "test-modpack-1.20.1" in mod["versions"]
    assert mod["versions"]["test-modpack-1.20.1"]["metadata"]["side"] == "both"


@patch("mpmanager.commands.packwiz")
def test_sync_from_modpack_updates_missing_side(temp_repo, sample_modpack_dir):
    """Test that sync updates side if not already set."""
    import mpmanager.commands as cmd_module
    cmd_module.packwiz.get_modpack_path = lambda d: temp_repo / d

    # Add mod without side
    commands.add_mod("test-mod")

    cmd_module.packwiz.get_all_mods_in_modpack.return_value = [
        {
            "file": "test-mod.pw.toml",
            "name": "Test Mod",
            "side": "both",
        }
    ]
    
    # Mock TOML data
    cmd_module.packwiz.get_mod_toml_data.return_value = {
        "name": "Test Mod",
        "side": "both"
    }
    cmd_module.packwiz.extract_metadata_from_toml.return_value = {
        "side": "both"
    }

    result = commands.sync_from_modpack("test-modpack-1.20.1")
    assert result == 0

    # Check that side was updated
    mod = data.get_mod("test-mod")
    assert mod["side"] == "both"

