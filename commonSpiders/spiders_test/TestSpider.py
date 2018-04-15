#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/15 15:46
 @File    : TestSpider.py
 @desc    :
'''
import datetime
import time

from scrapy import Spider, Request

class TestSpider(Spider):
    '''
    测试爬虫
    '''
    name = 'test_spider'
    key = 1

    def __init__(self):
        pass

    def start_requests(self):
        return [Request('http://www.baidu.com', callback=self.parse)]

    def parse(self, response):
        while True:
            time.sleep(5)
            yield Request('http://www.baidu.com/?a=%s' % datetime.datetime.now(), callback=self.finish)

    def finish(self, response):
        # print self
        print 1
