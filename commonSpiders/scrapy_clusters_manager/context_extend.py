#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/3 23:04
 @File    : context_extend.py
 @desc    :
'''
from commonSpiders.cache.cache import RedisCache
from commonSpiders.net.extend_context import ContextExtend
from commonSpiders.storage.mongodb.mongo_client import MongoDbClient
from commonSpiders.storage.mysql.sqlalchemy_engine import SqlSession


class RedisCacheContextExtend(ContextExtend):

    KEY = 'cache'

    def __init__(self, priority=1, async=True):
        redis = RedisCache()
        super(RedisCacheContextExtend, self).__init__(self.KEY, redis, priority, async)


class MongoDbContextExtend(ContextExtend):

    KEY = 'mongodb'

    def __init__(self, priority=2, async=True):
        mongodb = MongoDbClient()
        super(MongoDbContextExtend, self).__init__(self.KEY, mongodb, priority, async)


class MysqlContextExtend(ContextExtend):

    KEY = 'mysql'

    def __init__(self, priority=3, async=True):
        mysql = SqlSession().get_sql_session()
        super(MysqlContextExtend, self).__init__(self.KEY, mysql, priority, async)

