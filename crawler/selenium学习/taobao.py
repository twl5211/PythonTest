import os
import time
import re
import requests
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import atexit

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


class Taobao:
    def save_data(self):

        print("正在保存数据...")
        file_path = 'data.json'

        file_data = {}
        with open(file_path, 'r') as f:
            if len(f.read()) > 5:
                file_data: dict = json.load(f)
        with open(file_path, 'w') as f:
            self.data.update(file_data)
            f.write(json.dumps(self.data, indent=4, ensure_ascii=False))
            pass

        print("保存数据成功")

    def __init__(self):
        atexit.register(self.save_data)
        self.original_window = None
        self.shopListUrl = []
        self.data = {}
        self.session = None
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")

        self.driver = webdriver.Edge(options=options)

        self.driver.implicitly_wait(1.5)  # 显示等待页面加载完成找到元素才进入下一步，这块配置全局生效

        if not self.cookie():  # 判断本地cookie失效或没有cookie文件就返回FALSE则再次登录

            self.login()

        self.initCookie()

    def initCookie(self):
        selenium_cookies = self.driver.get_cookies()
        self.requests_cookies = {cookie['name']: cookie['value'] for cookie in selenium_cookies}
        # 创建一个 Requests 会话
        # 设置 Requests 会话的 Cookies
        self.session = requests.Session()
        self.session.cookies.update(self.requests_cookies)
        pass

    def new_page(self, element):
        element.click()
        # 切换到新窗口
        new_window = [window for window in self.driver.window_handles if window != self.original_window][0]
        self.driver.switch_to.window(new_window)
        '//*[@id="shop-info"]/div[2]/div[1]/div[2]/span'
        '//*[@id="shop-info"]/div[2]/div[2]/div[2]/span'
        dataXPATH = {
            '天猫': [
                '//*[@id="shop-info"]/div[2]', './div', './div[2]/span'
            ],
            '淘宝': [
                ['//*[@id="miniDSR"]', './span',
                 '//*[@id="header-content"]/div[2]/div/div/div[1]/div[1]/div/div/ul/li/p/a/span'],
                ['//*[@id="header-content"]/div[2]/div[2]/ul', './li', './span[2]/em',
                 '//*[@id="header-content"]/div[2]/div[3]/div[2]/div[1]/p[3]/a']
            ]
        }
        flag = 0
        '//*[@id="J_SiteNavBdL"]/li[1]/div[1]/span[1]'
        '//*[@id="J_SiteNavLogin"]/div[1]/div/a'
        current_XPATH = []
        if '天猫' in self.driver.title:
            current_XPATH = dataXPATH['天猫']
        else:

            try:
                # 判断属于淘宝的哪个页面
                self.driver.find_element(By.XPATH, '//*[@id="miniDSR"]')
                flag = 1
                current_XPATH = dataXPATH['淘宝'][0]
                pass
            except NoSuchElementException:
                flag = 2
                current_XPATH = dataXPATH['淘宝'][1]
                pass
            pass
        try:
            parent_li = self.driver.find_element(By.XPATH, current_XPATH[0])
            all_em = parent_li.find_elements(By.XPATH, current_XPATH[1])
        except NoSuchElementException:
            print(self.driver.title)
            # 关闭新窗口并切换回原始窗口
            cookies = self.driver.get_cookies()
            c = re.compile('"score":"(.*?)"')
            score = re.findall(c, self.driver.page_source)

            # 创建 ActionChains 对象
            actions = ActionChains(self.driver)
            element_to_hover_over = self.driver.find_element(By.XPATH,
                                                             '//*[@id="ice-container"]/div/div/div[2]/div/div/div[1]/div[2]')
            # 在元素上执行鼠标悬停操作
            actions.move_to_element(element_to_hover_over).perform()
            try:
                money = self.driver.find_element(By.XPATH,
                                                 '/html/body/div[7]/div/div[2]/div/div/div/div[1]/div[2]/span')
                score.append(money.text)
                print(score)
            except NoSuchElementException:
                print(score)
            self.driver.close()
            self.driver.switch_to.window(self.original_window)
            return

        if flag == 0 or flag == 2:
            for em in all_em:
                p = em.find_element(By.XPATH, current_XPATH[2])
                print(p.text)
                pass
            if flag == 2:
                money = self.driver.find_element(By.XPATH, current_XPATH[3])
                print(money.get_attribute('title'))
            pass

        elif flag == 1:
            for i in range(3, 9 + 1, 3):
                p = all_em[i]
                print(p.text)
            money = self.driver.find_element(By.XPATH, current_XPATH[2])
            print(money.get_attribute('title'))
            pass

        # 关闭新窗口并切换回原始窗口
        self.driver.close()
        self.driver.switch_to.window(self.original_window)
        pass

    def writeError(self, title, url):
        with open('./error.txt', 'a+') as f:
            f.write(title + ' : ' + url)
            f.write('\n')

    def getData(self, element):
        element.click()
        new_window = [window for window in self.driver.window_handles if window != self.original_window][0]
        self.driver.switch_to.window(new_window)
        page = self.driver.page_source

        pattern = ['"score":"(.*?)"', '<span class="dsr-num .*?">(.*?)</span>',
                   'class="shopdsr-score-con">(.*?)</span>',
                   '<span class="rateinfo">.*?<em>(.*?)</em>.*?<i class="rate-icon']
        result = []
        ' <span class="shopdsr-score-con">4.8</span>'
        index = 0
        while len(result) < 3:
            result = re.findall(pattern[index], page, re.S)

            index += 1
            if index == len(pattern):
                print(self.driver.current_url)
                break

        if len(result) == 3:
            result.insert(0, self.driver.title)
            print('title : ' + self.driver.title)
            print(result)

            pass

        # pattern = '<meta name="(.*?)" content=".*?">'
        # result = re.search(pattern, page)
        # if 'description' in result.group():
        #     print('PC店铺')
        #     try:
        #         pattern_shop_name = 'shopName":"(.*?)"'
        #         shop_name = re.search(pattern_shop_name, page)
        #         print(shop_name.group(1))
        #         pattern_score = '"score":"(.*?)"'
        #         result = re.findall(pattern_score, page, re.S)
        #
        #         data = {shop_name.group(1): {'描述': result[0], '服务': result[1], '物流': result[2]}}
        #         self.data.update(data)
        #         print(data)
        #     except:
        #         print("爬取错误")
        #         print(self.driver.current_url)
        #         self.writeError(self.driver.title, self.driver.current_url)
        # elif 'oversea' in result.group():
        #     print('海外店铺')
        #     try:
        #         '<span class="dsr-num red">4.8</span>'
        #         '<span class="dsr-num red">4.9</span>'
        #         pattern_shop_name = '<a class="shop-name-link" .*?>(.*?)</a>'
        #         shop_name = re.search(pattern_shop_name, page, re.S)
        #         pattern_score = '<span class="dsr-num red">(.*?)</span>'
        #         result = re.findall(pattern_score, page, re.S)
        #         data = {shop_name.group(1): {'描述': result[0], '服务': result[1], '物流': result[2]}}
        #         self.data.update(data)
        #         print(data)
        #     except:
        #         print("爬取错误")
        #         print(self.driver.current_url)
        #         self.writeError(self.driver.title, self.driver.current_url)
        #
        # elif 'referrer' in result.group():
        #     print('天猫店铺')
        #
        #     try:
        #         pattern_shop_name = '<meta property="og:title" content="(.*?)">'
        #         shop_name = re.search(pattern_shop_name, page, re.S)
        #         pattern_score = 'class="shopdsr-score-con">(.*?)</span>'
        #         result = re.findall(pattern_score, page)
        #         data = {shop_name.group(1): {'描述': result[0], '服务': result[1], '物流': result[2]}}
        #         self.data.update(data)
        #         print(data)
        #     except:
        #         print("爬取错误")
        #         print(self.driver.current_url)
        #         self.writeError(self.driver.title, self.driver.current_url)
        # else:
        #     print('未知网页类型')
        #     pass
        # 关闭新窗口并切换回原始窗口
        self.driver.close()
        self.driver.switch_to.window(self.original_window)
        pass

    def getUrl2(self, url):
        self.driver.get(url)
        # 等待二维码扫描登录完成，超时时间设置为30秒
        WebDriverWait(self.driver, 300).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="list-container"]'))
        )

        parent_div = self.driver.find_element(By.XPATH, '//*[@id="list-container"]')
        all_divs = parent_div.find_elements(By.XPATH, './li')
        for div in all_divs:
            try:
                # 尝试使用第一个 XPath 查找元素
                a = div.find_element(By.XPATH, "./ul/li[2]/h4/a[1]")

            except NoSuchElementException:
                self.driver.execute_script("window.scrollTo(0, 60);")
                try:
                    # 如果第一个 XPath 找不到元素，使用第二个 XPath 查找
                    '//*[@id="list-container"]/li[7]/div/ul/li[2]/h4/a[1]'
                    a = div.find_element(By.XPATH, "./div/ul/li[2]/h4/a[1]")  # 替换为你的备用 XPath
                    '//*[@id="list-container"]/li[12]/div/ul/li[2]/h4/a[1]'
                except NoSuchElementException:
                    print("错误，没找到网址")
                    a = None
            if a:
                self.shopListUrl.append(a.get_attribute("href"))

                # 保存当前窗口句柄
                self.original_window = self.driver.current_window_handle
                try:
                    self.getData(a)
                except:
                    print("错误执行 getData")

        pass

    def getUrl(self, word):
        # key = self.driver.find_element(By.XPATH, '//*[@id="q"]')
        # key.send_keys(word)
        # time.sleep(1)
        #
        # searchButton = self.driver.find_element(By.XPATH, '//*[@id="J_SearchForm"]/button')
        # searchButton.click()
        index = 0
        while True:
            url = f'https://shopsearch.taobao.com/search?initiative_id=staobaoz_20240502&q={word}&spm=a21n57.1&s={index}'
            self.getUrl2(url)
            index += 20

    def login(self):  # 登录方法分装

        self.driver.get("https://login.taobao.com/member/login.jhtml")
        try:
            # 等待二维码扫描登录完成，超时时间设置为30秒
            WebDriverWait(self.driver, 600).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="J_SiteNavLogin"]/div[1]/div/a'))
            )
            print("扫描登录成功！")

            # 登录成功后，打印页面标题和当前页面 URL
            print("登录成功，页面标题：", self.driver.title)
            print("当前页面 URL：", self.driver.current_url)

            cookies = self.driver.get_cookies()
            with open('cookies.json', 'w') as f:
                json.dump(cookies, f)

        except Exception as e:
            print("扫描登录超时或出现其他异常:", e)

    def cookie(self):
        if os.path.exists("cookies.json"):  # 判断这个文件是否存在
            url = "https://shopsearch.taobao.com/browse/shop_search.htm"
            self.driver.get(url)
            with open('cookies.json', 'r') as f:
                cookies = json.load(f)
            self.driver.delete_all_cookies()
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.get(url)  # 这个是再次刷新这不不可少
            # self.driver.refresh()

            try:
                if self.driver.find_element(By.XPATH, '//*[@id="J_SiteNavLogin"]/div[1]/div/a'):  # 判断登录存在，执行登录
                    print('使用cooking登录成功')
            except:
                print("cooking登录失败")

            return True
        else:
            return False


if __name__ == "__main__":
    m = Taobao()
    shopUrlList = m.getUrl('男装')
    pass
