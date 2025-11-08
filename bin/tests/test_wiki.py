"""
Tests for wiki.py module.
"""

from pathlib import Path

import pytest

from mod_manager import wiki


def test_get_repo_root(temp_repo):
    """Test getting repository root."""
    assert wiki.get_repo_root() == temp_repo


def test_get_mod_dir(temp_repo):
    """Test getting mod directory."""
    mod_dir = wiki.get_mod_dir("test-mod")
    assert mod_dir == temp_repo / "mods" / "test-mod"


def test_get_wiki_page_path(temp_repo):
    """Test getting wiki page path."""
    wiki_path = wiki.get_wiki_page_path("test-mod")
    assert wiki_path == temp_repo / "pages" / "mods" / "test-mod.md"


def test_has_custom_wiki_false(temp_repo):
    """Test checking for custom wiki when it doesn't exist."""
    assert wiki.has_custom_wiki("test-mod") is False


def test_has_custom_wiki_true(temp_repo):
    """Test checking for custom wiki when it exists."""
    mod_dir = temp_repo / "mods" / "test-mod"
    mod_dir.mkdir(parents=True)
    (mod_dir / "wiki.md").write_text("# Custom Wiki Content")
    assert wiki.has_custom_wiki("test-mod") is True


def test_generate_simple_wiki_page(temp_repo, sample_mod_data):
    """Test generating simple wiki page."""
    content = wiki.generate_simple_wiki_page("test-mod", sample_mod_data)
    assert "title: Test Mod" in content
    assert "## Test Mod" in content
    assert "### Side" in content
    assert "### Modpacks" in content


def test_generate_custom_wiki_page(temp_repo, sample_mod_data):
    """Test generating custom wiki page."""
    mod_dir = temp_repo / "mods" / "test-mod"
    mod_dir.mkdir(parents=True)
    (mod_dir / "wiki.md").write_text("# Custom Content\n\nSome custom text.")

    content = wiki.generate_custom_wiki_page("test-mod", sample_mod_data)
    assert "# Custom Content" in content
    assert "Some custom text." in content


def test_generate_wiki_page_simple(temp_repo, sample_mod_data):
    """Test generating wiki page (simple)."""
    wiki_path = wiki.generate_wiki_page("test-mod", sample_mod_data)
    assert wiki_path.exists()
    assert wiki_path.name == "test-mod.md"
    content = wiki_path.read_text()
    assert "title: Test Mod" in content


def test_generate_wiki_page_custom(temp_repo, sample_mod_data):
    """Test generating wiki page (custom)."""
    mod_dir = temp_repo / "mods" / "test-mod"
    mod_dir.mkdir(parents=True)
    (mod_dir / "wiki.md").write_text("# Custom Wiki")

    wiki_path = wiki.generate_wiki_page("test-mod", sample_mod_data)
    assert wiki_path.exists()
    content = wiki_path.read_text()
    assert "# Custom Wiki" in content


def test_generate_all_wiki_pages(temp_repo, sample_mod_data):
    """Test generating all wiki pages."""
    from mod_manager import data

    data.set_mod("test-mod", sample_mod_data)
    data.set_mod("test-mod-2", {"name": "Test Mod 2"})

    generated = wiki.generate_all_wiki_pages()
    assert len(generated) == 2
    assert all(p.exists() for p in generated)

