#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/15 16:48
 @File    : custom_crawlerprocess.py
 @desc    :
'''

import six
from scrapy.crawler import CrawlerProcess
from scrapy.settings import BaseSettings
from scrapy.utils.project import get_project_settings
from twisted.internet import defer

from commonSpiders.creeper.crawlers.crawlerjobinfo_manager import CrawlerJobInfoManager
from commonSpiders.creeper.crawlers.crawlers import CustomeCrawler
from commonSpiders.creeper.utils.utils import guid_generate


class CustomCrawlerProcess(CrawlerProcess):
    '''
    爬虫调度器进程
    '''

    def __init__(self, settings=None, install_root_handler=True, spiders_list=[]):
        super(CustomCrawlerProcess, self).__init__(settings, install_root_handler)
        # 存储原始配置
        self.source_settings = {}
        if isinstance(self.settings, BaseSettings):
            settings = self.settings.copy_to_dict()
        else:
            settings = get_project_settings().copy_to_dict()
        self.source_settings.update(settings)

        self._guid = guid_generate()

        # 存储当前可用的所有爬虫
        spiders_list = list(set(spiders_list))
        self.spiders_dict = {spider.name: spider for spider in spiders_list}

        # 存储爬虫对应的crawler
        self.spider_crawler = {}

        # 存储每个爬虫对应的个性化配置
        self.spider_settings = {}

        # 爬虫工作者状态管理器
        self.crawler_manager = CrawlerJobInfoManager()

    @property
    def guid(self):
        self._guid

    @guid.setter
    def guid(self, value):
        return

    def _create_crawler(self, spidercls):
        if isinstance(spidercls, six.string_types):
            spidercls = self.spider_loader.load(spidercls)
        return CustomeCrawler(spidercls, self.settings)

    def start(self, stop_after_crawl=True):
        super(CustomCrawlerProcess, self).start(stop_after_crawl)

    def stop(self):
        super(CustomCrawlerProcess, self).stop()

    def add_crawler(self, spider_class_obj, count, settings_config={}):

        if not isinstance(settings_config, dict):
            print('配置不能为空')
            return

        if not count:
            count = 1

        self.settings = self.source_settings.copy()
        self.settings.update(settings_config)
        for i in range(count):
            print('创建爬虫:%s' % i)
            spider_class_obj.index = i
            self.crawl(spider_class_obj)

    def add_crawler_by_spider_key(self, key, count, **settings):
        spider = self.spiders_dict.get(key, None)
        if spider:
            settings = settings or {}
            guid = guid_generate()
            spider.name = guid
            self.add_crawler(spider, count, settings)
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












