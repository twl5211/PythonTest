# -*- coding: utf-8 -*-
# @Time ： 2024/6/30 23:30
# @Auth ： HongBao
# @File ：taobao.py
# @IDE ：PyCharm
import scrapy
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
# from taobao.items import TaobaoItem

username='你的淘宝账号'
password='你的淘宝密码'
product_name='要查找的产品名称'

class TaobaobaoSpider(scrapy.Spider):
    name = 'taobaobao'
    # allowed_domains = ['www.taobao.com']
    start_urls = ['https://login.taobao.com/member/login.jhtml']

    def login(self,url):
        options = webdriver.ChromeOptions()
        #防止淘宝检查自动化脚本
        options.add_argument("--disable-blink-features=AutomationControlled")
        bro = webdriver.Chrome(options=options)
        bro.maximize_window()
        bro.get(url)
        sleep(1)   #休眠一秒，不要太快
        bro.find_element_by_name("fm-login-id").send_keys(username) #输入账号
        sleep(1)
        bro.find_element_by_name("fm-login-password").send_keys(password) #输入密码
        sleep(1)
        bro.find_element_by_xpath("//*[@id='login-form']/div[4]/button").click() #登录
        return bro

    def parse(self, response):
        response = str(response).split(" ")[1].replace(">","")  #获取url
        print(response)
        bro = self.login(response) #调用登录淘宝
        num = 1
        for i in range(3): #从第一页开始拿数据  拿3页
            url = "https://s.taobao.com/search?q={0}&s={1}".format(product_name,str(num))  #product: 商品名称
            num += 1
            bro.get(url)
            html = bro.page_source
        soup = BeautifulSoup(html, 'lxml')
        data_list = soup.find_all(class_='item J_MouserOnverReq')
        for data in data_list:
            data_soup = BeautifulSoup(str(data), 'lxml')
            # 图片链接
            img_url = "http:" + data_soup.find(class_='J_ItemPic img')['data-src']
            # 图片价格
            price = data_soup.find('strong').string
            # 图片标题
            title = data_soup.find(class_='J_ItemPic img')['alt']
            # 详情页
            detail_url = "https:" + data_soup.find(class_="pic-link J_ClickStat J_ItemPicA")["data-href"]
            bro.get(detail_url)
            sleep(1)
            html_second = bro.page_source
            soup = BeautifulSoup(html_second, 'lxml')

            try:
                svolume = soup.find(class_="tm-ind-item tm-ind-sellCount").text.replace("月销量", "")
            except:
                svolume = 0

            try:
                evaluate = soup.find(class_="tm-ind-item tm-ind-reviewCount canClick tm-line3").text.replace("累计评价", "")
            except:
                evaluate = 0

            try:
                integral = soup.find(class_="tm-ind-item tm-ind-emPointCount").text.replace("送天猫积分", "")
            except:
                integral = 0

            #处理获取的的数据，做数据清洗
            # item = TaobaoItem(img_url=img_url, price=price, title=title, svolume=svolume, evaluate=evaluate,
            #                   integral=integral, detail_url=detail_url)
            print(img_url,price,title,svolume,evaluate,integral,detail_url)
            # yield item
