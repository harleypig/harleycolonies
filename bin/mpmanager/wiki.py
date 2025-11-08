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

