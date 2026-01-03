@echo off
echo Installing dependencies...
echo.

python --version
if %errorlevel% neq 0 (
    echo ERROR: Python not found!
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Installation failed
    pause
    exit /b 1
)

echo.
echo SUCCESS: All dependencies installed!
echo You can now run run.bat to start the program
echo.
pause
