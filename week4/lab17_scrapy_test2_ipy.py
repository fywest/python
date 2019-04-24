# coding: utf-8
get_ipython().run_line_magic('load', 'lab17_scrapy_test1_ipy.py')
# %load lab17_scrapy_test1_ipy.py
import scrapy
from scrapy.http import HtmlResponse
#response=HtmlResponse('https://github.com/shiyanlou?tab=repositories')

print(response)
print(response.body)
#response.title
print(response.headers)
print(response.headers.get)
print(response.xpath('//title').extract())
response.xpath('//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[1]/h3/a')
response.xpath('//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[1]/h3/a/text()')
response.xpath('//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[1]/h3/a/text()').extract_first()
response.xpath('//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[1]/h3/a/text()').extract()
response.xpath('//*[@id="user-repositories-list"]/ul/li/div/div/h3/a/text()').extract()
response.xpath('//*[@id="user-repositories-list"]/ul/li/div/div/h3/a/text()').re('[a-z]+\-?[a-z]+')
response.xpath('//*[@id="user-repositories-list"]/ul/li/div/div/relative-time/datetime')
response.xpath('//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[3]/relative-time').extract()
date_time=response.xpath('//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[3]/relative-time').re('"(.+)"')
#['2019-04-24T02:38:19Z']
print(date_time)
get_ipython().run_line_magic('load', 'lab17_scrapy_test1_ipy.py')
# %load lab17_scrapy_test1_ipy.py
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
'''['<title>shiyanlou (实验楼在线教育) / Repositories · GitHub</title>']
['louplus-ml', 'louplus-dm', 'library', 'shiyanlou-docs', 'louplus-python', 'louplus-linux', 'dog', 'louplus-bigdata', 'lou', 'challenge', 'ele', 'php-crawler', 'louplus-php', 'trojan', 'jekyll-bootstrap', 'shiyanlou', 'cs', 'cssfinaltest', 'shiyanlou', 'cs', 'php-server', 'node-red', 'scrapy-weather', 'shiyanlou', 'cs', 'contact', 'shiyanlou', 'cs', 'flask', 'termbox-go', 'shiyanlou', 'cs', 'node-red', 'ifttt', 'sms', 'js-minesweeper', 'mininet', 'saepythondevguide']
['2019-04-24T02:38:19Z']
'''
