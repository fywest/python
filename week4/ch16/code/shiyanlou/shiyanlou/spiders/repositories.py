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
            yield{
                'name': course.xpath('.//h3/a/text()').re_first('[^\s]+'),
                'update_time': course.xpath('.//relative-time/@datetime').extract_first(),
            }

        next_name=response.xpath('//*[@id="user-repositories-list"]/div/div/a/text()').get()
        if next_name == 'Next':
            print(next_name)
            next_page=response.xpath('//*[@id="user-repositories-list"]/div/div/a/@href').get()
        else:
            print(next_name)
            next_page=response.xpath('//*[@id="user-repositories-list"]/div/div/a[2]/@href').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)




