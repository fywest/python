# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
#from flask_doc.items import PageItem

#from scrapy.selector import Selector


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
        print('****************************: ',str(response.url))
        text=response.xpath('//text()').extract()
        sentence=','.join(word.strip() for word in text)
        yield{
            'name':str(response.xpath('//body//h1/text()').extract_first()),
            'url':str(response.url),
            'content':sentence
            #'content':str(response.headers)
        }

        
        #yield item
