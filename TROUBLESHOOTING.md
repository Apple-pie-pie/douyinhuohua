# 故障排除指南

## 目录
1. [安装问题](#安装问题)
2. [启动问题](#启动问题)
3. [运行问题](#运行问题)
4. [功能问题](#功能问题)
5. [打包问题](#打包问题)

---

## 安装问题

### 问题：批处理文件闪退或显示乱码

**症状**：
- 双击bat文件后窗口立即关闭
- 显示类似 "'暂停' 不是内部或外部命令" 的错误

**原因**：
- 文件编码问题已修复
- 新版本使用英文输出，避免编码问题

**解决方案**：
1. 确保使用最新版本的批处理文件
2. 现在的文件使用英文提示，完全避免编码问题
3. 如果还有问题，使用命令行手动运行：
   ```cmd
   python main.py
   ```

### 问题：找不到Python

**症状**：
```
ERROR: Python not found!
```

**解决方案**：
1. 下载Python 3.7或更高版本：https://www.python.org/downloads/
2. 安装时**必须勾选** "Add Python to PATH"
3. 安装完成后，重启命令行窗口
4. 运行 `python --version` 验证安装

### 问题：pip安装失败

**症状**：
```
ERROR: Failed to install dependencies
```

**解决方案**：

**方法1**: 使用国内镜像
```cmd
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```

**方法2**: 升级pip
```cmd
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**方法3**: 单独安装每个包
```cmd
pip install PyQt5
pip install PyQtWebEngine
pip install pyinstaller
```

---

## 启动问题

### 问题：缺少PyQt5模块

**症状**：
```
ModuleNotFoundError: No module named 'PyQt5'
```

**解决方案**：
```cmd
pip install PyQt5 PyQtWebEngine
```

### 问题：缺少PyQtWebEngine

**症状**：
```
ModuleNotFoundError: No module named 'PyQt5.QtWebEngineWidgets'
```

**解决方案**：
```cmd
pip install PyQtWebEngine
```

### 问题：程序启动后立即崩溃

**诊断步骤**：
1. 运行系统检查：
   ```cmd
   check.bat
   ```

2. 运行依赖测试：
   ```cmd
   python test_dependencies.py
   ```

3. 查看错误信息并按照提示修复

---

## 运行问题

### 问题：程序显示空白页面

**原因**：
- 网络连接问题
- 抖音网站无法访问
- 代理设置问题

**解决方案**：
1. 检查网络连接
2. 在浏览器中访问 https://www.douyin.com/ 确认可以打开
3. 点击程序中的刷新按钮（🔄）
4. 如果使用代理，尝试关闭代理

### 问题：无法登录账号

**可能原因**：
- 账号密码错误
- 需要验证码
- 网络问题

**解决方案**：
1. 确认账号密码正确
2. 完成机器人验证（在程序内完成）
3. 如果反复要求验证，可能是账号安全限制，等待一段时间后再试
4. 尝试先在普通浏览器中登录确认账号状态

### 问题：页面加载慢

**解决方案**：
1. 这是正常的，抖音网页版本身加载较慢
2. 等待页面完全加载
3. 检查网络速度
4. 点击刷新按钮重新加载

---

## 功能问题

### 问题：快捷发送消息不起作用

**原因**：
- 抖音网页版的DOM结构已更新
- 未打开聊天窗口
- JavaScript注入失败

**解决方案**：
1. **手动操作**：即使自动发送失效，您仍可以在程序内手动操作
2. **确保打开聊天**：先在消息列表中点击好友，打开聊天窗口
3. **手动输入**：在网页的输入框中手动输入并发送
4. 程序提供完整浏览器功能，所有网页操作都可以手动完成

### 问题：表情按钮不工作

**解决方案**：
1. 这是正常的，表情按钮的功能依赖于自动发送
2. 您可以手动在网页中选择抖音表情
3. 或者直接在输入框中输入emoji表情

### 问题：工具栏按钮无响应

**解决方案**：
1. 等待页面完全加载
2. 刷新页面
3. 重启程序

---

## 打包问题

### 问题：打包失败

**症状**：
```
ERROR: Build failed
```

**解决方案**：

**步骤1**: 确保PyInstaller已安装
```cmd
pip install pyinstaller
```

**步骤2**: 清理旧文件
```cmd
rmdir /s /q dist
rmdir /s /q build
```

**步骤3**: 手动打包
```cmd
pyinstaller --clean --name="DouyinHuohua" --windowed --onefile main.py
```

### 问题：打包后的EXE文件很大

**说明**：
- 这是正常的（100-200MB）
- PyInstaller会打包Python解释器和所有依赖
- 这样做的好处是用户无需安装Python即可运行

### 问题：打包后的EXE运行出错

**诊断步骤**：
1. 以管理员身份运行
2. 添加杀毒软件白名单
3. 检查Windows Defender是否拦截

**如果问题持续**：
使用源代码运行（不打包）：
```cmd
python main.py
```

---

## 通用故障排除流程

### 步骤1: 系统检查
```cmd
check.bat
```

### 步骤2: 测试依赖
```cmd
python test_dependencies.py
```

### 步骤3: 查看错误信息
仔细阅读错误提示，通常会说明问题所在

### 步骤4: 重新安装
```cmd
pip uninstall PyQt5 PyQtWebEngine -y
pip install PyQt5 PyQtWebEngine
```

### 步骤5: 寻求帮助
如果以上都无法解决，请：
1. 记录完整错误信息
2. 记录操作系统版本
3. 记录Python版本
4. 提供问题反馈

---

## 常用命令参考

### 检查Python版本
```cmd
python --version
```

### 检查已安装的包
```cmd
pip list
```

### 查看包详情
```cmd
pip show PyQt5
pip show PyQtWebEngine
```

### 卸载包
```cmd
pip uninstall PyQt5 -y
pip uninstall PyQtWebEngine -y
```

### 重新安装所有依赖
```cmd
pip install -r requirements.txt --force-reinstall
```

### 使用国内镜像加速安装
```cmd
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple PyQt5 PyQtWebEngine
```

---

## 性能优化建议

1. **首次启动较慢**：正常现象，等待初始化完成
2. **减少网络延迟**：确保网络连接稳定
3. **关闭不必要的浏览器标签**：在程序内只打开需要的页面
4. **定期清理**：关闭程序后重新打开

---

## 已知限制

1. **自动发送功能**：可能因抖音网页更新而失效，但手动操作始终可用
2. **登录状态**：需要定期重新登录（抖音安全策略）
3. **验证码**：可能需要手动完成验证（正常安全措施）
4. **网页功能**：取决于抖音网页版的功能支持

---

## 预防措施

1. **定期更新**：保持Python和依赖包最新
2. **备份数据**：重要信息不要只依赖程序
3. **遵守规则**：遵守抖音用户协议
4. **安全第一**：不要在公共电脑上保持登录

---

更新时间：2026-01-03
