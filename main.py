#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
抖音续火花桌面程序
功能：在桌面端打开抖音网页版，用于续火花
"""

import sys
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QHBoxLayout, QPushButton, QLineEdit, QMessageBox,
    QToolBar, QAction
)
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from PyQt5.QtGui import QIcon


class DouyinHuohuaApp(QMainWindow):
    """抖音续火花主窗口"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """初始化用户界面"""
        self.setWindowTitle("抖音续火花助手")
        self.setGeometry(100, 100, 1200, 800)
        
        # 创建中心部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建主布局
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # 创建工具栏
        self.create_toolbar()
        
        # 创建浏览器视图
        self.browser = QWebEngineView()
        
        # 设置User-Agent，模拟正常浏览器
        profile = QWebEngineProfile.defaultProfile()
        profile.setHttpUserAgent(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        
        # 加载抖音网页版
        self.browser.setUrl(QUrl("https://www.douyin.com/"))
        
        # 将浏览器添加到布局
        main_layout.addWidget(self.browser)
        
        # 创建底部操作面板
        self.create_bottom_panel(main_layout)
        
        # 状态栏
        self.statusBar().showMessage("就绪 - 请先登录抖音账号")
        
    def create_toolbar(self):
        """创建工具栏"""
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        
        # 后退按钮
        back_action = QAction("← 后退", self)
        back_action.triggered.connect(self.browser.back)
        toolbar.addAction(back_action)
        
        # 前进按钮
        forward_action = QAction("前进 →", self)
        forward_action.triggered.connect(self.browser.forward)
        toolbar.addAction(forward_action)
        
        # 刷新按钮
        refresh_action = QAction("🔄 刷新", self)
        refresh_action.triggered.connect(self.browser.reload)
        toolbar.addAction(refresh_action)
        
        # 主页按钮
        home_action = QAction("🏠 主页", self)
        home_action.triggered.connect(self.go_home)
        toolbar.addAction(home_action)
        
        toolbar.addSeparator()
        
        # 消息页面按钮
        message_action = QAction("💬 消息", self)
        message_action.triggered.connect(self.go_to_messages)
        toolbar.addAction(message_action)
        
    def create_bottom_panel(self, parent_layout):
        """创建底部操作面板"""
        bottom_panel = QWidget()
        bottom_layout = QVBoxLayout()
        bottom_panel.setLayout(bottom_layout)
        
        # 快捷消息输入区
        input_layout = QHBoxLayout()
        
        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("在此输入要发送的消息（需要先在网页中打开聊天窗口）...")
        self.message_input.returnPressed.connect(self.send_message_via_js)
        
        send_button = QPushButton("发送消息")
        send_button.clicked.connect(self.send_message_via_js)
        
        input_layout.addWidget(self.message_input)
        input_layout.addWidget(send_button)
        
        bottom_layout.addLayout(input_layout)
        
        # 快捷操作按钮
        quick_actions_layout = QHBoxLayout()
        
        emoji_btn_1 = QPushButton("❤️")
        emoji_btn_1.clicked.connect(lambda: self.send_emoji("❤️"))
        
        emoji_btn_2 = QPushButton("👍")
        emoji_btn_2.clicked.connect(lambda: self.send_emoji("👍"))
        
        emoji_btn_3 = QPushButton("😊")
        emoji_btn_3.clicked.connect(lambda: self.send_emoji("😊"))
        
        emoji_btn_4 = QPushButton("🔥")
        emoji_btn_4.clicked.connect(lambda: self.send_emoji("🔥"))
        
        quick_msg_btn = QPushButton("快捷消息: 早安")
        quick_msg_btn.clicked.connect(lambda: self.send_quick_message("早安"))
        
        quick_actions_layout.addWidget(emoji_btn_1)
        quick_actions_layout.addWidget(emoji_btn_2)
        quick_actions_layout.addWidget(emoji_btn_3)
        quick_actions_layout.addWidget(emoji_btn_4)
        quick_actions_layout.addWidget(quick_msg_btn)
        quick_actions_layout.addStretch()
        
        bottom_layout.addLayout(quick_actions_layout)
        
        parent_layout.addWidget(bottom_panel)
        
    def go_home(self):
        """返回抖音主页"""
        self.browser.setUrl(QUrl("https://www.douyin.com/"))
        self.statusBar().showMessage("返回主页")
        
    def go_to_messages(self):
        """跳转到消息页面"""
        self.browser.setUrl(QUrl("https://www.douyin.com/messages"))
        self.statusBar().showMessage("打开消息页面")
        
    def send_message_via_js(self):
        """通过JavaScript发送消息"""
        message = self.message_input.text().strip()
        if not message:
            QMessageBox.warning(self, "提示", "请输入要发送的消息！")
            return
            
        # JavaScript代码：尝试在输入框中填充文本并触发发送
        # 注意：这个需要根据抖音的实际DOM结构调整
        js_code = f"""
        (function() {{
            // 尝试查找输入框
            var inputSelectors = [
                'textarea[placeholder*="消息"]',
                'textarea[placeholder*="说点什么"]',
                'div[contenteditable="true"]',
                'textarea'
            ];
            
            var input = null;
            for (var i = 0; i < inputSelectors.length; i++) {{
                input = document.querySelector(inputSelectors[i]);
                if (input) break;
            }}
            
            if (input) {{
                // 设置内容
                if (input.tagName === 'TEXTAREA') {{
                    input.value = '{message}';
                }} else {{
                    input.textContent = '{message}';
                }}
                
                // 触发输入事件
                var event = new Event('input', {{ bubbles: true }});
                input.dispatchEvent(event);
                
                // 尝试查找发送按钮并点击
                setTimeout(function() {{
                    var sendBtnSelectors = [
                        'button[type="submit"]',
                        'button:contains("发送")',
                        '.send-btn',
                        '[class*="send"]'
                    ];
                    
                    var sendBtn = null;
                    for (var i = 0; i < sendBtnSelectors.length; i++) {{
                        sendBtn = document.querySelector(sendBtnSelectors[i]);
                        if (sendBtn && !sendBtn.disabled) {{
                            sendBtn.click();
                            break;
                        }}
                    }}
                }}, 100);
                
                return '消息已填入输入框';
            }} else {{
                return '未找到输入框，请确保已打开聊天窗口';
            }}
        }})();
        """
        
        self.browser.page().runJavaScript(js_code, self.handle_js_result)
        self.message_input.clear()
        
    def send_emoji(self, emoji):
        """发送表情"""
        self.message_input.setText(emoji)
        self.send_message_via_js()
        
    def send_quick_message(self, message):
        """发送快捷消息"""
        self.message_input.setText(message)
        self.send_message_via_js()
        
    def handle_js_result(self, result):
        """处理JavaScript执行结果"""
        if result:
            self.statusBar().showMessage(str(result))
        else:
            self.statusBar().showMessage("操作已执行")
            
    def closeEvent(self, event):
        """关闭窗口事件"""
        reply = QMessageBox.question(
            self,
            "确认退出",
            "确定要退出抖音续火花助手吗？",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    """主函数"""
    # 启用高DPI支持
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    
    app = QApplication(sys.argv)
    app.setApplicationName("抖音续火花助手")
    
    # 创建并显示主窗口
    window = DouyinHuohuaApp()
    window.show()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
