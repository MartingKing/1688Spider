# -*- coding: utf-8 -*-
# scrapy genspider ali_spider https://www.1688.com/命令行自动生成这个文件
# scrapy startproject Ali1688Spider 命令行自动创建爬虫项目
import scrapy


# 进入黄页获取工商注册信息 TODO
# registerUrl = response.xpath('//a[@id="J_COMMON_GoToYellowPage"]/@href').extract()[0]
# yield scrapy.Request(registerUrl, callback=self.parse_companyinfo)


# 进入黄页获取信息
# def parse_companyinfo(self, response):
#     companyTag = response.xpath('//div[@class="company-detail-show"]//div[@class="content"]')
#     # print('companyTag>>>',companyTag)
#     products = companyTag.xpath('//table/tbody/tr[2]/text()').extract()
#     operateWays = companyTag.xpath('//table/tbody/tr[3]/text()').extract()
#     registerMoney = companyTag.xpath('//table/tbody/tr[5]/text()').extract()
#     registerTime = companyTag.xpath('//table/tbody/tr[6]/text()').extract()
#     registerAddr = companyTag.xpath('//table/tbody/tr[7]/text()').extract()
#     legal_representative = companyTag.xpath('//table/tbody/tr[9]/text()').extract()
#     companyCode = companyTag.xpath('//table/tbody/tr[10]/text()').extract()
#
#     companyDetailTag = companyTag.xpath('//table[@class="detail-info"]/tbody')
#     # print('companyDetailTag>>>',companyDetailTag)
#     companyMmber = companyDetailTag.xpath('//tr[2]/text()').extract()
#     customerGroup = companyDetailTag.xpath('//tr[4]/text()').extract()
#     companyProfitPerYear = companyDetailTag.xpath('//tr[5]/text()').extract()
#     companyOutputMoney = companyDetailTag.xpath('//tr[6]/text()').extract()
#     companyBrand = companyDetailTag.xpath('//tr[7]/text()').extract()
#     companyInfo = {
#         'products': products,
#         'operateWays': operateWays,
#         'registerMoney': registerMoney,
#         'registerTime': registerTime,
#         'registerAddr': registerAddr,
#         'legal_representative': legal_representative,
#         'companyCode': companyCode,
#         'companyMmber': companyMmber,
#         'customerGroup': customerGroup,
#         'companyProfitPerYear': companyProfitPerYear,
#         'companyOutputMoney': companyOutputMoney,
#         'companyBrand': companyBrand,
#     }
#     print(companyInfo)

class AliSpiderSpider(scrapy.Spider):
    name = 'test_spider1'
    # start_urls = ['https://shop1490258895041.1688.com/page/creditdetail.htm?spm=b26110380.2178313.result.13.116b6722cPLuBq']
    # start_urls = ['https://oksumayinhua.1688.com/page/creditdetail.htm?spm=a2615.7691473.autotrace-topNav.4.16215ad4rUsJvY']
    start_urls = ['https://fudele.1688.com/page/creditdetail.htm?spm=b26110380.2178313.result.36.77d15c71s36WNE']

    def parse(self, response):
        companyTag = response.xpath('//h1[@class="company-name"]')
        # 公司名称
        companyName = self.getListWithDefault(companyTag.xpath('./span/text()').extract())[0]
        companyName = self.replaceSpace(companyName)
        # 诚信年限
        loyaltyYears = \
        self.getListWithDefault(companyTag.xpath('./a[@class="icon icon-chengxintong"]/text()').extract())[0]
        # 诚信等级
        loyaltyLevel = self.getListWithDefault(companyTag.xpath('./a[last()]/text()').extract())[0]

        contactTag = response.xpath('//div[@class="text company-contact"]')
        # 联系人  J_STRENGTH_CompanyContact
        global contactPerson, telephone, mobile
        contactPerson = contactTag.xpath('//div[@id="J_COMMON_CompanyContact"]/span[@class="contact-info"]/text()').extract()#self.getListWithDefault()[0]
        # contactPerson = self.replaceSpace(contactPerson)
        # 有两种布局，ID不一样 如果一种没获取到数据换另一种
        if len(contactPerson) == 0:
            print('second contactPerson')
            contactPerson = \
            self.getListWithDefault(contactTag.xpath('//span[@id="J_STRENGTH_CompanyContact"]/text()').extract())[0]
            contactPerson = self.replaceSpace(contactPerson)
        # 固话
        telephone = \
        self.getListWithDefault(response.xpath('string(//span[@id="J_COMMON_CompanyInfoTelShow"])').extract())[0]
        telephone = self.replaceSpace(telephone)
        if len(telephone) == 0:
            print('second telephone')
            telephone = self.getListWithDefault(
                response.xpath('string(//span[@id="J_STRENGTH_CompanyInfoTelShow"])').extract())[0]
            telephone = self.replaceSpace(telephone)
        # 手机号码
        mobile = self.getListWithDefault(response.xpath('string(//div[@id="J_COMMON_CompanyInfoPhoneShow"])').extract())[0]
        mobile = self.replaceSpace(mobile)
        if len(mobile) == 0:
            print('second mobile')
            mobile = \
            self.getListWithDefault(response.xpath('string(//span[@id="J_STRENGTH_CompanyInfoPhoneShow"])').extract())[
                0]
            mobile = self.replaceSpace(mobile)

        # 成交数
        translateNum = self.getListWithDefault(
            response.xpath('string(//div[@id="J_CompanyTradeCreditRecord"]/ul/li[1])').extract())[0]
        translateNum = self.replaceSpace(translateNum)
        # 累计买家数
        buyerNum = self.getListWithDefault(
            response.xpath('string(//div[@id="J_CompanyTradeCreditRecord"]/ul/li[2])').extract())[0]
        buyerNum = self.replaceSpace(buyerNum)
        # 注册时间
        registerTime = self.getListWithDefault(response.xpath(
            'string(//div[@class="info-bottom"]//div[@class="info-box info-right"]//table/tr[1])')).extract()[0]
        registerTime = self.replaceSpace(registerTime)
        # 注册资金
        registerMoney = self.getListWithDefault(response.xpath(
            'string(//div[@class="info-bottom"]//div[@class="info-box info-right"]//table/tr[2])').extract())[0]
        registerMoney = self.replaceSpace(registerMoney)
        # 运营范围
        operateArea = self.getListWithDefault(response.xpath(
            'string(//div[@class="info-bottom"]//div[@class="info-box info-right"]//table/tr[3])').extract())[0]
        operateArea = self.replaceSpace(operateArea)
        # 地址
        address = self.getListWithDefault(response.xpath(
            'string(//div[@class="info-bottom"]//div[@class="info-box info-right"]//table/tr[4])').extract())[0]
        address = self.replaceSpace(address).replace("查看地图", "")

        companyCode = self.getListWithDefault(
            response.xpath('string(//div[@class="register-data"]//table/tbody/tr[3])').extract())[0]
        companyCode = companyCode.replace("法定代表人：", "")
        companyCode = self.replaceSpace(companyCode).replace("\xa0", "")
        starfNum = self.getListWithDefault(response.xpath('string(//li[@id="J_FCA_DepthInspectionTab_product"]/div/ul/li[1])').extract())[0]
        companyArea = self.getListWithDefault(response.xpath('string(//li[@id="J_FCA_DepthInspectionTab_product"]/div/ul/li[2])').extract())[0]
        equipmentNum = self.getListWithDefault(response.xpath('string(//li[@id="J_FCA_DepthInspectionTab_product"]/div/ul/li[3])').extract())[0]
        print(self.replaceSpace(starfNum))
        print(self.replaceSpace(companyArea))
        print(self.replaceSpace(equipmentNum))

        baseInfo = {
            'companyName': companyName,
            'loyaltyYears': loyaltyYears,
            'loyaltyLevel': loyaltyLevel,
            'contactPerson': contactPerson,
            'telephone': telephone,
            'mobile': mobile,
            'translateNum': translateNum,
            'buyerNum': buyerNum,
            'registerTime': registerTime,
            'registerMoney': registerMoney,
            'operateArea': operateArea,
            'address': address,
            'companyCode': companyCode,
        }
        # print(baseInfo)

    def replaceSpace(self, params):
        if params is None:
            return "--"
        else:
            newstr = params.strip()
            newstr = newstr.replace(" ", "")
            newstr = newstr.replace("\r", "")
            newstr = newstr.replace("\n", "")
            newstr = newstr.replace("\t", "")
            return newstr

    def getListWithDefault(self, mylist):
        if mylist is None:
            return ["no_data"]
        else:
            if (isinstance(mylist, list)):
                if mylist:
                    return mylist
                else:
                    return mylist.insert(0, "no_data")
            else:
                print("mylist is not list>>>", mylist)
                return self.replaceSpace(mylist)
