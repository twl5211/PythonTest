import scrapy
import os


class ItcastSpider(scrapy.Spider):
    name = 'test'
    start_urls = ['https://www.baidu.com']
    allowed_domains = ['baidu.com']
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'{page}.html'

        # 确保保存的目录存在
        os.makedirs('html_pages', exist_ok=True)
        path = os.path.join('html_pages', filename)

        with open('baidu.html', 'wb') as f:
            f.write(response.body)

        self.log(f'Saved file {filename}')
