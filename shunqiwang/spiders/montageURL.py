# encoding=utf-8
__author__ = 'Jonny'
__location__ = '北京'
__date__ = '2018/7/18 10:20'

import re
import requests

def montageUrl():
    headers = {'content-type': 'application/json',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    url = 'http://www.11467.com/dir.html'
    response = requests.get(url=url,headers=headers).text
    # print(response)
    # print('##########################################################################')
    patten = re.compile(r'http://www.11467.com/([a-z]+)/')
    temp_city_list = patten.findall(response)
    # print(temp_city_list)
    # print(len(temp_city_list))
    result_city_list = list(set(temp_city_list))
    result_city_list.sort(key=temp_city_list.index)
    print('##########################################################################')
    print(result_city_list)
    print('##########################################################################')
    # print(len(result_city_list))
    return result_city_list


if __name__ == '__main__':
    montageUrl()
