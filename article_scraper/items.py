# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Article(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    url=scrapy.Field()
    last_edited=scrapy.Field()

class Test(scrapy.Item):
    title=scrapy.Field()
    time=scrapy.Field()
    author=scrapy.Field()
    url=scrapy.Field()
    content=scrapy.Field()

class NewsArticle(scrapy.Item):
    title=scrapy.Field()
    author=scrapy.Field()
    time=scrapy.Field()
    description=scrapy.Field()
    content=scrapy.Field()
    url=scrapy.Field()
    site=scrapy.Field()
