#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/26 21:29
 @File    : items.py
 @desc    :
'''
import scrapy


class ItemBase(scrapy.Item):

    '''
    通用item
    '''

    def set_key(self, key):
        self.fields.update({
            key: {}
        })

    def set_attr(self, key, value):
        if key:
            self.set_key(key)
            self.update({
                key: value
            })
        return None