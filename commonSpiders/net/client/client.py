#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/1 22:45
 @File    : client.py
 @desc    :
'''
from importlib import import_module

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
        self.namespace = {}
        self._init_param()

    def _init_param(self):
        self.headers = self.settings.get("headers", {})
        self.cookies = self.settings.get("cookies", {})
        self.params = self.settings.get("cookies", {})
        self.ipproxy = self.settings.get("params", {})
        self.ip = self.settings.get("ip", "localhost")
        self.port = self.settings.get("port", 5000)

    def set_namespace(self, path, namespace):
        if not path or not namespace:
            return
        self.namespace.update({
            path: namespace
        })
        return self

    def run(self):
        print('开始客户端app')
        self.socketIO = SocketIO(self.ip, self.port)
        for path, namespace in self.namespace.items():
            self.socketIO.define(namespace, path)
        print(1)
        self.socketIO.wait()



