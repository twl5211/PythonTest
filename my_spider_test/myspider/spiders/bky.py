# -*- coding: utf-8 -*-
# @Time ： 2024/7/3 16:26
# @Auth ： HongBao
# @File ：bky.py
# @IDE ：PyCharm
# -*- coding: utf-8 -*-
# @Time ： 2024/7/1 16:05
# @Auth ： HongBao
# @File ：dd.py
# @IDE ：PyCharm
import json
import pprint
import random
import time

import scrapy

import re

from ..items import MyspiderItem


class ItcastSpider(scrapy.Spider):
    name = 'bky'
    allowed_domains = ["www.cnblogs.com"]

    def parse(self, response):
        print("这次请求是   ：   " + response.request.url)
        time.sleep(2)
        # father_element = response.xpath('//*[@id="component_59"]/li')
        elements = response.xpath('//article[@class="post-item"]/section')
        for element in elements:
            article = MyspiderItem()

            '//*[@id="digg_count_18274978"]'
            article['标题'] = element.xpath('./div/a/text()').extract()[0]
            content = element.xpath('./div/p/text()').extract()
            article['正文'] = self.clean_text(content)
            article['作者'] = element.xpath('./footer/a[1]/span/text()').extract()[0]
            article['时间'] = element.xpath('./footer/span[1]/span/text()').extract()[0]
            article['评论人数'] = element.xpath('./footer/a[2]/span/text()').extract()[0]
            article['点赞人数'] = element.xpath('./footer/a[3]/span/text()').extract()[0]
            article['观看人数'] = element.xpath('./footer/a[4]/span/text()').extract()[0]
            yield article
            pass

        # pprint.pprint(articles_list)

    def clean_text(self, articles_list):
        # 转换为单个字符串，并用空格连接
        clean_str = ' '.join(articles_list)
        # 移除多余的空白和换行
        clean_str = clean_str.replace('\n', '').replace('\r', '').strip()
        return clean_str
    def start_requests(self):
        headers = {
            'accept': 'text/plain, */*; q=0.01',
            'accept-language': 'zh-CN,zh;q=0.9',
            'content-type': 'application/json; charset=UTF-8',
            # Requests sorts cookies= alphabetically
            # 'cookie': '_ga=GA1.1.1688786784.1709538178; Hm_lvt_866c9be12d4a814454792b1fd0fed295=1719591697,1719766040,1719993531,1719997780; Hm_lpvt_866c9be12d4a814454792b1fd0fed295=1719999791; _ga_M95P3TTWJZ=GS1.1.1719993531.20.1.1719999809.0.0.0',
            'origin': 'https://www.cnblogs.com',
            'priority': 'u=1, i',
            'referer': 'https://www.cnblogs.com/cate/java/',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        url = 'https://www.cnblogs.com/AggSite/AggSitePostList'
        for i in range(1, 80):
            json_data = {
                'CategoryType': 'Picked',
                'ParentCategoryId': 0,
                'CategoryId': -2,
                'PageIndex': i,
                'TotalPostCount': 1639,
                'ItemListActionName': 'AggSitePostList',
            }
            yield scrapy.Request(
                url=url,
                method='POST',
                body=json.dumps(json_data),
                headers=headers,
                callback=self.parse
            )
        pass
