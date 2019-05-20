#scrapy runspider flask_test.py -o data.json
# -*- coding:utf-8 -*-
import scrapy

class FlaskSpider(scrapy.Spider):
    name='flask_test'
    start_urls=['http://flask.pocoo.org/docs/0.12',]

    def parse(self, response):
        for item in response.xpath('//*[@id="user-s-guide"]//a'):
            yield{
                'link':item.xpath('.//@href').extract_first()
            }
