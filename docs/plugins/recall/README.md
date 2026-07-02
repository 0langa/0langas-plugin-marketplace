# RECALL

Local-first project memory plugin for Codex, Claude Code, and Kimi Code.

## Repository

https://github.com/0langa/RECALL

## Plugin Root

```text
plugins/RECALL/plugins/recall
```

## Install

### Codex

```powershell
codex plugin marketplace add C:\Users\Julius\source\repos\0langas-plugin-marketplace
codex plugin add recall@0langas-personal
```

### Claude Code

```powershell
claude plugin marketplace add C:\Users\Julius\source\repos\0langas-plugin-marketplace
claude plugin install recall@0langas-personal
```

### Kimi Code

```text
/plugins marketplace C:\Users\Julius\source\repos\0langas-plugin-marketplace\kimi-marketplace.json
```

Direct install fallback:

```text
/plugins install C:\Users\Julius\source\repos\0langas-plugin-marketplace\plugins\RECALL\plugins\recall
/reload
```
