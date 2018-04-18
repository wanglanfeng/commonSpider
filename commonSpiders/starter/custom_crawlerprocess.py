#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/15 16:48
 @File    : custom_crawlerprocess.py
 @desc    :
'''
import uuid
from scrapy.crawler import CrawlerProcess
from scrapy.settings import BaseSettings, SettingsAttribute
from twisted.internet import defer


class CustomCrawlerProcess(CrawlerProcess):
    '''

    '''

    def __init__(self, settings=None, install_root_handler=True, spiders_list=[]):
        super(CustomCrawlerProcess, self).__init__(settings, install_root_handler)
        self.is_started = False
        # 存储当前个性化配置
        # self.settings

        # 存储当前可用的所有爬虫
        spiders_list = list(set(spiders_list))
        self.spiders_dict = {spider.name: spider for spider in spiders_list}

        # 存储原始配置
        self.source_settings = self.settings.copy()

        # 存储爬虫对应的crawler
        self.spider_crawler = {}

        # 存储每个爬虫对应的个性化配置
        self.spider_settings = {}

    def start(self, stop_after_crawl=True):
        super(CustomCrawlerProcess, self).start(stop_after_crawl)
        self.is_started = True

    def stop(self):
        super(CustomCrawlerProcess, self).stop()
        self.is_started = False

    def add_crawler(self, spider_class_obj, settings_config={}):

        self.settings = self.source_settings.copy()
        for key, val in settings_config.items():
            if isinstance(val, dict):
                self.settings.set(key, BaseSettings(val, 'default'), 'default')
            else:
                self.settings.set(key, SettingsAttribute(val, 'priority'))
        self.crawl(spider_class_obj)

    def add_crawler_by_spider_key(self, key, **settings):
        spider = self.spiders_dict.get(key, None)
        if spider:
            settings = settings or {}
            guid = uuid.uuid1()
            spider.name = guid
            self.add_crawler(spider, settings)
            crawlers_list = list(self.crawlers)
            cur_crawler = (crawlers_list and crawlers_list[-1]) or None
            if cur_crawler:
                self.spider_crawler.setdefault(key, {})
                self.spider_crawler[key].update({
                    guid: cur_crawler
                })
                self.spider_settings.setdefault(key, {})
                self.spider_settings[key].update({
                    guid: settings
                })

    def stop_crawler(self, spider_key):
        '''
        停掉某个爬虫任务
        :param spider_key:
        :return:
        '''
        crawler = self.spider_crawler.get(spider_key, None)
        if crawler:
            return defer.DeferredList([crawler.stop()])
        else:
            return None

    def config_spider_class(self, key, spider):
        self.spiders_dict.update({
            key: spider
        })
