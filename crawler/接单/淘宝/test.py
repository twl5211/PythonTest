# -*- coding: utf-8 -*-
# @Time ： 2024/7/1 20:12
# @Auth ： HongBao
# @File ：test.py
# @IDE ：PyCharm
'https://login.taobao.com/member/login.jhtml'
import json
import os
import pprint
import time
from requests.utils import cookiejar_from_dict
from playwright.sync_api import sync_playwright
import requests
headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'referer': 'https://s.taobao.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}
cookie_name = "cookies.json"
class TaoBao():
    def __init__(self):
        browser = playwright.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
        self.context = browser.new_context()
        self.page = browser.new_page()
        if not self.cookie():  # 判断本地cookie失效或没有cookie文件就返回FALSE则再次登录
            self.login()
            pass
        pass
    def login(self):


        # 打开登录页面
        self.page.goto("https://login.taobao.com/member/login.jhtml")


        print("请扫描二维码进行登录")
        self.page.wait_for_selector("#J_SiteNavLogin > div:nth-of-type(1) > div > a", timeout=60000)
        print("登录成功")
        self.save_cookies(cookie_name)
        pass
    def run(self):
        print("登录处理完毕")
        shop_data_url = 'https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20240701&js=1&localImgKey=&page=1&q=%E5%A5%B3%E8%A3%85&tab=all'
        self.page.goto(shop_data_url)

        for i in range(1, 10):


            self.page.click(f'div.Pagination--pgWrap--kfPsaVv > div > div > div > button:nth-child({i})')
            # 获取页面的 HTML 内容
            html_content = self.page.content()
            # 将 HTML 内容写入文件
            with open(f'{i}.html', 'w', encoding='utf-8') as f:
                f.write(html_content)
            elements = self.page.query_selector_all(
                '#pageContent > div.LeftLay--leftWrap--xBQipVc > div.LeftLay--leftContent--AMmPNfB > div.Content--content--sgSCZ12 > div > div')

            shops_data = []
            time.sleep(3)
            print(f"第{i}页")
            for element in elements:
                print(element)
                try:
                    shop_data = {}
                    'div.Title--descWrapper--HqxzYq0.Title--normalMod--HpNGsui > div > span'
                    element.wait_for_selector('div.Title--descWrapper--HqxzYq0.Title--normalMod--HpNGsui > div > span', state='visible')
                    print("标题")
                    shop_data['标题'] = element.query_selector(
                        'div.Title--descWrapper--HqxzYq0.Title--normalMod--HpNGsui > div > span').inner_text()
                    print("价格")
                    shop_data['价格'] = element.query_selector(
                        'div.Price--priceWrapper--Q0Dn7pN > div:nth-child(2) > span.Price--priceInt--ZlsSi_M').inner_text()
                    print("付款人数")
                    shop_data['付款人数'] = element.query_selector('span.Price--realSales--FhTZc7U').inner_text()
                    print("地区")
                    shop_data['地区'] = element.query_selector('div.Price--procity--_7Vt3mX > span').inner_text()
                    print("包邮")
                    shop_data['包邮'] = element.query_selector('div.Price--procity--_7Vt3mX > span').inner_text()
                    print("店铺名")
                    shop_data['店铺名'] = element.query_selector('div.ShopInfo--TextAndPic--yH0AZfx > a').inner_text()
                    print(shop_data['标题'])
                # shop_data['图片网址'] = element.query_selector('a>div>div>div>img').get_attribute('src')
                # shop_data['店铺网址'] = element.query_selector('div.ShopInfo--TextAndPic--yH0AZfx > a').get_attribute('href')
                    if element.query_selector('div.Title--descWrapper--HqxzYq0.Title--normalMod--HpNGsui > div > img'):
                        shop_data['平台'] = '天猫'
                    else:
                        shop_data['平台'] = '淘宝'
                except Exception as e:
                    continue
                    pass
                shops_data.append(shop_data)
            pprint.pprint(shops_data)
            pass
        self.page.wait_for_selector("#J_SiteNavLogin > div:nth-of-type(1) > div > a>b", timeout=6000000)
        pass

        # data_url = 'https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/'
        # cookies = self.page.context.cookies()
        # cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies}
        # print(cookies_dict)
        # session = requests.Session()
        # session.cookies = cookiejar_from_dict(cookies_dict)
        # response = session.get(url=data_url)
        # print(response.text)
        # print(cookies)
        # for cookie in session.cookies:
        #     print(f"{cookie.name}: {cookie.value}")
        #
        # print(response.headers)



    def save_cookies(self, filepath):
        cookies = self.page.context.cookies()
        with open(filepath, 'w') as file:
            json.dump(cookies, file)

    def load_cookies(self, filepath):
        with open(filepath, 'r') as file:
            cookies = json.load(file)
        self.page.context.add_cookies(cookies)
        # self.context.add_cookies(cookies)
    def cookie(self):
        if os.path.exists(cookie_name):  # 判断这个文件是否存在
            self.page.goto("https://shopsearch.taobao.com/browse/shop_search.htm")
            self.load_cookies(cookie_name)

            cookies = self.page.context.cookies()
            self.page.reload()
            print("All cookies:", cookies)
            try:
                if self.page.wait_for_selector("#J_SiteNavLogin > div:nth-of-type(1) > div > a", timeout=60000):
                    print('使用cooking登录成功')
            except:
                print()
                print("cooking登录失败")
                return False
            return True
        else:
            return False
if __name__ == '__main__':
    with sync_playwright() as playwright:
        tb = TaoBao()
        tb.run()
    pass
