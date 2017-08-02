# -*- coding: utf-8 -*-
import scrapy
import json
from lianjia.items import LianjiaItem
import time
import requests

def url_list():
    start_urls = []
    rp = requests.get(url='http://soa.dooioo.com/api/v4/online/house/ershoufang/search?access_token=7poanTTBCymmgE0FOn1oKp&channel=ershoufang&cityCode=sh&limit_count=1&limit_offset=1').content
    rp_j = json.loads(rp)
    for num in range(0,rp_j['data']['total_count'],50):
        url = "http://soa.dooioo.com/api/v4/online/house/ershoufang/search?access_token=7poanTTBCymmgE0FOn1oKp&channel=ershoufang&cityCode=sh&limit_count=50&limit_offset={}".format(num)
        start_urls.append(url)
    return start_urls



class LianjiaShSpider(scrapy.Spider):
    name = "lianjia_sh"
    allowed_domains = ["sh.lianjia.com"]
    start_urls = url_list()


    def parse(self, response):
        house_d= json.loads(response.body)
        try:
            for house in house_d['data']['list']:
                item = LianjiaItem()
                item['title'] = house['title']
                item['acreage'] = house['acreage']
                item['cityCode'] = house['cityCode']
                item['districtName'] = house['districtName']
                try:
                    item['face'] = house['face']
                except Exception as e:
                    item['face'] = '无'
                item['floor_state'] = house['floor_state']
                item['houseSellId'] = house['houseSellId']
                item['latitude'] =house['latitude']
                item['hall'] = house['hall']
                item['metroRemark'] = house['metroRemark']
                item['plateName'] = house['plateName']
                item['propertyName'] = house['propertyName']
                item['referAvgPrice'] = house['referAvgPrice']
                item['room'] = house['room']
                item['showPrice'] = house['showPrice']
                item['unitPrice'] =house['unitPrice']
                item['tags'] = house['unitPrice']
                item['crawl_date'] = time.strftime('%Y%m%d',time.localtime(time.time()))
                yield item
        except Exception as e:
			print e