# -*- coding: utf-8 -*-
import scrapy


class UsersSpider(scrapy.Spider):
    name = 'users'
    #allowed_domains = ['shiyanlou']
    #start_urls = ['http://shiyanlou/']

    def start_urls(self):

        return ('https://shiyanlou.com/user/{}/'.format(i) for i in range())

    def parse(self, response):
        pass
