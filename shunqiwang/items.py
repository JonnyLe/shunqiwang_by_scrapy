# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShunqiwangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #获取公司名称
    company = scrapy.Field()
    #获取公司的电话
    company_tel = scrapy.Field()
    #获取经理人电话
    company_phone_manager = scrapy.Field()
    #获取公司地址
    company_address = scrapy.Field()
    #获取网址
    company_net = scrapy.Field()
    #获取邮箱
    company_email = scrapy.Field()
    #获取公司状态
    company_state = scrapy.Field()
