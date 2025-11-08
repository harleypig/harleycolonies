#!/usr/bin/env python3
"""
CLI interface for mod-manager.
"""

import argparse
import sys

from mpmanager import commands


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Manage mods, generate modpacks, and create wiki pages"
    )
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Mod management commands
    mod_add = subparsers.add_parser("add", help="Add a new mod")
    mod_add.add_argument("mod_slug", help="Mod slug (identifier)")
    mod_add.add_argument("--curseforge-id", type=int, help="CurseForge project ID")
    mod_add.add_argument("--modrinth-id", help="Modrinth project ID")
    mod_add.add_argument(
        "--side",
        choices=["client", "server", "both"],
        help="Manually set mod side (client/server/both)",
    )

    mod_update = subparsers.add_parser("update", help="Update mod information")
    mod_update.add_argument("mod_slug", help="Mod slug")
    mod_update.add_argument(
        "--side",
        choices=["client", "server", "both"],
        help="Update mod side (client/server/both)",
    )

    mod_remove = subparsers.add_parser("remove", help="Remove a mod")
    mod_remove.add_argument("mod_slug", help="Mod slug to remove")

    # Modpack operations
    modpack_parser = subparsers.add_parser("modpack", help="Modpack operations")
    modpack_subparsers = modpack_parser.add_subparsers(
        dest="modpack_command", help="Modpack command"
    )

    modpack_add = modpack_subparsers.add_parser("add", help="Add mod to modpack")
    modpack_add.add_argument("modpack_dir", help="Modpack directory name")
    modpack_add.add_argument("mod_slug", help="Mod slug to add")

    modpack_remove = modpack_subparsers.add_parser(
        "remove", help="Remove mod from modpack"
    )
    modpack_remove.add_argument("modpack_dir", help="Modpack directory name")
    modpack_remove.add_argument("mod_slug", help="Mod slug to remove")

    modpack_reject = modpack_subparsers.add_parser(
        "reject", help="Mark mod as rejected in modpack"
    )
    modpack_reject.add_argument("modpack_dir", help="Modpack directory name")
    modpack_reject.add_argument("mod_slug", help="Mod slug to reject")
    modpack_reject.add_argument("--reason", required=True, help="Reason for rejection")

    modpack_sync = modpack_subparsers.add_parser(
        "sync", help="Sync modpack with mods.yaml"
    )
    modpack_sync.add_argument("modpack_dir", help="Modpack directory name")

    modpack_create = modpack_subparsers.add_parser(
        "create", help="Create new modpack"
    )
    modpack_create.add_argument("modpack_dir", help="Modpack directory name")
    modpack_create.add_argument("--mc-version", required=True, help="Minecraft version")
    modpack_create.add_argument(
        "--modloader", required=True, choices=["forge", "fabric", "quilt"], help="Modloader"
    )
    modpack_create.add_argument(
        "--modloader-version", help="Modloader version (optional)"
    )

    modpack_export = modpack_subparsers.add_parser(
        "export", help="Export modpack using packwiz"
    )
    modpack_export.add_argument("modpack_dir", help="Modpack directory name")

    # Wiki generation
    wiki = subparsers.add_parser("wiki", help="Generate wiki pages")
    wiki.add_argument(
        "--regenerate", action="store_true", help="Regenerate all wiki pages"
    )
    wiki.add_argument("--mod", help="Generate wiki page for specific mod")

    # Information
    list_cmd = subparsers.add_parser("list", help="List mods or modpacks")
    list_cmd.add_argument("--modpack", help="List mods in modpack")
    list_cmd.add_argument("--mod", help="Show information for specific mod")

    # Sync from existing modpack
    sync = subparsers.add_parser(
        "sync", help="Import from existing packwiz directory"
    )
    sync.add_argument("--from", required=True, dest="from_dir", help="Modpack directory to import from")

    # Side management
    side_cmd = subparsers.add_parser("side", help="Update mod side")
    side_cmd.add_argument("mod_slug", help="Mod slug")
    side_cmd.add_argument(
        "new_side",
        choices=["client", "server", "both"],
        help="New side value (client/server/both)",
    )
    side_cmd.add_argument(
        "--modpack",
        help="Update side for specific modpack (version-specific)",
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    # Route to appropriate command handler
    try:
        if args.command == "add":
            return commands.add_mod(
                args.mod_slug,
                curseforge_id=args.curseforge_id,
                modrinth_id=args.modrinth_id,
                side=args.side,
            )
        elif args.command == "update":
            return commands.update_mod(args.mod_slug, side=args.side)
        elif args.command == "remove":
            return commands.remove_mod(args.mod_slug)
        elif args.command == "modpack":
            if args.modpack_command == "add":
                return commands.modpack_add(args.modpack_dir, args.mod_slug)
            elif args.modpack_command == "remove":
                return commands.modpack_remove(args.modpack_dir, args.mod_slug)
            elif args.modpack_command == "reject":
                return commands.modpack_reject(
                    args.modpack_dir, args.mod_slug, args.reason
                )
            elif args.modpack_command == "sync":
                return commands.modpack_sync(args.modpack_dir)
            elif args.modpack_command == "create":
                return commands.modpack_create(
                    args.modpack_dir,
                    args.mc_version,
                    args.modloader,
                    modloader_version=args.modloader_version,
                )
            elif args.modpack_command == "export":
                return commands.modpack_export(args.modpack_dir)
            else:
                modpack_parser.print_help()
                return 1
        elif args.command == "wiki":
            return commands.generate_wiki(
                regenerate=args.regenerate, mod_slug=args.mod
            )
        elif args.command == "list":
            return commands.list_mods(modpack=args.modpack, mod_slug=args.mod)
        elif args.command == "sync":
            # Strip trailing slash from modpack directory
            modpack_dir = args.from_dir.rstrip("/")
            return commands.sync_from_modpack(modpack_dir)
        elif args.command == "side":
            return commands.update_mod_side(
                args.mod_slug, args.new_side, modpack_dir=args.modpack
            )
        else:
            parser.print_help()
            return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback

        traceback.print_exc()
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

