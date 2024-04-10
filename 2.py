# -*- coding: utf-8 -*-
# @Time : 2024-4-10 16:17
# @Author : wangxs1
# @Email : wangxs1@xiaopeng.com
# @File : 2.py
# @Software : PyCharm
# @Project : Cloud_Charge_Finish
# @bak :

import uiautomation as auto
#  获取notepad++ 窗口
notepad = auto.WindowControl(searchDepth=1, ClassName="Notepad++")
notepad.SetFocus()
data = notepad.MenuItemControl(Name='文件(F)')
data.Click()
print()