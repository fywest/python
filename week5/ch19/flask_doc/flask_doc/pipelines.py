# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
import redis
import json



class FlaskDocPipeline(object):
    def __init__(self):
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)

    def process_item(self, item, spider):
        print(item['url'])
        item['content']=re.sub(r'\s+',' ',item['content'])
        print(item['content'])

        self.redis.lpush('flask_doc:item',json.dumps(dict(item)))
        return item

def open_spider(self, spider):

        self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)
