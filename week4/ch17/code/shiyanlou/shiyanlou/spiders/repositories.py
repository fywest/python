# -*- coding:utf-8 -*-
import  scrapy
from shiyanlou.items import RepositoryItem

class ShiyanlouRepositorySpider(scrapy.Spider):
    name = 'repositories'

    start_urls = ['https://github.com/shiyanlou?tab=repositories',]

    def parse(self, response):
        print("******************************")
        self.logger.info("Parse function called on %s",response.url)

        for course in response.xpath('//*[@id="user-repositories-list"]/ul/li'):
                
            item = RepositoryItem()

            item['name']= course.xpath('.//h3/a/text()').re_first('[^\s]+')
            item['update_time']= course.xpath('.//relative-time/@datetime').extract_first()

            course_url = response.urljoin(course.xpath('.//h3/a/@href').extract_first())
            request = scrapy.Request(course_url, callback=self.parse_author)
            request.meta['item'] = item

            yield request
        
        next_name=response.xpath('//*[@id="user-repositories-list"]/div/div/a/text()').get()
        if next_name == 'Next':
            print(next_name)
            next_page=response.xpath('//*[@id="user-repositories-list"]/div/div/a/@href').get()
        else:
            print(next_name)
            next_page=response.xpath('//*[@id="user-repositories-list"]/div/div/a[2]/@href').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
       

    def parse_author(self, response):
        item = response.meta['item']
        item['commits'] = response.xpath('//*[@id="js-repo-pjax-container"]//ul/li[1]/a/span/text()').re_first('[0-9]+')
        item['branches'] = response.xpath('//*[@id="js-repo-pjax-container"]//ul/li[2]/a/span/text()').re_first('[0-9]+')
        item['release'] = response.xpath('//*[@id="js-repo-pjax-container"]//ul/li[3]/a/span/text()').re_first('[0-9]+')

        yield item



