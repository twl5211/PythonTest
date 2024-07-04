# -*- coding: utf-8 -*-
# @Time ： 2024/7/1 16:05
# @Auth ： HongBao
# @File ：dd.py
# @IDE ：PyCharm
import scrapy

import re



class ItcastSpider(scrapy.Spider):
    name = 'dd'
    start_urls = ['https://search.dangdang.com/?key=%D7%F7%BC%D2%B3%F6%B0%E6%C9%E7&category_path=01.05.16.00.00.00&page_index=1']
    def parse(self, response):
        books_data = []
        father_element = response.xpath('//*[@id="component_59"]/li')

        print(len(father_element))
        for i in father_element:
            book_data = {}
            '''//product.dangdang.com/29709583.html'''
            id = i.xpath('./p[@class="name"]/a/@href').extract()
            bt = (i.xpath('./p[@class="name"]/a/text()')).extract()
            ms = i.xpath('./p[@class="detail"]/text()').extract()
            jg = i.xpath('./p[@class="price"]/span/text()').extract()
            pl = i.xpath('./p[@class="search_star_line"]/a/text()').extract()
            pj = i.xpath('./p[@class="search_star_line"]/span/span/@style').extract()
            zz = i.xpath('./p[@class="search_book_author"]/span[1]/a/@title').extract()
            sj = i.xpath('./p[@class="search_book_author"]/span[2]/text()').extract()
            cbs = i.xpath('./p[@class="search_book_author"]/span[3]/a/text()').extract()
            book_data['id'] = id[0].split('.')[-2].split('/')[-1]
            book_data['bt'] = bt[0].strip(' ') if bt else ''
            book_data['描述'] = ms[0] if ms else ''
            book_data['优惠价'] = jg[0] if jg else ''
            book_data['原价'] = jg[1] if jg else ''
            book_data['评论数'] = int(re.search(r'\d+', pl[0]).group()) if pl else ''
            book_data['评价'] = int(re.search(r'\d+', pj[0]).group()) if pj else ''
            book_data['作者'] = '/'.join(zz) if zz else ''
            book_data['时间'] = sj[0].replace(' /', '') if sj else ''
            book_data['出版社'] = cbs[0]

            yield book_data
        #     books_data.append(book_data)
        # return books_data

