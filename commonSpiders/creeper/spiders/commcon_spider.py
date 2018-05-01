#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/27 20:52
 @File    : commcon_spider.py
 @desc    :
'''
import re
import time

from scrapy import Spider, Request


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
    item_parse_url_list = []
    # 起始url
    start_url = None

    __PAUSE_TIME = 1
    __PAUSE_SWITCH = False

    def __init__(self):
        print('初始化一个爬虫')
        self.pause_time = self.__PAUSE_TIME
        self.pause_switch = self.__PAUSE_SWITCH

    @classmethod
    def set_item_parse(cls, item_parse_list):
        for item_parse in item_parse_list:
            item_url = item_parse.get_html_url()
            cls.item_parse_url_list.append(item_url)
            cls.item_parse_dict.update({
                item_url: item_parse
            })

    def get_pause_switch(self):
        return self.pause_switch

    def set_pause_switch(self, time):
        if not time or not isinstance(time, int) or not (time <= 0 and time > 60):
            self.pause_switch = self.__PAUSE_TIME
        else:
            self.pause_switch = time

    def pause(self):
        # 暂停爬虫
        self.pause_switch = True

    def resume(self):
        # 恢复爬虫
        self.pause_switch = False

    def stop(self, reason):
        # 关闭自身
        self.close(self, reason)

    def start_requests(self):
        print('开始运行')
        print '爬虫编号：%s，爬虫名：%s，爬虫：%s\n' % (self.name,self.index, self)

        return [Request('http://www.baidu.com')]

    def parse(self, response):
        while self.pause_switch:
            time.sleep(self.pause_time)
        print('解析数据')

        for url_reg in self.item_parse_url_list:
            if re.match(url_reg, response.url):
                result_generator = self.item_parse_dict[url_reg].parse(response)
                for result in result_generator:
                    if result:
                        yield result




