# Marketplace release status

Updated: 2026-07-12

## Completed in current release

- Eight plugin repositories carry marketplace artwork and current Codex metadata.
- Agent Handoff provider versions agree at 0.2.2.
- Plugin Forge 0.2.0 fixes hosted MCP status and adds lossless provider-specific hook generation.
- Usage Pulse 0.1.1 round-trips provider hooks through Forge without losing provider identity.
- Codex, Claude Code, Kimi Code, and provider-neutral catalogs agree on supported plugins and versions.
- Computer Custom is declared for Codex and Claude Code; Kimi remains unsupported.
- Install examples use portable paths.
- Marketplace validator checks manifests, assets, provider parity, versions, submodules, and secret signatures.
- GitHub Actions runs marketplace validation on pushes and pull requests.
- 2026-07-06 PluginEval baseline and 2026-07-12 ChatGPT/Codex compatibility evidence are preserved.

## Operator setup

Configure repository secret `MARKETPLACE_SUBMODULE_TOKEN` with read-only access to all private plugin repositories. GitHub Actions needs it to clone private submodules.

## Optional follow-up

- Re-run PluginEval after improving low-activation Customization Control skills.
- Add automated release notes and submodule pointer update tooling to Plugin Forge.
- Remove obsolete versioned plugin cache directories after no ChatGPT tasks hold them open.
