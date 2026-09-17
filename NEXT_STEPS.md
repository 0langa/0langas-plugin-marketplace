# Marketplace release status

Updated: 2026-09-17

## Released

Marketplace **v1.0.22** updates RECALL to the published **1.6.0** release.
The Codex and Claude Code catalog pins and the Kimi Code submodule agree on
`v1.6.0` / `c2452a48845dfc72a3461076ec833f249326ba02`.
Every other plugin version and source pin remains unchanged.

Fresh full marketplace validation passed for all nine plugin entries and three
provider catalogs. Fresh isolated Codex and Claude Code installs of RECALL 1.6.0
passed from the candidate catalog. Both installed entrypoints initialized,
reported version 1.6.0, exposed all eight MCP tools, and returned the memory
contract. Claude reported no plugin load errors.

These are installation and direct MCP entrypoint checks. The native model
behavior limits listed in the [RECALL release report](https://github.com/0langa/RECALL/releases/tag/v1.6.0)
remain unchanged. The delivery checks below describe the previous all-plugin
v1.0.21 audit.

## Previous release

Marketplace **v1.0.21** publishes the verified bug-fix set: Computer Custom 0.1.6, Usage Pulse 0.1.9, Plugin Forge 0.2.13, Customization Control 0.1.5, Addonry 0.3.1, and Web.de Access 0.2.10. RECALL 1.5.5, Agent Handoff 0.2.5, and Plugin Evaluation Kimi 0.1.3 remain current.

No product decision or known release blocker remains for these patches. Addonry feature completion and Usage Pulse/Plugin Forge polish remain separate work.

## Verified delivery

- Codex and Claude native marketplace installs passed for all nine plugins; Claude reported zero plugin load errors.
- Eight Kimi managed-copy checks passed. Kimi verification uses Plugin Forge registration and direct MCP startup, without claiming a native Kimi CLI/UI installation test.
- All six MCP entrypoints initialized in each of the three provider layouts, including the Web.de 0.2.10 cold-start fix.
- 230 local unit tests passed, one optional fixture was skipped, and the additional Web.de cold-start integration passed. All five plugin repositories with CI passed their release checks; Customization Control passed local Python/Pester checks.
- All nine public source manifests and immutable release pins were verified. The provider-neutral registry and all three provider catalogs agree.
- Computer Custom passed real host discovery from its fresh install. Addonry passed its real Chrome CI scenarios.

The [release report](docs/audits/2026-09-09-confirmed-bug-fixes.md) and [portable verification record](docs/audits/2026-09-09-release-verification.json) contain the changes, versions, source SHAs, CI links, and exact verification limits.

## Existing sessions

Personal provider configuration and enable/disable preferences were preserved. Refresh the marketplace through the provider's normal update flow and start a new session to load the published versions. Computer Custom remains unsupported on Kimi.
