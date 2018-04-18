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

from commonSpiders.spiders_test.entity import DataItem


class TestSpider(Spider):
    '''
    测试爬虫
    '''
    name = 'test_spider'
    key = 1

    def __init__(self):
        print('初始化一个爬虫')
        pass

    def start_requests(self):
        print('开始运行')
        return [Request('http://www.baidu.com', callback=self.parse)]

    def parse(self, response):
        print('解析数据')
        # yield Request('http://localhost:9000/system/view/user_manage/?a=%s' % datetime.datetime.now())

