#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/9 22:05
 @File    : context_manager.py
 @desc    :
'''
from commonSpiders.utils.singleton import singleton


class ContextManagerBuild(object):

    @staticmethod
    def get_context_manager():
        return ContextManager()

    @classmethod
    def get_context(cls, key):
        cls.get_context_manager().get(key)

    @classmethod
    def set_context(cls, key, value):
        cls.get_context_manager().set_context(key, value)

    @classmethod
    def update_context(cls, data):
        if isinstance(data, dict):
            cls.get_context_manager().update(data)



@singleton
class ContextManager(dict):

    def set_context(self, key, value):
        if not key or not value:
            return
        self.setdefault(key, value)

    def get_context(self, key, default={}):
        if not key:
            return default
        return self.get(key, default)
