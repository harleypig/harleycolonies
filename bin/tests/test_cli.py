"""
Tests for CLI interface.
"""

import sys
from unittest.mock import patch

import pytest

from mpmanager import cli


def test_sync_from_strips_trailing_slash(temp_repo, sample_modpack_dir):
    """Test that sync --from strips trailing slashes."""
    with patch("mpmanager.cli.commands") as mock_commands:
        mock_commands.sync_from_modpack.return_value = 0
        
        # Simulate command line arguments
        test_args = ["modpack-manager", "sync", "--from", "test-modpack-1.20.1/"]
        
        with patch.object(sys, "argv", test_args):
            result = cli.main()
            assert result == 0
            # Verify sync_from_modpack was called with trailing slash stripped
            mock_commands.sync_from_modpack.assert_called_once_with("test-modpack-1.20.1")


def test_sync_from_without_trailing_slash(temp_repo, sample_modpack_dir):
    """Test that sync --from works without trailing slash."""
    with patch("mpmanager.cli.commands") as mock_commands:
        mock_commands.sync_from_modpack.return_value = 0
        
        # Simulate command line arguments
        test_args = ["modpack-manager", "sync", "--from", "test-modpack-1.20.1"]
        
        with patch.object(sys, "argv", test_args):
            result = cli.main()
            assert result == 0
            # Verify sync_from_modpack was called with the directory as-is
            mock_commands.sync_from_modpack.assert_called_once_with("test-modpack-1.20.1")


def test_side_command_canonical(temp_repo):
    """Test side command for canonical side update."""
    with patch("mpmanager.cli.commands") as mock_commands:
        mock_commands.update_mod_side.return_value = 0
        
        # Simulate command line arguments
        test_args = ["modpack-manager", "side", "test-mod", "both"]
        
        with patch.object(sys, "argv", test_args):
            result = cli.main()
            assert result == 0
            # Verify update_mod_side was called without modpack_dir
            mock_commands.update_mod_side.assert_called_once_with("test-mod", "both", modpack_dir=None)


def test_side_command_version_specific(temp_repo):
    """Test side command for version-specific side update."""
    with patch("mpmanager.cli.commands") as mock_commands:
        mock_commands.update_mod_side.return_value = 0
        
        # Simulate command line arguments
        test_args = ["modpack-manager", "side", "test-mod", "client", "--modpack", "test-modpack-1.20.1"]
        
        with patch.object(sys, "argv", test_args):
            result = cli.main()
            assert result == 0
            # Verify update_mod_side was called with modpack_dir
            mock_commands.update_mod_side.assert_called_once_with("test-mod", "client", modpack_dir="test-modpack-1.20.1")


def test_list_category_names(temp_repo):
    """Test list --category-names command."""
    with patch("mpmanager.cli.commands") as mock_commands:
        mock_commands.list_mods.return_value = 0
        
        # Simulate command line arguments
        test_args = ["modpack-manager", "list", "--category-names"]
        
        with patch.object(sys, "argv", test_args):
            result = cli.main()
            assert result == 0
            # Verify list_mods was called with category_names=True
            mock_commands.list_mods.assert_called_once_with(
                modpack=None,
                mod_slug=None,
                categories=None,
                category_names=True,
            )


def test_list_categories_all(temp_repo):
    """Test list --categories command (all categories)."""
    with patch("mpmanager.cli.commands") as mock_commands:
        mock_commands.list_mods.return_value = 0
        
        # Simulate command line arguments
        test_args = ["modpack-manager", "list", "--categories"]
        
        with patch.object(sys, "argv", test_args):
            result = cli.main()
            assert result == 0
            # Verify list_mods was called with empty categories list (show all)
            mock_commands.list_mods.assert_called_once_with(
                modpack=None,
                mod_slug=None,
                categories=[],
                category_names=False,
            )


def test_list_categories_filtered_comma(temp_repo):
    """Test list --categories with comma-separated categories."""
    with patch("mpmanager.cli.commands") as mock_commands:
        mock_commands.list_mods.return_value = 0
        
        # Simulate command line arguments
        test_args = ["modpack-manager", "list", "--categories", "adventure-rpg,library-api"]
        
        with patch.object(sys, "argv", test_args):
            result = cli.main()
            assert result == 0
            # Verify list_mods was called with parsed categories
            mock_commands.list_mods.assert_called_once_with(
                modpack=None,
                mod_slug=None,
                categories=["adventure-rpg", "library-api"],
                category_names=False,
            )


def test_list_categories_filtered_space(temp_repo):
    """Test list --categories with space-separated categories."""
    with patch("mpmanager.cli.commands") as mock_commands:
        mock_commands.list_mods.return_value = 0
        
        # Simulate command line arguments
        test_args = ["modpack-manager", "list", "--categories", "adventure-rpg", "library-api"]
        
        with patch.object(sys, "argv", test_args):
            result = cli.main()
            assert result == 0
            # Verify list_mods was called with parsed categories
            mock_commands.list_mods.assert_called_once_with(
                modpack=None,
                mod_slug=None,
                categories=["adventure-rpg", "library-api"],
                category_names=False,
            )

