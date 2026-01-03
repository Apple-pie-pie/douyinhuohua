@echo off
echo =====================================
echo Douyin Huohua Helper - Build Script
echo =====================================
echo.

REM Check if PyInstaller is installed
pip show pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo [INFO] Installing PyInstaller...
    pip install pyinstaller
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to install PyInstaller
        pause
        exit /b 1
    )
)

echo [INFO] Starting build process...
echo.

REM Clean previous build files
if exist "dist" (
    echo [CLEAN] Removing old dist directory...
    rmdir /s /q dist
)
if exist "build" (
    echo [CLEAN] Removing old build directory...
    rmdir /s /q build
)

REM Build with PyInstaller
echo [BUILD] Building with PyInstaller...
pyinstaller --clean ^
    --name="DouyinHuohua" ^
    --windowed ^
    --onefile ^
    --icon=NONE ^
    --add-data="README.md;." ^
    main.py

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Build failed
    pause
    exit /b 1
)

echo.
echo =====================================
echo [SUCCESS] Build completed!
echo =====================================
echo.
echo Executable location: dist\DouyinHuohua.exe
echo.
echo You can distribute the exe file to other users
echo.

pause
