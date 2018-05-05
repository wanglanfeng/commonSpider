#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/3 23:04
 @File    : context_extend.py
 @desc    :
'''
from commonSpiders.cache.cache import RedisCache
from commonSpiders.net.extend_context import ContextExtend


class RedisCacheContextExtend(ContextExtend):

    KEY = 'cache'

    def __init__(self, priority=1, async=True):
        redis = RedisCache()
        super(RedisCacheContextExtend, self).__init__(self.KEY, redis, priority, async)
