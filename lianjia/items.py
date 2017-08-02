# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

import time

class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    title = scrapy.Field()
    acreage = scrapy.Field()
    cityCode = scrapy.Field()
    districtName = scrapy.Field()
    face = scrapy.Field()
    floor_state = scrapy.Field()
    houseSellId = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    hall = scrapy.Field()
    metroRemark =  scrapy.Field()
    plateName = scrapy.Field()
    propertyName = scrapy.Field()
    referAvgPrice = scrapy.Field()
    room = scrapy.Field()
    showPrice = scrapy.Field()
    unitPrice = scrapy.Field()
    title = scrapy.Field()
    tags = scrapy.Field()
    crawl_date = scrapy.Field()





