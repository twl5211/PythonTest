# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # items.py
    标题 = scrapy.Field()
    正文 = scrapy.Field()
    作者 = scrapy.Field()
    时间 = scrapy.Field()
    评论人数 = scrapy.Field()
    点赞人数 = scrapy.Field()
    观看人数 = scrapy.Field()

    pass
