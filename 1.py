# -*- coding: utf-8 -*-
# @Time : 2024-4-10 11:43
# @Author : wangxs1
# @Email : wangxs1@xiaopeng.com
# @File : 1.py
# @Software : PyCharm
# @Project : Cloud_Charge_Finish
# @bak :
import time

import uiautomation as auto

def print_window_info(window, indent=0):
    """递归打印窗口信息及其子元素信息"""
    prefix = '  ' * indent

    # 打印窗口属性
    print(f"{prefix}窗口:")
    print(f"{prefix}  ClassName: {window.ClassName}")
    print(f"{prefix}  控件类型: {window.ControlTypeName}")
    print(f"{prefix}  名称: {window.Name}")
    print(f"{prefix}  自动化ID: {window.AutomationId}")

    if hasattr(window, 'IsEnabled'):
        print(f"{prefix}  是否启用: {window.IsEnabled}")

    if hasattr(window, 'IsVisible'):
        print(f"{prefix}  是否可见: {window.IsVisible}")

    # 递归打印子元素
    for child in window.GetChildren():
        print_window_info(child, indent + 1)

if __name__ == '__main__':
    # 获取顶级窗口并打印它们及其子元素的信息
    time.sleep(5)
    top_level_windows = auto.GetRootControl().GetChildren()
    notepad_windows = [i for i in top_level_windows if i.ClassName == 'Notepad++']
    print("顶级窗口及其子元素:")
    for window in notepad_windows:
        print_window_info(window)
