#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/27 21:40
 @File    : item_meta_parse.py
 @desc    :
'''
from commonSpiders.creeper.items.item_meta import TextDataMeta, FileDataMeta, UrlDataMeta, PhotoDataMeta, VideoDataMeta
from commonSpiders.creeper.parses.rule_parser import RegRuleParser


class DataMetaParse:
    '''
    数据元爬取解析类
    '''

    # 真正用于解析数据的解析器
    rule_parser_dict= {
        'reg': RegRuleParser # 正则解析器
    }
    # 默认的解析器的key
    DEFAULT_RULE_PARSER = 'reg'

    def __init__(self, key, rule, rule_parser_key):
        # 数据匹配规则
        self.dom_rule = rule
        # 数据存储时key
        self.key = key
        # 解析器类
        rule_parser_cls = self.rule_parser_dict.get(rule_parser_key, None) or self.rule_parser_dict.get(self.DEFAULT_RULE_PARSER)
        # 解析器对象
        self.parser = rule_parser_cls(self.dom_rule)

    def _parse_rule(self, response):
        '''
        解析数据
        :param response: 响应对象
        :return:
        '''
        return self.parser.parse(response)

    def parse(self, response):
        return self._parse_rule(response)


class TextDataMetaParse(DataMetaParse):

    def __init__(self, key, reg, rule_parser_key):
        super(TextDataMetaParse, self).__init__(key, reg, rule_parser_key)

    def parse(self, response):
        result = self._parse_rule(response)
        return result and TextDataMeta(self.key, result, response)


class UrlDataMetaParse(DataMetaParse):

    '''
    解析url
    '''

    def __init__(self, key, reg, rule_parser_key):
        super(UrlDataMetaParse, self).__init__(key, reg, rule_parser_key)

    def parse(self, response):
        result = self._parse_rule(response)
        return result and UrlDataMeta(self.key, result, response)


class FileDataMetaParse(DataMetaParse):

    '''
    解析文件
    '''

    def __init__(self, key, reg, rule_parser_key):
        super(FileDataMetaParse, self).__init__(key, reg, rule_parser_key)

    def parse(self, response):
        result = self._parse_rule(response)
        return result and FileDataMeta(self.key, result, response)


class PhotoDataMetaParse(DataMetaParse):

    '''
    解析图片
    '''

    def __init__(self, key, reg, rule_parser_key):
        super(PhotoDataMetaParse, self).__init__(key, reg, rule_parser_key)

    def parse(self, response):
        result = self._parse_rule(response)
        return result and PhotoDataMeta(self.key, result, response)


class VideoDataMetaParse(DataMetaParse):
    '''
    解析视频
    '''

    def __init__(self, key, reg, rule_parser_key):
        super(VideoDataMetaParse, self).__init__(key, reg, rule_parser_key)

    def parse(self, response):
        result = self._parse_rule(response)
        return result and VideoDataMeta(self.key, result, response)
