# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from datetime import datetime

class CheckItemPipeline:
    def process_item(self, article, spider):
        if not article['url'] or not article['last_edited'] or not article['title']:
            raise DropItem("Missing something..!")
        return article

class CleanDatePipeline:
    def process_item(self,article,spider):
        article['last_edited']=article['last_edited'].replace('This page was last edited on',' ').strip()
        article['last_edited']=datetime.strptime(article['last_edited'],'%d %B %Y, at %H:%M')
        return article

class NewsArticlePipeline:
    def process_item(self,newsArticle,spider):
        if not newsArticle["author"]:
            raise DropItem("Missing something...")
        newsArticle["content"]=[text.strip() for text in newsArticle['content']]
        return newsArticle
