# -*- coding: utf-8 -*-
import redis

from commonSpiders.redis.settings import get_redis_config
from commonSpiders.utils.singleton import Singleton, singleton


@singleton
class RedisClient(object):
    '''
    获取redis连接
    '''

    # __metaclass__ = Singleton

    def __init__(self):
        self.redis_clients = {}

    def get_redis(self, db, pool_use=True):
        '''
        获取redis
        :param db:
        :param pool_use:
        :return:
        '''
        config = get_redis_config(db)
        r = None
        if pool_use:
            pool = redis.ConnectionPool(host=config['host'], port=config['port'], db=db, password=db['pwd'])
            r = redis.Redis(connection_pool=pool)
        else:
            r = redis.StrictRedis(host=config['host'], port=config['port'], db=db, password=db['pwd'])

        self.redis_clients.setdefault(db, r)
        return r

