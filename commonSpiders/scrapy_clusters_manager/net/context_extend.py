#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/3 23:04
 @File    : context_extend.py
 @desc    :
'''
from commonSpiders.net.extend_context import ContextExtend


class RedisContextExtend(ContextExtend):

    def __init__(self, key, obj, priority='', async=True):

        super(RedisContextExtend, self).__init__(key, obj, priority, async)
