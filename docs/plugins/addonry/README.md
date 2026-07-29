# addonry

Marketplace entry for `addonry`.

| Field | Value |
|---|---|
| Repository | `https://github.com/0langa/Addonry` |
| Local source | `plugins/addonry` |
| Providers | Codex, Claude Code, Kimi Code |
| Version | `0.1.2` |

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

- Codex: `$addonry:create-chrome-extension ...`
- Claude Code: `/addonry:create-chrome-extension ...`
- Kimi Code: `/addonry:create-chrome-extension ...`
- Kimi Code 0.29.x Windows fallback: `/skill:create-chrome-extension ...`
