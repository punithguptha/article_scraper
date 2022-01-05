import scrapy


class CnnSpider(scrapy.Spider):
    name = 'cnn'
    allowed_domains = ['cnn.com']
    start_urls = ['http://cnn.com/']

    def parse(self, response):
        pass
