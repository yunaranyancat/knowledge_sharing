@echo off
:: Stop the W64Time service
echo Stopping the W64Time service...
sc stop W64Time >nul 2>&1

:: Delete the W64Time service
echo Deleting the W64Time service...
sc delete W64Time >nul 2>&1

:: Remove registry entries
echo Removing registry entries...
reg delete "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\svchost" /v TimeService /f >nul 2>&1
reg delete "HKLM\SYSTEM\CurrentControlSet\services\W64Time" /f >nul 2>&1

:: Remove the downloaded DLL file
echo Removing downloaded DLL file...
set "dll_path=%SystemRoot%\system32\w64time.dll"
if exist "%dll_path%" (
    del /f /q "%dll_path%"
    if exist "%dll_path%" (
        echo Failed to delete %dll_path%.
    ) else (
        echo Successfully deleted %dll_path%.
    )
) else (
    echo DLL file not found at %dll_path%.
)

:: Final message
echo Cleanup completed.
pause
