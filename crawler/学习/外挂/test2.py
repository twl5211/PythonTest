# -*- coding: utf-8 -*-
# @Time ： 2024/6/30 22:34
# @Auth ： HongBao
# @File ：test2.py
# @IDE ：PyCharm
import win32api
import win32con
import time

def move_mouse_diagonal(start_x, start_y, end_x, end_y, steps=100, duration=2):
    for i in range(steps + 1):
        # 计算当前步的 x 和 y 坐标
        x = start_x + (end_x - start_x) * i / steps
        y = start_y + (end_y - start_y) * i / steps
        # 设置鼠标位置
        win32api.SetCursorPos((int(x), int(y)))
        # 每次移动后的暂停时间
        time.sleep(duration / steps)

# 使用示例
screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

# 从左上角移动到右下角
move_mouse_diagonal(0, 0, screen_width, screen_height, steps=200, duration=5)
