# Integration Notes & Next Steps

## Concrete Tool Combinations

| Concern              | Existing tool                          | How we use it                          |
|----------------------|----------------------------------------|----------------------------------------|
| Pack definition      | packwiz + `bin/modpack-manager`        | Source of truth; all changes go through it |
| Server runtime       | itzg/minecraft-server                  | `PACKWIZ_URL` + existing compose       |
| Client automation    | Pendulum (or MCPFabric) + Baritone     | MCP tool-calling for tests             |
| Server commands      | RCON                                   | Health checks, give/tp, GameTest triggers |
| Mod search           | CurseForge / Modrinth APIs             | Discovery step before adding anything  |
| Metadata             | `moddata/mods.yaml`                    | Avoid re-testing rejected mods         |

## Environment Variables (itzg)

Key ones already documented by itzg and useful here:

- `PACKWIZ_URL` — URL to `pack.toml`
- `EULA=TRUE`
- `TYPE` / `VERSION` / loader version (or let packwiz drive them where supported)
- `ENABLE_RCON=true`, `RCON_PASSWORD`, `RCON_PORT`
- Memory limits, `MAX_PLAYERS` (low for tests), etc.

## Suggested First Concrete Tasks

1. Add a `server/test-compose.yml` (or a parameterized override) that
   points `PACKWIZ_URL` at a local or branch pack and enables RCON.
2. Document the exact Pendulum (or MCPFabric) install steps for the
   1.21.1 NeoForge pack, including how to start its MCP server.
3. Write one fixed scenario script (e.g. "join, run `/pendulum execute`
   a short Baritone goto, assert no crash") and a 20-line driver that
   starts the container, waits, runs the script, and collects logs.
4. Extend `modpack-manager` (or add a thin wrapper) with a `discover`
   subcommand that shells out to CurseForge/Modrinth search and prints
   candidates.
5. Only after the above works, consider wrapping the MCP calls in a
   small LangGraph or plain agent loop for the "describe a feature"
   wish goal.

## References

- [itzg packwiz docs][itzg-packwiz]
- [Packwiz][packwiz]
- Pendulum (CurseForge) and its MCP / Baritone API
- Existing repo: `server/`, `bin/modpack-manager`, `WORKFLOW.md`

[itzg-packwiz]: https://docker-minecraft-server.readthedocs.io/en/latest/mods-and-plugins/packwiz/
[packwiz]: https://packwiz.infra.link/
