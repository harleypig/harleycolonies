# HarleyColonies — Tests

## Layout

Single language, so the tests sit idiomatically beside the package they
cover rather than in a repo-root `tests/`:

```text
bin/
    mpmanager/          the package under test
    tests/
        conftest.py     shared fixtures
        test_*.py       13 modules, one per area
```

Areas covered: `cli`, `commands`, `data`, `integration`, `metadata`,
`packwiz`, `side_command`, `sync`, `toml_updates`, `validation`, `wiki`,
`wiki_clear`.

## Running

```bash
cd bin
python3 -m venv venv && venv/bin/pip install -r requirements.txt
venv/bin/python -m pytest tests/ -q
```

`bin/venv/` is gitignored. CI installs `bin/requirements.txt` and runs the
same command.

There is no `pytest.ini` / `[tool.pytest]` section — pytest runs on defaults,
which is why the commands above `cd bin` first (so `mpmanager` imports).

## Fixtures

`conftest.py` provides `temp_repo`, an **autouse** fixture: it builds a
throwaway repo tree under `tmp_path` and points the code at it, so no test
touches real repository files. Because it is autouse, every test gets it
whether or not it asks — meaning a change to that fixture's layout affects
the entire suite at once.

## Known failure: the suite is red on `master`

**34 of 103 tests fail**, and have been failing before any conventions work.
This is fixture drift, not flaky tests:

- `conftest.py` builds a `mods/` directory and mod entries with a flat
  schema.
- The code moved to `modpacks/` (`data.py` resolves
  `get_repo_root() / "modpacks" / "mods.yaml"`) and to a nested schema with
  `mod["modpacks"]` and `mod["side"]`.

So the failures surface as `KeyError: 'modpacks'`, `KeyError: 'side'`, and
path assertions against `mods/`. The 69 passing tests are the ones that never
touch the changed schema.

Consequences to respect:

- **pytest is not a required check** on the `master` ruleset — a permanently
  red required check would block every merge, including auto-merge. It runs
  and reports; it does not gate.
- Until it is fixed, **a green CI badge does not mean the tooling is
  verified**. Treat `bin/mpmanager/` changes as effectively untested and lean
  on manual verification.
- Fixing the fixtures is tracked as an issue, and promoting pytest to a
  required check is the closing step of that work.

## The bar

Per the global `testing.md`: cover success and failure paths, and each bug
fix lands a regression test that fails before the fix. New tests should use
the current `modpacks/` schema — do not copy the stale fixture patterns from
the failing modules.
