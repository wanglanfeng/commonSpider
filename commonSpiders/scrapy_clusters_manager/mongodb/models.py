#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/5 18:42
 @File    : models.py
 @desc    :
'''
import datetime

from mongoengine import StringField

from commonSpiders.storage.mongodb.mongo_model import BaseDocument


class CrawlerGroupSettingsItem(BaseDocument):
    '''
    某个爬虫组配置单元
    '''
    # 爬虫管理器唯一id
    crawler_process_guid = StringField(verbose_name="爬虫管理器全局唯一id")
    task_id = StringField(verbose_name="任务id")
    crawler_group_id = StringField(verbose_name="爬虫分组唯一id")

    # 一下为配置
    # 键
    key = StringField(verbose_name='爬虫配置单元键', default='')
    value = StringField(verbose_name="爬虫配置单元值", default='')






