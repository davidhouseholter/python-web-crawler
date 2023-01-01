import scrapy

class MySpiderSpider(scrapy.Spider):
    name = 'quotes_spider'
    allowed_domains = ['lens.xyz']
    start_urls = ['http://docs.lens.xyz/docs']

    def parse(self, response):
        quotes = response.xpath("//div[@class='quote']//span[@class='text']/text()").extract()
        yield {'quotes': quotes}