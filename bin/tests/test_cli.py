"""
Tests for CLI interface.
"""

import sys
from unittest.mock import patch

import pytest

from mpmanager import cli


def test_mod_sync_from_strips_trailing_slash(temp_repo, sample_modpack_dir):
    """Test that mod sync --from strips trailing slashes."""
    with patch("mpmanager.cli.commands") as mock_commands:
        mock_commands.mod_sync.return_value = 0
        
        # Simulate command line arguments
        test_args = ["modpack-manager", "mod", "sync", "--from", "test-modpack-1.20.1/"]
        
        with patch.object(sys, "argv", test_args):
            result = cli.main()
            assert result == 0
            # Verify mod_sync was called with trailing slash stripped
            mock_commands.mod_sync.assert_called_once_with(
                modpack_dir="test-modpack-1.20.1",
                mod_slug=None,
            )


def test_mod_sync_from_without_trailing_slash(temp_repo, sample_modpack_dir):
    """Test that mod sync --from works without trailing slash."""
    with patch("mpmanager.cli.commands") as mock_commands:
        mock_commands.mod_sync.return_value = 0
        
        # Simulate command line arguments
        test_args = ["modpack-manager", "mod", "sync", "--from", "test-modpack-1.20.1"]
        
        with patch.object(sys, "argv", test_args):
            result = cli.main()
            assert result == 0
            # Verify mod_sync was called with the directory as-is
            mock_commands.mod_sync.assert_called_once_with(
                modpack_dir="test-modpack-1.20.1",
                mod_slug=None,
            )


def test_mod_update_side(temp_repo):
    """Test mod update --side for canonical side update."""
    with patch("mpmanager.cli.commands") as mock_commands:
        mock_commands.mod_update.return_value = 0
        
        # Simulate command line arguments
        test_args = ["modpack-manager", "mod", "update", "test-mod", "--side", "both"]
        
        with patch.object(sys, "argv", test_args):
            result = cli.main()
            assert result == 0
            # Verify mod_update was called with side
            mock_commands.mod_update.assert_called_once_with(
                "test-mod",
                side="both",
                curseforge_id=None,
                modrinth_id=None,
            )


def test_modpack_sync_from_strips_trailing_slash(temp_repo, sample_modpack_dir):
    """Test that modpack sync --from strips trailing slashes."""
    with patch("mpmanager.cli.commands") as mock_commands:
        mock_commands.modpack_sync_from.return_value = 0
        
        # Simulate command line arguments
        test_args = ["modpack-manager", "modpack", "sync", "--from", "test-modpack-1.20.1/"]
        
        with patch.object(sys, "argv", test_args):
            result = cli.main()
            assert result == 0
            # Verify modpack_sync_from was called with trailing slash stripped
            mock_commands.modpack_sync_from.assert_called_once_with("test-modpack-1.20.1")


def test_mod_list_category_names(temp_repo):
    """Test mod list --category-names command."""
    with patch("mpmanager.cli.commands") as mock_commands:
        mock_commands.mod_list.return_value = 0
        
        # Simulate command line arguments
        test_args = ["modpack-manager", "mod", "list", "--category-names"]
        
        with patch.object(sys, "argv", test_args):
            result = cli.main()
            assert result == 0
            # Verify mod_list was called with category_names=True
            mock_commands.mod_list.assert_called_once_with(
                mod_slug=None,
                modpack=None,
                categories=None,
                category_names=True,
            )


def test_mod_list_categories_all(temp_repo):
    """Test mod list --categories command (all categories)."""
    with patch("mpmanager.cli.commands") as mock_commands:
        mock_commands.mod_list.return_value = 0
        
        # Simulate command line arguments
        test_args = ["modpack-manager", "mod", "list", "--categories"]
        
        with patch.object(sys, "argv", test_args):
            result = cli.main()
            assert result == 0
            # Verify mod_list was called with empty categories list (show all)
            mock_commands.mod_list.assert_called_once_with(
                mod_slug=None,
                modpack=None,
                categories=[],
                category_names=False,
            )


def test_mod_list_categories_filtered_comma(temp_repo):
    """Test mod list --categories with comma-separated categories."""
    with patch("mpmanager.cli.commands") as mock_commands:
        mock_commands.mod_list.return_value = 0
        
        # Simulate command line arguments
        test_args = ["modpack-manager", "mod", "list", "--categories", "adventure-rpg,library-api"]
        
        with patch.object(sys, "argv", test_args):
            result = cli.main()
            assert result == 0
            # Verify mod_list was called with parsed categories
            mock_commands.mod_list.assert_called_once_with(
                mod_slug=None,
                modpack=None,
                categories=["adventure-rpg", "library-api"],
                category_names=False,
            )


def test_mod_list_categories_filtered_space(temp_repo):
    """Test mod list --categories with space-separated categories."""
    with patch("mpmanager.cli.commands") as mock_commands:
        mock_commands.mod_list.return_value = 0
        
        # Simulate command line arguments
        test_args = ["modpack-manager", "mod", "list", "--categories", "adventure-rpg", "library-api"]
        
        with patch.object(sys, "argv", test_args):
            result = cli.main()
            assert result == 0
            # Verify mod_list was called with parsed categories
            mock_commands.mod_list.assert_called_once_with(
                mod_slug=None,
                modpack=None,
                categories=["adventure-rpg", "library-api"],
                category_names=False,
            )

