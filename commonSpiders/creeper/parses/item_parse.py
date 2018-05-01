#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/27 21:39
 @File    : item_parse.py
 @desc    :
'''
from scrapy import Request

from commonSpiders.creeper.items.item_meta import UrlDataMeta, BaseDataMeta
from commonSpiders.creeper.items.items import ItemBase


class ItemParser:
    '''
    数据集爬取解析类
    '''

    item_meta_dict = {}

    def __init__(self, task_id, html_url_reg,
                 item_meta_parser_configs, plan_id=None, key=None,
                 rule_parser_key='reg',
                 **kargs):
        '''
        初始化item解析器
        :param task_id:
        :param html_url_reg:
        :param item_meta_parser_configs:
        :param plan_id:
        :param key:
        :param rule_parser_key:
        :param kargs:
        '''
        # 任务id
        self.task_id = task_id
        # 计划id
        self.plan_id = plan_id
        # item的key
        self.key = key
        # 数据元解析集
        self.html_url_reg = html_url_reg
        # 解析工厂
        self.rule_parser_key = rule_parser_key or 'reg'
        self.item_meta_parser_list = []
        for item_meta_parser_config in item_meta_parser_configs:
            item_meta_parser = self._init_item_meta_parser(parse_factory=self.rule_parser_key, **item_meta_parser_config)
            if item_meta_parser:
                self.item_meta_parser_list.append(item_meta_parser)

    def set_meta_parse(self, item_meta_parser_config, parse_factory='reg'):
        '''
        设置元解析器
        :param item_meta_parser_config:
        :param parse_factory:
        :return:
        '''
        return self._init_item_meta_parser(parse_factory=parse_factory, **item_meta_parser_config)

    def _init_item_meta_parser(self, parse_factory='reg', **item_meta_parser_config):
        '''
        初始化元解析器，内部方法
        :param parse_factory:
        :param item_meta_parser_config:
        :return:
        '''
        parser_type = item_meta_parser_config.get('parser_type', None)

        if not parser_type:
            return None
        item_meta_parser_cls = self.item_meta_dict.get(parser_type, None)
        if not item_meta_parser_cls:
            return None
        key = item_meta_parser_config.get('key', None)
        dom_reg = item_meta_parser_config.get('dom_reg', None)
        item_meta_parser = item_meta_parser_cls(key, dom_reg, parse_factory)
        return item_meta_parser

    def get_html_url(self):
        '''
        获取item解析匹配的url
        :return:
        '''
        return self.html_url_reg

    def parse(self, response):
        '''
        解析数据
        :param html_page:
        :return:
        '''
        item = ItemBase()
        for item_meta_parser in self.item_meta_parser_list:
            item_meta = item_meta_parser.parse(response)
            if not item_meta:
                continue
            if isinstance(item_meta, BaseDataMeta) and item_meta.type == BaseDataMeta.URL_TYPE:
                yield Request(item_meta.data, item.get_headers())
            else:
                item.set_attr(item_meta_parser.key, item_meta)
        yield item



