# -*- coding: utf-8 -*-
# @Time ： 2024/6/30 22:38
# @Auth ： HongBao
# @File ：鼠标移动.py
# @IDE ：PyCharm
import win32api
import win32con
import win32gui
import time


def move_mouse_in_window(hwnd, start_x, start_y, end_x, end_y, steps=100, duration=2):
    # 获取窗口的左上角在屏幕上的位置
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    print(left, top, right, bottom)
    for i in range(steps + 1):

        # 计算当前步的 x 和 y 坐标
        x = start_x + (end_x - start_x) * i / steps
        y = start_y + (end_y - start_y) * i / steps

        # 将全局屏幕坐标转换为窗口内坐标
        relative_x, relative_y = win32gui.ScreenToClient(hwnd, (int(left + x), int(top + y)))
        print(x,y)
        print(relative_x, relative_y)
        # 构造鼠标位置参数

        lParam = win32api.MAKELONG(relative_x, relative_y)
        # 发送鼠标移动消息
        # win32api.SendMessage(hwnd, win32con.WM_MOUSEMOVE, 0, lParam)
        win32api.PostMessage(hwnd, win32con.WM_MOUSEMOVE, 0, lParam)

        # win32api.SetCursorPos((relative_x, relative_y))
        # 每次移动后的暂停时间
        time.sleep(duration / steps)


wd_name = u'PvZ Tools'
time.sleep(3)
# 使用示例
# 获取窗口句柄，使用窗口标题进行查找
hwnd = win32gui.FindWindow(None, "PvZ Tools")  # 替换成目标窗口的标题

# 检查是否找到窗口
if hwnd:
    print("11111111")
    # 在窗口内从左上角移动到右下角
    move_mouse_in_window(hwnd, 0, 0, 300, 300, steps=200, duration=5)
else:
    print("窗口未找到")
