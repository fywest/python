# coding: utf-8
response.css("div.quote")
quote=response.css("div.quote")[0]
quote
title = quote.css("span.text"::text).get()
title = quote.css("span.text::text").get()
title
tags = quote.css("div.tags a.tag::text").getall()
tags
for quote in response.css("div.quote"):
    text=quote.css("span.text::text").get()
    author=quote.css("small.author::text").get()
    tags=quote.css("div.tags a.tag::text").getall()
    print(dict(text=text, author=author, tags=tags))
    
get_ipython().run_line_magic('save', '/quit')
get_ipython().run_line_magic('save', 'quote1_ipy.py 1:10')
response.css('li.nex a').get()
response.css('li.next a').get()
response.css('li.next a text()').get()
response.css('li.next a=text()').get()
response.css('li.next a=text').get()
response.css('li.next a').get()
response.css('li.next a::text').get()
response.css('li.next a::attr(href)').get()
