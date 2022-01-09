import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from article_scraper.items import Test,NewsArticle
import json

class ApnewsSpider(CrawlSpider):
    name = 'apnews'
    allowed_domains = ['apnews.com']
    start_urls = ['http://apnews.com/']
    regexpnew=r'article\/[a-zA-Z0-9\-]+'
    rules=[Rule(LinkExtractor(allow=regexpnew),callback='parse_info',follow=True)]
    custom_settings={
        'FEED_URI':'apnews.json',
        'FEED_FORMAT':'json',
        'CLOSESPIDER_PAGECOUNT':100
    }

    def parse_info(self, response):
        newsArticle=NewsArticle();
        jsonData=json.loads(response.xpath('//script[@data-rh="true"]/text()').get())
        newsArticle["title"]=jsonData['headline']
        newsArticle["author"]=jsonData['author'][0]
        newsArticle["time"]=jsonData['datePublished']
        newsArticle["description"]=response.xpath('//meta[@name="description"]/@content').get()
        newsArticle["content"]=response.xpath("//div[@class='Article']/p/text()").getall()
        newsArticle["url"]=response.url
        newsArticle["site"]="apnews"
        return newsArticle
