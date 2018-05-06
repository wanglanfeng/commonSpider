#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/6 15:48
 @File    : persistent.py
 @desc    :
'''
from commonSpiders.net.extend_context import ContextExtend
from commonSpiders.scrapy_clusters_manager.mysql.persistent import MysqlPerisistence
from commonSpiders.storage.redis.redis_client import RedisClient
from commonSpiders.utils.singleton import singleton


@singleton
@ContextExtend.extend('service', priority=1, async=False)
class Service(object):

    def __init__(self):
        self.mysql_service = MysqlPerisistence()
        self.redis = RedisClient()

    def register_crawler_process_info(self, crawler_process_info):
        '''
        注册爬虫管理器
        :param crawler_process_info:
        :return:
        '''

    def get_crawler_group_config(self, task_id):
        '''
        获取爬虫组任务
        :param task_id:
        :return:
        '''