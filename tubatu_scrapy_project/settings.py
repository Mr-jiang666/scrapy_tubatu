# -*- coding: utf-8 -*-

# Scrapy settings for tubatu_scrapy_project project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tubatu_scrapy_project'

SPIDER_MODULES = ['tubatu_scrapy_project.spiders']
NEWSPIDER_MODULE = 'tubatu_scrapy_project.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = ''

# Obey robots.txt rules
#通常设置为False
ROBOTSTXT_OBEY = False


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#并发量，默认32
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#下载延迟
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#是否启用cookies
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#设置默认请求头
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#设置SPIDER中间件
#SPIDER_MIDDLEWARES = {
#    'tubatu_scrapy_project.middlewares.TubatuScrapyProjectSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#设置下载中间件
DOWNLOADER_MIDDLEWARES = {
   # 'tubatu_scrapy_project.middlewares.TubatuScrapyProjectDownloaderMiddleware': 543,
   #后面数字越小，优先级越高
   'tubatu_scrapy_project.middlewares.my_useragent': 300,
   # 'tubatu_scrapy_project.middlewares.my_proxy': 301,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#如果你要使用pipeline，你就要在setting里面启用，否则是不可用的
ITEM_PIPELINES = {
   'tubatu_scrapy_project.pipelines.TubatuScrapyProjectPipeline': 300,
   'tubatu_scrapy_project.pipelines.TubatuImagePipeline': 301,
}

#定义图片被下载到哪里
#下载到images这个文件夹中
IMAGES_STORE = 'images'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
