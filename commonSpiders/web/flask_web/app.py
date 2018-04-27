#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/19 20:09
 @File    : app.py
 @desc    :
'''
import threading
from importlib import import_module
from flask import Flask
from flask_socketio import SocketIO

from commonSpiders.web.flask_web.blueprint import register_blueprint


class App(threading.Thread):

    DEFAULT_IP = '0.0.0.0'
    DEFAULT_PORT = 5000

    app = Flask(__name__)

    def __init__(self, settings):
        threading.Thread.__init__(self)
        self.settings = {}
        self.ip = self.DEFAULT_IP
        self.port = self.DEFAULT_PORT
        self._load_settings(settings)
        self._init_app()
        register_blueprint(self.app)

    def _load_settings(self, settings_path):

        module = import_module(settings_path)
        for key in dir(module):
            if key.isupper():
                self.settings.update({
                    key: getattr(module, key)
                })

    def _init_app(self):
        port = self.settings.get('SERVER_PORT', None)
        self.port = port or self.port

    def set_context(self, key, context):

        if key is not None and context is not None:
            self.app.__setattr__(key, context)

    def config_app(self, key, obj):

        if key is not None and obj is not None:
            self.app.__setattr__(key, obj)

    def run(self):
        print('启动app')


class FlaskApp(App):

    def __init__(self, settings):
        super(FlaskApp, self).__init__(settings)

    def run(self):
        print('启动app')
        self.app.run(host=self.DEFAULT_IP, port=self.port)


class SocketIoApp(App):

    def __init__(self, settings):
        super(SocketIoApp, self).__init__(settings)
        self.socketio = SocketIO()

    def run(self):
        print('启动app')
        self.socketio.init_app(self.app)
        self.socketio.run(self.app, host=self.DEFAULT_IP, port=self.port)


