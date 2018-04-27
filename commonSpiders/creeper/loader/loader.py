#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/15 19:37
 @File    : loader.py
 @desc    :
'''
from scrapy.utils.project import get_project_settings

from commonSpiders.creeper.crawlermanagers.custom_crawlerprocess import CustomCrawlerProcess
from commonSpiders.test.TestSpider import TestSpider


class CrawlerLoader(object):

    def __init__(self):
        self.settings = get_project_settings()
        self.process = CustomCrawlerProcess(self.settings)
        self.process.config_spider_class("TestSpider", TestSpider)
        print '初始化爬虫进程'

    def start_craw(self, spider_key="", **settings):

        print '启动爬虫进程'
        if spider_key:
            self.process.add_crawler_by_spider_key(spider_key, settings)
            self.process.start(True)
        else:
            self.process.start(False)


