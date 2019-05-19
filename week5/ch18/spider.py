import json

from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

results = []

def parse(response):
    for user in response.xpath('//div[@class="common-content"]//div[@class="row comment-item"]'):
        result={}
        result['name']=user.xpath('.//div[@class="user-name"]/a/text()').re_first('[^\s]+')
        result['content']=user.xpath('.//div[@class="content"]//text()').re_first('[^\s]+')
        results.append(result)

def has_next_page(response):
    next_page=response.xpath('//div[@class="common-content"]//div[@class="base-pagination"]/nav/ul/li[2]').extract_first()
    return "disabled" not in next_page

def goto_next_page(driver):

    label=driver.find_element_by_xpath('//div[@class="common-content"]//div[@class="base-pagination"]/nav/ul/li[2]/a')
    try:
        label.click()
    except: #ElementClickInterceptedException:
        print("Element is not clickable at point (424, 3212)")

def wait_page_return(driver,page):
    time.sleep(10)
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//ul[@class="pagination"]/li[2]/a')))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//ul[@class="pagination"]/li[2]/a')))
    
def spider():

#driver = webdriver.PhantomJS()
    driver = webdriver.Chrome()
    url = 'https://www.shiyanlou.com/courses/427'
    driver.get(url)
    page = 1

    while True:
        wait_page_return(driver,page)
        html = driver.page_source
        response = HtmlResponse(url=url, body=html.encode('utf8'))
        parse(response)

        if not has_next_page(response):
            break
        print("*********** page: ",str(page))
        page += 1
        goto_next_page(driver)

    with open('/home/fywest/git/python/week5/ch18/comments.json','w') as f:
        f.write(json.dumps(results))

if __name__ == '__main__':
    spider()
