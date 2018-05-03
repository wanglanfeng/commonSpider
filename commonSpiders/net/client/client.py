#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/1 22:45
 @File    : client.py
 @desc    :
'''

from socketIO_client import SocketIO

from commonSpiders.net.app import BaseApp


class Client(BaseApp):

    def __init__(self, settings=''):
        super(Client, self).__init__(settings)
        self.headers = {}
        self.cookies = {}
        self.params = {}
        self.ipproxy = {}
        self.socketIO = None
        self.namespace_dict = {}
        self.extend_context = {}
        self._init_param()

    def _init_param(self):
        self.headers = self.settings.get("headers", {})
        self.cookies = self.settings.get("cookies", {})
        self.params = self.settings.get("cookies", {})
        self.ipproxy = self.settings.get("params", {})
        self.ip = self.settings.get("ip", None) or 'localhost'
        self.port = self.settings.get("port", None) or self.DEFAULT_PORT

    def set_namespace(self, path, namespace):
        if not path or not namespace:
            return
        self.namespace_dict.update({
            path: namespace
        })
        return self

    def set_context(self, key, obj):
        if not key or not obj:
            return

        self.extend_context.update({
            key: obj
        })

    def run(self):
        print('开始客户端app')
        self.socketIO = SocketIO(self.ip, self.port)
        # 将环境设置到io对象中
        setattr(self.socketIO, 'extend_context', self.extend_context)
        for path, namespace in self.namespace_dict.items():
            self.socketIO.define(namespace, path)
        self.socketIO.wait()



