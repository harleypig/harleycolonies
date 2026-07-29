# TODO

## Tooling: backup, mod lists & blueprints

- **Wiki page: client-side-only mods.** A curated reference list of
  known client-side-only mods that work on any server, so they can be
  installed when connecting to any server I play on. This is a general
  "mods I can always run client-side" catalogue, separate from the
  HarleyColonies pack's mod list (though some may also end up in my own
  modpack). Approach: use **packwiz** to maintain a "fake" modpack — a
  packwiz directory used only as a tracking store, never built or
  published — to hold these mods. `packwiz` then handles fetching each
  mod's metadata into per-mod `.pw.toml` files (name, side, links,
  source). Generate the wiki page under `pages/` by parsing those
  `.pw.toml` files for the name and `metadata.*.website` / `source`
  link, the same data shape as the real packs. Seed the fake pack from
  `MyCSOMods.txt` rescued from the stale clone (see migration checklist
  in `.claude/CLAUDE.md`) and grow it over time.

- **Backup script: mod reinstall manifest.** `bin/backup-instance`
  excludes mod jars (regenerable), so the backup needs a record of which
  mods to reinstall. The script is **instance-agnostic** (works against
  any server/instance), so it must read the defining mod list **from the
  target instance itself**, not from this repo's packs. Discover whatever
  the target uses to define its mods (e.g. a packwiz pack bundled in the
  instance, a Modrinth `modrinth.index.json`, a MultiMC/Prism manifest,
  or, failing any of those, the jars present in the instance `mods/`
  dir), compare it against what is actually installed, and write a
  manifest of mod names to the backup directory. Decide what the manifest
  captures: mods present in the instance, and ideally flag drift
  (installed-but-not-in-list / in-list-but-not-installed). Handle the
  case where the target has no machine-readable mod list at all.

- **Default blueprints directory.** Keep a canonical/default
  `blueprints/` set tracked in the repo so a fresh instance starts from
  a known baseline. Decide its home and how the backup script and a new
  instance relate to it (seed-from vs back-up-to). Relates to the
  Blueprints & Schematics section below.

## Game design

- Add or create a datapack that [increases jungle sapling
    resources](https://www.youtube.com/watch?v=htbD9vbf9cw)

## Blueprints & Schematics

- Make blueprints of farms
- Can baritone read/build from minecolonies blueprints?
- Do sites like planetminecraft have farm blueprints? Or worlds with farms I can make blueprints from?
- Maybe make blueprints have road builtin?
- Can I make groupings a parent/child?
- Look into using auto-leveling for some blueprints
- ??? Make residence the parent, guardtower, cookery, and bakery child with auto-leveling?
- Some hut blocks may require material not available when the main blueprint is laid down. Those will need to be either created at later levels for the blueprint, or a marker left at the spot and depend on the player to place the hut block correctly.
- Maybe have multiple farms in the main blueprint, one field for each farm. Create separate blueprints for extra fields.
- Some farm field blueprints with both above and below ground fields?
- Same for plantations ... have multiple plantation huts, one field for each and create separate blueprints for extra plantation fields. (see [this section](https://minecolonies.com/wiki/tutorials/schematics#plantation-fields) of the schematics link, as well as the following related sections.)
- Fisher hut should have both a water/pool integrated and a version that can be used with an existing body of water.
- For the mine, do the required blocks need to be cobblestone if they're tagged 'cobble'?
- Custom mineshafts? Is that only the vertical, initial shaft, or the horizontal shafts, or both?

## Farms & Resources

- Figure out a way to use the same farm to do all of them (multiple uses - cactus, bamboo, sugarcane can be used to make bonemeal; bamboo and kelp can be used as a fuel source)

## Minecolonies - Buildings & Huts

- I don't like the quarry, I won't be using it. I'll have to see if it can be incorporated to my satisfaction. Can the opening for the quarry be underground?
- NOTE: A barrackstower doesn't need to be a tower. It could be quonset hut.
- ???: Will putting all animals in the same pen cause confusion for the worker?
- Can multiple meat farmer's use a single field?
- Can a plantation field have multiple items growing from it, even if the worker isn't harvesting them?

## Mods & Configuration

- Locations of the configuration files for the mods will be added later.
- https://www.curseforge.com/minecraft/mc-mods/ready-player-fun

## Technical / Code

- TODO: Can `blocksToAvoidBreaking` be a HashSet or ImmutableSet? (from Settings.java)

## Misc / Questions

- Add my planet minecraft [collection](https://www.planetminecraft.com/collection/287500/harleycolonies/) somewhere
- Check out these mods:
  - [Lithosphere](https://modrinth.com/datapack/lithosphere) - Be sure to check the Recommendations section
  - [Still Life](https://modrinth.com/datapack/still-life) - Incompatible with Biomes O' Plenty
  - [Old English Style](https://www.planetminecraft.com/mod/old-english-stylepack-for-minecolonies-1-20/)
- Consider design where house is above ground (e.g., above space for
    mushrooms, netherwart, etc. or even build a series of farm fields where
    house is 3 blocks up, and guard towers on the corners.
