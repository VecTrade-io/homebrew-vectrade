# Contributing to homebrew-vectrade

## Overview

This repository contains the official [Homebrew](https://brew.sh/) tap for the VecTrade CLI.

**This tap is auto-generated.** Formula files are pushed by [GoReleaser](https://goreleaser.com/) when a new [vectrade-cli](https://github.com/VecTrade-io/vectrade-cli) release is published. Manual edits to `Formula/vectrade.rb` will be overwritten.

## Repository Structure

```
homebrew-vectrade/
├── Formula/
│   └── vectrade.rb          # Homebrew formula (auto-generated)
├── .github/
│   └── workflows/
│       └── ci.yml            # CI validation pipeline
├── tests/
│   └── test_formula.py       # Formula structure validation
├── pytest.ini                # Test configuration
├── CONTRIBUTING.md           # This file
├── README.md                 # User-facing docs
├── LICENSE                   # MIT
└── .gitignore
```

## How Releases Work

1. A new tag is pushed to `vectrade-cli` (e.g., `v0.2.0`).
2. GoReleaser builds binaries for all platforms.
3. GoReleaser generates `Formula/vectrade.rb` with correct URLs and SHA256 hashes.
4. GoReleaser pushes the formula to this repo's `main` branch.

## Running Tests Locally

```bash
# Install pytest
pip install pytest

# Run all validation tests
pytest tests/ -v
```

## What the Tests Validate

- Formula file exists and is non-empty
- Correct class naming convention (filename ↔ class name)
- Required fields present: `desc`, `homepage`, `version`, `license`, `url`, `sha256`
- URLs point to correct GitHub releases
- Multi-platform support (macOS + Linux, amd64 + arm64)
- Shell completions (bash, zsh, fish) are installed
- Test block verifies `version` and `--help`
- Ruby syntax conventions (2-space indent, no tabs, frozen_string_literal)

## When to Manually Edit

You should only edit this repo to:

- Update CI workflows
- Add/improve validation tests
- Fix README or docs

**Never** manually edit `Formula/vectrade.rb` — it will be overwritten on next release.
