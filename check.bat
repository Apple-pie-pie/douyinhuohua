@echo off
echo =====================================
echo System Check - Douyin Huohua Helper
echo =====================================
echo.

echo [1/5] Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo [ERROR] Python is NOT installed!
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    goto :error
) else (
    echo [OK] Python is installed
)
echo.

echo [2/5] Checking pip...
pip --version
if %errorlevel% neq 0 (
    echo [ERROR] pip is NOT available!
    goto :error
) else (
    echo [OK] pip is available
)
echo.

echo [3/5] Checking PyQt5...
pip show PyQt5 >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] PyQt5 is NOT installed
    echo Run install.bat to install dependencies
) else (
    echo [OK] PyQt5 is installed
    pip show PyQt5 | findstr "Version"
)
echo.

echo [4/5] Checking PyQtWebEngine...
pip show PyQtWebEngine >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] PyQtWebEngine is NOT installed
    echo Run install.bat to install dependencies
) else (
    echo [OK] PyQtWebEngine is installed
    pip show PyQtWebEngine | findstr "Version"
)
echo.

echo [5/5] Checking main.py...
if exist "main.py" (
    echo [OK] main.py found
) else (
    echo [ERROR] main.py NOT found!
    echo Make sure you are in the correct directory
    goto :error
)
echo.

echo =====================================
echo Check completed!
echo =====================================
echo.
echo If all checks passed, you can run start.bat
echo If any warnings shown, run install.bat first
echo.
pause
exit /b 0

:error
echo.
echo =====================================
echo [ERROR] System check failed!
echo =====================================
echo.
echo Please fix the errors above and try again
echo.
pause
exit /b 1
