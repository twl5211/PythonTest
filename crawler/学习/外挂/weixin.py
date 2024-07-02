# -*- coding: utf-8 -*-
# @Time ： 2024/6/30 22:54
# @Auth ： HongBao
# @File ：weixin.py
# @IDE ：PyCharm
import time

import win32api
import win32clipboard
import win32con
import win32gui


def clipboard_get():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data


def clipboard_set(data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, data)

    win32clipboard.CloseClipboard()
    return True


def open_chat_window(name):
    handle = win32gui.FindWindow('WeChatMainWndForPC', "微信")
    print(handle)

    # SW_SHOWNORMAL 显示并激活窗口，恢复正常大小（初始化时用这个参数）
    win32gui.ShowWindow(handle, win32con.SW_SHOWNORMAL)
    # 设置窗口置顶
    win32gui.SetForegroundWindow(handle)

    # 获取微信的窗口大小和位置
    info = win32gui.GetWindowRect(handle)
    print(info)
    print(type(info))
    # 移动鼠标到搜索窗口
    win32api.SetCursorPos((info[0] + 120, info[1] + 40))

    time.sleep(0.2)
    # 鼠标左键点击
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    clipboard_set(name)
    print(clipboard_get())
    # 搜索关键字
    time.sleep(0.2)
    win32api.keybd_event(17, 0, 0, 0)  # ctrl
    win32api.keybd_event(86, 0, 0, 0)  # v
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键

    time.sleep(1)
    x = win32api.GetCursorPos()[0]
    y = win32api.GetCursorPos()[1] + 70
    win32api.SetCursorPos((x, y))

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.3)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

    return handle


def move_edit(handle1, name):
    # SW_MINIMIZE 最小化
    win32gui.ShowWindow(handle1, win32con.SW_MINIMIZE)
    handle = win32gui.FindWindow('ChatWnd', name)
    # tid = win32gui.FindWindowEx(handle, None, 'Edit', None)
    # print(tid)
    print(handle)
    info = win32gui.GetWindowRect(handle)

    print(info)
    # SW_SHOWNORMAL 显示并激活窗口，恢复正常大小（初始化时用这个参数）
    win32gui.ShowWindow(handle, win32con.SW_SHOWNORMAL)
    # 设置窗口置顶
    win32gui.SetForegroundWindow(handle)

    win32api.SetCursorPos((info[2] - 320, info[3] - 80))
    pass


def send_message(message):
    # ChatWnd一

    time.sleep(0.3)
    clipboard_set(message)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

    win32api.keybd_event(17, 0, 0, 0)  # ctrl
    win32api.keybd_event(86, 0, 0, 0)  # v
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键

    win32api.keybd_event(13, 0, 0, 0)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    pass


if __name__ == '__main__':

    name = '顾子琪'
    handle = open_chat_window(name)

    move_edit(handle, name)

    message = "这是一个最好的时代，也是一个最坏的时代；这是一个智慧的年代，这是一个愚蠢的年代；这是一个信任的时期，这是一个怀疑的时期；这是一个光明的季节，这是一个黑暗的季节；这是希望之春，这是失望之冬；人们面前应有尽有，人们面前一无所有；人们正踏上天堂之路，人们正走向地狱之门。"
    send_message(message)


# ChatWnd一

# time.sleep(0.1)
#
# print(clipboard_get())
#
# s = "这是一个最好的时代，也是一个最坏的时代；这是一个智慧的年代，这是一个愚蠢的年代；这是一个信任的时期，这是一个怀疑的时期；这是一个光明的季节，这是一个黑暗的季节；这是希望之春，这是失望之冬；人们面前应有尽有，人们面前一无所有；人们正踏上天堂之路，人们正走向地狱之门。"
# #
# l = s.split('；')
# for i in s:
#     time.sleep(0.5)
#     clipboard_set(i)
#     print(clipboard_get())
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
#
#     win32api.keybd_event(17, 0, 0, 0)  # ctrl
#     win32api.keybd_event(86, 0, 0, 0)  # v
#     win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
#     win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
#
#     win32api.keybd_event(13, 0, 0, 0)
#     win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
#     print(clipboard_get())

# 输入
# time.sleep(0.2)
# clipboard_set('上')
#
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
#
# time.sleep(0.2)
# win32api.keybd_event(17, 0, 0, 0)  # ctrl
# win32api.keybd_event(86, 0, 0, 0)  # v
# win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
# win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
#
#
# win32api.keybd_event(13, 0, 0, 0)
# win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
# print(clipboard_get())
# #
# # 输入
# time.sleep(0.2)
# clipboard_set('好')
#
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
# # 输入
# time.sleep(0.2)
# win32api.keybd_event(17, 0, 0, 0)  # ctrl
# win32api.keybd_event(86, 0, 0, 0)  # v
# win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
# win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
#
#
# win32api.keybd_event(13, 0, 0, 0)
# win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
# print(clipboard_get())
