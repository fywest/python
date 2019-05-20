# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from flask_doc.items import PageItem

from scrapy.selector import Selector


class FlaskSpider(CrawlSpider):
    name = 'flask'
    allowed_domains = ['flask.pocoo.org']
    #start_urls = ['http://flask.pocoo.org/']
    start_urls = ['http://flask.pocoo.org/docs/0.12']

    rules = (
        Rule(LinkExtractor(tags=('a',),attrs=('href',)), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        #item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        #return item
        item = PageItem()
        url=str(response.url)
        content=str(response.body)
        item['url']=url
        item['content']=content

        
        yield item
