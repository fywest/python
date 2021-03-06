# -*- coding:utf-8 -*-
import  scrapy

class ShiyanlouCoursesSpider(scrapy.Spider):

    name = 'shiyanlou-github'

    def start_requests(self):
        url_tmpl = 'https://github.com/shiyanlou?tab=repositories&page={}'
#urls = (url_tmpl.format(i) for i in range(1,5))
        urls = ['https://github.com/shiyanlou?tab=repositories',]
        for url in urls:
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for course in response.css('div.course-body'):
            yield{
                'name': course.css('div.course-name::text').extract_first(),
                'description': course.css('div.course-desc::text').extract_first(),
                'type': course.css('div.course-footer span.pull-right::text').extract_first(default='Free'),
                'student': course.xpath('.//span[contains(@class, "pull-left")]/text()[2]').re_first('[^\d]*(\d+)[^\d]*')
            }


