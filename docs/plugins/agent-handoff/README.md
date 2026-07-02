# Agent Handoff

Cross-agent handoff plugin for Codex, Claude Code, and Kimi Code.

## Repository

https://github.com/0langa/agent-handoff-cck

## Install

### Codex

Install from the marketplace repo once submodules are initialized:

```powershell
codex plugin marketplace add C:\Users\Julius\source\repos\0langas-plugin-marketplace
codex plugin add agent-handoff@0langas-personal
```

### Claude Code

Install from the marketplace repo once submodules are initialized:

```powershell
claude plugin marketplace add C:\Users\Julius\source\repos\0langas-plugin-marketplace
claude plugin install agent-handoff@0langas-personal
```

### Kimi Code

Browse this custom marketplace inside Kimi Code:

```text
/plugins marketplace C:\Users\Julius\source\repos\0langas-plugin-marketplace\kimi-marketplace.json
```

Or install the source plugin checkout directly:

```text
/plugins install C:\Users\Julius\source\repos\0langas-plugin-marketplace\plugins\agent-handoff
/reload
```

Then use namespaced commands such as `/agent-handoff:status`.

## Private Repository Note

`agent-handoff-cck` is private. Remote install by URL only works in clients that can authenticate to GitHub. Local clone/submodule fallback:

```powershell
git submodule update --init --recursive
cd plugins\agent-handoff
uv sync --extra dev
uv run agent-handoff --help
```

## Validation

Validated on July 2, 2026:

- `uv run pytest`: 44 passed
- `claude plugin validate C:\Users\Julius\source\repos\agent-handoff-cck`: passed
- CLI provider flows for `codex`, `claude-code`, and `kimi-code`: passed
- Cross-provider flow `codex -> claude-code -> kimi-code`: passed
