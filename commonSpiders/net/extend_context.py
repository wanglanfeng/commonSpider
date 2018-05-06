#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/2 21:06
 @File    : extend_context.py
 @desc    :
'''
from functools import wraps

extend_list = []


class ContextExtend(object):
    '''
    扩展
    '''
    # 默认的扩展初始化优先级
    DEFUALT_PRIORITY = 1
    # 扩展对象初始化时默认会调用obj的方法的名称
    DEFAULT_START_FUNC = 'extend_start'

    def __init__(self, key, obj, priority=1, async=True, func=None):
        self.key = key
        self.obj = obj
        self.priority = priority or self.DEFUALT_PRIORITY
        self.async = async
        self.start_func = func
        self.app = None

    def start(self, func=None):
        start_func = func or self.start_func or (self.obj and getattr(self.obj, self.DEFAULT_START_FUNC, None))
        if start_func and callable(start_func):
            start_func()
        else:
            print('extend')

    @classmethod
    def extend(cls, key, priority=1, async=False, func=None):
        if key in extend_list:
            raise Exception('%s服务已被扩展过' % key)
        else:
            extend_list.append(key)

        def decorator(cls_obj):
            @wraps(cls_obj)
            def getinstance(*args, **kw):
                obj = cls_obj(*args, **kw)
                return cls(key, obj, priority=priority, async=async, func=func)

            return getinstance

        return decorator
