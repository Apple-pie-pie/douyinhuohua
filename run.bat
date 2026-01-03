@echo off
chcp 65001 >nul
echo =====================================
echo 抖音续火花助手 - 测试启动脚本
echo =====================================
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] 未检测到Python，请先安装Python 3.7或更高版本
    echo 下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [信息] Python已安装
python --version
echo.

REM 检查是否已安装依赖
echo [信息] 检查依赖包...
pip show PyQt5 >nul 2>&1
if %errorlevel% neq 0 (
    echo [提示] 未检测到PyQt5，正在安装依赖包...
    echo.
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo [错误] 依赖包安装失败
        pause
        exit /b 1
    )
    echo.
    echo [成功] 依赖包安装完成
) else (
    echo [信息] 依赖包已安装
)

echo.
echo [启动] 正在启动抖音续火花助手...
echo.

REM 启动程序
python main.py

if %errorlevel% neq 0 (
    echo.
    echo [错误] 程序运行出错
    pause
    exit /b 1
)

pause
