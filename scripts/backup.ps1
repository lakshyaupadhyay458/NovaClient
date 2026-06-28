Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "   NOVA CLIENT AUTOMATED BACKUP ENGINE   " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

# 1. Move to the project root folder to ensure commands execute correctly
Set-Location "$PSScriptRoot\.."

# 2. Automatically grab a clean date and time string for our save file note
$CurrentDateTime = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$CommitMessage = "auto-backup: snapshot saved on $CurrentDateTime"

Write-Host "Step 1: Staging modified and new source files..." -ForegroundColor Yellow
git add .

Write-Host "Step 2: Bundling file snapshot packages..." -ForegroundColor Yellow
git commit -m "$CommitMessage"

Write-Host "Step 3: Uploading data streams safely to GitHub cloud..." -ForegroundColor Yellow
git push origin main

Write-Host "==========================================" -ForegroundColor Green
Write-Host "SUCCESS: Nova Client project fully backed up!" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green