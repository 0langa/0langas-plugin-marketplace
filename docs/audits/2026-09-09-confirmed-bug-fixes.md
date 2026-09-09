# Plugin maintenance release verification — 2026-09-09

The audit led to six maintenance releases. This work fixes reproduced defects; Addonry feature completion and Usage Pulse/Plugin Forge polish remain separate work. No product decision is required for these patches.

## Released changes

| Plugin | Version | Repair |
| --- | --- | --- |
| Computer Custom | 0.1.6 | Use the current host-provided `@oai/sky` API; keep policy enforcement and legacy-client support; read the installed official documentation. |
| Usage Pulse | 0.1.9 | Accept public `from` arguments while dispatching Python `from_` correctly in `pulse.range` and `pulse.export`. |
| Plugin Forge | 0.2.13 | Discover versioned Claude/Codex caches, read Codex MCP registration from TOML, and recognize provider-specific hook discovery without inferring enabled state from cache presence. |
| Customization Control | 0.1.5 | Scan actual cache and Kimi managed layouts with the correct provider manifest; correct helper paths in the audit and dedupe skills. |
| Addonry | 0.3.1 | Keep runtime inputs local, preserve package-manager cache settings, and retain evidence-bound fixture bytes on Windows checkouts. |
| Web.de Access | 0.2.10 | Report the packaged MCP version, update vulnerable dependencies, approve only the pinned keytar native install script, and bootstrap dependencies from the Kimi entrypoint. |

Web.de 0.2.9 contained the initial version/dependency repairs. Fresh-install checks found two additional startup defects; 0.2.10 supersedes it. The immutable 0.2.9 release was retained.

## Verification

- 230 local unit tests passed across the six repositories; one optional Plugin Forge real-marketplace fixture was skipped. Usage Pulse coverage is 87.34%. Applicable Ruff, mypy, syntax, generated-output, public-safety, and dependency-audit checks passed.
- Web.de's additional cold-start integration test creates a package with no `node_modules`, invokes the actual Kimi entrypoint, verifies native keytar, and discovers 20 MCP tools. npm 12.0.2 runs this gate in CI. No mailbox access or mail sending is involved.
- Computer Custom passed real Codex host app/window discovery from its fresh published 0.1.6 install. The wrapper was distinct from the official API and no input actions were sent.
- Addonry CI includes real Chrome verification of a generated extension and toolbar/activeTab behavior. Local checkout filtering with Windows CRLF settings preserved the recorded digests for all 17 cross-browser fixture files.
- Direct MCP probes exercise initialization and tool discovery, plus four Usage Pulse range/export calls with result checks and Plugin Forge's read-only installed-plugin audit.
- Quick static evaluation ran for four edited skills. Those heuristic estimates do not certify end-user behavior or replace the runtime checks.

## Fresh-install findings

The native Codex and Claude install matrix passed for all nine plugins from the public HTTPS marketplace. The first Claude attempt exposed a Windows Git path-limit failure when MSIX expanded the test home under AppData. The test script now defaults to a short system-drive path on Windows and a temporary path on other systems. Its full native-provider run then passed.

Fresh Web.de runtime checks exposed npm 12's blocked native lifecycle script and Kimi's direct-server entrypoint. The package now records a version-pinned approval for `keytar@7.9.0` and all providers use dependency bootstrap. This follows npm's [project install-script approval policy](https://docs.npmjs.com/cli/v11/commands/npm-install-scripts/); no global allow-all policy was changed.

Final public-package checks passed: nine native Codex installs, nine native Claude installs with zero load errors, and eight Kimi managed-copy checks. All six MCP entrypoints initialized and listed tools in each provider layout (18 successful MCP checks). Usage Pulse's four data-checked calls and Plugin Forge's read-only audit also passed in all three layouts. Web.de 0.2.10 was reinstalled and retested after its follow-up release.

All nine published source manifests were fetched anonymously, and every release tag resolved to its catalog SHA. Full marketplace validation passed, including versions, provider membership, assets, source pins, submodules, and the public secret-signature scan. See the [portable verification record](2026-09-09-release-verification.json) for the tested catalog commit, exact catalog hashes, source SHAs, and provider results.

### Released source commits and CI

| Plugin | Release | Commit | CI |
| --- | --- | --- | --- |
| computer-custom | [v0.1.6](https://github.com/0langa/computer-custom/releases/tag/v0.1.6) | [353c9e8c](https://github.com/0langa/computer-custom/commit/353c9e8c0408fc53619da78a1e237397670b97fe) | [Passed](https://github.com/0langa/computer-custom/actions/runs/34384877543) |
| usage-pulse | [v0.1.9](https://github.com/0langa/usage-pulse/releases/tag/v0.1.9) | [a331dfe6](https://github.com/0langa/usage-pulse/commit/a331dfe691319f3d6cfca4652fab7ef2377ad633) | [Passed](https://github.com/0langa/usage-pulse/actions/runs/34384881207) |
| plugin-forge | [v0.2.13](https://github.com/0langa/plugin-forge/releases/tag/v0.2.13) | [72e72c4a](https://github.com/0langa/plugin-forge/commit/72e72c4a00e4cc50740fc9e8c218a20b92eb1703) | [Passed](https://github.com/0langa/plugin-forge/actions/runs/34384885430) |
| customization-control | [v0.1.5](https://github.com/0langa/customization-control/releases/tag/v0.1.5) | [6dc8caf2](https://github.com/0langa/customization-control/commit/6dc8caf232fe1dfb956a5d734e83d0c283828809) | No workflow; local Python/Pester checks passed |
| Addonry | [v0.3.1](https://github.com/0langa/Addonry/releases/tag/v0.3.1) | [84389db7](https://github.com/0langa/Addonry/commit/84389db7f1dedc569595f5b2beaad063227bb618) | [Passed](https://github.com/0langa/Addonry/actions/runs/34384893293) |
| Web.de Access | [v0.2.10](https://github.com/0langa/Web.de-Access/releases/tag/v0.2.10) | [192cad61](https://github.com/0langa/Web.de-Access/commit/192cad61288ae49f1c1c98bd13d6945abb2ac026) | [Passed](https://github.com/0langa/Web.de-Access/actions/runs/34387153699) |

## Scope and preserved state

- Codex and Claude are verified through their native marketplace installers. Kimi checks use isolated managed copies registered with Plugin Forge, then launch each declared MCP entrypoint directly; they do not claim a native Kimi CLI installation/UI test.
- Computer Custom is unsupported on Kimi and is absent from that catalog.
- Existing personal provider configuration, enabled/disabled settings, and credential stores were not changed. Long-running sessions still need normal plugin refresh and a new session to load updated code.
- The pre-existing Customization Control skill-path fixes are included. Its marketplace submodule's apparent dirty status was line-ending-only; the original bytes were preserved before moving to the released commit.
- An empty, unowned Git index lock dated 2026-08-28 was preserved under a backup name before retrying the Usage Pulse submodule checkout. No Git process was running.
- No unverified Firefox scenario, live mailbox operation, or product-polish completion is claimed.
