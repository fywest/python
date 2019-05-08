# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import UserItem

class UsersSpider(scrapy.Spider):
    name = 'users'
    #allowed_domains = ['shiyanlou']
    start_urls = ['']
    
    @property
    def start_urls(self):

        return ('https://shiyanlou.com/user/{}/'.format(i) for i in range(525000, 524800,-10))

    def parse(self, response):
        yield UserItem({
                'name':response.xpath('//*[@class="user-meta"]/span[1]/text()').re_first('\S+'),
                'join_date':response.xpath('//*[@class="user-join-date"]/text()').re_first('[0-9]+\-[0-9]+\-[0-9]+'),
                'learn_courses_num':response.xpath('//*[@class="user-courses-data"]/div/div/div/span[1]/text()').re_first('[0-9]+'),
                })
