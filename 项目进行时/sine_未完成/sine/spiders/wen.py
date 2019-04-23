# -*- coding: utf-8 -*-
import scrapy
from sine.items import SineItem

class WenSpider(scrapy.Spider):
    name = 'wen'
    allowed_domains = ['news.sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        #pass
		item = SineItem()