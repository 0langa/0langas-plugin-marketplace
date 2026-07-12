# Customization Control

Audit, deduplicate, repair, sync, and manage agent customizations across Codex, Claude Code, and Kimi Code.

## Repository

https://github.com/0langa/customization-control

## Install

### Codex

Install from the marketplace repo once submodules are initialized:

```powershell
codex plugin marketplace add .
codex plugin add customization-control@0langas-plugins
```

### Claude Code

Install from the marketplace repo once submodules are initialized:

```powershell
claude plugin marketplace add .
claude plugin install customization-control@0langas-plugins
```

### Kimi Code

Browse this custom marketplace inside Kimi Code:

```text
/plugins marketplace C:\path\to\0langas-plugin-marketplace\kimi-marketplace.json
```

Or install the source plugin checkout directly:

```text
/plugins install C:\path\to\0langas-plugin-marketplace\plugins\customization-control
```

## Skills

| Skill | Purpose |
|---|---|
| customization-audit | Inventory all customizations, detect issues, route to narrower skills |
| customization-dedupe | Remove identical duplicates with dry-run plan and quarantine |
| customization-sync | Create/repair provider discovery symlinks |
| customization-repair | Fix broken symlinks, invalid manifests, stale entries |
| marketplace-manager | Validate/update marketplace.json entries |
| windows-customization-guard | Windows path safety (internal, auto-invoked) |

## Version

0.1.0
