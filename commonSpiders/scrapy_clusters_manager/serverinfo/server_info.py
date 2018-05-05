#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/5 12:12
 @File    : server_info.py
 @desc    :
'''
from commonSpiders.cache.redis_data_model import RedisInfo


class ServerInfo(RedisInfo):

    def __init__(self):

        self.setdefault('ip', '')
        self.setdefault('cpu', {
            # 频率
            'freq': 0,
            # 使用率
            'used': 0
        })
        self.setdefault('mem', {
            'total': 0,
            'used': 0
        })
