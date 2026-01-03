#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试脚本 - 验证所有依赖是否正确安装
"""

import sys

print("=" * 60)
print("Testing Douyin Huohua Helper Dependencies")
print("=" * 60)
print()

# 测试1: Python版本
print("[1/5] Checking Python version...")
print(f"Python version: {sys.version}")
version_info = sys.version_info
if version_info.major >= 3 and version_info.minor >= 7:
    print("✓ Python version OK (3.7+)")
else:
    print("✗ Python version too old. Please upgrade to 3.7+")
    sys.exit(1)
print()

# 测试2: PyQt5
print("[2/5] Checking PyQt5...")
try:
    from PyQt5 import QtCore
    print(f"✓ PyQt5 imported successfully")
    print(f"  Version: {QtCore.PYQT_VERSION_STR}")
except ImportError as e:
    print(f"✗ PyQt5 import failed: {e}")
    print("  Run: pip install PyQt5")
    sys.exit(1)
print()

# 测试3: PyQt5.QtWidgets
print("[3/5] Checking PyQt5.QtWidgets...")
try:
    from PyQt5.QtWidgets import QApplication
    print("✓ PyQt5.QtWidgets imported successfully")
except ImportError as e:
    print(f"✗ PyQt5.QtWidgets import failed: {e}")
    sys.exit(1)
print()

# 测试4: PyQtWebEngine
print("[4/5] Checking PyQtWebEngine...")
try:
    from PyQt5.QtWebEngineWidgets import QWebEngineView
    print("✓ PyQtWebEngine imported successfully")
except ImportError as e:
    print(f"✗ PyQtWebEngine import failed: {e}")
    print("  Run: pip install PyQtWebEngine")
    sys.exit(1)
print()

# 测试5: PyInstaller
print("[5/5] Checking PyInstaller...")
try:
    import PyInstaller
    print("✓ PyInstaller installed")
except ImportError:
    print("⚠ PyInstaller not installed (optional, needed only for building)")
    print("  To install: pip install pyinstaller")
print()

print("=" * 60)
print("✓ All required dependencies are installed!")
print("=" * 60)
print()
print("You can now run the application:")
print("  - Double click: start.bat")
print("  - Or run: python main.py")
print()
