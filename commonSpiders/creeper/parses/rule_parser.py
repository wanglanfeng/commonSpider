#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/1 0:13
 @File    : rule_parser.py
 @desc    :
'''
import re


class RuleParser:

    def __init__(self, rule):
        pass

    def parse(self, response):
        pass


class RegRuleParser(RuleParser):

    def __init__(self, rule):
        self.reg_pattern = re.compile(rule)

    def parse(self, response):
        data_list = self.reg_pattern.findall(response.body)
        return data_list and data_list[0] or None