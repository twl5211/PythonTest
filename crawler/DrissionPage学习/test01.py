# -*- coding: utf-8 -*-
# @Time ： 2024/7/2 9:11
# @Auth ： HongBao
# @File ：test01.py
# @IDE ：PyCharm
import json
import os
import re
import time
from pprint import pprint
from threading import Thread
import pymysql
from DrissionPage import ChromiumPage
from DataRecorder import Recorder


class TaoBao():
    def __init__(self, filename):

        self.mysql_url = '127.0.0.1'
        self.mysql_password = '123456'
        self.mysql_db = 'dd_shop'
        self.mysql_user = 'root'
        self.cookie_filename = filename
        # # 新建页面对象
        self.page = ChromiumPage()
        #
        # if not self.init_cookie():  # 判断本地cookie失效或没有cookie文件就返回FALSE则再次登录
        #     self.login()
        #     pass
        # pass

    def init_cookie(self):
        if os.path.exists(self.cookie_filename):  # 判断这个文件是否存在
            self.page.get("https://shopsearch.taobao.com/browse/shop_search.htm")
            self.load_cookies()
            self.page.refresh()
            try:
                if self.page.ele("#J_SiteNavLogin > div:nth-of-type(1) > div > a", timeout=6):
                    print('使用cooking登录成功')
            except:
                print("cooking登录失败")
                return False
            return True
        else:
            return False

    def save_cookies(self):
        cookies = self.page.cookies(as_dict=True, all_domains=True)
        with open(self.cookie_filename, 'w') as file:
            json.dump(cookies, file)

    def load_cookies(self):
        with open(self.cookie_filename, 'r') as file:
            cookies = json.load(file)
        self.page.set.cookies(cookies)

    def login(self):
        self.page.get("https://login.taobao.com/member/login.jhtml")
        print("请扫描二维码进行登录")
        self.page.ele('xpath://*[@id="J_SiteNavLogin"]/div[1]/div/a', timeout=60000)
        print("登录成功")
        pass

    def start(self):
        print('开始爬取')
        recorder = Recorder('taobao.csv')
        for i in range(1, 2):
            time.sleep(2)
            url = f"https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20240701&js=1&localImgKey=&page={i}&q=女装&tab=all"
            Thread(target=self.collect, args=(url, recorder, i)).start()
            pass
        pass

    def connect_mysql(self, save_data):
        self.client = pymysql.connect(user=self.mysql_user, password=self.mysql_password, host=self.mysql_url,
                                      db=self.mysql_db)
        self.cursor = self.client.cursor()
        # SQL 插入语句，使用 %s 作为占位符
        sql = '''insert into taobao(id,title, priceWap, procity,realSales, nick, price,price, pic_path,shopInfo_title,auctionURL) values (%s, %s, %s,%s, %s, %s,%s, %s, %s, %s)'''
        # 执行参数化查询
        self.cursor.execute(sql, (save_data['item']))
        # 提交事务
        self.client.commit()
        pass

    def collect(self, url, recorder, title):
        """用于采集的方法
        :param tab: ChromiumTab 对象
        :param recorder: Recorder 记录器对象
        :param title: 类别标题
        :return: None
        """
        self.page.listen.start('/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/')  # 指定监听目标并启动监听
        self.page.get(url)
        self.page.ele('xpath://*[@id="pageContent"]/div[1]/div[3]/div[3]/div/div[1]/a/div/div[1]/div[1]/img[1]',
                      timeout=60000)
        packet = self.page.listen.wait()  # 等待数据包
        # 正则表达式模式
        pattern = r"mtopjsonp1\((.*)\)"
        # 使用 re.search() 查找匹配
        match = re.search(pattern, packet.response.body)

        item_list = match.group(1)
        itemsArray = json.loads(item_list)
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(itemsArray['data']['itemsArray'], f)
        shop_list = []

        for item in itemsArray['data']['itemsArray']:
            shop_data = {
                'title': item['title'].split('<')[0],
                'priceWap': item['priceWap'],
                'procity': item['procity'],
                'realSales': item['realSales'],
                'nick': item['nick'],
                'price': item['price'],
                'pic_path': item['pic_path'],
                'item_id': item['item_id'],
                'shopInfo_title': item['shopInfo']['title'],
                'shopInfo_url': item['shopInfo']['url'],
                'auctionURL': item['auctionURL']
            }
            shop_list.append(shop_data)
        pprint(shop_list)

        # num = 1  # 当前采集页数
        # while True:
        #     # 遍历所有标题元素
        #     for i in tab.eles('xpath:'):
        #         # 获取某页所有库名称，记录到记录器
        #         recorder.add_data((title, i.text, num))
        #
        #     # 如果有下一页，点击翻页
        #     btn = tab('@rel=next', timeout=2)
        #     if btn:
        #         btn.click(by_js=True)
        #         tab.wait.load_start()
        #         num += 1
        #
        #     # 否则，采集完毕
        #     else:
        #         break


def collect(tab, recorder, title):
    """用于采集的方法
    :param tab: ChromiumTab 对象
    :param recorder: Recorder 记录器对象
    :param title: 类别标题
    :return: None
    """
    num = 1  # 当前采集页数
    while True:
        # 遍历所有标题元素
        for i in tab.eles('.title project-namespace-path'):
            # 获取某页所有库名称，记录到记录器
            recorder.add_data((title, i.text, num))

        # 如果有下一页，点击翻页
        btn = tab('@rel=next', timeout=2)
        if btn:
            btn.click(by_js=True)
            tab.wait.load_start()
            num += 1

        # 否则，采集完毕
        else:
            break


def main():
    t = TaoBao('cookies.json')
    # t.save_cookies()
    t.start()
    # # 第一个标签页访问网址
    # page.get('https://gitee.com/explore/ai')
    # # 获取第一个标签页对象
    # tab1 = page.get_tab()
    # # 新建一个标签页并访问另一个网址
    # tab2 = page.new_tab('https://gitee.com/explore/machine-learning')
    # # 获取第二个标签页对象
    # tab2 = page.get_tab(tab2)

    # # 新建记录器对象
    # recorder = Recorder('data.csv')
    #
    # # 多线程同时处理多个页面
    # Thread(target=collect, args=(tab1, recorder, 'ai')).start()
    # Thread(target=collect, args=(tab2, recorder, '机器学习')).start()


if __name__ == '__main__':
    main()
