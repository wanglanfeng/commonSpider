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

    def __init__(self, key, crawlerprocess, priority='', async=True):
        if not isinstance(crawlerprocess, CrawlerLoader):
            raise Exception('初始化异常')
        super(CrawlerProcessExtend, self).__init__(key, crawlerprocess, priority, async)

    def start(self):
        print('扩展初始化')
        self.obj.start_craw()