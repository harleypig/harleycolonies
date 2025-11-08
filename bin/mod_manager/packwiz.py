#!/usr/bin/env python3
"""
Packwiz integration for modpack operations.
"""

import subprocess
from pathlib import Path
from tomlkit import parse, dumps


def get_repo_root():
    """Get repository root directory."""
    return Path(__file__).parent.parent.parent


def get_modpack_path(modpack_dir):
    """Get path to modpack directory."""
    return get_repo_root() / modpack_dir


def run_packwiz(command, modpack_dir, *args, check=True):
    """Run packwiz command in modpack directory."""
    modpack_path = get_modpack_path(modpack_dir)
    if not modpack_path.exists():
        raise FileNotFoundError(f"Modpack directory not found: {modpack_dir}")

    cmd = ["packwiz"] + command.split() + list(args)
    result = subprocess.run(
        cmd,
        cwd=str(modpack_path),
        capture_output=True,
        text=True,
        check=check,
    )
    return result


def install_mod(modpack_dir, mod_slug, source="curseforge", project_id=None):
    """Install mod using packwiz."""
    modpack_path = get_modpack_path(modpack_dir)

    if source == "curseforge":
        if not project_id:
            # Try to get from mods.yaml
            from mod_manager import data

            mod = data.get_mod(mod_slug)
            if mod and "curseforge_id" in mod:
                project_id = mod["curseforge_id"]
            else:
                # Try to search by name
                cmd = ["packwiz", "curseforge", "install", mod_slug]
                result = subprocess.run(
                    cmd,
                    cwd=str(modpack_path),
                    capture_output=True,
                    text=True,
                )
                return result
        cmd = ["packwiz", "curseforge", "install", str(project_id)]
    elif source == "modrinth":
        if not project_id:
            cmd = ["packwiz", "modrinth", "install", mod_slug]
        else:
            cmd = ["packwiz", "modrinth", "install", project_id]
    else:
        raise ValueError(f"Unknown source: {source}")

    result = subprocess.run(
        cmd,
        cwd=str(modpack_path),
        capture_output=True,
        text=True,
    )
    return result


def remove_mod(modpack_dir, mod_file):
    """Remove mod from modpack using packwiz."""
    modpack_path = get_modpack_path(modpack_dir)
    cmd = ["packwiz", "remove", mod_file]

    result = subprocess.run(
        cmd,
        cwd=str(modpack_path),
        capture_output=True,
        text=True,
    )
    return result


def export_modpack(modpack_dir):
    """Export modpack using packwiz."""
    modpack_path = get_modpack_path(modpack_dir)
    cmd = ["packwiz", "curseforge", "export"]

    result = subprocess.run(
        cmd,
        cwd=str(modpack_path),
        capture_output=True,
        text=True,
    )
    return result


def get_mod_side_from_packwiz(modpack_dir, mod_file):
    """Get mod side from packwiz .pw.toml file."""
    modpack_path = get_modpack_path(modpack_dir)
    mod_toml_path = modpack_path / "mods" / mod_file

    if not mod_toml_path.exists():
        return None

    try:
        with open(mod_toml_path, "r") as f:
            data = parse(f.read())
            return data.get("side")
    except Exception:
        return None


def find_mod_file(modpack_dir, mod_slug):
    """Find packwiz .pw.toml file for mod in modpack."""
    modpack_path = get_modpack_path(modpack_dir)
    mods_dir = modpack_path / "mods"

    if not mods_dir.exists():
        return None

    # Try exact match first
    exact_match = mods_dir / f"{mod_slug}.pw.toml"
    if exact_match.exists():
        return exact_match.name

    # Search for files containing mod_slug
    for mod_file in mods_dir.glob("*.pw.toml"):
        if mod_slug.lower() in mod_file.stem.lower():
            return mod_file.name

    return None


def create_modpack(modpack_dir, mc_version, modloader, modloader_version=None):
    """Create new modpack using packwiz."""
    modpack_path = get_modpack_path(modpack_dir)
    modpack_path.mkdir(parents=True, exist_ok=True)

    # Initialize packwiz
    cmd = ["packwiz", "init", "--name", modpack_dir, "--author", "HarleyColonies"]
    result = subprocess.run(
        cmd,
        cwd=str(modpack_path),
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        return result

    # Update pack.toml with versions
    try:
        pack_toml = modpack_path / "pack.toml"
        with open(pack_toml, "r") as f:
            data = parse(f.read())

        if "versions" not in data:
            data["versions"] = {}

        data["versions"]["minecraft"] = mc_version
        data["versions"][modloader] = modloader_version or "latest"

        with open(pack_toml, "w") as f:
            f.write(dumps(data))
    except Exception as e:
        print(f"Warning: Could not update pack.toml: {e}")

    return result


def get_all_mods_in_modpack(modpack_dir):
    """Get list of all mod files in modpack."""
    modpack_path = get_modpack_path(modpack_dir)
    mods_dir = modpack_path / "mods"

    if not mods_dir.exists():
        return []

    mod_files = []
    for mod_file in mods_dir.glob("*.pw.toml"):
        try:
            with open(mod_file, "r") as f:
                data = parse(f.read())
                mod_name = data.get("name", mod_file.stem)
                mod_files.append({
                    "file": mod_file.name,
                    "name": mod_name,
                    "side": data.get("side"),
                })
        except Exception:
            continue

    return mod_files

