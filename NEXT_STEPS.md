# Marketplace release status

Updated: 2026-09-09

## Current delivery

The six confirmed-bug patch releases are published: Computer Custom 0.1.6, Usage Pulse 0.1.9, Plugin Forge 0.2.13, Customization Control 0.1.5, Addonry 0.3.1, and Web.de Access 0.2.9. Every repository that defines CI passed it at the released commit; Customization Control passed its local Python and Pester checks.

The v1.0.21 marketplace candidate pins those exact release tags and full commit SHAs. Codex and Claude catalogs, the provider-neutral registry, and Kimi submodule paths agree. Fresh public-source install verification is in progress before the marketplace release tag is published.

No product decision blocks these patches. Addonry feature completion and Usage Pulse/Plugin Forge polish remain separate follow-up work. Computer Custom supports Codex and Claude Code; Kimi remains unsupported.

## Operator setup

All plugin source repositories are public. GitHub Actions checks out submodules anonymously; no CI secret is required. Existing provider enable/disable preferences are preserved during the isolated verification.

## Follow-up

- Finish public-source install verification and record the results with the v1.0.21 release.
- Continue unfinished product work only with its own scoped instructions.
