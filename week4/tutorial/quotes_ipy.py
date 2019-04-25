# coding: utf-8
response.css('title')
response.css('title::text').getall()
response.css('title::text').get()
response.css('title::text').re(r'Quotes.*')
response.css('title::text').re(r'Q\w+')
response.css('title::text').re(r'\w+')
response.css('title::text').re(r'(\w+) to (\w+)')
response.xpath('//title')
