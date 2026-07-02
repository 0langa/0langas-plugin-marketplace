# Plugin Evaluation Kimi

Three-layer quality evaluation plugin for agent plugins and skills.

## Repository

https://github.com/0langa/plugin-evaluation-kimi

## Plugin Root

```text
plugins/plugin-evaluation-kimi
```

## Install

### Codex

```powershell
codex plugin marketplace add C:\Users\Julius\source\repos\0langas-plugin-marketplace
codex plugin add plugin-evaluation-kimi@0langas-plugins
```

### Claude Code

```powershell
claude plugin marketplace add C:\Users\Julius\source\repos\0langas-plugin-marketplace
claude plugin install plugin-evaluation-kimi@0langas-plugins
```

### Kimi Code

```text
/plugins marketplace C:\Users\Julius\source\repos\0langas-plugin-marketplace\kimi-marketplace.json
```

Direct install fallback:

```text
/plugins install C:\Users\Julius\source\repos\0langas-plugin-marketplace\plugins\plugin-evaluation-kimi
/reload
```
