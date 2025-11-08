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


def generate_mods_index():
    """Generate pages/mods.md index page with all mods grouped by category."""
    from mpmanager import data

    mods_data = data.load_mods()
    mods = mods_data.get("mods", {})

    # Build structure: {category: [(mod_slug, mod_name)]}
    categorized_mods = {}
    uncategorized_mods = []

    for mod_slug, mod_info in mods.items():
        name = mod_info.get("name", mod_slug)
        metadata = mod_info.get("metadata", {})
        categories = metadata.get("categories", [])

        if categories:
            for category in categories:
                if category not in categorized_mods:
                    categorized_mods[category] = []
                categorized_mods[category].append((mod_slug, name))
        else:
            uncategorized_mods.append((mod_slug, name))

    # Sort categories alphabetically
    sorted_categories = sorted(categorized_mods.keys())

    # Sort mods within each category by name
    for category in categorized_mods:
        categorized_mods[category].sort(key=lambda x: x[1].lower())

    # Sort uncategorized mods by name
    uncategorized_mods.sort(key=lambda x: x[1].lower())

    # Generate markdown content
    content = "# Mods\n\n"
    content += "This page lists all mods across all modpacks in mods/mods.yaml, grouped by category.\n\n"

    # Add categorized mods
    for category in sorted_categories:
        content += f"## {category}\n\n"
        for mod_slug, mod_name in categorized_mods[category]:
            content += f"- [{mod_name}](mods/{mod_slug}.md)\n"
        content += "\n"

    # Add uncategorized mods if any
    if uncategorized_mods:
        content += "## Uncategorized\n\n"
        for mod_slug, mod_name in uncategorized_mods:
            content += f"- [{mod_name}](mods/{mod_slug}.md)\n"
        content += "\n"

    # Write to pages/mods.md
    index_path = get_mods_index_path()
    index_path.parent.mkdir(parents=True, exist_ok=True)

    with open(index_path, "w") as f:
        f.write(content)

    return index_path

