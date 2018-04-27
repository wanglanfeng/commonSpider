#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/27 21:41
 @File    : crawlers.py
 @desc    :
'''
from scrapy.crawler import Crawler

from commonSpiders.creeper.utils.utils import guid_generate


class CustomeCrawler(Crawler):
    '''
    自定义爬虫工作对象类
    '''

    def __init__(self, spidercls, settings=None):
        super(CustomeCrawler, self).__init__(spidercls, settings=settings)
        self._guid = guid_generate()

    @property
    def guid(self):
        return self._guid

    @guid.setter
    def guid(self, val):
        pass