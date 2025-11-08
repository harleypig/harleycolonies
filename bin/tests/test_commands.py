"""
Tests for commands.py module.
"""

import subprocess
from unittest.mock import MagicMock, patch

import pytest

from mod_manager import commands, data, packwiz


def test_add_mod(temp_repo):
    """Test adding a mod."""
    result = commands.add_mod("test-mod", curseforge_id=12345, side="both")
    assert result == 0
    mod = data.get_mod("test-mod")
    assert mod is not None
    assert mod["curseforge_id"] == 12345
    assert mod["side"] == "both"


def test_add_mod_duplicate(temp_repo):
    """Test adding a duplicate mod."""
    commands.add_mod("test-mod")
    result = commands.add_mod("test-mod")
    assert result == 1


def test_update_mod(temp_repo):
    """Test updating a mod."""
    commands.add_mod("test-mod")
    result = commands.update_mod("test-mod", side="client")
    assert result == 0
    mod = data.get_mod("test-mod")
    assert mod["side"] == "client"


def test_update_mod_not_found(temp_repo):
    """Test updating a mod that doesn't exist."""
    result = commands.update_mod("nonexistent", side="client")
    assert result == 1


def test_remove_mod(temp_repo):
    """Test removing a mod."""
    commands.add_mod("test-mod")
    result = commands.remove_mod("test-mod")
    assert result == 0
    assert data.get_mod("test-mod") is None


def test_remove_mod_not_found(temp_repo):
    """Test removing a mod that doesn't exist."""
    result = commands.remove_mod("nonexistent")
    assert result == 1


@patch("mod_manager.commands.validation")
@patch("mod_manager.commands.packwiz")
def test_modpack_add(temp_repo, sample_modpack_dir):
    """Test adding mod to modpack."""
    import mod_manager.commands as cmd_module
    cmd_module.packwiz.get_modpack_path = lambda d: temp_repo / d
    cmd_module.packwiz.find_mod_file = lambda d, s: "test-mod.pw.toml"
    cmd_module.packwiz.get_mod_side_from_packwiz = lambda d, f: "both"

    cmd_module.validation.check_packwiz_available.return_value = (True, None)
    cmd_module.validation.validate_mod_data.return_value = (True, None)
    cmd_module.validation.validate_mod_id.return_value = (True, None)
    cmd_module.packwiz.install_mod.return_value = MagicMock(returncode=0)

    commands.add_mod("test-mod", curseforge_id=12345)
    result = commands.modpack_add("test-modpack-1.20.1", "test-mod")
    assert result == 0


@patch("mod_manager.commands.packwiz")
@patch("mod_manager.commands.validation")
def test_modpack_remove(temp_repo, sample_modpack_dir):
    """Test removing mod from modpack."""
    import mod_manager.commands as cmd_module
    cmd_module.packwiz.get_modpack_path = lambda d: temp_repo / d
    cmd_module.packwiz.find_mod_file = lambda d, s: "test-mod.pw.toml"
    cmd_module.packwiz.remove_mod.return_value = MagicMock(returncode=0)
    cmd_module.validation.validate_mod_data.return_value = (True, None)

    commands.add_mod("test-mod")
    data.add_to_modpack("test-mod", "test-modpack-1.20.1", "installed_in")
    result = commands.modpack_remove("test-modpack-1.20.1", "test-mod")
    assert result == 0


def test_modpack_reject(temp_repo):
    """Test rejecting mod from modpack."""
    commands.add_mod("test-mod")
    result = commands.modpack_reject("test-modpack-1.20.1", "test-mod", "Test reason")
    assert result == 0
    mod = data.get_mod("test-mod")
    rejected = mod["modpacks"]["rejected_in"]
    assert any(r.get("modpack") == "test-modpack-1.20.1" for r in rejected)


def test_list_mods_empty(temp_repo):
    """Test listing mods when none exist."""
    result = commands.list_mods()
    assert result == 0


def test_list_mods(temp_repo):
    """Test listing mods."""
    commands.add_mod("test-mod", side="both")
    result = commands.list_mods()
    assert result == 0


def test_list_mods_with_modpack(temp_repo):
    """Test listing mods in a modpack."""
    commands.add_mod("test-mod")
    data.add_to_modpack("test-mod", "test-modpack-1.20.1", "installed_in")
    result = commands.list_mods(modpack="test-modpack-1.20.1")
    assert result == 0


def test_list_mods_specific_mod(temp_repo):
    """Test listing specific mod information."""
    commands.add_mod("test-mod", side="both")
    result = commands.list_mods(mod_slug="test-mod")
    assert result == 0


def test_list_mods_not_found(temp_repo):
    """Test listing a mod that doesn't exist."""
    result = commands.list_mods(mod_slug="nonexistent")
    assert result == 1

