# Testing Environment

## Goal

Spin up a disposable Minecraft server that matches the current packwiz
pack, join one or more automated clients, and exercise mod interactions
(especially MineColonies + other mods) without manual play.

## Core Pieces (all existing)

### Server

- `itzg/minecraft-server` image.
- Environment: `EULA=TRUE`, `TYPE` / loader matching the pack, and
  `PACKWIZ_URL` pointing at the pack under test.
- For local iteration the URL can be a `packwiz serve` process; for CI it
  can be a raw GitHub URL of a branch or a temporary artifact.
- RCON enabled so tests can also issue server commands and read responses.
- Resource limits and a short-lived volume so containers are cheap to
  create and destroy.

### Clients / Bots

- **Pendulum** (NeoForge 1.21.1 supported) or **MCPFabric**.
  - Exposes an MCP server (JSON-RPC over TCP).
  - JavaScript API + optional Baritone bindings (`br.goto`, `br.mine`,
    `br.build`, `br.farm`, etc.).
  - Screenshot and GUI automation support for visual checks.
- One or more client containers (or local clients) that:
  1. Install the same pack (packwiz-installer, client side).
  2. Start with Pendulum + Baritone.
  3. Expose the MCP port to the test runner.

### Test Runner

- Can be a simple Python/Node script, a GitHub Action, or a thin agent
  that speaks MCP.
- Responsibilities:
  - Wait for server ready (itzg health / RCON ping).
  - Connect to Pendulum MCP.
  - Execute a library of scenario scripts (or LLM-generated ones).
  - Collect: server log excerpts, client log, TPS samples, exceptions,
    screenshots, Baritone success/failure.
  - Tear everything down.

## Example Scenarios Worth Automating

- Place a MineColonies building supply block / hut and verify a citizen
  can path to it (Baritone or citizen AI).
- Interact with a Create contraption that crosses a colony area.
- Long-distance Baritone travel while chunks load (stress test).
- Inventory / crafting sequences that involve multiple mods.
- World-gen checks (e.g. the rare-cave-entrance example) by sampling
  surface and underground air blocks after generation.

## Integration with Existing Repo Tooling

- Pack changes still go through `bin/modpack-manager` so `moddata/` stays
  consistent.
- Server compose patterns can be copied from `server/docker-compose.yml`
  and parameterized.
- Logs and artifacts can be uploaded as CI artifacts or stored under a
  gitignored `work/test-runs/` directory.

## Incremental Approach

1. Manual: `docker run` with `PACKWIZ_URL` + a local Pendulum client.
2. Scripted: one Python (or shell) driver that starts/stops the container
   and sends a fixed Pendulum script.
3. Library of scenarios + optional agent that proposes new ones from
   failure logs.
