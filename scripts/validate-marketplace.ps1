[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repoRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot ".."))
$errors = [System.Collections.Generic.List[string]]::new()

function Add-ValidationError([string]$Message) {
    $script:errors.Add($Message)
}

function Read-JsonFile([string]$RelativePath) {
    $path = Join-Path $repoRoot $RelativePath
    try {
        return Get-Content -LiteralPath $path -Raw | ConvertFrom-Json
    }
    catch {
        Add-ValidationError "$RelativePath is not valid JSON: $($_.Exception.Message)"
        return $null
    }
}

function Test-UniqueNames([object[]]$Values, [string]$Surface) {
    foreach ($duplicate in @($Values | Group-Object | Where-Object Count -gt 1)) {
        Add-ValidationError "$Surface contains duplicate plugin '$($duplicate.Name)'"
    }
}

function Resolve-PluginRoot([string]$RelativePath, [string]$PluginName) {
    if (-not $RelativePath.StartsWith("./")) {
        Add-ValidationError "$PluginName source must start with './': $RelativePath"
    }
    $resolved = [IO.Path]::GetFullPath((Join-Path $repoRoot $RelativePath))
    if (-not $resolved.StartsWith($repoRoot + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) {
        Add-ValidationError "$PluginName source escapes marketplace root"
        return $null
    }
    if (-not (Test-Path -LiteralPath $resolved -PathType Container)) {
        Add-ValidationError "$PluginName source directory is missing: $RelativePath"
        return $null
    }
    return $resolved
}

function Read-PluginManifest([string]$PluginRoot, [string]$RelativePath, [string]$PluginName) {
    $path = Join-Path $PluginRoot $RelativePath
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        Add-ValidationError "$PluginName manifest is missing: $RelativePath"
        return $null
    }
    try {
        return Get-Content -LiteralPath $path -Raw | ConvertFrom-Json
    }
    catch {
        Add-ValidationError "$PluginName manifest is invalid JSON: $RelativePath"
        return $null
    }
}

$registry = Read-JsonFile "plugins.json"
$codexMarketplace = Read-JsonFile ".agents/plugins/marketplace.json"
$claudeMarketplace = Read-JsonFile ".claude-plugin/marketplace.json"
$kimiMarketplace = Read-JsonFile "kimi-marketplace.json"

if ($null -eq $registry -or $null -eq $codexMarketplace -or $null -eq $claudeMarketplace -or $null -eq $kimiMarketplace) {
    throw "Marketplace validation failed while parsing registry files."
}

Test-UniqueNames @($registry.plugins.name) "plugins.json"
Test-UniqueNames @($codexMarketplace.plugins.name) "Codex marketplace"
Test-UniqueNames @($claudeMarketplace.plugins.name) "Claude marketplace"
Test-UniqueNames @($kimiMarketplace.plugins.id) "Kimi marketplace"

$codexNames = @($codexMarketplace.plugins.name)
$claudeNames = @($claudeMarketplace.plugins.name)
$kimiNames = @($kimiMarketplace.plugins.id)

foreach ($plugin in $registry.plugins) {
    $name = [string]$plugin.name
    $providers = @($plugin.providers)
    $root = Resolve-PluginRoot ("./" + ([string]$plugin.pluginRoot).Replace("\", "/")) $name
    if ($null -eq $root) { continue }

    $providerContracts = @(
        @{ Provider = "codex"; Marketplace = $codexNames; Manifest = ".codex-plugin/plugin.json" },
        @{ Provider = "claude-code"; Marketplace = $claudeNames; Manifest = ".claude-plugin/plugin.json" },
        @{ Provider = "kimi-code"; Marketplace = $kimiNames; Manifest = "kimi.plugin.json" }
    )

    foreach ($contract in $providerContracts) {
        $declared = $providers -contains $contract.Provider
        $listed = $contract.Marketplace -contains $name
        if ($declared -ne $listed) {
            Add-ValidationError "$name provider '$($contract.Provider)' disagrees with marketplace membership"
        }
        if (-not $declared) { continue }

        $manifest = Read-PluginManifest $root $contract.Manifest $name
        if ($null -eq $manifest) { continue }
        if ([string]$manifest.name -ne $name) {
            Add-ValidationError "$name manifest name mismatch in $($contract.Manifest)"
        }
        if ($manifest.PSObject.Properties.Name -contains "version" -and [string]$manifest.version -ne [string]$plugin.version) {
            Add-ValidationError "$name version mismatch: registry=$($plugin.version), $($contract.Provider)=$($manifest.version)"
        }
    }

    $codexManifest = Read-PluginManifest $root ".codex-plugin/plugin.json" $name
    if ($null -ne $codexManifest -and $null -ne $codexManifest.interface) {
        $assetPaths = @()
        foreach ($field in @("composerIcon", "logo", "screenshots")) {
            $property = $codexManifest.interface.PSObject.Properties[$field]
            if ($null -ne $property) {
                $assetPaths += @($property.Value)
            }
        }
        foreach ($assetPath in @($assetPaths | Where-Object { $_ })) {
            if (-not ([string]$assetPath).StartsWith("./")) {
                Add-ValidationError "$name asset path must start with './': $assetPath"
                continue
            }
            if (-not (Test-Path -LiteralPath (Join-Path $root ([string]$assetPath)) -PathType Leaf)) {
                Add-ValidationError "$name asset is missing: $assetPath"
            }
        }
    }
}

foreach ($entry in $codexMarketplace.plugins) {
    $source = if ($entry.source -is [string]) { [string]$entry.source } else { [string]$entry.source.path }
    $null = Resolve-PluginRoot $source ([string]$entry.name)
}
foreach ($entry in $claudeMarketplace.plugins) {
    $null = Resolve-PluginRoot ([string]$entry.source) ([string]$entry.name)
}
foreach ($entry in $kimiMarketplace.plugins) {
    $null = Resolve-PluginRoot ([string]$entry.source) ([string]$entry.id)
}

$portableFiles = @("README.md", "plugins.json") + @(
    Get-ChildItem -LiteralPath (Join-Path $repoRoot "docs/plugins") -Recurse -File -Filter "*.md" |
        ForEach-Object { $_.FullName.Substring($repoRoot.Length + 1) }
)
foreach ($relativePath in $portableFiles) {
    $content = Get-Content -LiteralPath (Join-Path $repoRoot $relativePath) -Raw
    if ($content -match '(?i)C:\\Users\\[^\\]+') {
        Add-ValidationError "$relativePath contains a user-specific Windows path"
    }
}

$highConfidenceSecretPatterns = @(
    '-----BEGIN (RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----',
    'github_pat_[A-Za-z0-9_]{20,}',
    'gh[pousr]_[A-Za-z0-9]{20,}',
    'sk-[A-Za-z0-9_-]{20,}',
    'AKIA[0-9A-Z]{16}'
)
$trackedFiles = git -C $repoRoot ls-files | ForEach-Object { Join-Path $repoRoot $_ } | Where-Object { Test-Path -LiteralPath $_ -PathType Leaf }
foreach ($path in $trackedFiles) {
    try { $content = Get-Content -LiteralPath $path -Raw -ErrorAction Stop } catch { continue }
    foreach ($pattern in $highConfidenceSecretPatterns) {
        if ($content -match $pattern) {
            Add-ValidationError "$($path.Substring($repoRoot.Length + 1)) matches a high-confidence secret pattern"
            break
        }
    }
}

$submoduleStatus = @(git -C $repoRoot submodule status --recursive)
foreach ($line in $submoduleStatus) {
    if ($line -match '^[-+U]') {
        Add-ValidationError "Submodule state is not pinned cleanly: $($line.Substring(0, [Math]::Min($line.Length, 80)))"
    }
}

if ($errors.Count -gt 0) {
    $errors | ForEach-Object { Write-Error $_ -ErrorAction Continue }
    throw "Marketplace validation failed with $($errors.Count) error(s)."
}

Write-Host "Marketplace validation passed: $(@($registry.plugins).Count) plugins, 3 provider catalogs, no high-confidence secrets."
