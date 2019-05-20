# coding: utf-8
response.headers
link=response('//*[@id="user-s-guide"]//a/@href')
link=response.xpath('//*[@id="user-s-guide"]//a/@href')
link
link=response.xpath('//*[@id="user-s-guide"]//a/@href').extract_all()
link=response.xpath('//*[@id="user-s-guide"]//a/@href').extract_first()
link
link=response.xpath('//*[@id="user-s-guide"]//a/@href').extract_all()
link=response.xpath('//*[@id="user-s-guide"]//a')
link[1]
link[2]
link
link=response.xpath('//*[@id="user-s-guide"]//a/@href')
link[1]
link[1].extract_first()
link=response.xpath('//*[@id="user-s-guide"]//a/@href').extract_first()
link
link=response.xpath('//*[@id="user-s-guide"]//a/@href').extract_all()
link=response.xpath('//*[@id="user-s-guide"]//a/@href')
link1=link.extract_first()
link1
link1=link[0].extract_first()
link[0]
link=response.xpath('//*[@id="user-s-guide"]//a/@href')
link
link[1]
link[2]
link[2].data()
link=response.xpath('//*[@id="user-s-guide"]//a/@href').data()
link=response.xpath('//*[@id="user-s-guide"]//a/@href')
link1=link[1]
link1
link1.xpath('/@data')
link1.xpath('//@data')
link1.xpath('@data')
link=response.xpath('//*[@id="user-s-guide"]//a/@href')
link
link=response.xpath('//*[@id="user-s-guide"]//a/@href')
link=response.xpath('//*[@id="user-s-guide"]//a')
link
link=response.xpath('//*[@id="user-s-guide"]//a/@href')
link
link=response.xpath('//*[@id="user-s-guide"]//a')
link
link=response.xpath('//*[@id="user-s-guide"]//a')
link[1]
link[1].xpath('/@href')
link[1].xpath('.//@href')
link[1].xpath('.//@href').extract_first()
link=response.xpath('//*[@id="user-s-guide"]//a/@href')
link1=link.get()
link1
link
link=response.xpath('//*[@id="user-s-guide"]//a/@href'),get()
link=response.xpath('//*[@id="user-s-guide"]//a/@href').get()
link
link=response.xpath('//*[@id="user-s-guide"]//a/@href')
link[1]
response
response.title
response.headers
response.body
link[1].body
link[1].get().body
response.body
response.url
from scrapy.linkextractors import linkExtractor
from scrapy.linkextractors import LinkExtractor
item=LinkExtractor(tags('a','area'),attrs('href',))
item=LinkExtractor(attrs('href',))
item=LinkExtractor(attrs=('href',))
item
for i in item:
    print(i.text)
    
item=LinkExtractor(attrs=('href',)).extract_links(response)
item
for i in item:
    print(i.text)
    
item=LinkExtractor(tags=('a',)attrs=('href',)).extract_links(response)
item=LinkExtractor(tags=('a'),attrs=('href',)).extract_links(response)
for i in item:
    print(i.text)
    
for i in item:
    print(i.url)
    
for i in item:
    print(i.url)
    print(i.body)
    
for i in item:
    print(i.url)
    print(i.body)
    
for i in item:
    print(i.url)
    
    
for i in item1:[1:10]:
    print(i.url)

    
    
for i in item1[1:10]:
    print(i.url)
    

    
    
for i in item[1:10]:
    print(i.url)
    
    

    
    
for i in item[1:10]:
    print(i.url)
    print(type(i))
    
    
    

    
    
for i in item[1:10]:
    print(i.url)
    print(type(i))
    print(i.text)
    
    
    
    

    
    
for i in item[1:10]:
    print(i.url)
    print(type(i))
    print(i.text)
    sel=selector(i)
    print(sel.body)
    
    
    
    
    

    
    
for i in item[1:10]:
    print(i.url)
    print(type(i))
    print(i.text)
    sel=Selector(i)
    print(sel.body)
    
    
    
    
    

    
    
from scrapy.selector import Selector
for i in item[1:10]:
    print(i.url)
    print(type(i))
    print(i.text)
    sel=Selector(i)
    print(sel.body)
    
    
    
    
    
    

    
    
for i in item[1:10]:
    print(i.url)
    print(type(i))
    print(i.text)
    sel=Selector(i)
    print(sel)
    
    
    
    
    
    
    

    
    
for i in item[1:10]:
    print(i.url)
    print(type(i))
    print(i.text)
    sel=Selector(i)
    print(sel)
    
    
    
    
    
    
    

    
    
for i in item[1:10]:
    print(i.url)
    print(i.text)
    
   
    
    
    
    
    
    
    

    
    
for i in item[1:10]:
    print(i.url)
    print(i.text)
    
   
    
    
    
    
    
    
    

    
    
response.title
response.headers
response.text
response.xpath('//text()')
response.xpath('//text()').extract_all()
response.xpath('//text()').extract_first()
response.xpath('//text()').get()
response.xpath('//text()').extract()
text=response.xpath('//text()').extract()
text
text=response.xpath('//text()').extract()
sentense=' '.join(text)
sentense
sentense=' '.join(text.strip())
sentense=' '.join(word.strip() for word in text)
sentense
word_list=(word.strip() for word in text)
word_list
word_list=[word.strip() for word in text]
word_list
sentense=','.join(word.strip() for word in text)
sentense
sentense='\n'.join(word.strip() for word in text)
sentense
sentense=','.join(word.strip() for word in text)
sentense
sentense=','.join(word.strip() for word in text)
