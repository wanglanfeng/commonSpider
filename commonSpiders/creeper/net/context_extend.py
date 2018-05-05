#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/2 23:01
 @File    : context_extend.py
 @desc    :
'''
from commonSpiders.creeper.loader.loader import CrawlerLoader
from commonSpiders.net.extend_context import ContextExtend


class CrawlerProcessExtend(ContextExtend):

    KEY = 'crawler_loader'

    def __init__(self, async=True):
        self.crawler_loader = CrawlerLoader()
        super(CrawlerProcessExtend, self).__init__(self.KEY, self.crawler_loader, 5, async)

    def start(self):
        print('扩展初始化')
        self.obj.start_craw()