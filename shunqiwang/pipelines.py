# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from shunqiwang import settings
import pymongo

class ShunqiwangPipeline(object):
    def __init__(self):
        host = settings.MONGODB_HOST
        port = settings.MONGODB_PORT
        dbname = settings.MONGODB_DBNAME
        sheet = settings.MONGODB_SHEET
        client = pymongo.MongoClient(host=host,port=port)
        db = client[dbname]
        self.collection = db[sheet]


    def process_item(self, item, spider):
        info = dict(item)
        self.collection.insert(info)
        return item

    def close_spider(self):
        pass