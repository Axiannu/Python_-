# -*- coding: utf-8 -*-
import scrapy
from tvs.items import TvsItem

class QinmeiSpider(scrapy.Spider):
    name = 'qinmei'
    allowed_domains = ["tencent.com"]

    #start_urls = ["https://tieba.baidu.com/f?kw=%E5%81%87%E9%9D%A2%E9%AA%91%E5%A3%AB"]
	
	#url = "http://hr.tencent.com/position.php?&start="
    #offset = 0

    start_urls = ["http://hr.tencent.com/position.php?&start=0"]

    def parse(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
        #pass
		item = TvsItem()

		item['name'] = each.xpath("./td[1]/a/text()").extract()[0]
		#print each.extract()[0]
		yield item