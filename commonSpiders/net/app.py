#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/2 21:42
 @File    : app.py
 @desc    :
'''
import threading
from importlib import import_module


class BaseApp(threading.Thread):
    # 服务初始化默认优先级
    DEFAULT_PRIORITY = 0
    # 服务初始化默认绑定ip
    DEFAULT_IP = '0.0.0.0'
    # 服务初始化默认绑定端口
    DEFAULT_PORT = 5000

    def __init__(self, settings=''):
        threading.Thread.__init__(self)
        self.settings = {}
        self.ip = self.DEFAULT_IP
        self.port = self.DEFAULT_PORT
        self._load_settings(settings)

    def _load_settings(self, settings_path):
        '''
        根据settings路径加载settings配置
        :param settings_path:
        :return:
        '''
        if not settings_path:
            return
        module = import_module(settings_path)
        for key in dir(module):
            if key.isupper():
                self.settings.update({
                    key.lower(): getattr(module, key)
                })
