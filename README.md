# 抖音续火花助手

一个在网页版续火花的桌面程序，每天只需要在桌面端启动即可实现续火花。

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-green.svg)](https://pypi.org/project/PyQt5/)
[![License](https://img.shields.io/badge/License-Educational-orange.svg)](LICENSE)

## 📖 项目简介

本程序是一个Windows桌面应用，内嵌抖音网页版，方便用户进行续火花操作。

## ✨ 功能特点

- ✅ 在程序内连接抖音网页版
- ✅ 支持账号登录和机器人验证（在桌面端完成）
- ✅ 支持输入文字或表情进行续火花
- ✅ 提供快捷表情按钮（❤️ 👍 😊 🔥）
- ✅ 快捷消息功能
- ✅ 完整的浏览器导航功能
- ✅ 保持登录状态
- ✅ 可打包成独立EXE文件

## 🚀 快速开始

### 三步开始使用

```bash
# 1. 安装依赖
双击 install.bat

# 2. 启动程序  
双击 start.bat

# 3. 在程序中登录抖音并使用
```

详细说明请查看 **[快速开始指南 (QUICKSTART.md)](QUICKSTART.md)**

## 📁 项目结构

```
douyinhuohua/
├── main.py              # 主程序（PyQt5桌面应用）
├── requirements.txt     # Python依赖包列表
├── install.bat          # 依赖安装脚本
├── start.bat            # 快速启动脚本
├── run.bat              # 完整启动脚本
├── build.bat            # 打包脚本
├── main.spec            # PyInstaller配置
├── QUICKSTART.md        # 快速开始指南 ⭐
├── USAGE.md             # 详细使用说明
└── README.md            # 项目说明（本文件）
```

## 📚 文档导航

- **[快速开始 (QUICKSTART.md)](QUICKSTART.md)** - 3步开始使用 ⭐ 推荐新手
- **[详细使用说明 (USAGE.md)](USAGE.md)** - 完整功能介绍和使用技巧
- **[故障排除 (TROUBLESHOOTING.md)](TROUBLESHOOTING.md)** - 问题解决方案 🔧

## 💻 使用方法

### 简单使用（推荐）

1. **安装** → 双击 `install.bat`
2. **启动** → 双击 `start.bat`  
3. **使用** → 登录后开始续火花

### 完整步骤

1. **启动程序**：双击 `start.bat` 或 `run.bat`
2. **登录账号**：在程序内完成抖音账号登录
3. **打开消息**：点击工具栏的 "💬 消息" 按钮
4. **选择好友**：在消息列表中点击要续火花的好友
5. **发送消息**：使用底部输入框或快捷按钮发送消息

### 打包成EXE（可选）

```bash
# 打包成独立EXE文件（无需Python环境即可运行）
双击 build.bat

# 打包完成后
dist/DouyinHuohua.exe  # 可以分发给其他人使用
```

## 技术栈

- **Python 3.7+**
- **PyQt5** - GUI框架
- **PyQtWebEngine** - 网页浏览引擎
- **PyInstaller** - 打包工具

## 系统要求

- Windows 7/8/10/11
- Python 3.7 或更高版本（如使用源代码运行）
- 网络连接

## 注意事项

- 程序通过JavaScript与网页交互，抖音网页版更新可能影响自动发送功能
- 即使自动发送失效，仍可在程序内手动操作
- 首次使用需要登录账号
- 请遵守抖音平台用户协议

## 免责声明

本程序仅供学习和研究使用，请遵守抖音平台的用户协议和相关法律法规。使用本程序所产生的任何后果由使用者自行承担。

## 许可证

本项目仅供个人学习使用。