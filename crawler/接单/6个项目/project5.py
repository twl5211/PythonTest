# -*- coding: utf-8 -*-
# @Time ： 2024/7/1 10:16
# @Auth ： 陈楷雄
# @File ：project5.py
# @IDE ：PyCharm
import pprint

import requests
from lxml import html
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36",
}
base_url = 'https://www.shicimingju.com/'
url = 'https://www.shicimingju.com/book/sanguoyanyi.html'

response = requests.get(url,headers=headers)

response.encoding = 'utf-8'

tree = html.fromstring(response.text)

chapters_xpath = '//*[@id="main_left"]/div/div[4]/ul/li/a'
chapters = tree.xpath(chapters_xpath)
book_list = []
for chapter in chapters:
    book = {
        'title': chapter.xpath('./text()')[0],
        'url': base_url + chapter.xpath('./@href')[0]
    }
    book_list.append(book)


pprint.pprint(book_list)