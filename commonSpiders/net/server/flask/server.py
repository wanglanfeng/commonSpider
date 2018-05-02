#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/2 22:06
 @File    : server.py
 @desc    :
'''
from flask import Flask
from flask_socketio import SocketIO

from commonSpiders.net.app import BaseApp


class App(BaseApp):

    app = Flask(__name__)

    def __init__(self, settings=''):
        super(App, self).__init__(settings)
        self._init_app()

    def _init_app(self):
        '''
        初始化app需要的数据
        :return:
        '''
        port = self.settings.get('SERVER_PORT', None)
        self.port = port or self.port

    def set_context(self, key, context):
        '''
        直接将app需要用到的信息加载到app对象上
        :param key:
        :param context:
        :return:
        '''
        if key is not None and context is not None:
            self.app.__setattr__(key, context)

    def run(self):
        print('启动app')


class FlaskApp(App):

    def __init__(self, settings=''):
        super(FlaskApp, self).__init__(settings)

    def run(self):
        print('启动flask app')
        self.app.run(host=self.DEFAULT_IP, port=self.port)


class SocketIoApp(App):

    def __init__(self, settings=''):
        super(SocketIoApp, self).__init__(settings)
        self.socketio = SocketIO()

    def run(self):
        print('启动socketio app')
        self.socketio.init_app(self.app)
        self.socketio.run(self.app, host=self.DEFAULT_IP, port=self.port)
