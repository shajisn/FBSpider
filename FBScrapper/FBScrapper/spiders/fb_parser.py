import sys

import scrapy
from scrapy.spider import BaseSpider
from scrapy.http import FormRequest
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from scrapy.http import Request

class DmozSpider(BaseSpider):
    name = "test"

    def start_requests(self):
        header_vals = {'Accept-Language': ['en'],
            'Content-Type': ['application/x-www-form-urlencoded'],
            'Accept-Encoding': ['gzip,deflate'],
            'Accept': ['text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'],
            'User-Agent': ['Mozilla/5.0 Gecko/20070219 Firefox/2.0.0.2']
        }

        start_url = ['https://www.facebook.com/login.php?login_attempt=1&lwv=111'];
        yield scrapy.Request(url=start_url[0], headers=header_vals, callback=self.parse)

    def parse(self, response):
        # print('Login form----------------------' , response.body)
        return [FormRequest.from_response(response, formname='login_form',
            formdata={'email':'08075950793','pass':'Snap$Snap6'}, 
            callback=self.after_login)]

    def after_login(self, response):
        if "authentication failed" in response.body:
            self.log("Login failed", level=log.ERROR)
            return
        else
            self.log("Login Success ", level=log.INFO)
            return Request(query, callback=self.page_parse)

    def page_parse(self, response):
        hxs = HtmlXPathSelector(response)
        print(hxs)
        items = hxs.select('//div[@class="_4_yl"]')
        count = 0
        print(items)