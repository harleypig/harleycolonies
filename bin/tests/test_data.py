"""
Tests for data.py module.
"""

import yaml
from pathlib import Path

import pytest

from mpmanager import data


def test_get_repo_root(temp_repo):
    """Test getting repository root."""
    assert data.get_repo_root() == temp_repo


def test_load_mods_empty(temp_repo):
    """Test loading empty mods.yaml."""
    mods = data.load_mods()
    assert mods == {"mods": {}}


def test_save_and_load_mods(temp_repo, sample_mod_data):
    """Test saving and loading mods."""
    data.set_mod("test-mod", sample_mod_data)
    loaded = data.load_mods()
    assert "test-mod" in loaded["mods"]
    assert loaded["mods"]["test-mod"]["name"] == "Test Mod"


def test_get_mod(temp_repo, sample_mod_data):
    """Test getting a mod."""
    data.set_mod("test-mod", sample_mod_data)
    mod = data.get_mod("test-mod")
    assert mod is not None
    assert mod["name"] == "Test Mod"


def test_get_mod_not_found(temp_repo):
    """Test getting a mod that doesn't exist."""
    mod = data.get_mod("nonexistent")
    assert mod is None


def test_remove_mod(temp_repo, sample_mod_data):
    """Test removing a mod."""
    data.set_mod("test-mod", sample_mod_data)
    assert data.remove_mod("test-mod") is True
    assert data.get_mod("test-mod") is None


def test_remove_mod_not_found(temp_repo):
    """Test removing a mod that doesn't exist."""
    assert data.remove_mod("nonexistent") is False


def test_add_to_modpack_installed_in(temp_repo):
    """Test adding mod to installed_in list."""
    data.set_mod("test-mod", {})
    data.add_to_modpack("test-mod", "test-modpack", "installed_in")
    mod = data.get_mod("test-mod")
    assert "test-modpack" in mod["modpacks"]["installed_in"]


def test_add_to_modpack_rejected_in(temp_repo):
    """Test adding mod to rejected_in list."""
    data.set_mod("test-mod", {})
    data.add_to_modpack("test-mod", "test-modpack", "rejected_in", "Test reason")
    mod = data.get_mod("test-mod")
    rejected = mod["modpacks"]["rejected_in"]
    assert any(r.get("modpack") == "test-modpack" for r in rejected)


def test_remove_from_modpack(temp_repo):
    """Test removing mod from modpack."""
    data.set_mod("test-mod", {})
    data.add_to_modpack("test-mod", "test-modpack", "installed_in")
    assert data.remove_from_modpack("test-mod", "test-modpack") is True
    mod = data.get_mod("test-mod")
    assert "test-modpack" not in mod["modpacks"].get("installed_in", [])


def test_get_modpack_list(temp_repo):
    """Test getting modpack list type."""
    data.set_mod("test-mod", {})
    data.add_to_modpack("test-mod", "test-modpack", "installed_in")
    list_type = data.get_modpack_list("test-mod", "test-modpack")
    assert list_type == "installed_in"

