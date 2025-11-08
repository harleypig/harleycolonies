# Mod Manager Tests

Tests for the mod-manager script using pytest.

## Running Tests

From the repository root:

```bash
# Install test dependencies
pip install -r requirements.txt

# Run all tests
pytest bin/tests/

# Run specific test file
pytest bin/tests/test_data.py

# Run with verbose output
pytest bin/tests/ -v

# Run with coverage
pytest bin/tests/ --cov=mod_manager --cov-report=html
```

## Test Structure

- `conftest.py` - Pytest fixtures and configuration
- `test_data.py` - Tests for data management (YAML operations)
- `test_commands.py` - Tests for command implementations
- `test_packwiz.py` - Tests for packwiz integration
- `test_wiki.py` - Tests for wiki page generation
- `test_validation.py` - Tests for validation functions
- `test_sync.py` - Tests for sync functionality
- `test_integration.py` - Integration tests for full workflows

## Fixtures

- `temp_repo` - Creates a temporary repository structure
- `sample_mod_data` - Sample mod data for testing
- `sample_modpack_dir` - Sample modpack directory structure
- `sample_mod_toml` - Sample mod .pw.toml file

