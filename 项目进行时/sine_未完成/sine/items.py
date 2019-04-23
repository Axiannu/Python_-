# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SineItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    #大标题
    B_title = scrapy.Field()
    #大标题_URL
    B_url = scrapy.Field()

    #小标题
    S_title = scrapy.Field()
    #小标题_URL
    S_url = scrapy.Field()
    
    #文章_标题
    A_title = scrapy.Field()
    #文章_URL
    A_url = scrapy.Field()
    #文章_内容
    A_text = scrapy.Field()
