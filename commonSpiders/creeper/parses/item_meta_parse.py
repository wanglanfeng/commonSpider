#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/27 21:40
 @File    : item_meta_parse.py
 @desc    :
'''

class DataMetaParse:
    '''
    数据元爬取解析类
    '''

    def __init__(self):
        self.guid = ''
        # 数据正则
        self.dom_reg = ''
        # 是否要保持header，默认保存
        self.store_headers = True
        # 是否需要加入爬虫队列
        self.crawl_flag = False
        # 遇到需要爬取的url时要添加的参数信息
        self.request_extra_config = {}
        # 数据存储时key
        self.key = ''
        # 数据给人使用的名
        self.name = ''
        # 数据类型（根据类型创建对应的数据源），文件类型，text类型
        self.data_type = ''

    def is_crawl(self):
        '''
        判断是否需要爬取数据
        :return:
        '''
        return self.crawl_flag

    def is_store_headers(self):
        '''
        是否需要存储headers
        :return:
        '''
        return self.store_headers
