"""
Tests for sync functionality.
"""

from unittest.mock import MagicMock, patch

import pytest

from mod_manager import commands, data, packwiz


@patch("mod_manager.commands.packwiz")
def test_sync_from_modpack(temp_repo, sample_modpack_dir, sample_mod_toml):
    """Test syncing from existing modpack."""
    import mod_manager.commands as cmd_module
    cmd_module.packwiz.get_modpack_path = lambda d: temp_repo / d

    cmd_module.packwiz.get_all_mods_in_modpack.return_value = [
        {
            "file": "test-mod.pw.toml",
            "name": "Test Mod",
            "side": "both",
        }
    ]

    result = commands.sync_from_modpack("test-modpack-1.20.1")
    assert result == 0

    # Check that mod was added
    mod = data.get_mod("test-mod")
    assert mod is not None
    assert mod["name"] == "Test Mod"
    assert mod["side"] == "both"

    # Check that mod was added to installed_in
    assert "test-modpack-1.20.1" in mod["modpacks"]["installed_in"]


@patch("mod_manager.commands.packwiz")
def test_sync_from_modpack_preserves_side(temp_repo, sample_modpack_dir):
    """Test that sync preserves existing side setting."""
    import mod_manager.commands as cmd_module
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

    result = commands.sync_from_modpack("test-modpack-1.20.1")
    assert result == 0

    # Check that side was preserved
    mod = data.get_mod("test-mod")
    assert mod["side"] == "client"  # Should not be overwritten


@patch("mod_manager.commands.packwiz")
def test_sync_from_modpack_updates_missing_side(temp_repo, sample_modpack_dir):
    """Test that sync updates side if not already set."""
    import mod_manager.commands as cmd_module
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

    result = commands.sync_from_modpack("test-modpack-1.20.1")
    assert result == 0

    # Check that side was updated
    mod = data.get_mod("test-mod")
    assert mod["side"] == "both"

