#!/usr/bin/env python3
"""
CLI interface for modpack-manager.
"""

import argparse
import sys

from mpmanager import commands


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Manage mods, modpacks, and generate wiki pages"
    )
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Mod commands
    mod_parser = subparsers.add_parser("mod", help="Mod operations")
    mod_subparsers = mod_parser.add_subparsers(
        dest="mod_command", help="Mod command"
    )

    # mod create
    mod_create = mod_subparsers.add_parser("create", help="Create mod entry and install using Packwiz")
    mod_create.add_argument("mod_slug", help="Mod slug (identifier)")
    mod_create.add_argument("--modpack", required=True, help="Modpack directory (must exist)")
    mod_create.add_argument("--curseforge-id", type=int, help="CurseForge project ID")
    mod_create.add_argument("--category", help="Category to add files from (pass-through to packwiz)")
    mod_create.add_argument("--file-id", type=int, help="CurseForge file ID (pass-through to packwiz)")

    # mod list
    mod_list = mod_subparsers.add_parser("list", help="List mods")
    mod_list.add_argument("--slug", help="Show information for specific mod")
    mod_list.add_argument("--modpack", help="Show mods in specific modpack")
    mod_list.add_argument(
        "--categories",
        nargs="*",
        help="Show categorized list. Use without arguments for all categories, or specify category names (comma or space separated)",
    )
    mod_list.add_argument(
        "--category-names",
        action="store_true",
        help="Show alphabetized list of all category names",
    )

    # mod refresh
    mod_refresh = mod_subparsers.add_parser("refresh", help="Refresh a mod's metadata from packwiz TOML")
    mod_refresh.add_argument("mod_slug", help="Mod slug")
    mod_refresh.add_argument("--modpack", help="Modpack directory to read TOML from")
    mod_refresh.add_argument("--force-remote", action="store_true", help="Replace local integrations/dependencies with remote values")

    # mod update
    mod_update = mod_subparsers.add_parser("update", help="Update mod information")
    mod_update.add_argument("mod_slug", help="Mod slug")
    mod_update.add_argument(
        "--side",
        choices=["client", "server", "both"],
        help="Update mod side (client/server/both)",
    )
    mod_update.add_argument("--curseforge-id", type=int, help="CurseForge project ID")
    mod_update.add_argument("--modrinth-id", help="Modrinth project ID")

    # mod remove
    mod_remove = mod_subparsers.add_parser("remove", help="Remove mod")
    mod_remove.add_argument("mod_slug", help="Mod slug to remove")
    mod_remove.add_argument("--from-modpack", help="Remove from modpack only (not from modpacks directory)")

    # mod sync
    mod_sync = mod_subparsers.add_parser("sync", help="Sync mod from modpack")
    mod_sync.add_argument("--from", required=True, dest="from_dir", help="Modpack directory to sync from")
    mod_sync.add_argument("--slug", help="Sync specific mod slug (otherwise syncs all mods)")

    # Modpack commands
    modpack_parser = subparsers.add_parser("modpack", help="Modpack operations")
    modpack_subparsers = modpack_parser.add_subparsers(
        dest="modpack_command", help="Modpack command"
    )

    # modpack create
    modpack_create = modpack_subparsers.add_parser("create", help="Create new modpack")
    modpack_create.add_argument("modpack_dir", help="Modpack directory name")
    modpack_create.add_argument("--mc-version", required=True, help="Minecraft version")
    modpack_create.add_argument(
        "--modloader", required=True, choices=["forge", "fabric", "quilt"], help="Modloader"
    )
    modpack_create.add_argument(
        "--modloader-version", help="Modloader version (optional)"
    )

    # modpack list
    modpack_list = modpack_subparsers.add_parser("list", help="List modpacks or mods in modpack")
    modpack_list.add_argument("--dir", help="List mods in specific modpack")

    # modpack update
    modpack_update = modpack_subparsers.add_parser("update", help="Update modpack metadata")
    modpack_update.add_argument("modpack_dir", help="Modpack directory name")
    modpack_update.add_argument("--mc-version", help="Minecraft version")
    modpack_update.add_argument("--modloader", choices=["forge", "fabric", "quilt"], help="Modloader")

    # modpack remove
    modpack_remove = modpack_subparsers.add_parser("remove", help="Remove modpack")
    modpack_remove.add_argument("modpack_dir", help="Modpack directory name")
    modpack_remove.add_argument("--from-filesystem", action="store_true", help="Delete modpack directory from filesystem")

    # modpack sync
    modpack_sync = modpack_subparsers.add_parser("sync", help="Sync modpack")
    modpack_sync.add_argument("modpack_dir", nargs="?", help="Modpack directory name (for syncing TO modpack)")
    modpack_sync.add_argument("--from", dest="from_dir", help="Sync modpacks/mods.yaml FROM modpack (imports all mods)")

    # modpack add
    modpack_add = modpack_subparsers.add_parser("add", help="Add mod to modpack")
    modpack_add.add_argument("modpack_dir", help="Modpack directory name")
    modpack_add.add_argument("mod_slug", help="Mod slug to add")

    # modpack remove (mod from modpack)
    modpack_remove_mod = modpack_subparsers.add_parser("remove-mod", help="Remove mod from modpack")
    modpack_remove_mod.add_argument("modpack_dir", help="Modpack directory name")
    modpack_remove_mod.add_argument("mod_slug", help="Mod slug to remove")

    # modpack reject
    modpack_reject = modpack_subparsers.add_parser("reject", help="Mark mod as rejected in modpack")
    modpack_reject.add_argument("modpack_dir", help="Modpack directory name")
    modpack_reject.add_argument("mod_slug", help="Mod slug to reject")
    modpack_reject.add_argument("--reason", required=True, help="Reason for rejection")

    # modpack export
    modpack_export = modpack_subparsers.add_parser("export", help="Export modpack using packwiz")
    modpack_export.add_argument("modpack_dir", help="Modpack directory name")

    # Wiki commands
    wiki_parser = subparsers.add_parser("wiki", help="Wiki operations")
    wiki_subparsers = wiki_parser.add_subparsers(
        dest="wiki_command", help="Wiki command"
    )

    # wiki generate
    wiki_generate = wiki_subparsers.add_parser("generate", help="Generate wiki pages")
    wiki_generate.add_argument(
        "--all",
        action="store_true",
        help="Generate all wiki pages (destructive: clears pages/mods and removes pages/mods.md)",
    )
    wiki_generate.add_argument("--mod", help="Generate wiki page for specific mod")
    wiki_generate.add_argument(
        "--index",
        action="store_true",
        help="Generate pages/mods.md index page with all mods grouped by category",
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    # Route to appropriate command handler
    try:
        if args.command == "mod":
            if args.mod_command == "create":
                return commands.mod_create(
                    args.mod_slug,
                    modpack_dir=args.modpack,
                    curseforge_id=args.curseforge_id,
                    category=args.category,
                    file_id=args.file_id,
                )
            elif args.mod_command == "list":
                categories = None
                if args.categories is not None:
                    if len(args.categories) == 0:
                        categories = []
                    else:
                        categories = []
                        for cat_arg in args.categories:
                            if "," in cat_arg:
                                categories.extend([c.strip() for c in cat_arg.split(",")])
                            else:
                                categories.append(cat_arg.strip())
                        categories = [c for c in categories if c]
                return commands.mod_list(
                    mod_slug=args.slug,
                    modpack=args.modpack,
                    categories=categories,
                    category_names=args.category_names,
                )
            elif args.mod_command == "refresh":
                return commands.mod_refresh(
                    args.mod_slug,
                    modpack_dir=args.modpack,
                    force_remote=bool(args.force_remote),
                )
            elif args.mod_command == "update":
                return commands.mod_update(
                    args.mod_slug,
                    side=args.side,
                    curseforge_id=args.curseforge_id,
                    modrinth_id=args.modrinth_id,
                )
            elif args.mod_command == "remove":
                return commands.mod_remove(
                    args.mod_slug,
                    from_modpack=args.from_modpack,
                )
            elif args.mod_command == "sync":
                modpack_dir = args.from_dir.rstrip("/")
                return commands.mod_sync(
                    modpack_dir=modpack_dir,
                    mod_slug=args.slug,
                )
            else:
                mod_parser.print_help()
                return 1
        elif args.command == "modpack":
            if args.modpack_command == "create":
                return commands.modpack_create(
                    args.modpack_dir,
                    args.mc_version,
                    args.modloader,
                    modloader_version=args.modloader_version,
                )
            elif args.modpack_command == "list":
                return commands.modpack_list(modpack_dir=args.dir)
            elif args.modpack_command == "update":
                return commands.modpack_update(
                    args.modpack_dir,
                    mc_version=args.mc_version,
                    modloader=args.modloader,
                )
            elif args.modpack_command == "remove":
                return commands.modpack_remove(
                    args.modpack_dir,
                    from_filesystem=args.from_filesystem,
                )
            elif args.modpack_command == "sync":
                if args.from_dir:
                    from_dir = args.from_dir.rstrip("/")
                    return commands.modpack_sync_from(from_dir)
                elif args.modpack_dir:
                    modpack_dir = args.modpack_dir.rstrip("/")
                    return commands.modpack_sync(modpack_dir)
                else:
                    modpack_sync.print_help()
                    return 1
            elif args.modpack_command == "add":
                return commands.modpack_add(args.modpack_dir, args.mod_slug)
            elif args.modpack_command == "remove-mod":
                return commands.modpack_remove_mod(args.modpack_dir, args.mod_slug)
            elif args.modpack_command == "reject":
                return commands.modpack_reject(
                    args.modpack_dir, args.mod_slug, args.reason
                )
            elif args.modpack_command == "export":
                return commands.modpack_export(args.modpack_dir)
            else:
                modpack_parser.print_help()
                return 1
        elif args.command == "wiki":
            if args.wiki_command == "generate":
                return commands.wiki_generate(
                    all_pages=args.all,
                    mod_slug=args.mod,
                    index=args.index,
                )
            else:
                wiki_parser.print_help()
                return 1
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
