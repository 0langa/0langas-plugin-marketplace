# Marketplace release status

Updated: 2026-09-09

## Released

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
