"""
Tests for TOML file updates.
"""

from pathlib import Path

import pytest

from mpmanager import packwiz


def test_update_mod_side_in_toml(temp_repo, sample_modpack_dir, sample_mod_toml):
    """Test updating side in TOML file."""
    # Ensure the modpack directory exists
    modpack_dir = temp_repo / "test-modpack-1.20.1"
    modpack_dir.mkdir(exist_ok=True)
    (modpack_dir / "mods").mkdir(exist_ok=True)
    
    # Create the TOML file
    mod_toml = modpack_dir / "mods" / "test-mod.pw.toml"
    mod_toml.write_text('name = "Test Mod"\nside = "both"\n')
    
    result = packwiz.update_mod_side_in_toml("test-modpack-1.20.1", "test-mod.pw.toml", "client")
    assert result is True
    
    # Read the file and check side was updated
    content = mod_toml.read_text()
    assert 'side = "client"' in content
    assert 'side = "both"' not in content


def test_update_mod_side_in_toml_not_found(temp_repo, sample_modpack_dir):
    """Test updating side in non-existent TOML file."""
    result = packwiz.update_mod_side_in_toml("test-modpack-1.20.1", "nonexistent.pw.toml", "client")
    assert result is False


def test_get_mod_toml_data(temp_repo, sample_modpack_dir, sample_mod_toml):
    """Test getting TOML data for a mod."""
    # Ensure the modpack directory exists
    modpack_dir = temp_repo / "test-modpack-1.20.1"
    modpack_dir.mkdir(exist_ok=True)
    (modpack_dir / "mods").mkdir(exist_ok=True)
    
    # Create the TOML file
    mod_toml = modpack_dir / "mods" / "test-mod.pw.toml"
    mod_toml.write_text('name = "Test Mod"\nside = "both"\n')
    
    toml_data = packwiz.get_mod_toml_data("test-modpack-1.20.1", "test-mod.pw.toml")
    assert toml_data is not None
    assert toml_data.get("name") == "Test Mod"
    assert toml_data.get("side") == "both"


def test_get_mod_toml_data_not_found(temp_repo, sample_modpack_dir):
    """Test getting TOML data for non-existent file."""
    toml_data = packwiz.get_mod_toml_data("test-modpack-1.20.1", "nonexistent.pw.toml")
    assert toml_data is None

