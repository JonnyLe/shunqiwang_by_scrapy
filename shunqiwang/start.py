# encoding=utf-8
__author__ = 'Jonny'
__location__ = '北京'
__date__ = '2018/7/18 14:35'

from scrapy import cmdline

def start():
    cmdline.execute('scrapy crawl shunQiWangSpider'.split())


if __name__ == '__main__':
    start()