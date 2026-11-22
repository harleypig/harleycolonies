# Mod Discovery & Custom Scaffolding

## Wish Goal

Describe a desired feature in ordinary language and have the system:

1. Search for an existing mod (or small set of mods) that already does it.
2. If none are suitable, scaffold a minimal custom solution (datapack,
   KubeJS script, or thin NeoForge mod).

### Example

> "I want to create a world where surface entrances to the cave world are
> rare (controlled by a setting), and there are no air blocks 20 or so
> blocks below wherever the surface has been generated."

Possible existing approaches to check first:

- World-gen mods / datapacks that control cave density or surface openings
  (Lithosphere and similar were already noted in `TODO.md`).
- Terrain-modification or "fill air below surface" style mods.
- Structure / feature mods that can suppress or relocate cave entrances.

## Leveraging Existing Tools

- **CurseForge & Modrinth search APIs** (or the web UIs + scraping as a
  fallback). Query by keywords, categories (world generation, utility),
  Minecraft version, and loader (NeoForge / Forge).
- **Local `moddata/mods.yaml`** and the rejected-mods list so we do not
  re-suggest things already evaluated.
- **`bin/modpack-manager`** once a candidate is chosen: `mod create` +
  `modpack add` keeps the packwiz TOML and metadata in sync.
- For custom work: NeoForge MDK template, or simpler routes first
  (datapack via packwiz, KubeJS if already in the pack).

## Suggested Workflow (can be scripted or agent-driven)

1. Parse the request into searchable terms + constraints (MC version,
   loader, must-not-break MineColonies).
2. Query CurseForge + Modrinth. Rank by relevance, download count,
   last-updated, and open issues mentioning conflicts.
3. Present top candidates with links, side (client/server/both), and a
   one-line "why it might fit".
4. If the human (or a later automated check) rejects them all:
   - Prefer a datapack or KubeJS solution when the change is data-driven.
   - Otherwise generate a minimal NeoForge mod skeleton (one mixin or
     one feature registration) with a clear TODO and config option.
5. Add the result to the pack via `modpack-manager` and proceed to the
   testing plan.

## Open Questions

- How aggressive should automatic addition be vs. always requiring human
  confirmation?
- Should rejected candidates be recorded in `moddata` with a reason so
  future searches skip them?
