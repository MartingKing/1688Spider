# -*- coding: utf-8 -*-
import re

import scrapy

#下一页逻辑
class TestSpiderSpider(scrapy.Spider):
    name = 'test_spider2'
    start_urls = ['https://s.1688.com/company/-B1B1BEA9.html?netType=1%2C11&earseDirect=false&button_click=top&pageSize=30&n=y&offset=3&beginPage=2']

    def parse(self, response):
        total_page = response.xpath('//span[@class="total-page"]/text()').extract()[0]
        totalpage = re.sub("\D", "", total_page)
        cur_page = response.xpath('//span[@class="page-cur"]/text()').extract()[0]
        next_url = response.xpath('//a[@class="page-next"]/@href').extract_first()
        result = {
            'total_page':totalpage,
            'cur_page':cur_page,
            'next_url':next_url,
        }
        print(result)
