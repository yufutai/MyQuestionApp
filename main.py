# -*- coding: utf-8 -*-
import os
import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

# 自动获取文件路径（兼容打包环境和开发环境）
def get_resource_path(filename):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), filename)

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        # 界面标题
        self.add_widget(Label(text="🔍 题库搜索神器", font_size='24sp', bold=True))

        # 输入框
        self.search_input = TextInput(hint_text="请输入题目关键词...", multiline=False)
        self.add_widget(self.search_input)

        # 搜索按钮
        btn = Button(text="开始搜索", font_size='20sp')
        btn.bind(on_press=self.search_question)
        self.add_widget(btn)

        # 结果显示区
        self.result_label = Label(text="结果将显示在这里", font_size='18sp', halign='center')
        self.add_widget(self.result_label)

    def search_question(self, instance):
        keyword = self.search_input.text
        if not keyword:
            self.result_label.text = "请输入内容！"
            return

        # 读取题目文件
        file_path = get_resource_path("题目.txt")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if keyword in content:
                    self.result_label.text = f"✅ 找到关于【{keyword}】的答案！\n(此处模拟显示答案)"
                else:
                    self.result_label.text = "❌ 未找到相关题目"
        except FileNotFoundError:
            self.result_label.text = "⚠️ 错误：找不到题目.txt文件"
        except Exception as e:
            self.result_label.text = f"发生错误: {str(e)}"

class MyApp(App):
    def build(self):
        Window.size = (400, 600) 
        return MainLayout()

if __name__ == '__main__':
    MyApp().run()
