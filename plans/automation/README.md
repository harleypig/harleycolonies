# Automation & Testing Plans

Series of plans for an automated testing environment and public-server
management workflow for HarleyColonies. The guiding principle is to
leverage existing, well-maintained tools rather than reinvent them:

- **Packwiz** + the existing `bin/modpack-manager` for pack definition and
  export.
- **itzg/minecraft-server** Docker image (already used in `server/`) with
  native `PACKWIZ_URL` support.
- **Pendulum** (or MCPFabric) + **Baritone** for client-side automation
  and AI-agent control via MCP.
- **RCON**, server logs, and (where useful) Minecraft's GameTest framework
  for server-side checks.
- CurseForge / Modrinth APIs and search for mod discovery.

These are planning documents, not implementation. Each file is a
self-contained plan that can be turned into issues or worked independently.

## Contents

1. [01-overview.md](01-overview.md) — High-level goals and constraints.
2. [02-mod-discovery.md](02-mod-discovery.md) — Wish-goal workflow: describe a
   feature, search for existing mods, fall back to scaffolding a custom one.
3. [03-testing-environment.md](03-testing-environment.md) — Ephemeral itzg
   containers + Pendulum/Baritone clients for interaction testing.
4. [04-public-server.md](04-public-server.md) — Promoting a validated pack to
   the public server and ongoing management.
5. [05-integration-notes.md](05-integration-notes.md) — Concrete tool
   combinations, environment variables, and next concrete steps.

## Non-goals

- Building a full custom multi-agent framework from scratch when Pendulum
  (or MCPFabric) already exposes an MCP interface.
- Replacing `modpack-manager` or packwiz; extend or call them.
- Client-side-only solutions that cannot run headless or in Docker for
  automated CI-style testing.
