---
provider: codex
topic: chatgpt-plugin-runtime-2026-07
checked_at: 2026-07-12
stability: volatile
refresh_after_days: 1
sources:
  - url: https://learn.chatgpt.com/docs/changelog
    title: Codex changelog
  - url: https://learn.chatgpt.com/docs/plugins
    title: Plugins
  - url: https://learn.chatgpt.com/docs/build-plugins
    title: Build plugins
  - url: https://help.openai.com/en/articles/20001354-gpt-56-in-chatgpt
    title: GPT-5.6 in ChatGPT
  - url: https://help.openai.com/en/articles/11369540-using-codex-with-chatgpt
    title: Using Codex with your ChatGPT plan
claims:
  - Codex joined the ChatGPT desktop app on 2026-07-09; plugin management moved into Settings.
  - Repo marketplaces remain at .agents/plugins/marketplace.json; .claude-plugin/marketplace.json remains legacy-compatible.
  - Every Codex plugin still requires .codex-plugin/plugin.json and may bundle skills, apps, MCP servers, hooks, and assets.
  - Local plugins install into a versioned cache; source changes require reinstall or app restart, and bundled capabilities become available in a new task.
  - GPT-5.6 requires ChatGPT desktop app 26.707.30751 or Codex CLI 0.144.0 or newer.
  - Plugin execution uses host sandbox and approval policy; external services retain their own authentication and access controls.
used_by:
  - codex-chatgpt-compatibility-audit-2026-07-12
---

## Notes

GPT-5.6 changes model behavior and minimum client versions, not plugin manifest shape. Codex CLI 0.144 adds interactive MCP authentication and a read-only-versus-write app approval mode. Workspace app/plugin controls now apply across supported ChatGPT and Codex surfaces.
