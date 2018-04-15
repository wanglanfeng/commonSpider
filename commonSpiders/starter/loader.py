#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/15 19:37
 @File    : loader.py
 @desc    :
'''
from scrapy.crawler import CrawlerProcess
from scrapy.settings import BaseSettings
from scrapy.utils.project import get_project_settings

from commonSpiders.spiders_test.TestSpider import TestSpider
from commonSpiders.utils.singleton import singleton


@singleton
class CrawlerLoader(object):

    def __init__(self):
        self.settings = get_project_settings()
        self.process = CrawlerProcess(self.settings)
        print '初始化爬虫进程'

    def start_craw(self):

        print '启动爬虫进程'
        spider = TestSpider
        self.settings.set('DOWNLOADER_MIDDLEWARES', BaseSettings({
            'commonSpiders.downloader_middlewares.middlewares.Test1Middleware': 550
        }, 'default'), 'default')
        self.process.crawl(spider)
        self.process.start()


