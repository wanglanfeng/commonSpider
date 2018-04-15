#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/15 16:48
 @File    : custom_crawlerprocess.py
 @desc    :
'''
from scrapy.crawler import CrawlerProcess
from twisted.internet import defer


class CustomCrawlerProcess(CrawlerProcess):
    '''

    '''

    def __init__(self, settings=None, install_root_handler=True, spiders_list=[]):
        super(CustomCrawlerProcess, self).__init__(settings, install_root_handler)
        # 存储当前个性化配置
        # self.settings

        # 存储当前可用的所有爬虫
        spiders_list = list(set(spiders_list))
        self.spiders = {spider.name: spider for spider in spiders_list}

        # 存储原始配置
        self.source_settings = self.settings

        # 存储爬虫对应的crawler
        self.spider_crawler = {}

        # 存储每个爬虫对应的个性化配置
        self.spider_settings = {}


    def add_new_crawler(self, settings_config, spider):

        pass

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
