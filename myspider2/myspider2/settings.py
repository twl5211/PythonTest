# Scrapy settings for myspider2 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html


MYSQL_URL = '127.0.0.1'
MYSQL_DB = 'dd_shop'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'



BOT_NAME = "myspider2"

SPIDER_MODULES = ["myspider2.spiders"]
NEWSPIDER_MODULE = "myspider2.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/114.0.0.0 "
              "Safari/537.36")

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

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
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}
DEFAULT_REQUEST_HEADERS = {
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
   "Accept-Language": "en",
    'Cookie':'bid=EvKTDU4vUgc; _pk_id.100001.4cf6=9141ade64c12c190.1719730843.; __utmc=30149280; __utmz=30149280.1719730843.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=223695111; __utmz=223695111.1719730843.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __yadk_uid=5xSpks42DYc4LnNGlbRMYA5mxUrWl3qv; ll="118238"; _vwo_uuid_v2=D6D095E4A2176CE9F92071575DE51AE71|75f344a23b1384fb64311f3d2da5fee5; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1719737601%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D2ck9xuxCT7Y-B4KHekWYTGgQlh6yD2mmFEnPCG9b0AyY1c3xF7G2Tvs3U4keRB0t%26wd%3D%26eqid%3D9832d31e0006a6940000000266810297%22%5D; __utma=30149280.1969858920.1719730843.1719735305.1719737602.3; __utma=223695111.459899252.1719730843.1719735305.1719737602.3; ap_v=0,6.0'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "myspider2.middlewares.Myspider2SpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "myspider2.middlewares.Myspider2DownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "myspider2.pipelines.Myspider2Pipeline": 300,
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
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
