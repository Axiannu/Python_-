# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tencentdeep.items import TencentdeepItem

class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=#a0']

    link_rule = LinkExtractor(allow = ('start=\d+'))

    rules = (
        Rule(link_rule, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        #item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        #return item
        
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentdeepItem()

            # 职位名称
            item['position'] = each.xpath("./td[1]/a/text()").extract()[0]
            # 详情连接
            item['positionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            item['tepy'] = each.xpath("./td[2]/text()").extract()[0]
            # 人数
            item['num'] = each.xpath("./td[3]/text()").extract()[0]
            # 地点
            item['location'] = each.xpath("./td[4]/text()").extract()[0]
            # 时间
            item['time'] = each.xpath("./td[5]/text()").extract()[0]

            yield item