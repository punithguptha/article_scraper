# Scrapy settings for article_scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'article_scraper'

SPIDER_MODULES = ['article_scraper.spiders']
NEWSPIDER_MODULE = 'article_scraper.spiders'

#Instead of in the commands one can use this file to also specify certain settings
# The CLOSESPIDER_PAGECOUNT setting doesnt exactly give us the results number that we are looking for..Since before the closing of the spider if there are some other requests in the queue they will get executed which leads to more than the specified amount of results
# CLOSESPIDER_PAGECOUNT=20
# FEED_URI='articles.json'
# FEED_FORMAT='json'
# FEED_EXPORT_ENCODING='utf-8'
# FEED_URI='articles.csv'
# FEED_FORMAT='csv'

# FEED_URI='cnntest.json'
# FEED_FORMAT='json'
# FEED_EXPORT_ENCODING='utf-8'

# FEED_URI='yahootest.json'
# FEED_FORMAT='json'
FEED_EXPORT_ENCODING='utf-8'

# FEED_URI='articles.xml'
# FEED_FORMAT='xml'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'article_scraper (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'article_scraper.middlewares.ArticleScraperSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'article_scraper.middlewares.ArticleScraperDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# The number beside pipeline is the priority..Lower gets executed first
ITEM_PIPELINES = {
   # 'article_scraper.pipelines.CheckItemPipeline': 100,
   # 'article_scraper.pipelines.CleanDatePipeline':200
   'article_scraper.pipelines.NewsArticlePipeline': 100
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
