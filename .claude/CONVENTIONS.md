# HarleyColonies — Conventions

Repo-specific conventions. Anything not stated here follows the global
config.

## Sentinels

```text
auto-merge: enabled
resolve-task: autonomous
merge-finalization: enforce
team-managed: enabled
```

- **`auto-merge: enabled`** — invoking **push-pr** is consent through merge
  on green CI. The merge still obeys the `master` ruleset; the opt-in skips
  the prompt, not the checks. Read from the **default branch**, so it applies
  from the PR *after* the one that declares it. `delete_branch_on_merge` is
  on, as this sentinel requires.
- **`resolve-task: autonomous`** — **resolve-task** may skip its ask-gate for
  **trivial** items, after CI is green. Also read from the default branch.
- **`merge-finalization: enforce`** — merge-time finalization is a hard block,
  not a reminder: completed `[x]` items must be pruned and their issues closed
  before a merge lands.
- **`team-managed: enabled`** — the main thread acts as the PM/orchestrator
  and dispatches substantive edits to the owning role-subagent. The hook
  nudges; it never blocks. Read from the working tree, so it is live
  immediately.

## Versioning & tagging

**Method: `subdir`.** The two modpacks version independently and ship as
separate artifacts, so each is tagged on its own:

```text
harleycolonies-1.20.1/vX.Y.Z
harleycolonies-1.21.1/vX.Y.Z
```

- The authoritative version for a pack is the `version` field in its
  `pack.toml`; a tag records a release of that pack, and the two must agree.
- Both packs are pre-1.0, so **alpha rules apply** — breakage is expected and
  the `y.z` split is loose. Reaching `v1.0.0` is a deliberate decision, not a
  drift.
- Annotated tags only, at the merge commit on `master`, never moved once
  pushed.
- The repo carries **no tags yet**; the first release of either pack
  establishes the pattern. Use the **release-tag** skill.

Nothing in the repo outside the two pack directories is a shipped artifact,
so a repo-level `vX.Y.Z` tag would version nothing meaningful.

## Quality assurance

Concrete commands for this repo. Every `qa.md` dimension carries a status;
several are genuinely N/A for a wiki-plus-tooling repo with no runtime
surface.

| # | Dimension | Status | Notes |
| --- | --- | --- | --- |
| 1 | Format | **Active** | `pre-commit run --config .pre-commit-config-fix.yaml --all-files` |
| 2 | Lint | **Partial** | Markdown (markdownlint) and YAML/TOML/JSON syntax are Active. Python (`ruff`) and shell (`shellcheck`) are **Planned** — see the pre-commit phase-2 issue. |
| 3 | Type-check | **Off** | `bin/mpmanager/` carries no type annotations; adding them is not currently worth the churn. |
| 4 | Code smell / complexity | **Off** | Deferred until Python lint (dim 2) lands — `ruff` covers part of it. |
| 5 | Security | **Planned** | No SAST/SCA yet. `bin/requirements.txt` is unpinned, so there is nothing for SCA to resolve against; pinning is the prerequisite. |
| 6 | Tests | **Active (failing)** | `pytest bin/tests/` — **34 of 103 fail on `master`**, pre-existing: the fixtures assert an old `mods/` schema the code replaced. Tracked; not a required check until fixed. |
| 7 | UI/UX & accessibility | **N/A** | No UI. The wiki is Gollum-rendered Markdown. |
| 8 | End-to-end | **N/A** | No running application. |
| 9 | Compatibility | **Off** | The packs target fixed Minecraft/loader versions declared in `pack.toml`; there is no compatibility matrix to sweep. |
| 10 | Performance & load | **N/A** | No service, no measurable workload. |
| 11 | Reliability & observability | **N/A** | `server/docker-compose.yml` runs a third-party image; we do not operate it as a monitored service. |
| 12 | Build | **Planned** | Pack export (`packwiz`) is manual. No automated build or artifact check. |
| 13 | Documentation | **Active** | markdownlint via pre-commit; the doc bar in `documentation.md`. No changelog — the repo does not keep one. |
| 14 | Code review | **Off (informal)** | Solo repo. The `master` ruleset requires a PR but not an approval, so review is a self-review in practice. |
| 15 | CI | **Active** | `.github/workflows/ci.yml` — pre-commit and pytest jobs. |

## Markdown

- Prose wraps at **78 columns** (the global convention). `.markdownlint.json`
  sets MD013 to 200 so long **table rows and code lines** are not flagged —
  that is a tooling allowance, not permission to write 200-column prose.
- The wiki under `pages/` is rendered by **Gollum**, so intra-wiki links are
  page-relative and extensionless (`[Huts](style/huts)`), not `.md` paths.
- Each wiki page opens with a `--- title: ... ---` frontmatter block.

## Repo layout gotchas

- **`moddata/`** is the mod metadata and wiki store (`moddata/mods.yaml`,
  per-mod `wiki.md`). It was called `modpacks/` until #7 renamed it — that
  name collided with the actual packs. Inside it, `moddata/<pack-name>/`
  holds per-modpack *state* (`info.yaml`, `mods.yaml`) and shares its name
  with the real pack at the repo root; they are different things.
- **`archive/`** is retained historical config, not live content.
