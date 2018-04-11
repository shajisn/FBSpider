import scrapy

# name: identifies the Spider. It must be unique within a project, that is,
#     you can’t set the same name for different Spiders.
#
# start_requests(): must return an iterable of Requests (
#     you can return a list of requests or write a generator function) which the Spider will
#     begin to crawl from. Subsequent requests will be generated successively from these
#     initial requests.
#
# parse(): a method that will be called to handle the response downloaded for each of the
#     requests made. The response parameter is an instance of TextResponse that holds the
#     page content and has further helpful methods to handle it.
#
# The parse() method usually parses the response, extracting the scraped data as dicts and
#     also finding new URLs to follow and creating new requests (Request) from them.
#
# Scrapy schedules the scrapy.Request objects returned by the start_requests method of the Spider.
#     Upon receiving a response for each one, it instantiates Response objects and calls the
#     callback method associated with the request (in this case, the parse method)
#     passing the response as argument.


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

class QuotesSpider1(scrapy.Spider):
    name = "quotes1"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)

import scrapy


class QuotesSpider2(scrapy.Spider):
    name = "quotes2"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

import scrapy


class QuotesSpider3(scrapy.Spider):
    name = "quotes3"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)