#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/1 22:10
 @File    : flask_context_extend.py
 @desc    :
'''


class FlaskContextExtend:

    DEFUALT_PRIORITY = 1

    def __init__(self, key, obj, priority, async=True):
        self.key = key
        self.obj = obj
        self.priority = priority or self.DEFUALT_PRIORITY
        self.async = async

    def start(self):
        pass
