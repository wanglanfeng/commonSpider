#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/15 15:46
 @File    : TestSpider.py
 @desc    :
'''

from scrapy import Spider, Request


class TestSpider(Spider):
    '''
    测试爬虫
    '''
    index = None
    name = 'test_spider'
    key = 1

    item_parse_dict = {}
    item_parse_list = []

    def __init__(self):
        print('初始化一个爬虫')
        pass

    def start_requests(self):
        print('开始运行')
        print '爬虫编号：%s，爬虫名：%s，爬虫：%s\n' % (self.name,self.index, self)
        return [Request('http://www.baidu.com', callback=self.parse)]

    def parse(self, response):
        print('解析数据')
        # yield Request('http://localhost:9000/system/view/user_manage/?a=%s' % datetime.datetime.now())

