# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
import time

import requests


class MyProxyMiddlleWare(object):

    def process_request(self, request, spider):
        # 得到地址
        proxy = self.get_Random_Proxy()
        # 设置代理
        request.meta['proxy'] = proxy

    def process_response(self, request, response, spider):
        # 如果该ip不能使用，更换下一个ip
        if response.status != 200:
            proxy = self.get_Random_Proxy()
            print("this is response ip:" + proxy)
            # 对当前reque加上代理
            request.meta['proxy'] = proxy
            return request
        return response

    def get_Random_Proxy(self):
        '''随机从文件中读取proxy'''
        while 1:
            with open('usefull_ip.txt', 'r') as f:
                proxies = f.readlines()
                if proxies:
                    break
                else:
                    time.sleep(1)
        proxy = random.choice(proxies).strip()
        return proxy

        # 这个方法是从接口获取ip
        # url = 'http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=0&port=11&pack=41020&ts=1&ys=0&cs=0&lb=1&sb=0&pb=45&mr=2&regions='
        # result = requests.get(url).json()
        # if(len(result["data"])>0):
        #     ip = result["data"][0]["ip"]
        #     port = result["data"][0]["port"]
        #     proxy = "http://" + str(ip) + ":" + str(port)
        #     print('当前IP》》》',proxy)
        #     return proxy
        #
        # else:
        #     time.sleep(1)
        #     return self.get_Random_Proxy()

