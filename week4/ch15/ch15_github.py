# -*- coding:utf-8 -*-
import  scrapy

class ShiyanlouCoursesSpider(scrapy.Spider):

    name = 'shiyanlou-courses'

    def start_requests(self):
        url_tmpl = 'https://github.com/shiyanlou?tab=repositories'

#return (url_tmpl.format(i) for i in range(1,4))
        urls=['https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all',
'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&cursor=bz0yMA%3D%3D',
'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&cursor=bz00MA%3D%3D',
'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&cursor=bz02MA%3D%3D',
'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&cursor=bz04MA%3D%3D',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        print("*******************************************************")
        print(response.url)
        print("*******************************************************")
        for course in response.xpath('//*[@id="__layout"]/div/div[1]/div/div[1]/div/          div[1]/div/div[2]/div[1]/div'):
            yield{
                'name': course.xpath('.//h6[contains(@class,"course-name")]/text()').extract_first(),
                'description': course.xpath('.//div[contains(@class,"course-desc")]/text()').extract_first(),
                'type': course.xpath('.//span[contains(@class,"course-type")]/text()').extract_first(default='Free'),
                'student': course.xpath('.//span[contains(@class,"students-count")]/span/text()').extract_first(),
            }

