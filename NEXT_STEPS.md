# Marketplace release status

Updated: 2026-09-19

## Released

Marketplace **v1.0.23** updates Computer Custom to the published **0.2.0**
self-contained rebuild. The Codex and Claude Code catalogs and the development
submodule agree on `v0.2.0` / `91b2bd0c9bc7b2dbcc4c545aacbe10671730896e`.
Computer Custom remains intentionally unsupported on Kimi Code.

Fresh full marketplace validation passed for all nine plugin entries and three
provider catalogs. Fresh isolated Codex and Claude Code installs of Computer
Custom 0.2.0 passed from the candidate catalog. Claude registered the bundled
MCP server with no plugin load error. The packaged server initialized directly,
exposed all 24 tools, and returned live helper status.

The source release passed 109 local tests, the public-safety scan, packaging,
signed-helper verification, and its GitHub CI. Existing sessions still need a
marketplace refresh and client restart before they load the new plugin copy.

## Previous release

Marketplace **v1.0.22** updates RECALL to the published **1.6.0** release. The
Codex and Claude Code catalog pins and the Kimi Code submodule agree on
`v1.6.0` / `c2452a48845dfc72a3461076ec833f249326ba02`.

Every other plugin version and source pin remained unchanged in v1.0.22.

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
