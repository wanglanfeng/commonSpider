#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/2 23:02
 @File    : socketio_namespace.py
 @desc    :
'''
import time

from socketIO_client import BaseNamespace


class HeartNamspace(BaseNamespace):

    '''
    心跳
    '''

    DEFAULT_INTERVAL = 5

    def on_connect(self):
        self._ping()

    def on_disconnect(self):
        self._ping()

    def on_reconnect(self):
        pass

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
