# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentdeepItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    # 职位名称
    position = scrapy.Field()
    # 详情连接
    positionlink = scrapy.Field()
    # 职位类别
    tepy = scrapy.Field()
    # 人数
    num = scrapy.Field()
    # 地点
    location = scrapy.Field()
    # 时间
    time = scrapy.Field()
