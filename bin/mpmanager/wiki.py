#!/usr/bin/env python3
"""
Wiki page generation for mods.
"""

from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def get_repo_root():
    """Get repository root directory."""
    return Path(__file__).parent.parent.parent


def get_mod_dir(mod_slug):
    """Get mod custom directory."""
    return get_repo_root() / "mods" / mod_slug


def get_wiki_page_path(mod_slug):
    """Get path to wiki page for mod."""
    return get_repo_root() / "pages" / "mods" / f"{mod_slug}.md"


def has_custom_wiki(mod_slug):
    """Check if mod has custom wiki.md file."""
    mod_dir = get_mod_dir(mod_slug)
    wiki_file = mod_dir / "wiki.md"
    return wiki_file.exists()


def _get_template():
    """Get Jinja2 template for wiki pages."""
    script_dir = Path(__file__).parent.parent
    template_dir = script_dir
    env = Environment(loader=FileSystemLoader(str(template_dir)))
    return env.get_template("wiki-page-template.j2")


def _get_index_template():
    """Get Jinja2 template for mods index page."""
    script_dir = Path(__file__).parent.parent
    template_dir = script_dir
    env = Environment(loader=FileSystemLoader(str(template_dir)))
    return env.get_template("mods-index-template.j2")


def generate_simple_wiki_page(mod_slug, mod_data):
    """Generate simple wiki page for mod."""
    name = mod_data.get("name", mod_slug)
    description = mod_data.get("description", "")
    side = mod_data.get("side", "unknown")

    modpacks = mod_data.get("modpacks", {})
    installed_in = modpacks.get("installed_in", [])

    template = _get_template()
    content = template.render(
        name=name,
        description=description,
        side=side,
        installed_in=installed_in,
    )

    return content


def generate_custom_wiki_page(mod_slug, mod_data):
    """Generate custom wiki page using mod's wiki.md file."""
    mod_dir = get_mod_dir(mod_slug)
    wiki_file = mod_dir / "wiki.md"

    if not wiki_file.exists():
        return generate_simple_wiki_page(mod_slug, mod_data)

    # Read custom wiki content
    with open(wiki_file, "r") as f:
        custom_content = f.read()

    # Add modpack list if not already present
    modpacks = mod_data.get("modpacks", {})
    installed_in = modpacks.get("installed_in", [])

    if installed_in and "### Modpacks" not in custom_content:
        custom_content += "\n\n### Modpacks\n\n"
        custom_content += "This mod is installed in the following modpacks:\n\n"
        for modpack in installed_in:
            custom_content += f"- {modpack}\n"

    return custom_content


def generate_wiki_page(mod_slug, mod_data):
    """Generate wiki page for mod (simple or custom)."""
    if has_custom_wiki(mod_slug):
        content = generate_custom_wiki_page(mod_slug, mod_data)
    else:
        content = generate_simple_wiki_page(mod_slug, mod_data)

    # Write to pages/mods/
    wiki_path = get_wiki_page_path(mod_slug)
    wiki_path.parent.mkdir(parents=True, exist_ok=True)

    with open(wiki_path, "w") as f:
        f.write(content)

    return wiki_path


def generate_all_wiki_pages():
    """Generate wiki pages for all mods."""
    from mpmanager import data

    mods_data = data.load_mods()
    mods = mods_data.get("mods", {})

    generated = []
    for mod_slug, mod_info in mods.items():
        wiki_path = generate_wiki_page(mod_slug, mod_info)
        generated.append(wiki_path)

    return generated


def get_mods_index_path():
    """Get path to mods index page."""
    return get_repo_root() / "pages" / "mods.md"


def get_mods_wiki_dir():
    """Get path to mods wiki directory."""
    return get_repo_root() / "pages" / "mods"


def clear_wiki_pages():
    """Clear all wiki pages (destructive operation).
    
    Removes all files in pages/mods/ and removes pages/mods.md.
    """
    import shutil
    
    repo_root = get_repo_root()
    mods_wiki_dir = get_mods_wiki_dir()
    mods_index = get_mods_index_path()
    
    # Remove pages/mods directory if it exists
    if mods_wiki_dir.exists():
        print(f"Removing {mods_wiki_dir}")
        shutil.rmtree(mods_wiki_dir)
    
    # Remove pages/mods.md if it exists
    if mods_index.exists():
        print(f"Removing {mods_index}")
        mods_index.unlink()


def _clean_display_name(name):
    """Clean display name by removing non-alphanumeric characters and bracketed explanations.
    
    This helps prevent markdown link issues with special characters in display names.
    """
    import re
    
    # Remove bracketed content (e.g., [Forge], (Fabric/Forge), etc.)
    # This handles explanatory information like [Forge], [Fabric], etc.
    name = re.sub(r'\[[^\]]*\]', '', name)
    name = re.sub(r'\([^\)]*\)', '', name)
    
    # Strip leading/trailing whitespace and clean up multiple spaces
    name = re.sub(r'\s+', ' ', name).strip()
    
    return name


def generate_mods_index():
    """Generate pages/mods.md index page with all mods grouped by category."""
    from mpmanager import data

    mods_data = data.load_mods()
    mods = mods_data.get("mods", {})

    # Build structure: {category: [(mod_slug, mod_name, display_name)]}
    categorized_mods = {}
    uncategorized_mods = []

    for mod_slug, mod_info in mods.items():
        name = mod_info.get("name", mod_slug)
        display_name = _clean_display_name(name)
        metadata = mod_info.get("metadata", {})
        categories = metadata.get("categories", [])

        if categories:
            for category in categories:
                if category not in categorized_mods:
                    categorized_mods[category] = []
                categorized_mods[category].append((mod_slug, display_name))
        else:
            uncategorized_mods.append((mod_slug, display_name))

    # Sort categories alphabetically
    sorted_categories = sorted(categorized_mods.keys())

    # Sort mods within each category by name
    for category in categorized_mods:
        categorized_mods[category].sort(key=lambda x: x[1].lower())

    # Sort uncategorized mods by name
    uncategorized_mods.sort(key=lambda x: x[1].lower())

    # Generate markdown content using Jinja2 template
    template = _get_index_template()
    content = template.render(
        sorted_categories=sorted_categories,
        categorized_mods=categorized_mods,
        uncategorized_mods=uncategorized_mods,
    )

    # Write to pages/mods.md
    index_path = get_mods_index_path()
    index_path.parent.mkdir(parents=True, exist_ok=True)

    with open(index_path, "w") as f:
        f.write(content)

    return index_path

