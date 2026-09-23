# Marketplace release status

Updated: 2026-09-23

## Open: new plugin logos (not released)

A new logo set for all nine plugins is approved and committed to the marketplace
`assets/<plugin>/{icon.png,logo.png}` (1024 px, transparent corners). Addonry got
its first `assets/addonry/` folder; it still has no `screenshot-1.png`. The plugin
repositories and their Codex manifests still carry the old art. Do not release
until the owner asks.

Remaining work, one plugin at a time, when the owner starts it:

1. Copy the new art into each plugin repository. `dormant/plugin-asset-kit` does
   this (`plugin-asset-kit sync`, dry-run first, then `sync --apply --plugin <name>`).
   Its built-in default still points at the pre-2026-08-24 path
   `C:\Users\Julius\source\repos\0langas-plugin-marketplace`; pass the current
   `maintained\` path explicitly.
2. Computer Custom has no `brandColor` in its Codex manifest. The logo uses `#E0457B`.
3. Each plugin then needs its own commit and release, and this marketplace needs
   the usual pin update and validation.

Source of the set: `docs/logo-explorations/round-4-final/`. `final.py` draws every
mark and the preview `final.html`; `render.mjs` turns `svg/` into `png/` with
`@resvg/resvg-js` (install it in a scratch folder, not here). Design rules the owner
set: brand disc with thin ring, one fold crease (lit upper left), a hard two-ink
split, no stray slivers or jogs. Earlier rounds 1-3 are kept local only and are
excluded through `.git/info/exclude`.

## Released

Marketplace **v1.0.24** updates Computer Custom to the published **0.2.1**
Codex MCP registration fix. The Codex and Claude Code catalogs and the development
submodule agree on `v0.2.1` / `136e1059de6d7629202a693ccc98d22046559939`.
Computer Custom remains intentionally unsupported on Kimi Code.

Fresh full marketplace validation passed for all nine plugin entries and three
provider catalogs. Fresh isolated Codex and Claude Code installs of Computer
Custom 0.2.1 passed from the candidate catalog. Both provider packages register
the bundled MCP server. The packaged server initialized directly, exposed all
24 tools, and returned live helper status.

The source release passed 110 local tests, the public-safety scan, packaging,
signed-helper verification, and its GitHub CI. Existing sessions still need a
marketplace refresh and client restart before they load the new plugin copy.

## Previous release

Marketplace **v1.0.23** updates Computer Custom to the published **0.2.0**
self-contained rebuild. The Codex and Claude Code catalogs and the development
submodule agree on `v0.2.0` / `91b2bd0c9bc7b2dbcc4c545aacbe10671730896e`.
Computer Custom remains intentionally unsupported on Kimi Code.

## Earlier release

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
