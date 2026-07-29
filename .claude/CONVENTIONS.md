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

## Deliverability — nothing ships yet

**Nothing in this repo is currently deliverable.** It is the consolidation of
several earlier attempts, and every piece is still being brought under
control. That is the governing constraint for the sections below:

- **Do not build release machinery ahead of a deliverable.** No tags, no
  version bumps, no publish workflow until the thing being released exists in
  shippable form.
- **Add checks per piece, not repo-wide.** A pre-commit hook or CI job is
  added when a piece stabilizes, scoped to that piece. A gate over
  unconsolidated code produces noise that gets ignored or worked around,
  which is worse than no gate — the phase-1 baseline is deliberately narrow
  for exactly this reason.

Asked whether something should be gated, versioned, or released, the default
answer is **not yet**; establish which piece is under control first.

## What this repo owns, and what it does not

**packwiz controls how the modpack is built.** This repo *stores modpack
information* — mod metadata in `moddata/`, per-mod config and wiki sources.
The build is packwiz's job.

The user maintains a fork, **`harleypig/packwiz`** (upstream
`packwiz/packwiz`), cloned at `~/projects/minecraft/packwiz/packwiz`. So
packwiz's behaviour is **changeable**, not fixed.

When a need would be better handled by packwiz, **file it as an issue on the
fork** rather than building a workaround here. Growing local tooling around a
build concern is how the retired `mpmanager` layer came about.

## Versioning & tagging

**Method: `subdir`** — each shippable component versions independently and is
tagged on its own, as `<component>/vX.Y.Z`.

**No component qualifies yet, so the repo carries no tags and none should be
cut.** This section records the intended scheme so it is not reinvented; it
is not a process to start using.

Components that will eventually need a version stream:

- the two packwiz packs — authoritative version is the `version` field in
  each `pack.toml`
- **Lazybones**, once it exists as a style pack rather than a design
  document. It is meant to be usable on other people's servers, so it is a
  distributable artifact in its own right and will need a `pack.json`
  version (see `pages/style/style-packs.md`). Its tag prefix is
  **undecided** — settle that when the pack is real.

When tagging does begin: annotated tags only, at the merge commit on
`master`, never moved once pushed; pre-1.0 means **alpha rules** (breakage
expected, loose `y.z`), and reaching `v1.0.0` is a deliberate decision. Use
the **release-tag** skill.

## Quality assurance

Concrete commands for this repo. Every `qa.md` dimension carries a status.

Read these against *nothing ships yet*, above: a **Planned** here means "when
that piece is under control", not "soon". Statuses are per-piece, so a
dimension can be Active for the wiki and Off for the server at the same time.

| # | Dimension | Status | Notes |
| --- | --- | --- | --- |
| 1 | Format | **Active** | `pre-commit run --config .pre-commit-config-fix.yaml --all-files` |
| 2 | Lint | **Partial** | Markdown (markdownlint) and YAML/TOML/JSON syntax are Active. Python (`ruff`) and shell (`shellcheck`) are **Planned** — see the pre-commit phase-2 issue. |
| 3 | Type-check | **Off** | `bin/mpmanager/` carries no type annotations; adding them is not currently worth the churn. |
| 4 | Code smell / complexity | **Off** | Deferred until Python lint (dim 2) lands — `ruff` covers part of it. |
| 5 | Security | **Planned** | No SAST/SCA yet. `bin/requirements.txt` is unpinned, so there is nothing for SCA to resolve against; pinning is the prerequisite. |
| 6 | Tests | **Active (failing)** | `pytest bin/tests/` — **34 of 103 fail on `master`**, pre-existing: the fixtures assert an old `mods/` schema the code replaced. Tracked; not a required check until fixed. |
| 7 | UI/UX & accessibility | **N/A** | No UI. The wiki is Gollum-rendered Markdown. |
| 8 | End-to-end | **Off** | There *is* a running application — the server plus a pack a player actually loads — so this is not N/A. Nothing exercises that path today; verification is manual. |
| 9 | Compatibility | **Planned** | Each pack targets a fixed Minecraft/loader pair, but **Lazybones** is meant to run on other people's servers, so it will need a real compatibility story once it is a pack. |
| 10 | Performance & load | **Off** | The server is small and single-purpose; no measured workload today. Not N/A — it is a running service, just not one under load pressure. |
| 11 | Reliability & observability | **Planned** | The server (`server/`) is **operated**, not merely configured, so this applies. Nothing is monitored yet — no health checks, no alerting. |
| 12 | Build | **Off** | The modpack build belongs to **packwiz**, not this repo (see above). Automating an export here would be building the wrong thing in the wrong place. |
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
