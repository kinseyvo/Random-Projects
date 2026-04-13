# --- Set Cached Domain Logon Count ---
Write-Output "Setting cached domain logon count..."
$cachedLogonsRegPath = "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon"
$cachedLogonsRegName = "CachedLogonsCount"
$cachedLogonsValue = 2   # adjust as needed (0 for none, 1 for remote users, etc.)

If (-not (Test-Path $cachedLogonsRegPath)) {
    New-Item -Path $cachedLogonsRegPath -Force | Out-Null
}
Set-ItemProperty -Path $cachedLogonsRegPath -Name $cachedLogonsRegName -Value $cachedLogonsValue -Type String

Write-Output "Cached domain logon count set to $cachedLogonsValue. A reboot is required for this to fully apply."

# --- Verification output ---
Write-Output "Verification Results:"

Write-Output "Cached Logons:"
Get-ItemProperty -Path $cachedLogonsRegPath | Select-Object CachedLogonsCount