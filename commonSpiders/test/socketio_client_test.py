#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/2 20:34
 @File    : socketio_client_test.py
 @desc    :
'''
import time

from socketIO_client import BaseNamespace

from commonSpiders.creeper.loader.loader import CrawlerLoader
from commonSpiders.net.client.client import Client
from commonSpiders.net.client.client_run import ClientRun
from commonSpiders.net.extend_context import ContextExtend


class TestNameSpace(BaseNamespace):

    def on_connect(self):
        print('[Connected]')
        self.emit('test', {'aa': 1})

    def on_test(self, data):
        print('客户端响应')
        self.emit('test', {'aa': 1})

    def on_reconnect(self):
        print('[Reconnected]')

    def on_disconnect(self):
        print('[Disconnected]')


class CrawlerProcessExtend(ContextExtend):

    def __init__(self, key, crawlerprocess):
        if not isinstance(crawlerprocess, CrawlerLoader):
            raise Exception('初始化异常')
        super(CrawlerProcessExtend, self).__init__(key, crawlerprocess)

    def start(self):
        print('扩展初始化')
        self.obj.start_craw()


class HeartTest(BaseNamespace):

    def on_connect(self):
        self.emit('ping', {'aa': 1})

    def on_pong(self, data):
        print('客户端心跳响应')
        time.sleep(2)
        self.emit('ping', {'aa': 1})

    def on_ping(self, data):
        print('客户端心跳ping')
        time.sleep(2)
        self.emit('pong', {'aa': 1})


if __name__ == '__main__':
    client = Client()
    client.set_namespace("/test", TestNameSpace),
    client.set_namespace('/heart', HeartTest)
    ClientRun(client).run()
