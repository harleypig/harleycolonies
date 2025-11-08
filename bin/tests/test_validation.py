"""
Tests for validation.py module.
"""

import pytest

from mod_manager import validation


def test_check_packwiz_available():
    """Test checking if packwiz is available."""
    available, error = validation.check_packwiz_available()
    # This will depend on whether packwiz is installed
    assert isinstance(available, bool)
    if not available:
        assert error is not None


def test_validate_yaml_structure_valid():
    """Test validating valid YAML structure."""
    data = {"mods": {"test-mod": {}}}
    valid, error = validation.validate_yaml_structure(data)
    assert valid is True
    assert error is None


def test_validate_yaml_structure_invalid():
    """Test validating invalid YAML structure."""
    data = "not a dict"
    valid, error = validation.validate_yaml_structure(data)
    assert valid is False
    assert error is not None


def test_validate_yaml_structure_missing_mods():
    """Test validating YAML structure missing mods key."""
    data = {}
    valid, error = validation.validate_yaml_structure(data)
    assert valid is False
    assert "mods" in error.lower()


def test_validate_mod_data_valid():
    """Test validating valid mod data."""
    mod_data = {
        "name": "Test Mod",
        "side": "both",
        "modpacks": {
            "installed_in": ["modpack1"],
            "rejected_in": [{"modpack": "modpack2", "reason": "Test"}],
        },
    }
    valid, error = validation.validate_mod_data(mod_data)
    assert valid is True
    assert error is None


def test_validate_mod_data_invalid_side():
    """Test validating mod data with invalid side."""
    mod_data = {"side": "invalid"}
    valid, error = validation.validate_mod_data(mod_data)
    assert valid is False
    assert "side" in error.lower()


def test_validate_mod_data_invalid_modpacks():
    """Test validating mod data with invalid modpacks structure."""
    mod_data = {"modpacks": "not a dict"}
    valid, error = validation.validate_mod_data(mod_data)
    assert valid is False
    assert "modpacks" in error.lower()


def test_validate_mod_id_curseforge():
    """Test validating CurseForge mod ID."""
    valid, error = validation.validate_mod_id("test-mod", 12345, "curseforge")
    assert valid is True
    assert error is None


def test_validate_mod_id_curseforge_invalid():
    """Test validating invalid CurseForge mod ID."""
    valid, error = validation.validate_mod_id("test-mod", "not-an-int", "curseforge")
    assert valid is False
    assert "integer" in error.lower()


def test_validate_mod_id_modrinth():
    """Test validating Modrinth mod ID."""
    valid, error = validation.validate_mod_id("test-mod", "abc123", "modrinth")
    assert valid is True
    assert error is None

