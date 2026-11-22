# Overview

## Goals

1. **Automated testing of mod interactions** for the HarleyColonies packs
   (especially MineColonies-centric behavior on NeoForge 1.21.1 and the
   older Forge 1.20.1 pack).
2. **Exportable packs** that remain ordinary packwiz directories so any
   packwiz-installer client or the itzg image can consume them.
3. **Public server management** that re-uses the same pack definition and
   the existing `server/` docker-compose stack.
4. **Wish-goal mod discovery**: a human describes a desired world/behavior
   in natural language; the system searches CurseForge/Modrinth (and the
   local `moddata/`); if nothing suitable exists it scaffolds a minimal
   custom mod or datapack.

## Constraints & Preferences

- Prefer existing tools. Packwiz, `modpack-manager`, itzg's image, Pendulum,
  Baritone, and RCON have already done the hard work.
- Keep the source of truth in the existing packwiz directories
  (`harleycolonies-1.21.1/`, etc.) and `moddata/`.
- Testing environments must be disposable (ephemeral Docker containers).
- Any AI/agent layer should sit on top of the MCP interfaces already
  provided by Pendulum or MCPFabric rather than inventing a new protocol.
- MineColonies remains the central mod; any testing or discovery workflow
  must be able to express "does this break colonies / citizens / blueprints?"

## High-Level Flow

```text
Natural-language request
        ↓
Mod discovery (CurseForge/Modrinth + local moddata)
        ↓
(optional) scaffold custom mod / datapack / KubeJS
        ↓
Update packwiz pack via modpack-manager
        ↓
Spin ephemeral itzg container (PACKWIZ_URL)
        ↓
Join Pendulum+Baritone client(s) → run interaction scripts
        ↓
Collect logs / TPS / screenshots / exceptions
        ↓
Human or agent review → promote to public server or reject
```

The rest of the plans fill in each stage.
