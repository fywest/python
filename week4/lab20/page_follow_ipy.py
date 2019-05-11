# coding: utf-8
name=response.xpath('//h4[@class="course-info-name course-name inline-block"]/text()')
name
author=response.xpath('//div[@class="mooc-info"]/div[@class="teacher-info"]/span[1]/span/text()')
author
url_list=response.xpath('//div[@class="side-box course-advanced-box"]//div[@class="course-list"]/ul/li/a/@href')
url_list
