# -*- coding: utf-8 -*-

# Scrapy settings for shunqiwang project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'shunqiwang'

SPIDER_MODULES = ['shunqiwang.spiders']
NEWSPIDER_MODULE = 'shunqiwang.spiders'


#导入数据库设置
MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_SHEET = 'SHUN_QI_COMP'
MONGODB_DBNAME = 'SHUNQUWAGN'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'shunqiwang (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 4
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'shunqiwang.middlewares.ShunqiwangSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'shunqiwang.middlewares.ShunqiwangDownloaderMiddleware': 543,
    'shunqiwang.middlewares.ShunqiwangUserAgentMiddleware':200,
    # 'shunqiwang.middlewares.ShunqiwangProxyMiddleware':300,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'shunqiwang.pipelines.ShunqiwangPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# HTTPERROR_ALLOWED_CODES = [400]#上面报的是400，就把400加入


USER_AGENT = [
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
]
PROXIES = [
    # {'ip_port':'http://61.135.217.7:80','user_password':''},
    {'ip_port':'125.120.200.49:6666','user_password':''},
    {'ip_port':'23.241.116.66:18118','user_password':''},
    {'ip_port':'121.231.155.251:6666','user_password':''},
    {'ip_port':'118.31.220.3:8080','user_password':''},
    {'ip_port':'101.236.21.22:8866','user_password':''},
    {'ip_port':'121.231.32.242:6666','user_password':''},
    {'ip_port':'143.137.202.110:53281','user_password':''},
    {'ip_port':'103.110.88.6:8080','user_password':''},
    {'ip_port':'197.255.41.120:53281','user_password':''},
    # {'ip_port':'http://219.141.153.43:80','user_password':''},
    {'ip_port':'185.56.245.219:8080','user_password':''},
    # {'ip_port':'http://119.136.145.159:808','user_password':''},
    # {'ip_port':'http://180.118.86.44:9000','user_password':''},
    # {'ip_port':'http://123.180.69.45:8010','user_password':''},
    # {'ip_port':'http://145.239.77.20:8','user_password':''},

]