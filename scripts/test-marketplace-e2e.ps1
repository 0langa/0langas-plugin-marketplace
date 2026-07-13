[CmdletBinding()]
param(
    [ValidateSet('all', 'codex', 'claude')]
    [string]$Provider = 'all',
    [string]$MarketplaceSource,
    [switch]$KeepTemp
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$repoRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
if ([string]::IsNullOrWhiteSpace($MarketplaceSource)) {
    $MarketplaceSource = $repoRoot
}

$plugins = @(
    'webde-access',
    'recall',
    'plugin-evaluation-kimi',
    'agent-handoff',
    'customization-control',
    'plugin-forge',
    'usage-pulse',
    'computer-custom'
)

function Invoke-Native([string]$Command, [string[]]$Arguments) {
    & $Command @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "$Command failed with exit code $LASTEXITCODE"
    }
}

$isolationRoot = [IO.Path]::GetFullPath((Join-Path $env:LOCALAPPDATA '0langas-marketplace-e2e')).TrimEnd([IO.Path]::DirectorySeparatorChar)
$testRoot = [IO.Path]::GetFullPath((Join-Path $isolationRoot ([guid]::NewGuid().ToString('N'))))
if (-not $testRoot.StartsWith($isolationRoot + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) {
    throw "Unsafe temporary test root: $testRoot"
}
New-Item -ItemType Directory -Path $testRoot | Out-Null

if ($env:GITHUB_TOKEN) {
    $pair = "x-access-token:$env:GITHUB_TOKEN"
    $basic = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes($pair))
    $env:GIT_CONFIG_COUNT = '1'
    $env:GIT_CONFIG_KEY_0 = 'http.https://github.com/.extraheader'
    $env:GIT_CONFIG_VALUE_0 = "AUTHORIZATION: basic $basic"
}

try {
    Invoke-Native (Join-Path $PSScriptRoot 'validate-marketplace.ps1') @()
    Invoke-Native 'claude' @('plugin', 'validate', $repoRoot)

    if ($Provider -in @('all', 'codex')) {
        $env:CODEX_HOME = Join-Path $testRoot 'codex'
        New-Item -ItemType Directory -Path $env:CODEX_HOME | Out-Null
        Invoke-Native 'codex' @('plugin', 'marketplace', 'add', $MarketplaceSource)
        foreach ($plugin in $plugins) {
            Invoke-Native 'codex' @('plugin', 'add', "$plugin@0langas-plugins")
        }
        Invoke-Native 'codex' @('plugin', 'list')
    }

    if ($Provider -in @('all', 'claude')) {
        $env:CLAUDE_CONFIG_DIR = Join-Path $testRoot 'claude'
        New-Item -ItemType Directory -Path $env:CLAUDE_CONFIG_DIR | Out-Null
        Invoke-Native 'claude' @('plugin', 'marketplace', 'add', $MarketplaceSource)
        foreach ($plugin in $plugins) {
            Invoke-Native 'claude' @('plugin', 'install', "$plugin@0langas-plugins", '--scope', 'user')
        }
        $claudeListJson = (& claude plugin list --json | Out-String)
        if ($LASTEXITCODE -ne 0) {
            throw "claude plugin list failed with exit code $LASTEXITCODE"
        }
        Write-Host $claudeListJson
        $claudePlugins = @($claudeListJson | ConvertFrom-Json)
        $pluginsWithErrors = @($claudePlugins | Where-Object {
            $errorsProperty = $_.PSObject.Properties['errors']
            $null -ne $errorsProperty -and @($errorsProperty.Value).Count -gt 0
        })
        if ($pluginsWithErrors.Count -gt 0) {
            $details = $pluginsWithErrors | ForEach-Object {
                "$($_.id): $(@($_.errors) -join '; ')"
            }
            throw "Claude plugin load errors detected: $($details -join ' | ')"
        }
    }

    Write-Host "Marketplace E2E passed for provider '$Provider' using '$MarketplaceSource'."
}
finally {
    if ($KeepTemp) {
        Write-Host "Kept isolated client homes at $testRoot"
    }
    elseif (Test-Path -LiteralPath $testRoot) {
        $resolved = [IO.Path]::GetFullPath($testRoot)
        if (-not $resolved.StartsWith($isolationRoot + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) {
            throw "Refusing to remove unsafe test path: $resolved"
        }
        Remove-Item -LiteralPath $resolved -Recurse -Force
    }
}
