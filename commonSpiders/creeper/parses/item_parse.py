#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/27 21:39
 @File    : item_parse.py
 @desc    :
'''
from commonSpiders.creeper.utils.utils import guid_generate


class ItemParse:
    '''
    数据集爬取解析类
    '''

    def __init__(self, key, name, html_url_reg):
        self.guid = guid_generate()
        # 页面url正则
        self.html_url_reg = ''
        # item的key
        self.key = ''
        # item名称
        self.name = ''
        # 数据元解析集
        self.data_meta_parse = []

    def set_meta_parse(self):
        pass

    def parse(self, html_page):
        '''
        解析数据
        :param html_page:
        :return:
        '''
        pass
