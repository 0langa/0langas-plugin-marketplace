# Agent Handoff

Cross-agent handoff plugin for Codex, Claude Code, and Kimi Code.

## Repository

https://github.com/0langa/agent-handoff-cck

## Install

### Codex

```powershell
codex plugin marketplace add https://github.com/0langa/0langas-plugin-marketplace.git
codex plugin add agent-handoff@0langas-plugins
```

### Claude Code

```powershell
claude plugin marketplace add https://github.com/0langa/0langas-plugin-marketplace.git
claude plugin install agent-handoff@0langas-plugins
```

### Kimi Code

Browse this custom marketplace inside Kimi Code:

```text
/plugins marketplace C:\path\to\0langas-plugin-marketplace\kimi-marketplace.json
```

Or install the source plugin checkout directly:

```text
/plugins install C:\path\to\0langas-plugin-marketplace\plugins\agent-handoff
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

Validated on July 13, 2026:

- `uv run --extra dev pytest -q`: 72 passed
- Fresh Codex and Claude marketplace install from the pinned Git source: passed
