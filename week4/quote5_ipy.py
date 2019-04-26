# coding: utf-8
course=response.xpath('//*[@id="user-repositories-list"]/ul')
course
course[0]
name=course[0].css('h3 a::text').get()
name
name
name=course[0].css('h3 a::text').get()
name
course=response.xpath('//*[@id="user-repositories-list"]/ul/li')
course
course[0]
name=course[0].xpath('.div/div/h3/a/text()').re('[a-z]+\-?[a-z]+')
name
name=course[0].xpath('.h3/a/text()').re('[a-z]+\-?[a-z]+')
name=course[0].xpath('h3/a/text()').re('[a-z]+\-?[a-z]+')
name
name=course[0].xpath('div/div/a/text()').re('[a-z]+\-?[a-z]+')
name
name=course[0]
name
name1
name1=course[0].xpath('.//h3')
name1
name1=course[0].xpath('.//h3/text()').extract()
name1
name1=course[0].xpath('.//h3/a/text()').extract()
name1
name1
name1=course[0].xpath('.//h3/a/text()').re('\w+')
name1
name1=course[0].xpath('.//h3/a/text()').re('[a-z]+\-?[a-z]+')
