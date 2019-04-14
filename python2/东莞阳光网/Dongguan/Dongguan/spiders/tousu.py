# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Dongguan.items import DongguanItem

class TousuSpider(CrawlSpider):
    name = 'tousu'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']


    rules = (
        Rule(LinkExtractor(allow=r'type=4&page=\d+')),
        Rule(LinkExtractor(allow=r'/html/question/\d+/\d+.shtml'), callback='parse_item')
    )

    def parse_item(self, response):
        #item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        #return item
        item = DongguanItem()
        
        # 标题
        item['title'] = response.xpath('//div[@class="wzy1"]//span[@class="niae2_top"]/text()').extract()[0]
        # 编号
        item['number'] = response.xpath('//div[@class="wzy1"]//td[@valign="middle"]/span[2]/text()').extract()[0]
        # 内容
        try:
            item['content'] = response.xpath('//div[@class="wzy1"]//div[@class="contentext"]/text()').extract()[0]
        except :
            pass
        #item['content'] = response.xpath('//div[@class="wzy1"]//div[@class="contentext"]/text()').extract()[0]
        # 链接地址
        item['url'] = response.url

        yield item