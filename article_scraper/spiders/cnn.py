import scrapy
from datetime import date
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from article_scraper.items import Test,NewsArticle

class CnnSpider(CrawlSpider):
    name = 'cnn'
    allowed_domains = ["edition.cnn.com"]
    start_urls = ['http://edition.cnn.com/']
    regexpnew=r'\/202[0-9]\/[0-9][0-9]\/[0-9][0-9]\/[\-a-zA-Z]+\/[a-zA-Z\-]+\/index.html';
    rules=[Rule(LinkExtractor(allow=regexpnew),callback='parse_info',follow=True)]
    custom_settings={
        'FEED_URI':'cnnnews.json',
        'FEED_FORMAT':'json',
        'CLOSESPIDER_PAGECOUNT':100
    }


    def parse_info(self, response):
        newsArticle=NewsArticle()
        newsArticle["title"]=response.xpath('//h1[@class="pg-headline"]/text()').get()
        newsArticle["author"]=response.xpath("//span[@class='metadata__byline__author']/a/text()").get()
        newsArticle["time"]=response.xpath('//p[@class="update-time"]/text()').get()
        newsArticle["description"]=response.xpath('//meta[@name="description"]/@content').get()
        newsArticle["content"]=response.xpath('//div[@itemprop="articleBody"]/section/div[@class="l-container"]//*/text()').getall()
        newsArticle["url"]=response.url
        newsArticle["site"]="cnn"
        return newsArticle
