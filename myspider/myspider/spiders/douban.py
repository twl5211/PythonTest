import scrapy

from scrapy import Request, Selector, item
from scrapy.selector.unified import Selector
import re

class ItcastSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    # def get_cookie(self):
    #     data = '''bid=EvKTDU4vUgc; _pk_id.100001.4cf6=9141ade64c12c190.1719730843.; __utmc=30149280; __utmz=30149280.1719730843.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=223695111; __utmz=223695111.1719730843.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __yadk_uid=5xSpks42DYc4LnNGlbRMYA5mxUrWl3qv; ll="118238"; _vwo_uuid_v2=D6D095E4A2176CE9F92071575DE51AE71|75f344a23b1384fb64311f3d2da5fee5; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1719737601%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D2ck9xuxCT7Y-B4KHekWYTGgQlh6yD2mmFEnPCG9b0AyY1c3xF7G2Tvs3U4keRB0t%26wd%3D%26eqid%3D9832d31e0006a6940000000266810297%22%5D; _pk_ses.100001.4cf6=1; __utma=30149280.1969858920.1719730843.1719735305.1719737602.3; __utmb=30149280.0.10.1719737602; __utma=223695111.459899252.1719730843.1719735305.1719737602.3; __utmb=223695111.0.10.1719737602; ap_v=0,6.0'''
    #
    #     temp = data.split('; ')
    #     cookie = {}
    #     for i in temp:
    #         key = i.split('=')
    #         cookie[key[0]] = key[1]
    #     return cookie
    #     pass

    def parse(self, response):
        print(response.request.headers)
        move_item = {}
        move_item['title'] = response.xpath('//div[@class="hd"]/a/span[1]/text()').extract()
        move_item['detail_url'] = response.xpath('//div[@class="hd"]/a/@href').extract()
        move_item['main_actor'] = response.xpath('//*[@id="info"]/span[3]/span[2]/span/a').extract()
        move_item['scriptwriter'] = response.xpath('//*[@id="info"]/span[2]/span[2]/a/@href').extract()
        for url in move_item['detail_url']:
            print("执行",url)
            yield Request(url=url, callback=self.parse_detail, meta={'move_item': move_item})
            break
            pass

    def parse_detail(self, response):
        move_item = response.meta['move_item']

        move_item['director'] = response.xpath('//*[@id="info"]/span[1]/span[2]/a/text()').extract()
        rule_str = r'''
        <span class="pl">制片国家/地区:</span>(?P<country>.*?)<br/>
        <span class="pl">语言:</span>(.*?)<br/>
        <span class="pl">上映日期:</span> <span property="v:initialReleaseDate" content=".*?">(.*?)</span> / <span property="v:initialReleaseDate" content=".*?">.*?</span><br/>
        <span class="pl">片长:</span> <span property="v:runtime" content=".*?">(.*?)</span><br/>
        <span class="pl">又名:</span>.*?<br/>
        <span class="pl">IMDb:</span>.*?<br>'''

        temp = re.compile(rule_str, re.S)

        are, language, release_time, time = re.findall(temp, response.text)[0]
        move_item['area'] = are
        move_item['language'] = language
        move_item['release_time'] = release_time
        move_item['time'] = time
        print(move_item)
        return move_item
        pass
