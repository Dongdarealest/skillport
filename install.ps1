# SkillPort one-line installer for Windows.
# Usage: .\install.ps1 <pack> <ai>
#   pack: human-touch-pack, shipsafe-pack, guard-pack | design-pack | writing-pack | coding-pack
#   ai:   claude | cursor | codex | chatgpt
param([Parameter(Mandatory=$true)][string]$Pack, [Parameter(Mandatory=$true)][string]$Ai)
$ErrorActionPreference = "Stop"
$base = "https://github.com/Dongdarealest/skillport/raw/main/packs/$Pack"
$tmp = Join-Path $env:TEMP ("skillport-" + [guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Path $tmp | Out-Null
Write-Host "Downloading $Pack..."
Invoke-WebRequest -Uri "$base/$Pack.zip" -OutFile "$tmp\pack.zip"
Expand-Archive -Path "$tmp\pack.zip" -DestinationPath "$tmp\x"
$src = Join-Path $tmp "x\$Pack\for-$Ai"
if (-not (Test-Path $src)) { Write-Host "Unknown AI target: $Ai (use claude, cursor, codex or chatgpt)"; exit 1 }
switch ($Ai) {
  "claude" { $dest = Join-Path $HOME ".claude\skills"; New-Item -ItemType Directory -Force -Path $dest | Out-Null; Copy-Item "$src\*" -Destination $dest -Recurse -Force; Write-Host "Done. $Pack is installed for Claude in $dest" }
  "cursor" { $dest = Join-Path (Get-Location) ".cursor\rules"; New-Item -ItemType Directory -Force -Path $dest | Out-Null; Copy-Item "$src\.cursor\rules\*.mdc" -Destination $dest -Force; Write-Host "Done. $Pack rules are in $dest" }
  "codex" { $agents = Join-Path (Get-Location) "AGENTS.md"; if (-not (Test-Path $agents)) { New-Item -ItemType File -Path $agents | Out-Null }; Add-Content -Path $agents -Value "`n"; Add-Content -Path $agents -Value (Get-Content "$src\AGENTS.md" -Raw); Write-Host "Done. $Pack was added to $agents" }
  "chatgpt" { Write-Host "ChatGPT installs by pasting. Open these files and paste each one into your custom GPT or project instructions:"; Get-ChildItem $src | ForEach-Object { $_.Name } }
}
