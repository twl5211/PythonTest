# -*- coding: utf-8 -*-
# @Time ： 2024/7/2 9:32
# @Auth ： HongBao
# @File ：test02.py
# @IDE ：PyCharm
import time

from DrissionPage import SessionPage

page = SessionPage()
page.get('http://www.baidu.com')
page.get('http://gitee.com')
for i in page.cookies(as_dict=False, all_domains=True):
    print(i)
print('\n' * 4)
print(page.cookies(as_dict=True, all_domains=True))