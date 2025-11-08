"""
Tests for metadata extraction and merging functionality.
"""

from unittest.mock import patch

import pytest

from mpmanager import data, packwiz


def test_extract_metadata_from_toml_curseforge(temp_repo):
    """Test extracting CurseForge metadata from TOML."""
    toml_data = {
        "name": "Test Mod",
        "side": "both",
        "update": {
            "curseforge": {
                "project-id": 12345
            }
        },
        "metadata": {
            "curseforge": {
                "website": "https://www.curseforge.com/minecraft/mc-mods/test-mod",
                "wiki": "https://wiki.example.com",
                "issues": "https://github.com/test/issues",
                "source": "https://github.com/test/repo",
                "categories": ["library-api", "utility-qol"]
            }
        }
    }
    
    metadata = packwiz.extract_metadata_from_toml(toml_data)
    
    assert metadata["curseforge_id"] == 12345
    assert metadata["side"] == "both"
    assert metadata["website"] == "https://www.curseforge.com/minecraft/mc-mods/test-mod"
    assert metadata["wiki"] == "https://wiki.example.com"
    assert metadata["issues"] == "https://github.com/test/issues"
    assert metadata["source"] == "https://github.com/test/repo"
    assert metadata["categories"] == ["library-api", "utility-qol"]


def test_extract_metadata_from_toml_modrinth(temp_repo):
    """Test extracting Modrinth metadata from TOML."""
    toml_data = {
        "name": "Test Mod",
        "side": "client",
        "update": {
            "modrinth": {
                "project-id": "abc123"
            }
        },
        "metadata": {
            "modrinth": {
                "url": "https://modrinth.com/mod/test-mod"
            }
        }
    }
    
    metadata = packwiz.extract_metadata_from_toml(toml_data)
    
    assert metadata["modrinth_id"] == "abc123"
    assert metadata["side"] == "client"
    assert metadata["website"] == "https://modrinth.com/mod/test-mod"


def test_merge_metadata_first_time(temp_repo):
    """Test merging metadata for first time (canonical)."""
    metadata = {
        "curseforge_id": 12345,
        "side": "both",
        "website": "https://example.com",
        "categories": ["library"]
    }
    
    data.merge_metadata("test-mod", metadata, "test-modpack-1.20.1")
    
    mod = data.get_mod("test-mod")
    assert mod["curseforge_id"] == 12345
    assert mod["side"] == "both"
    assert mod["metadata"]["website"] == "https://example.com"
    assert mod["metadata"]["categories"] == ["library"]


def test_merge_metadata_version_specific_differences(temp_repo):
    """Test merging metadata with version-specific differences."""
    # First modpack - canonical metadata
    metadata1 = {
        "curseforge_id": 12345,
        "side": "both",
        "website": "https://example.com",
        "categories": ["library"]
    }
    data.merge_metadata("test-mod", metadata1, "test-modpack-1.20.1")
    
    # Second modpack - different metadata
    metadata2 = {
        "curseforge_id": 12345,  # Same
        "side": "client",  # Different
        "website": "https://example.com",  # Same
        "categories": ["library", "utility"]  # Different
    }
    data.merge_metadata("test-mod", metadata2, "test-modpack-1.21.1")
    
    mod = data.get_mod("test-mod")
    # Canonical should remain unchanged
    assert mod["side"] == "both"
    assert mod["metadata"]["categories"] == ["library"]
    
    # Version-specific should have differences
    assert "versions" in mod
    assert "test-modpack-1.21.1" in mod["versions"]
    version_meta = mod["versions"]["test-modpack-1.21.1"]["metadata"]
    assert version_meta["side"] == "client"
    assert version_meta["categories"] == ["library", "utility"]


def test_merge_metadata_same_values_no_version_specific(temp_repo):
    """Test that identical metadata doesn't create version-specific entry."""
    metadata = {
        "curseforge_id": 12345,
        "side": "both",
        "website": "https://example.com"
    }
    
    # First modpack
    data.merge_metadata("test-mod", metadata, "test-modpack-1.20.1")
    
    # Second modpack with same metadata
    data.merge_metadata("test-mod", metadata, "test-modpack-1.21.1")
    
    mod = data.get_mod("test-mod")
    # Should not have version-specific entries if metadata is identical
    assert "versions" not in mod or "test-modpack-1.21.1" not in mod.get("versions", {})


def test_merge_metadata_side_differences(temp_repo):
    """Test merging metadata with side differences."""
    # First modpack
    metadata1 = {"side": "both"}
    data.merge_metadata("test-mod", metadata1, "test-modpack-1.20.1")
    
    # Second modpack with different side
    metadata2 = {"side": "client"}
    data.merge_metadata("test-mod", metadata2, "test-modpack-1.21.1")
    
    mod = data.get_mod("test-mod")
    # Canonical side should be "both"
    assert mod["side"] == "both"
    
    # Version-specific side should be "client"
    assert mod["versions"]["test-modpack-1.21.1"]["metadata"]["side"] == "client"

