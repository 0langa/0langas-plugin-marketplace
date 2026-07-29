# addonry

Marketplace entry for `addonry`.

| Field | Value |
|---|---|
| Repository | `https://github.com/0langa/Addonry` |
| Local source | `plugins/addonry` |
| Providers | Codex, Claude Code, Kimi Code |
| Version | `0.1.0` |

## Install

```powershell
codex plugin marketplace add 0langa/0langas-plugin-marketplace
codex plugin add addonry@0langas-plugins
claude plugin marketplace add 0langa/0langas-plugin-marketplace
claude plugin install addonry@0langas-plugins
```

```text
/plugins install C:\path\to\0langas-plugin-marketplace\plugins\addonry
```

After installation, restart provider session and invoke manually:

- Codex: `$create-chrome-extension ...`
- Claude Code: `/addonry:create-chrome-extension ...`
- Kimi Code: `/skill:create-chrome-extension ...`
