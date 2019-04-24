# coding: utf-8
import scrapy
from scrapy.http import HtmlResponse
#response=HtmlResponse('https://github.com/shiyanlou?tab=repositories')

#print(response)
#print(response.body)
#response.title
#print(response.headers)
#print(response.headers.get)
print(response.xpath('//title').extract())
response.xpath('//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[1]/h3/a')
response.xpath('//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[1]/h3/a/text()')
response.xpath('//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[1]/h3/a/text()').extract_first()
response.xpath('//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[1]/h3/a/text()').extract()
response.xpath('//*[@id="user-repositories-list"]/ul/li/div/div/h3/a/text()').extract()
name=response.xpath('//*[@id="user-repositories-list"]/ul/li/div/div/h3/a/text()').re('[a-z]+\-?[a-z]+')
print(name)

response.xpath('//*[@id="user-repositories-list"]/ul/li/div/div/relative-time/datetime')
response.xpath('//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[3]/relative-time').extract()
date_time=response.xpath('//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[3]/relative-time').re('"(.+)"')
#['2019-04-24T02:38:19Z']
print(date_time)
