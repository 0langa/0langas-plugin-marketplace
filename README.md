# 0langa Plugin Marketplace

Private plugin marketplace for personal Codex, Claude Code, and Kimi Code plugins.

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

Source plugins live under `plugins/` as git submodules. Per-plugin notes live under `docs/plugins/`.

## Plugins

- [webde-access](docs/plugins/webde-access/README.md)
- [recall](docs/plugins/recall/README.md)
- [plugin-evaluation-kimi](docs/plugins/plugin-evaluation-kimi/README.md)
- [agent-handoff](docs/plugins/agent-handoff/README.md)

## Install From This Marketplace

### Codex

```powershell
codex plugin marketplace add C:\Users\Julius\source\repos\0langas-plugin-marketplace
codex plugin add webde-access@0langas-personal
codex plugin add recall@0langas-personal
codex plugin add plugin-evaluation-kimi@0langas-personal
codex plugin add agent-handoff@0langas-personal
```

### Claude Code

```powershell
claude plugin marketplace add C:\Users\Julius\source\repos\0langas-plugin-marketplace
claude plugin install webde-access@0langas-personal
claude plugin install recall@0langas-personal
claude plugin install plugin-evaluation-kimi@0langas-personal
claude plugin install agent-handoff@0langas-personal
```

### Kimi Code

Browse this custom marketplace inside Kimi Code, then install the plugins from the marketplace UI:

```text
/plugins marketplace C:\Users\Julius\source\repos\0langas-plugin-marketplace\kimi-marketplace.json
```

Direct install commands are also supported:

```text
/plugins install C:\Users\Julius\source\repos\0langas-plugin-marketplace\plugins\webde-access
/plugins install C:\Users\Julius\source\repos\0langas-plugin-marketplace\plugins\RECALL\plugins\recall
/plugins install C:\Users\Julius\source\repos\0langas-plugin-marketplace\plugins\plugin-evaluation-kimi
/plugins install C:\Users\Julius\source\repos\0langas-plugin-marketplace\plugins\agent-handoff
/reload
```
