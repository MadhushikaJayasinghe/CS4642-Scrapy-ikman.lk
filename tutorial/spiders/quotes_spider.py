import re
from urlparse import urljoin


import scrapy
from scrapy import Request
from scrapy.selector import HtmlXPathSelector

from tutorial.items import TutorialItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        with open('ikman_urls.csv') as f:
            urls = f.readlines()
        urls = [x.strip() for x in urls]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        item = TutorialItem()
        item['title'] = response.css('title::text').extract_first()
        item['name'] = response.css('div.item-content a.item-title.h4::text').extract_first()
        item['url'] = response.url
        item['price'] = response.css('div.item-content p.item-info strong::text').extract_first()
        item['location'] = response.css('div.item-content p.item-location span.item-area::text').extract_first()
        item['category'] = response.css('div.item-content p.item-location span.item-cat::text').extract_first()
        item['date'] = response.css('div.item-date::text').extract_first()

        yield item

        print item