# Changelog

## 2026-07-13

- Released Plugin Evaluation Kimi 0.1.2, Customization Control 0.1.2, Plugin Forge 0.2.2, Usage Pulse 0.1.3, and Computer Custom 0.1.3.
- Corrected duplicate Claude hook registration found by clean-room installation and made E2E fail on client-reported plugin load errors.
- Replaced Codex and Claude submodule-relative marketplace sources with HTTPS release refs pinned to full commit SHAs, allowing GitHub marketplace installs without submodule initialization.
- Added isolated Codex and Claude marketplace E2E installation coverage for all eight plugins.
- Expanded marketplace validation for remote source parity, immutable pins, safe subdirectories, and embedded-credential rejection.
- Updated install documentation for direct `0langa/0langas-plugin-marketplace` registration.
- Released Computer Custom 0.1.2 with restored Codex runtime compatibility, safer confirmation fallback, and expanded policy/audit tests.

## 2026-07-12

- Added ChatGPT-hosted Codex and GPT-5.6 compatibility evidence.
- Published visual metadata and assets across all eight plugins.
- Bumped artwork-bearing plugin releases so immutable caches receive metadata updates.
- Fixed Agent Handoff version parity and released Plugin Forge 0.2.0.
- Released Usage Pulse 0.1.1 with lossless provider hook generation.
- Added deterministic marketplace validation and GitHub Actions enforcement.
- Removed user-specific install paths and reconciled Computer Custom provider metadata.
- Recorded the 2026-07-06 PluginEval baseline artifacts.

## 2026-07-05

- Added marketplace registration for `plugin-forge`, `usage-pulse`, and `computer-custom`.
- Documented install commands for newly registered plugins.
- Synced submodule pointers after publish-readiness fixes in touched plugins.
