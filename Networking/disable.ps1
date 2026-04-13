<#
.SYNOPSIS
Disables NBNS (NetBIOS over TCP/IP), mDNS (multicast DNS), LLMNR, SMBv1, 
and sets cached domain logon count on Windows endpoints.
To be deployed via Intune.

WARNING: Modifies registry. Always test on non-production machines first!
#>

# --- Backup Registry (System Restore Point for safety) ---
Checkpoint-Computer -Description "Pre_Hardening_Script" -RestorePointType "Modify_Settings"

# --- Disable NetBIOS over TCP/IP (NBNS) ---
Write-Output "Disabling NetBIOS over TCP/IP..."
Get-WmiObject -Class Win32_NetworkAdapterConfiguration -Filter "IPEnabled = TRUE" |
ForEach-Object {
    $_.SetTcpipNetbios(2)  # 0 = Default (DHCP), 1 = Enable, 2 = Disable
}

# --- Disable mDNS (multicast DNS) ---
Write-Output "Disabling mDNS..."
$mdnsRegPath = "HKLM:\SYSTEM\CurrentControlSet\Services\Dnscache\Parameters"
$mdnsRegName = "EnableMDNS"
$mdnsRegValue = 0

If (-not (Test-Path $mdnsRegPath)) {
    New-Item -Path $mdnsRegPath -Force | Out-Null
}
Set-ItemProperty -Path $mdnsRegPath -Name $mdnsRegName -Value $mdnsRegValue -Type DWord

Write-Output "mDNS disabled (EnableMDNS set to 0). A reboot is required for this to fully apply."

# --- Disable LLMNR ---
Write-Output "Disabling LLMNR..."
$llmnrRegPath = "HKLM:\Software\Policies\Microsoft\Windows NT\DNSClient"
$llmnrRegName = "EnableMulticast"
$llmnrRegValue = 0

If (-not (Test-Path $llmnrRegPath)) {
    New-Item -Path $llmnrRegPath -Force | Out-Null
}
Set-ItemProperty -Path $llmnrRegPath -Name $llmnrRegName -Value $llmnrRegValue -Type DWord

Write-Output "LLMNR disabled (EnableMulticast set to 0)."

# --- Disable SMBv1 ---
Write-Output "Disabling SMBv1..."
$smbRegPath = "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters"
$smbRegName = "SMB1"
$smbRegValue = 0

If (-not (Test-Path $smbRegPath)) {
    New-Item -Path $smbRegPath -Force | Out-Null
}
Set-ItemProperty -Path $smbRegPath -Name $smbRegName -Value $smbRegValue -Type DWord

# Also disable SMBv1 client-side support
$smbClientRegPath = "HKLM:\SYSTEM\CurrentControlSet\Services\mrxsmb10"
$smbClientRegName = "Start"
$smbClientRegValue = 4   # 4 = Disabled service

If (Test-Path $smbClientRegPath) {
    Set-ItemProperty -Path $smbClientRegPath -Name $smbClientRegName -Value $smbClientRegValue -Type DWord
}

Write-Output "SMBv1 disabled (both server and client components). A reboot is required for this to fully apply."

# --- Set Cached Domain Logon Count ---
Write-Output "Setting cached domain logon count..."
$cachedLogonsRegPath = "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon"
$cachedLogonsRegName = "CachedLogonsCount"
$cachedLogonsValue = 4   # adjust as needed (0 for none, 1 for remote users, etc.)

If (-not (Test-Path $cachedLogonsRegPath)) {
    New-Item -Path $cachedLogonsRegPath -Force | Out-Null
}
Set-ItemProperty -Path $cachedLogonsRegPath -Name $cachedLogonsRegName -Value $cachedLogonsValue -Type String

Write-Output "Cached domain logon count set to $cachedLogonsValue. A reboot is required for this to fully apply."

# --- Verification output ---
Write-Output "Verification Results:"

Write-Output "NBNS:"
Get-WmiObject -Class Win32_NetworkAdapterConfiguration -Filter "IPEnabled = TRUE" |
Select-Object Description, TcpipNetbiosOptions

Write-Output "mDNS:"
Get-ItemProperty -Path $mdnsRegPath | Select-Object EnableMDNS

Write-Output "LLMNR:"
Get-ItemProperty -Path $llmnrRegPath | Select-Object EnableMulticast

Write-Output "SMBv1 (Server):"
Get-ItemProperty -Path $smbRegPath | Select-Object SMB1

Write-Output "SMBv1 (Client):"
If (Test-Path $smbClientRegPath) {
    Get-ItemProperty -Path $smbClientRegPath | Select-Object Start
} Else {
    Write-Output "SMBv1 client driver not present."
}

Write-Output "Cached Logons:"
Get-ItemProperty -Path $cachedLogonsRegPath | Select-Object CachedLogonsCount