#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/2 23:02
 @File    : socketio_client_namespace.py
 @desc    :
'''
import time

from socketIO_client import BaseNamespace


class ClientBaseNamespace(BaseNamespace):

    KEY = '/base'

    def __init__(self, io, path):
        super(ClientBaseNamespace, self).__init__(io, path)
        self.extend_context = self.__dict__['_io'].__dict__['extend_context']


class HeartNamspace(ClientBaseNamespace):

    '''
    心跳
    '''
    KEY = '/heart'

    DEFAULT_INTERVAL = 5

    def on_connect(self):
        print '连接'
        self._ping()

    def on_disconnect(self):
        self._ping()

    def on_reconnect(self):
        self._ping()

    def on_ping(self, data):
        self._pong(data)

    def on_pong(self, data):
        print('客户端心跳响应')
        self._ping(data)

    def _ping(self, data=None):
        time.sleep(self.DEFAULT_INTERVAL)
        self.emit('ping', {'aa': 1})

    def _pong(self, data=None):
        self.emit('pong', {'aa': 1})


class CmdNamespace(BaseNamespace):

    '''

    '''
    def on_cmd(self, data):
        pass
