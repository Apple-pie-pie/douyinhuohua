@echo off
chcp 65001 >nul
echo =====================================
echo 抖音续火花助手 - 打包脚本
echo =====================================
echo.

REM 检查PyInstaller是否安装
pip show pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo [提示] 正在安装PyInstaller...
    pip install pyinstaller
    if %errorlevel% neq 0 (
        echo [错误] PyInstaller安装失败
        pause
        exit /b 1
    )
)

echo [信息] 开始打包应用程序...
echo.

REM 清理之前的打包文件
if exist "dist" (
    echo [清理] 删除旧的dist目录...
    rmdir /s /q dist
)
if exist "build" (
    echo [清理] 删除旧的build目录...
    rmdir /s /q build
)

REM 使用PyInstaller打包
echo [打包] 正在使用PyInstaller打包...
pyinstaller --clean ^
    --name="抖音续火花助手" ^
    --windowed ^
    --onefile ^
    --icon=NONE ^
    --add-data="README.md;." ^
    main.py

if %errorlevel% neq 0 (
    echo.
    echo [错误] 打包失败
    pause
    exit /b 1
)

echo.
echo =====================================
echo [成功] 打包完成！
echo =====================================
echo.
echo 可执行文件位置: dist\抖音续火花助手.exe
echo.
echo 您可以将 dist 文件夹中的 exe 文件分发给其他用户使用
echo.

pause
