#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/1 22:36
 @File    : socket_server_test.py
 @desc    :
'''
from flask import current_app
from flask_socketio import Namespace

from commonSpiders.creeper.loader.loader import CrawlerLoader
from commonSpiders.net.extend_context import ContextExtend
from commonSpiders.net.server.flask.server import SocketIoApp
from commonSpiders.net.server.flask.server_run import FlaskRun


class TestNameSpace(Namespace):

    def on_connect(self):
        print('服务端连接')

    def on_test(self, data):
        print('服务端测试')
        self.emit('test', {'aa': 1})


class Heart(Namespace):

    def on_ping(self, data):
        print('服务端心跳ping')
        aa = current_app
        self.emit('pong', {'aa': 1})

    def on_pong(self, data):
        print('服务端心跳响应')
        self.emit('ping', {'aa': 1})


class CrawlerProcessExtend(ContextExtend):

    def __init__(self, key, crawlerprocess, priority='', async=True):
        if not isinstance(crawlerprocess, CrawlerLoader):
            raise Exception('初始化异常')
        super(CrawlerProcessExtend, self).__init__(key, crawlerprocess, priority, async)

    def start(self):
        print('扩展初始化')
        self.obj.start_craw()


if __name__ == '__main__':
    app = SocketIoApp()
    app.socketio.on_namespace(TestNameSpace('/test'))
    app.socketio.on_namespace(Heart("/heart"))
    FlaskRun(app, [CrawlerProcessExtend('crawlerprocess', CrawlerLoader(), -1)]).run()