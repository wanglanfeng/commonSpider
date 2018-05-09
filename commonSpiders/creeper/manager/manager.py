#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/15 19:37
 @File    : manager.py
 @desc    :
'''
import datetime
import threading

from scrapy.utils.project import get_project_settings

from commonSpiders.creeper.crawlermanagers.custom_crawlerprocess import CustomCrawlerProcess
from commonSpiders.creeper.spiders.commcon_spider import BaseSpider
from commonSpiders.net.extend_context import ContextExtend
from commonSpiders.utils.server_utils import get_guid_by_mac, get_mac_address
from commonSpiders.utils.singleton import singleton

KEY = 'crawler_process_manager'


@singleton
@ContextExtend.extend(KEY)
class CrawlerProcessManager(object):

    INIT_CRAWLER_PROCESS_FLAG = False

    def __init__(self):
        self.settings = get_project_settings()
        self.mac = get_mac_address()
        self.init_crawler_process_list = []
        self.init_crawler_process_list += self.settings.get('CRAWLER_PROCEESS', ['default'])
        self.process_dict = {}
        print '初始化爬虫进程管理器'

    def get_crawler_process(self, crawler_process_guid):
        return self.process_dict.get(crawler_process_guid, None)

    def create_crawler_process(self, name, settings):
        if not name:
            return False
        print '初始化爬虫进程'
        guid = get_guid_by_mac(name)
        process = CustomCrawlerProcess(settings, guid=guid)
        process.config_spider_class("common", BaseSpider)
        threading.Thread(target=self.run_crawler_process, args=(process,)).start()
        self.process_dict.setdefault(guid, process)
        return True

    def start_craw(self):
        for name in self.init_crawler_process_list:
            self.create_crawler_process(name, self.settings)
        self.INIT_CRAWLER_PROCESS_FLAG = True

    @staticmethod
    def run_crawler_process(process):
        print '启动爬虫进程[%s][%s]' % (process.guid, datetime.datetime.now())
        process.start(False)

    def extend_start(self):
        self.start_craw()


