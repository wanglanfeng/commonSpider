#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/5 16:58
 @File    : test.py
 @desc    :
'''
from mongoengine import StringField
from mongoengine.base import BaseDocument

from commonSpiders.scrapy_clusters_manager.mysql.models import CrawlerProcessInfo
from commonSpiders.storage.mongodb.mongo_client import MongoDbClient
from commonSpiders.storage.mysql.sqlalchemy_engine import SqlSession


class Test(BaseDocument):

    name = StringField(verbose_name="配置的key", required=False)

    meta = {'db_alias': 'default', 'collection': 'settings_meta'}


# spider_setting_con = Test._get_collection()


if __name__ == '__main__':
    # MongoDbClient()
    # print(1)
    # Test.objects
    sqlSession = SqlSession()
    session = sqlSession.get_sql_session()
    # session.query(CrawlerProcessInfo)
    print(1)


