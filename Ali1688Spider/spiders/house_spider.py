# -*- coding: utf-8 -*-
import scrapy


class HouseSpiderSpider(scrapy.Spider):
    name = 'house_spider'
    start_urls = ['http://www.gzcc.gov.cn/data/laho/ProjectSearch.aspx/']

    def parse(self, response):
        houselist = response.xpath('//div[@class="resultList"]/div[@class="bd"]/table[@class="resultTableC"]/tbody/tr')
        for item in  houselist:
            numer = item.xpath('string(./td[1])').extract()
            proName = item.xpath('string(./td[2])').extract()
            devComp = item.xpath('string(./td[3])').extract()
            preCode = item.xpath('string(./td[4])').extract()
            proAddr = item.xpath('string(./td[5])').extract()
            selledNum = item.xpath('string(./td[6])').extract()
            unselledNum = item.xpath('string(./td[7])').extract()
            result={
                'numer':numer,
                'proName':proName,
                'devComp':devComp,
                'preCode':preCode,
                'proAddr':proAddr,
                'selledNum':selledNum,
                'unselledNum':unselledNum,
            }
            print(result)

