# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from settings import *
import pymongo


info_list = []

class LianjiaPipeline(object):

    def __init__(self):
        self.client = pymongo.MongoClient(host=MONGO_HOST,port=MONGO_PORT)
        self.db = self.client[MONGO_DB]
        self.mongo = self.db[MONGO_COLL]

    def item_isExist(self, item):
        count = self.mongo.find({"crawl_date":item['crawl_date'], "houseSellId":item["houseSellId"]}).count()
        return count

    def process_item(self, item, spider):
        global info_list
        if self.item_isExist(item) == 0:
            info_list.append(item)
            print "info list length:",len(info_list)
            if len(info_list) > 100:
                response = self.mongo.insert_many(info_list)
                if response:
                    print "insert mongodb~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~success!!!"
                    info_list = []
                else:
                    print "insert mongodb~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~faild!!!"
