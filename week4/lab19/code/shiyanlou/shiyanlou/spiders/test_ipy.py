# coding: utf-8
response.body
name=response.xpath('//*[@class="user-meta"]/span[1]/text()').extract_first()
name
join_date=response.xpath('//*[@class="user-join-date"]/span[1]/text()').extract_first()
join_date
join_date=response.xpath('//*[@class="user-join-date"]/span[2]/text()').extract_first()
join_date
join_date=response.xpath('//*[@class="user-join-date"]/text()').extract_first()
join_date
num=response.xpath('//*[@class="user-       courses-data"]/span[1]/text()').extract_first()
num
num=response.xpath('//*[@class="user-courses-data"]/span[1]/text()').extract_first()
num
num=response.xpath('//*[@class="user-courses-data"]/span/text()').extract_first()
num
num=response.xpath('//*[@class="user-courses-data"]/div/div/span/text()').extract_first()
num
num=response.xpath('//*[@class="user-courses-data"]/div/div/div/span/text()').extract_first()
num
num=response.xpath('//*[@class="user-courses-data"]/div/div/div/span/text()').re_first('^\(/d\)$')
num
num=response.xpath('//*[@class="user-courses-data"]/div/div/div/span/text()').re_first('^.$')
num
num=response.xpath('//*[@class="user-courses-data"]/div/div/div/span/text()').re_first('^.+$')
num
num=response.xpath('//*[@class="user-courses-data"]/div/div/div/span/text()').re_first('.+')
num
num=response.xpath('//*[@class="user-courses-data"]/div/div/div/span/text()').re_first('[0-9]')
num
join_date=response.xpath('//*[@class="user-join-date"]/text()').extract_first()
join_date
join_date=response.xpath('//*[@class="user-join-date"]/text()').re_first('[0-9]-[0-9]-[0-1]')
join_date
join_date=response.xpath('//*[@class="user-join-date"]/text()').re_first('[0-9]\-[0-9]\-[0-1]')
join_date
join_date=response.xpath('//*[@class="user-join-date"]/text()').re_first('[0-9]')
join_date
join_date=response.xpath('//*[@class="user-join-date"]/text()').re_first('[0-9]+')
join_date
join_date=response.xpath('//*[@class="user-join-date"]/text()').re_first('[0-9]+[0-9]+[0-9]')
join_date
join_date=response.xpath('//*[@class="user-join-date"]/text()').re_first('[0-9]+\-[0-9]+[0-9]')
join_date
join_date=response.xpath('//*[@class="user-join-date"]/text()').re_first('[0-9]+\-[0-9]+\-[0-9]+')
join_date
name=response.xpath('//*[@class="user-meta"]/span[1]/text()').extract_first()
name
name=response.xpath('//*[@class="user-meta"]/span[1]/text()').re_first('^\s')
name
name=response.xpath('//*[@class="user-meta"]/span[1]/text()').re_first('^s')
name
name=response.xpath('//*[@class="user-meta"]/span[1]/text()').re_first('\w')
name
name=response.xpath('//*[@class="user-meta"]/span[1]/text()').re_first('\S')
name
name=response.xpath('//*[@class="user-meta"]/span[1]/text()').re_first('\S+')
name
