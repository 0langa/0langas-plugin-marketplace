# Web.de Access

Private Web.de mailbox connector for Codex, Claude Code, and Kimi Code.

## Repository

https://github.com/0langa/Web.de-Access

## Plugin Root

```text
plugins/webde-access
```

## Install

### Codex

```powershell
codex plugin marketplace add 0langa/0langas-plugin-marketplace
codex plugin add webde-access@0langas-plugins
```

### Claude Code

```powershell
claude plugin marketplace add 0langa/0langas-plugin-marketplace
claude plugin install webde-access@0langas-plugins
```

### Kimi Code

```text
/plugins marketplace C:\path\to\0langas-plugin-marketplace\kimi-marketplace.json
```

Direct install fallback:

```text
/plugins install C:\path\to\0langas-plugin-marketplace\plugins\webde-access
/reload
```

## Notes

Keep mailbox credentials in local environment files or provider secret storage. Do not commit `.env` or exported mailbox data into this marketplace.
