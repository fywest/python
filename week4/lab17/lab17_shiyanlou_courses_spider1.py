# -*- coding:utf-8 -*-
import  scrapy

class ShiyanlouCoursesSpider(scrapy.Spider):

    name = 'shiyanlou-github'
    start_urls = ['https://github.com/shiyanlou?tab=repositories',]

#def start_requests(self):
       #start_urls = ['https://github.com/shiyanlou?tab=repositories',]

    def parse(self, response):

        for course in response.xpath('//*[@id="user-repositories-list"]/ul/li'):
            yield{
#'name': course.xpath('.//h3/a/text()').re('[a-z]+\-?[a-z]+'),
#'name': course.xpath('.//h3/a/text()').extract(),
                'name': course.css('a::text').get(),
            }


