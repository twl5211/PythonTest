# -*- coding: utf-8 -*-
# @Time ： 2024/6/30 21:50
# @Auth ： HongBao
# @File ：test02.py
# @IDE ：PyCharm
import win32con
import win32api
import win32gui
import win32process


def mouse_click(x, y):
    win32api.SetCursorPos([x, y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    z = win32api.GetCursorPos()

def ceshi():

    win32gui.CreateWindow("sdfdgd",  "sdfgf", win32con.WS_EX_OVERLAPPEDWINDOW, 100, 100, 300, 300,None,None,my,None)
    hld = win32gui.FindWindow(None, u"计算器")  # 返回窗口标题为Adobe Acrobat的句柄
    print(hld)

    # 获得进程和线程  0线程 1进程
    process_id = win32process.GetWindowThreadProcessId(hld)[1]
    print(process_id)

    # 打开进程
    process_handle = win32api.OpenProcess(0x1F0FFF, True, process_id)
    print(process_handle)


if __name__ == '__main__':
    ceshi()
    # mouse_click(30, 150)
