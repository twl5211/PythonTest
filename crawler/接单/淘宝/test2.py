# -*- coding: utf-8 -*-
# @Time ： 2024/7/1 23:21
# @Auth ： HongBao
# @File ：test2.py
# @IDE ：PyCharm
from playwright.sync_api import sync_playwright
import requests
from requests.utils import cookiejar_from_dict


def get_playwright_cookies(page):
    # 获取 Playwright 的 Cookie
    cookies = page.context.cookies()
    # 转换为 requests 库的 Cookie 格式
    cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies}
    return cookies_dict


def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://example.com/login")

    # 示例：填写并提交登录表单
    page.fill("input[name='username']", "your_username")
    page.fill("input[name='password']", "your_password")
    page.click("button[type='submit']")

    # 等待导航完成
    page.wait_for_load_state('networkidle')

    # 获取并转换 Playwright 的 Cookies
    cookies_dict = get_playwright_cookies(page)
    browser.close()

    # 使用 requests 进行 HTTP 请求
    session = requests.Session()
    session.cookies = cookiejar_from_dict(cookies_dict)
    response = session.get("https://example.com/secure-page")
    print("使用 requests 获取的内容:", response.text[:200])


with sync_playwright() as playwright:
    run(playwright)
