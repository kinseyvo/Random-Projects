# Disable the built-in Administrator account
$admin = Get-LocalUser -Name "Administrator" -ErrorAction SilentlyContinue
if ($admin -and $admin.Enabled) {
    Disable-LocalUser -Name "Administrator"
    Write-Output "Built-in Administrator account disabled."
} else {
    Write-Output "Built-in Administrator account already disabled or not found."
}

# Disable other local admin accounts except the current logged-in user
$currentUser = "$env:COMPUTERNAME\$env:USERNAME"
$admins = Get-LocalGroupMember -Group "Administrators" | Where-Object {
    $_.ObjectClass -eq "User" -and $_.Name -ne $currentUser -and $_.Name -ne "Administrator"
}

foreach ($adminUser in $admins) {
    $userName = $adminUser.Name -replace '^[^\\]+\\', ''
    $user = Get-LocalUser -Name $userName -ErrorAction SilentlyContinue
    if ($user -and $user.Enabled) {
        Disable-LocalUser -Name $userName
        Write-Output "Disabled local admin user: $userName"
    }
}