# coding: utf-8
response.url
response.title
response.headers
response.xpath('//*[@id="__layout"]/div/div[1]/div/div[1]/div/div[1]/div/div[2]')
course=response.xpath('//*[@id="__layout"]/div/div[1]/div/div[1]/div/div[1]/div/div[2]').extract_first()
course
course[0]
course=response.xpath('//*[@id="__layout"]/div/div[1]/div/div[1]/div/div[1]/div/div[2]/div[1]/div[1]').extract_first()
course
name=course.css('div.course-name::text').extrat_first()
course=response.xpath('//*[@id="__layout"]/div/div[1]/div/div[1]/div/div[1]/div/div[2]/div[1]/div[1]').get()
name=course.css('div.course-name::text').extrat_first()
course=response.xpath('//*[@id="__layout"]/div/div[1]/div/div[1]/div/div[1]/div/div[2]/div[1]/div[1]').get()
course=response.xpath('//*[@id="__layout"]/div/div[1]/div/div[1]/div/div[1]/div/div[2]/div[1]/div[1]')
name=course.css('div.course-name::text').extrat_first()
name=course.css('div.course-name::text').extract_first()
name
course
name=course.xpath('.//h6/text()').extract_first()
name
name=course.xpath('.//h6[contains(class,"course-name")]/text()').extract_first()
name
name=course.xpath('.//h6[contains(@class,"course-name")]/text()').extract_first()
nme
name
description=course.xpath('.//[contains(@class,"course-desc")]/text()').extract_first()
description=course.xpath('.//div[contains(@class,"course-desc")]/text()').extract_first()
description
type_info=course.xpath('.//span[contains(@class,"course-type")]/text()').extract_first()
type_info
student=course.xpath('.//span[contains(@class,"students-count")]/span/text()').extract_first()
student
