#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/18 20:56
 @File    : entity.py
 @desc    :
'''
import scrapy


class DataItem(scrapy.Item):

    name = scrapy.Field()