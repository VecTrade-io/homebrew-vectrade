# homebrew-vectrade

[![CI](https://github.com/VecTrade-io/homebrew-vectrade/actions/workflows/ci.yml/badge.svg)](https://github.com/VecTrade-io/homebrew-vectrade/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/VecTrade-io/homebrew-vectrade)](LICENSE)

Official [Homebrew](https://brew.sh/) tap for the [VecTrade CLI](https://github.com/VecTrade-io/vectrade-cli).

## Quick Start

```bash
# Add the tap
brew tap VecTrade-io/vectrade

# Install the CLI
brew install vectrade
```

## Usage

```bash
# Verify installation
vectrade version

# Get help
vectrade --help

# Example: fetch a quote
vectrade quote AAPL
```

## Upgrade

```bash
brew update
brew upgrade vectrade
```

## Uninstall

```bash
brew uninstall vectrade
brew untap VecTrade-io/vectrade
```

## Shell Completions

The formula installs shell completions for **bash**, **zsh**, and **fish** automatically.

If completions don't load automatically, restart your shell or source the completion file:

```bash
# bash
source $(brew --prefix)/etc/bash_completion.d/vectrade

# zsh (usually automatic if using brew's site-functions)
autoload -U compinit && compinit
```

## Platform Support

| OS    | Architecture | Status |
|-------|-------------|--------|
| macOS | Intel (x86_64) | ✅ |
| macOS | Apple Silicon (arm64) | ✅ |
| Linux | x86_64 | ✅ |
| Linux | arm64 | ✅ |

## How It Works

This tap is automatically updated by [GoReleaser](https://goreleaser.com/) when a new CLI version is released. Formula files are pushed here by the CI pipeline — do not edit them manually.

## Issues & Support

Please file bugs and feature requests on the **[vectrade-cli](https://github.com/VecTrade-io/vectrade-cli/issues)** repository.

## Links

- [VecTrade CLI](https://github.com/VecTrade-io/vectrade-cli) — source repository
- [Documentation](https://docs.vectrade.io/sdks/cli) — CLI usage guide
- [Releases](https://github.com/VecTrade-io/vectrade-cli/releases) — all CLI versions
- [Contributing](CONTRIBUTING.md) — how this repo is structured

## License

MIT — see [LICENSE](LICENSE).
