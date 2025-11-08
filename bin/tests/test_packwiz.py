"""
Tests for packwiz.py module.
"""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from mod_manager import packwiz


def test_get_repo_root(temp_repo):
    """Test getting repository root."""
    assert packwiz.get_repo_root() == temp_repo


def test_get_modpack_path(temp_repo):
    """Test getting modpack path."""
    path = packwiz.get_modpack_path("test-modpack")
    assert path == temp_repo / "test-modpack"


@patch("subprocess.run")
def test_install_mod_curseforge(mock_run, temp_repo, sample_modpack_dir):
    """Test installing mod from CurseForge."""
    mock_run.return_value = MagicMock(returncode=0, stdout="", stderr="")

    result = packwiz.install_mod("test-modpack-1.20.1", "test-mod", "curseforge", 12345)
    assert result.returncode == 0
    mock_run.assert_called_once()


@patch("subprocess.run")
def test_remove_mod(mock_run, temp_repo, sample_modpack_dir):
    """Test removing mod from modpack."""
    mock_run.return_value = MagicMock(returncode=0, stdout="", stderr="")

    result = packwiz.remove_mod("test-modpack-1.20.1", "test-mod.pw.toml")
    assert result.returncode == 0
    mock_run.assert_called_once()


def test_get_mod_side_from_packwiz(temp_repo, sample_modpack_dir, sample_mod_toml):
    """Test getting mod side from packwiz file."""
    side = packwiz.get_mod_side_from_packwiz("test-modpack-1.20.1", "test-mod.pw.toml")
    assert side == "both"


def test_find_mod_file(temp_repo, sample_modpack_dir, sample_mod_toml):
    """Test finding mod file in modpack."""
    mod_file = packwiz.find_mod_file("test-modpack-1.20.1", "test-mod")
    assert mod_file == "test-mod.pw.toml"


def test_find_mod_file_not_found(temp_repo, sample_modpack_dir):
    """Test finding mod file that doesn't exist."""
    mod_file = packwiz.find_mod_file("test-modpack-1.20.1", "nonexistent")
    assert mod_file is None


def test_get_all_mods_in_modpack(temp_repo, sample_modpack_dir, sample_mod_toml):
    """Test getting all mods in modpack."""
    mods = packwiz.get_all_mods_in_modpack("test-modpack-1.20.1")
    assert len(mods) == 1
    assert mods[0]["file"] == "test-mod.pw.toml"
    assert mods[0]["name"] == "Test Mod"
    assert mods[0]["side"] == "both"


@patch("subprocess.run")
def test_create_modpack(mock_run, temp_repo):
    """Test creating a new modpack."""
    mock_run.return_value = MagicMock(returncode=0, stdout="", stderr="")

    result = packwiz.create_modpack("new-modpack", "1.20.1", "forge", "47.2.0")
    assert result.returncode == 0
    mock_run.assert_called_once()

