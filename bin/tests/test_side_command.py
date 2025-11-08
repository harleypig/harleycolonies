"""
Tests for side command functionality.
"""

from unittest.mock import patch

import pytest

from mpmanager import commands, data, packwiz


def test_update_mod_side_canonical(temp_repo, sample_modpack_dir, sample_mod_toml):
    """Test updating canonical side."""
    # Add mod with side
    commands.add_mod("test-mod", side="both")
    data.add_to_modpack("test-mod", "test-modpack-1.20.1", "installed_in")
    
    # Mock packwiz functions
    with patch("mpmanager.commands.packwiz") as mock_packwiz:
        mock_packwiz.get_modpack_path = lambda d: temp_repo / d
        mock_packwiz.find_mod_file.return_value = "test-mod.pw.toml"
        mock_packwiz.update_mod_side_in_toml.return_value = True
        
        result = commands.update_mod_side("test-mod", "client")
        assert result == 0
        
        mod = data.get_mod("test-mod")
        assert mod["side"] == "client"
        
        # Should have tried to update TOML
        mock_packwiz.update_mod_side_in_toml.assert_called()


def test_update_mod_side_version_specific(temp_repo, sample_modpack_dir, sample_mod_toml):
    """Test updating version-specific side."""
    # Add mod with canonical side
    commands.add_mod("test-mod", side="both")
    data.add_to_modpack("test-mod", "test-modpack-1.20.1", "installed_in")
    
    # Mock packwiz functions
    with patch("mpmanager.commands.packwiz") as mock_packwiz:
        mock_packwiz.get_modpack_path = lambda d: temp_repo / d
        mock_packwiz.find_mod_file.return_value = "test-mod.pw.toml"
        mock_packwiz.update_mod_side_in_toml.return_value = True
        
        result = commands.update_mod_side("test-mod", "client", modpack_dir="test-modpack-1.20.1")
        assert result == 0
        
        mod = data.get_mod("test-mod")
        # Canonical side should remain unchanged
        assert mod["side"] == "both"
        
        # Version-specific side should be updated
        assert "versions" in mod
        assert "test-modpack-1.20.1" in mod["versions"]
        assert mod["versions"]["test-modpack-1.20.1"]["metadata"]["side"] == "client"
        
        # Should have updated TOML
        mock_packwiz.update_mod_side_in_toml.assert_called_once()


def test_update_mod_side_not_found(temp_repo):
    """Test updating side for non-existent mod."""
    result = commands.update_mod_side("nonexistent", "both")
    assert result == 1


def test_update_mod_side_canonical_updates_all_modpacks(temp_repo, sample_modpack_dir):
    """Test that updating canonical side updates TOML in all modpacks."""
    # Add mod to multiple modpacks
    commands.add_mod("test-mod", side="both")
    data.add_to_modpack("test-mod", "test-modpack-1.20.1", "installed_in")
    data.add_to_modpack("test-mod", "test-modpack-1.21.1", "installed_in")
    
    # Create second modpack
    modpack2 = temp_repo / "test-modpack-1.21.1"
    modpack2.mkdir()
    (modpack2 / "mods").mkdir()
    (modpack2 / "mods" / "test-mod.pw.toml").write_text('name = "Test Mod"\nside = "both"\n')
    
    with patch("mpmanager.commands.packwiz") as mock_packwiz:
        mock_packwiz.get_modpack_path = lambda d: temp_repo / d
        mock_packwiz.find_mod_file.return_value = "test-mod.pw.toml"
        mock_packwiz.update_mod_side_in_toml.return_value = True
        
        result = commands.update_mod_side("test-mod", "client")
        assert result == 0
        
        # Should have updated TOML in both modpacks
        assert mock_packwiz.update_mod_side_in_toml.call_count == 2


def test_update_mod_side_skips_version_specific(temp_repo, sample_modpack_dir):
    """Test that canonical side update skips modpacks with version-specific side."""
    # Add mod with version-specific side
    commands.add_mod("test-mod", side="both")
    data.add_to_modpack("test-mod", "test-modpack-1.20.1", "installed_in")
    
    # Set version-specific side
    mods_data = data.load_mods()
    mod = mods_data["mods"]["test-mod"]
    mod["versions"] = {
        "test-modpack-1.20.1": {
            "metadata": {
                "side": "server"
            }
        }
    }
    data.save_mods(mods_data)
    
    with patch("mpmanager.commands.packwiz") as mock_packwiz:
        mock_packwiz.get_modpack_path = lambda d: temp_repo / d
        mock_packwiz.find_mod_file.return_value = "test-mod.pw.toml"
        mock_packwiz.update_mod_side_in_toml.return_value = True
        
        result = commands.update_mod_side("test-mod", "client")
        assert result == 0
        
        # Should not have updated TOML (version-specific side exists)
        mock_packwiz.update_mod_side_in_toml.assert_not_called()

