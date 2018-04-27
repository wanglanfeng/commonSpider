#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/27 20:52
 @File    : commcon_spider.py
 @desc    :
'''
from scrapy import Spider


class BaseSpider(Spider):

    # 爬虫序号
    index = None
    # 爬虫名
    name = 'base'
    # 爬虫代表key
    key = 1
    # 爬虫数据解析对象
    item_parse_dict = {}
    # 匹配页面url正则
    item_parse_list = []
    # 起始url
    start_url = None

    def __init__(self):
        print('初始化一个爬虫')

    def start_requests(self):
        print('开始运行')
        print '爬虫编号：%s，爬虫名：%s，爬虫：%s\n' % (self.name,self.index, self)

        # return [Request('http://www.baidu.com', callback=self.parse)]

    def parse(self, response):
        print('解析数据')

    def pause(self):
        # 暂停爬虫
        pass

    def resume(self):
        # 恢复爬虫
        pass

    def stop(self, reason):
        # 关闭自身
        self.close(self, reason)


