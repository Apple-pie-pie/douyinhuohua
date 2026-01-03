@echo off
echo =====================================
echo Douyin Huohua Helper - Run Script
echo =====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not found. Please install Python 3.7 or higher
    echo Download: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [INFO] Python is installed
python --version
echo.

REM Check if dependencies are installed
echo [INFO] Checking dependencies...
pip show PyQt5 >nul 2>&1
if %errorlevel% neq 0 (
    echo [INFO] PyQt5 not found. Installing dependencies...
    echo.
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to install dependencies
        pause
        exit /b 1
    )
    echo.
    echo [SUCCESS] Dependencies installed successfully
) else (
    echo [INFO] Dependencies already installed
)

echo.
echo [START] Launching Douyin Huohua Helper...
echo.

REM Start the program
python main.py

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Program execution failed
    pause
    exit /b 1
)

pause
