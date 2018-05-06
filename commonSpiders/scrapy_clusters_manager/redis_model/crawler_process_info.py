#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/5 11:58
 @File    : crawler_process_info.py
 @desc    :
'''
from commonSpiders.cache.redis_data_model import RedisInfo


class CrawlerProcessStatusInfo(RedisInfo):
    '''
    爬虫管理器状态信息
    '''

    # 默认缓存时间
    EX = 60
    KEY_PREFIX = ['scrapy', 'crawlermanager']

    def __init__(self):
        # ip
        self.setdefault('ip', '')
        # 爬虫管理器全局id
        self.setdefault('guid', '')
        # 是否连接
        self.setdefault('link', False)


class CrawlerProcessConfig(RedisInfo):

    def __init__(self):

        pass
