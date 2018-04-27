#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/15 20:19
 @File    : my_thread.py
 @desc    :
'''
import threading
import time

from scrapy.settings import BaseSettings

from commonSpiders.test.TestSpider import TestSpider


class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, process):
        threading.Thread.__init__(self)
        self.process = process
        print '初始化线程'

    def run(self):
        print '启动线程'
        while True:
            time.sleep(5)
            # print "Starting "

    def add_new_spider(self):
        '''

        :return:
        '''
        spider = TestSpider
        # spider.name = '%s' % datetime.datetime.now()
        spider.key = 2
        self.process.settings.set('DOWNLOADER_MIDDLEWARES', BaseSettings({
            'commonSpiders.downloader_middlewares.middlewares.Test2Middleware': 550
        }, 'default'), 'default')
        self.process.crawl(spider)
