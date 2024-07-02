# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Myspider2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    标题 = scrapy.Field()
    描述 = scrapy.Field()
    优惠价 = scrapy.Field()
    原价 = scrapy.Field()
    评论数 = scrapy.Field()
    评价 = scrapy.Field()
    作者 = scrapy.Field()
    时间 = scrapy.Field()
    出版社 = scrapy.Field()

    pass
