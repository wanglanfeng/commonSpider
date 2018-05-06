#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/6 12:34
 @File    : persistent.py
 @desc    :
'''
from commonSpiders.storage.mysql.sqlalchemy_engine import SqlSession
from commonSpiders.utils.singleton import singleton


@singleton
class MysqlPerisistence(object):

    def __init__(self):

        self.session = SqlSession().get_sql_session()

    def insert_crawler_process_info(self):
        '''
        注册爬虫管理器时插入数据
        :return:
        '''
        pass

    def update_crawler_process_info(self):
        '''
        更新爬虫管理器信息
        :return:
        '''
        pass

    def get_crawler_task(self, task_id):
        '''
        获取爬虫任务
        :return:
        '''

    def get_crawler_group_settings(self, task_id):
        '''
        获取爬虫配置
        :return:
        '''

    def get_crawler_items(self, task_id):
        '''
        获取爬虫解析使用的item信息,用于解析item
        :return:
        '''
        '''
        1 获取item信息
        2 获取datasource信息
        3 获取itemmeta信息
        '''
        pass

