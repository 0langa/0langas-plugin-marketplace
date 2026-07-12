# 0langa Plugin Marketplace

Private plugin marketplace for 0langa's Codex, Claude Code, and Kimi Code plugins.

This repository keeps provider-specific marketplace files in one place while using the source plugin repositories as submodules.

## Setup

```powershell
git clone https://github.com/0langa/0langas-plugin-marketplace.git
cd 0langas-plugin-marketplace
git submodule update --init --recursive
```

Private submodules require GitHub authentication.

## Registry

Provider-neutral plugin metadata lives in `plugins.json`.

Provider-native marketplace files:

- Codex: `.agents/plugins/marketplace.json`
- Claude Code: `.claude-plugin/marketplace.json`
- Kimi Code: `kimi-marketplace.json`

Codex now runs inside the ChatGPT desktop app. This repo layout remains current:
ChatGPT reads `.agents/plugins/marketplace.json`, installs versioned plugin copies
under `~/.codex/plugins/cache/`, and loads newly installed skills/tools in a new
task. After changing a local plugin, reinstall it or restart ChatGPT before testing.

Source plugins live under `plugins/` as git submodules. Per-plugin notes live under `docs/plugins/`.

## Validate Before Publishing

```powershell
./scripts/validate-marketplace.ps1
```

Validation checks catalog uniqueness, provider parity, submodule roots, manifest
versions, declared assets, portable install examples, and high-confidence secret
signatures. Without extra credentials, GitHub Actions checks catalog parity,
portability, pinned gitlinks, and secret hygiene. Configure a least-privileged
`MARKETPLACE_SUBMODULE_TOKEN` with read access to the private plugin repositories
to add full manifest and asset validation.

## Plugins

- [webde-access](docs/plugins/webde-access/README.md)
- [recall](docs/plugins/recall/README.md)
- [plugin-evaluation-kimi](docs/plugins/plugin-evaluation-kimi/README.md)
- [agent-handoff](docs/plugins/agent-handoff/README.md)
- [customization-control](docs/plugins/customization-control/README.md)
- [plugin-forge](docs/plugins/plugin-forge/README.md)
- [usage-pulse](docs/plugins/usage-pulse/README.md)
- [computer-custom](docs/plugins/computer-custom/README.md)

## Install From This Marketplace

### Codex

```powershell
codex plugin marketplace add .
codex plugin add webde-access@0langas-plugins
codex plugin add recall@0langas-plugins
codex plugin add plugin-evaluation-kimi@0langas-plugins
codex plugin add agent-handoff@0langas-plugins
codex plugin add customization-control@0langas-plugins
codex plugin add plugin-forge@0langas-plugins
codex plugin add usage-pulse@0langas-plugins
codex plugin add computer-custom@0langas-plugins
```

### Claude Code

```powershell
claude plugin marketplace add .
claude plugin install webde-access@0langas-plugins
claude plugin install recall@0langas-plugins
claude plugin install plugin-evaluation-kimi@0langas-plugins
claude plugin install agent-handoff@0langas-plugins
claude plugin install customization-control@0langas-plugins
claude plugin install plugin-forge@0langas-plugins
claude plugin install usage-pulse@0langas-plugins
claude plugin install computer-custom@0langas-plugins
```

### Kimi Code

Browse this custom marketplace inside Kimi Code, then install the plugins from the marketplace UI:

```text
/plugins marketplace C:\path\to\0langas-plugin-marketplace\kimi-marketplace.json
```

Direct install commands are also supported:

```text
/plugins install C:\path\to\0langas-plugin-marketplace\plugins\webde-access
/plugins install C:\path\to\0langas-plugin-marketplace\plugins\RECALL\plugins\recall
/plugins install C:\path\to\0langas-plugin-marketplace\plugins\plugin-evaluation-kimi
/plugins install C:\path\to\0langas-plugin-marketplace\plugins\agent-handoff
/plugins install C:\path\to\0langas-plugin-marketplace\plugins\customization-control
/plugins install C:\path\to\0langas-plugin-marketplace\plugins\plugin-forge
/plugins install C:\path\to\0langas-plugin-marketplace\plugins\usage-pulse
/reload
```
