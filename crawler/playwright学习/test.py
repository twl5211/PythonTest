# -*- coding: utf-8 -*-
# @Time ： 2024/7/1 19:52
# @Auth ： HongBao
# @File ：test.py
# @IDE ：PyCharm
from playwright.sync_api import sync_playwright
import requests

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.baidu.com")

    # 获取 cookies
    cookies = page.context.cookies()
    cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies}
    print("Cookies:", cookies_dict)

    # 获取 headers
    headers = page.evaluate("() => { return JSON.stringify([...navigator.userAgent]) }")
    print("Headers:", headers)

    # 使用 cookies 和 headers 进行请求
    response = requests.get("https://example.com/api/data", cookies=cookies_dict, headers={"User-Agent": headers})
    print("API Response:", response.text)

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
