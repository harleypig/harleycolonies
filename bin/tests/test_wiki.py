"""
Tests for wiki.py module.
"""

from pathlib import Path

import pytest

from mpmanager import wiki


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
    """Test generating simple wiki page with Jinja2 template."""
    # Create template file
    template_file = temp_repo / "bin" / "wiki-page-template.j2"
    template_file.parent.mkdir(parents=True, exist_ok=True)
    template_file.write_text("""---
title: {{ name }}
---

## {{ name }}

{{ description }}

### Side

{{ side }}

### Modpacks

{% if installed_in %}
This mod is installed in the following modpacks:

{% for modpack in installed_in %}
- {{ modpack }}
{% endfor %}
{% else %}
This mod is not currently installed in any modpacks.
{% endif %}
""")
    
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
    from mpmanager import data

    data.set_mod("test-mod", sample_mod_data)
    data.set_mod("test-mod-2", {"name": "Test Mod 2"})

    generated = wiki.generate_all_wiki_pages()
    assert len(generated) == 2
    assert all(p.exists() for p in generated)


def test_generate_mods_index(temp_repo, sample_mod_data):
    """Test generating mods index page."""
    from mpmanager import data

    # Set up mods with categories
    mod_data_1 = sample_mod_data.copy()
    mod_data_1["metadata"] = {
        "categories": ["adventure-rpg", "library-api"]
    }
    data.set_mod("test-mod-1", mod_data_1)
    
    mod_data_2 = {"name": "Test Mod 2"}
    mod_data_2["metadata"] = {
        "categories": ["library-api"]
    }
    data.set_mod("test-mod-2", mod_data_2)
    
    mod_data_3 = {"name": "Test Mod 3"}
    # No categories for test-mod-3
    data.set_mod("test-mod-3", mod_data_3)

    # Generate index
    index_path = wiki.generate_mods_index()

    assert index_path.exists()
    content = index_path.read_text()

    # Check that categories are present
    assert "## adventure-rpg" in content
    assert "## library-api" in content
    assert "## Uncategorized" in content

    # Check that mods are linked
    assert "[Test Mod](mods/test-mod-1.md)" in content
    assert "[Test Mod 2](mods/test-mod-2.md)" in content
    assert "[Test Mod 3](mods/test-mod-3.md)" in content

    # Check that Test Mod appears in both categories (duplicate allowed)
    adventure_section = content.split("## adventure-rpg")[1].split("##")[0]
    library_section = content.split("## library-api")[1].split("##")[0]
    assert "Test Mod" in adventure_section
    assert "Test Mod" in library_section


def test_clean_display_name(temp_repo):
    """Test cleaning display names with special characters."""
    # Test removing bracketed content
    assert wiki._clean_display_name("Legendary Tooltips [Forge]") == "Legendary Tooltips"
    assert wiki._clean_display_name("Mod Name (Fabric/Forge)") == "Mod Name"
    assert wiki._clean_display_name("Test [Forge] [Fabric]") == "Test"
    
    # Test with parentheses
    assert wiki._clean_display_name("Mod (NeoForge)") == "Mod"
    
    # Test normal names
    assert wiki._clean_display_name("Simple Mod Name") == "Simple Mod Name"
    
    # Test multiple spaces
    assert wiki._clean_display_name("Mod  [Forge]  Name") == "Mod Name"


def test_generate_mods_index_cleans_names(temp_repo):
    """Test that mods index cleans display names."""
    from mpmanager import data

    # Add mod with bracketed name
    mod_data = {"name": "Legendary Tooltips [Forge]"}
    mod_data["metadata"] = {
        "categories": ["adventure-rpg"]
    }
    data.set_mod("legendary-tooltips", mod_data)

    # Generate index
    index_path = wiki.generate_mods_index()

    assert index_path.exists()
    content = index_path.read_text()

    # Check that display name is cleaned (no brackets)
    assert "[Legendary Tooltips](mods/legendary-tooltips.md)" in content
    assert "[Forge]" not in content  # Should not appear in the link text


def test_generate_mods_index_no_categories(temp_repo):
    """Test generating mods index page with no categorized mods."""
    from mpmanager import data

    # Add mods without categories
    data.set_mod("test-mod-1", {"name": "Test Mod 1"})
    data.set_mod("test-mod-2", {"name": "Test Mod 2"})

    # Generate index
    index_path = wiki.generate_mods_index()

    assert index_path.exists()
    content = index_path.read_text()

    # Check that uncategorized section exists
    assert "## Uncategorized" in content
    assert "[Test Mod 1](mods/test-mod-1.md)" in content
    assert "[Test Mod 2](mods/test-mod-2.md)" in content

