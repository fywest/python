import scrapy

class UserContentSpider(scrapy.Spider):
    name = "shiyanlou"
    start_urls=['https://www.shiyanlou.com/courses/427',]

    def parse(self, response):
        print("********************")

        for user in response.xpath('//div[@class="common-content"]//div[@class="row comment-item"]'):
            yield{
                'name':user.xpath('.//div[@class="user-name"]/a/text()').re_first('[^\s]+'),
                'content':user.xpath('.//div[@class="content"]//text()').re_first('[^\s]+'),
            }


