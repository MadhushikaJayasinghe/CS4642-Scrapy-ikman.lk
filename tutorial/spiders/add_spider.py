import scrapy


class AdsSpider(scrapy.Spider):
    name = "ads"

    def start_requests(self):
        with open('ikman_urls.csv') as f:
            urls = f.readlines()
        urls = [x.strip() for x in urls]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        name = response.css('div.item-content a.item-title.h4::text').extract_first()
        filename = '%s.html' % name
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)