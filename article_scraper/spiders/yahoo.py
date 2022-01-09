import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from article_scraper.items import Test,NewsArticle

class YahooSpider(CrawlSpider):
    name = 'yahoo'
    allowed_domains = ['news.yahoo.com']
    start_urls = ['http://news.yahoo.com/']
    regexpnew=r'[a-zA-Z0-9\-]+.html'
    rules=[Rule(LinkExtractor(allow=regexpnew),callback='parse_info',follow=True)]
    custom_settings={
        'FEED_URI':'yahoonews.json',
        'FEED_FORMAT':'json',
        'CLOSESPIDER_PAGECOUNT':100
    }

    def parse_info(self,response):
        newsArticle=NewsArticle()
        newsArticle["title"]=response.xpath('//h1[@data-test-locator="headline"]/text()').get()
        newsArticle["author"]=response.xpath("//span[@class='caas-author-byline-collapse']/text()").get()
        newsArticle["time"]=response.xpath('//div[@class="caas-attr-time-style"]//time/text()').get()
        newsArticle["description"]=response.xpath('//meta[@name="description"]/@content').get()
        newsArticle["content"]=response.xpath("//div[@class='caas-body']/p/text()").getall()
        newsArticle["url"]=response.url
        newsArticle["site"]="yahoo"
        return newsArticle

    def parse_info_test(self, response):
        test=Test()
        test["title"]=response.xpath('//h1[@data-test-locator="headline"]/text()').get()
        test["time"]=response.xpath('//div[@class="caas-attr-time-style"]//time/text()').get()
        test["author"]=response.xpath("//span[@class='caas-author-byline-collapse']/text()").get()
        test["content"]=response.xpath("//div[@class='caas-body']/p/text()").getall()
        test["url"]=response.url
        return test
