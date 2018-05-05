#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/5 10:53
 @File    : cache.py
 @desc    :
'''
from commonSpiders.storage.redis.redis_client import RedisClient


class BaseCache(object):

    '''
    默认的缓存处理器
    '''

    def __init__(self):
        self.cache = None
        self.cache = {}

    def set_cache(self, key, data, time=0, default_val="", *args, **kwargs):
        default_val = data or default_val
        if not key or not data:
            return False
        self.cache.setdefault(key, {
            'data': default_val,
            'time': -1 if time == 0 else time
        })
        return True

    def get_cache(self, key, default_val=None, *args, **kwargs):
        default_val = default_val or {}
        if not key:
            return default_val
        return self.cache.get(key, default_val)


class RedisCache(BaseCache):

    def __init__(self):
        self.redis_client = RedisClient()

    def set_cache(self, key, data, time=0, default_val="", *args, **kwargs):
        time = None if not time else time
        data = data or default_val
        client = self._get_client(*args, **kwargs)
        client.set(key, data, ex=time)
        return True

    def get_cache(self, key, default_val=None, *args, **kwargs):
        client = self._get_client(*args, **kwargs)
        return client.get(key) or default_val

    def _get_client(self, *args, **kwargs):
        db = kwargs.get('db', 0)
        client = self.redis_client.get_redis(db)
        return client

