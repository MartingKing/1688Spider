import random
import time

import requests
# 获取ip地址工具类


head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6815.400 QQBrowser/10.3.3006.400',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9'
}
url = 'http://webapi.http.zhimacangku.com/getip?num=20&type=2&pro=0&city=0&yys=0&port=11&pack=41010&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=110000,130000,140000,150000,210000,310000,320000,330000,340000,350000,360000,370000,410000,420000,430000,440000,500000,510000,530000,610000,620000'
result = requests.get(url).json()

def writeIpFormJsonToText():
    url = 'http://webapi.http.zhimacangku.com/getip?num=30&type=2&pro=&city=0&yys=0&port=11&pack=41020&ts=1&ys=0&cs=0&lb=1&sb=0&pb=45&mr=2&regions='
    result = requests.get(url).json()
    for i in range(0, len(result["data"])):
        ip = result["data"][i]["ip"]
        port = result["data"][i]["port"]
        proxy = "http://" + str(ip) + ":" + str(port)
        with open('usefull_ip.txt', 'a', newline='') as f:
            f.write(proxy + '\n')
        print(proxy)

#测试从接口获取的ip可以用的存进txt，不能用的过滤掉
def textIpIsUsefull():
    shoplist_url='https://s.1688.com/company/company_search.htm?keywords=%B9%E3%B6%AB&netType=1%2C11&n=y&sortType=pop&pageSize=30&offset=3&beginPage=50'
    shopdetail_url='https://dwyywj.1688.com/page/creditdetail.htm?spm=b26110380.2178313.result.9.2d942112OtIGEJ'
    url = 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=&city=0&yys=0&port=11&pack=41020&ts=1&ys=0&cs=0&lb=1&sb=0&pb=45&mr=2&regions='
    result = requests.get(url).text
    print(result)
    if(result is not None):
        proxy = "http://"+result
        plist = requests.get(shoplist_url, headers=head, proxies={"http":proxy})
        if(plist.status_code==200):
            pdetail = requests.get(shopdetail_url, headers=head, proxies={"http": proxy})
            if(pdetail.status_code==200):
                with open('usefull_ip.txt', 'a', newline='') as f:
                    f.write(proxy)
    else:
        print('result is None',result)
        textIpIsUsefull()
    time.sleep(1)
    textIpIsUsefull()

def textIpIsUsefullFromJson():
    shoplist_url = 'https://s.1688.com/company/company_search.htm?keywords=%BA%A3%C4%CF&pageSize=30&offset=3&beginPage=1'
    shopdetail_url = 'https://litree.1688.com/page/creditdetail.htm?spm=b26110380.2178313.result.13.78a3a06dnwTa9o'

    url = 'http://webapi.http.zhimacangku.com/getip?num=20&type=2&pro=&city=0&yys=0&port=11&pack=41010&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='
    result = requests.get(url).json()
    if(len(result["data"])>0):
        for i in range(0, len(result["data"])):
            ip = result["data"][i]["ip"]
            port = result["data"][i]["port"]
            proxy = "http://" + str(ip) + ":" + str(port)
            plist = requests.get(shoplist_url, headers=head, proxies={"http": proxy})
            if (plist.status_code == 200):
                pdetail = requests.get(shopdetail_url, headers=head, proxies={"http": proxy})
                if (pdetail.status_code == 200):
                    print(proxy)
    else:
        print('result is None',result)
        textIpIsUsefullFromJson()
    time.sleep(1)
    textIpIsUsefullFromJson()

def testIpIsOK(shoplist_url,proxy):
    plist = requests.get(shoplist_url, headers=head, proxies={"http": proxy})
    if (plist.status_code == 200):
        print(proxy)
    else:
        print('proxy is bad!')

shoplist_url='https://s.1688.com/company/company_search.htm?keywords=%D5%E3%BD%AD&netType=1%2C11&earseDirect=false&button_click=top&n=y&pageSize=30&offset=3&beginPage=47'
shoplist_url2='https://shop2z148z22722z4.1688.com/page/creditdetail.htm?spm=b26110380.2178313.result.10.38ac5c715lBs3C'
proxy = 'http://175.154.201.241:4226'

# testIpIsOK(shoplist_url2,proxy)
textIpIsUsefullFromJson()