"""
Integration tests for mod-manager workflow.
"""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from mod_manager import commands, data, packwiz, wiki


@patch("mod_manager.commands.packwiz")
@patch("mod_manager.commands.validation")
def test_full_workflow_add_mod_to_modpack(
    temp_repo, sample_modpack_dir
):
    """Test full workflow: add mod, add to modpack, generate wiki."""
    import mod_manager.commands as cmd_module
    cmd_module.packwiz.get_modpack_path = lambda d: temp_repo / d

    cmd_module.validation.check_packwiz_available.return_value = (True, None)
    cmd_module.validation.validate_mod_data.return_value = (True, None)
    cmd_module.packwiz.install_mod.return_value = MagicMock(returncode=0)
    cmd_module.packwiz.find_mod_file.return_value = "test-mod.pw.toml"
    cmd_module.packwiz.get_mod_side_from_packwiz.return_value = "both"

    # 1. Add mod (check if it already exists from previous test)
    mod = data.get_mod("test-mod")
    if mod is None:
        result = commands.add_mod("test-mod", curseforge_id=12345, side="both")
        assert result == 0

    # 2. Add to modpack
    result = commands.modpack_add("test-modpack-1.20.1", "test-mod")
    assert result == 0

    # 3. Generate wiki
    mod = data.get_mod("test-mod")
    wiki_path = wiki.generate_wiki_page("test-mod", mod)
    assert wiki_path.exists()

    # 4. Verify mod is in installed_in
    mod = data.get_mod("test-mod")
    assert "test-modpack-1.20.1" in mod["modpacks"]["installed_in"]


@patch("mod_manager.commands.packwiz")
def test_workflow_reject_and_remove(temp_repo, sample_modpack_dir):
    """Test workflow: reject mod, then remove from modpack."""
    # Note: packwiz is already patched, but we need to set up the lambda
    import mod_manager.commands as cmd_module
    cmd_module.packwiz.get_modpack_path = lambda d: temp_repo / d

    # Add mod
    commands.add_mod("test-mod")

    # Reject mod
    result = commands.modpack_reject("test-modpack-1.20.1", "test-mod", "Conflicts")
    assert result == 0

    # Verify mod is in rejected_in
    mod = data.get_mod("test-mod")
    rejected = mod["modpacks"]["rejected_in"]
    assert any(r.get("modpack") == "test-modpack-1.20.1" for r in rejected)

    # Verify mod is not in installed_in
    assert "test-modpack-1.20.1" not in mod["modpacks"].get("installed_in", [])


def test_workflow_custom_wiki(temp_repo):
    """Test workflow with custom wiki page."""
    # Create mod with custom wiki
    mod_dir = temp_repo / "mods" / "test-mod"
    mod_dir.mkdir(parents=True)
    (mod_dir / "wiki.md").write_text("# Custom Wiki\n\nCustom content here.")

    mod_data = {"name": "Test Mod", "side": "both"}
    data.set_mod("test-mod", mod_data)

    # Generate wiki
    wiki_path = wiki.generate_wiki_page("test-mod", mod_data)
    assert wiki_path.exists()

    # Verify custom content is included
    content = wiki_path.read_text()
    assert "# Custom Wiki" in content
    assert "Custom content here." in content

