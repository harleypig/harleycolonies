"""
Tests for wiki page clearing functionality.
"""

import pytest

from mpmanager import commands, data, wiki


def test_clear_wiki_pages(temp_repo):
    """Test clearing wiki pages."""
    # Create some wiki pages
    mods_wiki_dir = wiki.get_mods_wiki_dir()
    mods_wiki_dir.mkdir(parents=True, exist_ok=True)
    
    # Create a test wiki page
    test_page = mods_wiki_dir / "test-mod.md"
    test_page.write_text("# Test Mod")
    
    # Create mods index
    mods_index = wiki.get_mods_index_path()
    mods_index.write_text("# Mods Index")
    
    # Verify files exist
    assert test_page.exists()
    assert mods_index.exists()
    
    # Clear wiki pages
    wiki.clear_wiki_pages()
    
    # Verify files are removed
    assert not mods_wiki_dir.exists()
    assert not mods_index.exists()


def test_clear_wiki_pages_nonexistent(temp_repo):
    """Test clearing wiki pages when they don't exist."""
    # Clear wiki pages (should not error)
    wiki.clear_wiki_pages()
    
    # Verify directories don't exist
    mods_wiki_dir = wiki.get_mods_wiki_dir()
    mods_index = wiki.get_mods_index_path()
    
    assert not mods_wiki_dir.exists()
    assert not mods_index.exists()


def test_generate_wiki_destructive(temp_repo):
    """Test generating wiki pages with --generate (destructive mode)."""
    # Add a mod
    commands.add_mod("test-mod", curseforge_id=12345)
    mods_data = data.load_mods()
    mods_data["mods"]["test-mod"]["name"] = "Test Mod"
    data.save_mods(mods_data)
    
    # Create some existing wiki pages
    mods_wiki_dir = wiki.get_mods_wiki_dir()
    mods_wiki_dir.mkdir(parents=True, exist_ok=True)
    old_page = mods_wiki_dir / "old-mod.md"
    old_page.write_text("# Old Mod")
    
    mods_index = wiki.get_mods_index_path()
    mods_index.write_text("# Old Index")
    
    # Verify old files exist
    assert old_page.exists()
    assert mods_index.exists()
    
    # Generate wiki pages (destructive mode)
    result = commands.generate_wiki(generate=True)
    assert result == 0
    
    # Verify old files are removed
    assert not old_page.exists()
    # Old index is removed but new one is created, so check that a new one exists
    # (the old content is gone, but the file is recreated)
    
    # Verify new wiki page was created
    new_page = mods_wiki_dir / "test-mod.md"
    assert new_page.exists()
    
    # Verify new index page was created (replaces the old one)
    new_index = wiki.get_mods_index_path()
    assert new_index.exists()
    # Verify it has new content (not the old "# Old Index")
    index_content = new_index.read_text()
    assert "# Old Index" not in index_content
    assert "Test Mod" in index_content

