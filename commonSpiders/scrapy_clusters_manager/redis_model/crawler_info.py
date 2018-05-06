#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/5 12:24
 @File    : crawler_info.py
 @desc    :
'''
from commonSpiders.cache.redis_data_model import RedisInfo


class CrawlerGroupInfo(RedisInfo):
    '''
    爬虫工状态管理器
    '''

    def __init__(self):
        self.setdefault('guid', '')
        self.setdefault('spider', {
            'key': '',
            'class': ''
        })
        # 爬虫个性配置
        self.setdefault('settings', {})
        # 解析配置
        self.setdefault('parse', None)
        # 管道配置
        self.setdefault('pipeline', None)


class CrawlerInfo(RedisInfo):
    '''
    爬虫对象信息
    '''
    STANDING = 'standing'
    RUNNING = 'running'
    DIE = 'die'

    def __init__(self):
        self.setdefault('group_guid', '')
        self.setdefault('state', '')