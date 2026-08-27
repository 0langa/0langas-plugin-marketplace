# Changelog

## 2026-08-27 (v1.0.20)

- Released Addonry 0.3.0 with shared Chrome and Firefox Manifest V3 targeting, acceptance-driven repair loops, source-bound browser proof, and deterministic local packaging.
- Pinned Codex and Claude Code catalogs plus the Kimi Code submodule to immutable `v0.3.0` / `9600198104e411c9284c873d6c36ccf51a737a3e`.
- Reconciled stale Plugin Forge and Usage Pulse documentation with their already-published 0.2.12 and 0.1.8 catalog versions.

## 2026-08-19 (v1.0.19)

- Released RECALL 1.5.5. Its Codex manifest now declares the MCP server inline, so a Codex
  install registers RECALL's tools instead of loading only its skills; users who worked around
  this with a hand-written `[mcp_servers.recall]` block in `~/.codex/config.toml` should delete
  it after updating.
- Pinned the Codex and Claude Code catalogs plus the Kimi Code submodule to immutable `v1.5.5` /
  `c07e9766e5cb079e08787a1145a75749050da7a6`.

## 2026-08-05 (v1.0.18)

- Released Agent Handoff 0.2.5. Its Kimi Code Windows launcher now creates the project environment under Kimi's cache, avoiding stale managed-copy `.venv` links; the release also restores the documented `agent-handoff verify` CLI command.
- Pinned Codex and Claude Code catalogs plus the Kimi Code submodule to immutable `v0.2.5` / `1f5a4f3ebb33783b676c9f7222f661931dadb477`.

## 2026-08-05 (v1.0.17)

- Released Kimi Code MCP launcher repairs: Agent Handoff 0.2.4, Plugin Forge 0.2.12, and Usage Pulse 0.1.8 resolve the user-level Windows uv.exe before starting their Python MCP servers.
- Pinned Codex and Claude Code catalogs plus Kimi Code submodules to each repaired immutable tag and full commit SHA.

## 2026-08-05

- Released Addonry 0.2.1, Agent Handoff 0.2.3, Computer Custom 0.1.5, Customization Control 0.1.4, Plugin Evaluation Kimi 0.1.3, Plugin Forge 0.2.11, RECALL 1.5.4, Usage Pulse 0.1.7, and Web.de Access 0.2.8.
- Pinned every Codex and Claude Code marketplace source to its immutable release tag and full commit SHA; Kimi Code consumes the matching submodule checkouts.
- Removed 22 empty tracked stderr logs and ignored local RECALL project state.
- Normalized GitHub shorthand to HTTPS in published E2E tests and install documentation so Claude Code does not fall back to SSH for private marketplace clones.
- Reused an inherited GitHub authorization header in E2E instead of appending a duplicate header.
- Re-pinned Plugin Forge catalog entries and Kimi submodule checkout to immutable `v0.2.11` / `82352d01ab13924725340677b4caa5d9f08eab8d`.

## 2026-08-01

- Updated Addonry to 0.2.0 with source-bound final-ready evidence, real toolbar-action and activeTab verification, broader security validation, and hardened MCP/provider startup.
- Pinned Codex and Claude Code marketplace entries to immutable tag `v0.2.0` and commit `0cabdc6b694bf03e54b1c087bba92f75904895ee`; Kimi Code consumes same checked-out submodule.

## 2026-07-30

- Updated Addonry to 0.1.4 after branded Chrome 137+ removal of `--load-extension`; install helper now fails closed without changing browser processes.
- Replaced obsolete normal-Chrome restart/install claims with supported `chrome://extensions` **Load unpacked** guidance and explicit isolated-browser boundaries.
- Updated Addonry to 0.1.3 with durable personal extension storage and authorized graceful Chrome restart/load automation.
- Verified normal Chrome session restoration, command-line extension load, isolated real-Chrome extension behavior, and Chrome DevTools MCP startup.
- Preserved caller Git config overrides and added focused-plugin selection in marketplace E2E so external exFAT clean-room runs remain usable.

## 2026-07-29

- Updated Addonry to 0.1.2 with verified manual Kimi skill fallback for Kimi 0.29.x Windows command-registry failures.
- Updated Addonry to 0.1.1 with provider-native manual activation, safe MCP root resolution, and identity-based external runtime routing.
- Added Addonry 0.1.0 for Codex, Claude Code, and Kimi Code, pinned to immutable tag and full commit SHA.
- Added manual-only Chrome extension workflow with pinned Chrome DevTools MCP and real-Chrome verification.

## 2026-07-28

- Updated Codex marketplace pins for Web.de Access 0.2.7, Plugin Forge 0.2.7, and Usage Pulse 0.1.6.
- Updated Claude and registry metadata for Plugin Forge 0.2.7 and refreshed provider documentation.
- Verified full marketplace validation plus isolated Codex installation of all eight plugins.

## 2026-07-27

- Privacy hotfix: Web.de Access 0.2.4 removes the last literal workstation identity marker from public regression code.
- Hotfix: Plugin Forge 0.2.4 and Usage Pulse 0.1.5 now launch generated MCP servers from cached plugin project roots without host-directory editable installs.
- Released Computer Custom 0.1.4 with reliable official-first bootstrap, live Computer Use guidance, and confirmation-based administrative policy gates.
- Updated Codex and Claude Code marketplace pins to immutable tag `v0.1.4` and commit `3f984b7f53c32c349c26a8edf5eaa4fd6b919e6f`.
- Released Web.de Access 0.2.3 with generic credential migration names, redacted smoke output, dependency updates, and public-safety regression coverage.
- Released Customization Control 0.1.3, removing tracked handoff artifacts containing workstation paths.
- Released Plugin Forge 0.2.3 with public-data cleanup and reliable direct hook entrypoints.
- Released Usage Pulse 0.1.4, fixing Codex/Claude MCP startup and direct hook entrypoints.
- Released RECALL 1.5.3, removing workstation identity from manuals, baselines, and tests.
- Updated every changed Codex and Claude marketplace entry to immutable release tags and full commit SHAs.

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
