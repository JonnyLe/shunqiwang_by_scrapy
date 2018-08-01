# encoding=utf-8
__author__ = 'Jonny'
__location__ = '北京'
__date__ = '2018/7/19 15:00'


import requests
from lxml import etree
import time

def testSpider1():
    '''
    用于测试xpath是否能抓到页面中的某个数据，简化框架的测试的流程
    :return:
    '''
    proxys = [
        {'HTTP':'61.135.217.7:80'},
        {'HTTPS':'125.120.200.49:6666'},
        {'HTTPS': '223.241.116.66:18118'},
        {'HTTPS': '121.231.155.251:6666'},
        {'HTTPS': '118.31.220.3:8080'},
        {'HTTPS': '101.236.21.22:8866'},
        {'HTTPS': '121.231.32.242:6666'},
        {'HTTPS': '143.137.202.110:53281'},
        {'HTTPS': '103.110.88.6:8080'},
        {'HTTPS': '197.255.41.120:53281'},
        {'HTTP': '219.141.153.43:80'},
        {'HTTPS': '185.56.245.219:8080'},
        {'HTTP': '119.136.145.159:808'},
        {'HTTP': '180.118.86.44:9000'},
        {'http': '123.180.69.45:8010'},
        {'http': '145.239.77.20:80'},
    ]
    url = 'https://www.baidu.com'
    # for proxy in proxys:
    #     response = requests.get(url = url,proxies=proxy)
    #     time.sleep(3)
    #     print('##############################################################')
    #     print(' response:',proxy,'------',response.status_code)
    #     print('request:',response.headers)
    #     print('##############################################################')
    response = requests.get(url=url)
    print(response.url)
    # response = etree.HTML(response.text)
    # company  = response.xpath('td[contains(text(),"经营状态:")]/following::td[1]/text()')


if __name__ == '__main__':
    testSpider1()