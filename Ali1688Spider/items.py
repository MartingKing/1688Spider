# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


#

class Ali1688SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    detailurl = scrapy.Field()
    companyName = scrapy.Field()
    loyaltyYears = scrapy.Field()
    loyaltyLevel = scrapy.Field()
    contactPerson = scrapy.Field()
    telephone = scrapy.Field()
    mobile = scrapy.Field()
    translateNum = scrapy.Field()
    buyerNum = scrapy.Field()
    registerTime = scrapy.Field()
    registerMoney = scrapy.Field()
    operateArea = scrapy.Field()
    address = scrapy.Field()
    companyCode = scrapy.Field()
    starfNum = scrapy.Field()
    companyArea = scrapy.Field()
    equipmentNum = scrapy.Field()
