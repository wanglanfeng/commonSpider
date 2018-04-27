#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/14 23:35
 @File    : singleton.py
 @desc    :
'''
from functools import wraps

instances = {}
def singleton(cls):
    '''
    实现单例的装饰器
    :param cls:
    :return:
    '''
    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance

class Singleton(object):

    '''
    实现单例的元类
    '''
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance