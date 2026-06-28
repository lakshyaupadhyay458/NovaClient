Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "   NOVA CLIENT LIVE AUTOMATED MONITORING ENGINE   " -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host " Status: ACTIVE - Watching for file saves..." -ForegroundColor Green
Write-Host " Leave this window open in the background to auto-sync." -ForegroundColor Gray
Write-Host " Press Ctrl + C to stop monitoring." -ForegroundColor DarkRed
Write-Host "==================================================" -ForegroundColor Cyan

# 1. Establish path tracking targeting our root folder space
$TargetFolder = "$PSScriptRoot\.."
$BackupScript = "$PSScriptRoot\backup.ps1"

# 2. Instantiate a native Windows FileSystemWatcher object
$Watcher = New-Object System.IO.FileSystemWatcher
$Watcher.Path = (Resolve-Path $TargetFolder).Path
$Watcher.IncludeSubdirectories = $true
$Watcher.EnableRaisingEvents = $true

# Filter out background temp files and git metadata folder so it doesn't loop infinitely
$FilterBlock = {
    param($FullPath)
    if ($FullPath -like "*\.git*" -or $FullPath -like "*\__pycache__*" -or $FullPath -like "*\.novaclient*") {
        return $true
    }
    return $false
}

# 3. Define the live action block triggered on every file save event
$Action = {
    $Path = $Event.SourceEventArgs.FullPath
    
    # Check our filter block rules
    if (&$FilterBlock $Path) { return }
    
    $ChangeType = $Event.SourceEventArgs.ChangeType
    $Time = (Get-Date -Format "HH:mm:ss")
    
    Write-Host "`n[Event Detected at $Time] File ${ChangeType}: $Path" -ForegroundColor Magenta
    Write-Host "Launching background cloud synchronization pipeline..." -ForegroundColor Yellow
    
    # Execute our backup script automatically
    & $BackupScript
}

# 4. Bind the script action engine to Change, Create, and Delete system actions
$Handlers = @()
$Handlers += Register-ObjectEvent $Watcher "Changed" -Action $Action
$Handlers += Register-ObjectEvent $Watcher "Created" -Action $Action
$Handlers += Register-ObjectEvent $Watcher "Deleted" -Action $Action

# Keep the console thread alive running in the background listening for clicks
try {
    while ($true) { Start-Sleep -Seconds 1 }
}
finally {
    # Clean up system event handlers nicely if the user closes it with Ctrl+C
    foreach ($Handler in $Handlers) {
        Unregister-Event -SourceIdentifier $Handler.Name
    }
    $Watcher.Dispose()
    Write-Host "`nMonitoring stopped safely." -ForegroundColor Yellow
}
