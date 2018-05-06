#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/15 19:37
 @File    : manager.py
 @desc    :
'''
from scrapy.utils.project import get_project_settings

from commonSpiders.creeper.crawlermanagers.custom_crawlerprocess import CustomCrawlerProcess
from commonSpiders.creeper.spiders.commcon_spider import BaseSpider
from commonSpiders.net.extend_context import ContextExtend
from commonSpiders.utils.singleton import singleton

KEY = 'crawler_process_manager'


@singleton
@ContextExtend.extend(KEY)
class CrawlerProcessManager(object):

    def __init__(self, net=None):
        self.settings = get_project_settings()
        self.net = None
        self.process_dict = {}
        self.process = CustomCrawlerProcess(self.settings, net=net)
        self.process.config_spider_class("common", BaseSpider)
        print '初始化爬虫进程'

    def start_craw(self):

        print '启动爬虫进程'
        self.process.set_net(self.net)
        self.process.start(False)

    def extend_start(self):
        self.start_craw()


