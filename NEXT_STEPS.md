# Marketplace release status

Updated: 2026-08-05

## Completed in current release

- Marketplace v1.0.18 pins Agent Handoff 0.2.5, Plugin Forge 0.2.12, and Usage Pulse 0.1.8. Agent Handoff now creates its Kimi runtime environment under Kimi's cache, avoiding stale managed-copy `.venv` links; all launchers resolve user-level Windows uv.exe when Kimi child PATH omits it.
- Other source releases remain current: Addonry 0.2.1, Computer Custom 0.1.5, Customization Control 0.1.4, Plugin Evaluation Kimi 0.1.3, RECALL 1.5.4, and Web.de Access 0.2.8.
- Codex and Claude Code catalogs pin every source to its release tag and full commit SHA; Kimi Code consumes the same checked-out submodules.
- Codex, Claude Code, Kimi Code, and provider-neutral catalogs agree on supported plugins and versions.
- Computer Custom is declared for Codex and Claude Code; Kimi remains unsupported.
- Install examples use portable paths.
- Marketplace validator checks manifests, assets, provider parity, versions, submodules, and secret signatures.
- GitHub Actions runs marketplace validation on pushes and pull requests.
- 2026-07-06 PluginEval baseline and 2026-07-12 ChatGPT/Codex compatibility evidence are preserved.
- Removed 22 empty tracked stderr logs and ignored local RECALL project state.

## Operator setup

Optionally configure repository secret `MARKETPLACE_SUBMODULE_TOKEN` with read-only access to all private plugin repositories. CI is useful without it and adds full manifest/asset validation when it is present.

## Optional follow-up

- Reconcile active Codex, Claude Code, and Kimi Code installs from this published marketplace release.
- Re-run PluginEval after improving low-activation Customization Control skills.
