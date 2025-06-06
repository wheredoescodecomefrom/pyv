# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.1.0] - 2025-06-05

### ✨ Added

- `pyv doctor`: diagnose environment issues (build tools, git, internet, PATH)
- `pyv exec`: run a command using a specific Python version
- `pyv link`: create a virtual environment from a specific version
- Global packages file (`~/.pyv/globals.txt`) — auto-installed on version install
- `pyv clean`: clean up build directories and temporary files
- Mirror support via `--mirror` option in `pyv install`
- Auto-switch behavior now smarter across nested `.python-version` folders

### 🛠 Changed

- Improved error reporting for failed installs and missing versions
- Better output formatting for `pyv list`
- Updated README with shell hook instructions and command examples

### 🐛 Fixed

- `pyv update` now handles missing `.git` directory gracefully
- Correct shim logic fallback when `.python-version` is not present
- `pyv list` no longer fails on non-directory files in `versions/`

---

## [1.0.0] - 2025-06-01

### 🚀 Initial release

- Install any version of Python from source
- Global and per-project version switching
- `.python-version` support for local version use
- `pyv install`, `use`, `list`, `current`, `uninstall`, `available`, `update`
- Install script via `curl | bash`
- GitHub Actions CI workflow
