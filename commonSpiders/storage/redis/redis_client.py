# -*- coding: utf-8 -*-
import redis

from commonSpiders.creeper.utils.singleton import singleton
from commonSpiders.storage.redis.settings import get_redis_config


@singleton
class RedisClient(object):
    '''
    获取redis连接
    '''

    # __metaclass__ = Singleton

    def __init__(self, host='127.0.0.1', port=6379, pwd=''):
        self.redis_clients = {}
        self.host = host
        self.port = port
        self.pwd = pwd

    def get_redis(self, db, pool_use=True):
        '''
        获取redis
        :param db:
        :param pool_use:
        :return:
        '''
        config = get_redis_config(db)
        host = self.host or config['host']
        port = self.port or config['port']
        password = self.pwd or config['pwd']
        r = self.redis_clients.get(db, None)
        if not r:
            if pool_use:
                pool = redis.ConnectionPool(host=host, port=port, db=db, password=password)
                r = redis.Redis(connection_pool=pool)
            else:
                r = redis.StrictRedis(host=host, port=port, db=db, password=password)

            self.redis_clients.setdefault(db, r)
        return r

