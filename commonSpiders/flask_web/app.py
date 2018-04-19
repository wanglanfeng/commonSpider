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

from commonSpiders.flask_web.blueprint import register_blueprint


class App(threading.Thread):

    app = Flask(__name__)

    def __init__(self, settings):
        threading.Thread.__init__(self)
        self.settings = {}
        # self._load_settings(settings)
        register_blueprint(self.app)

    def _load_settings(self, settings_path):

        module = import_module(settings_path)
        for key in dir(module):
            if key.isupper():
                self.settings.update({
                    key: getattr(module, key)
                })

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
        super(FlaskApp).__init__(settings)

    def run(self):
        print('启动app')
        self.app.run()


class SocketIoApp(App):

    def __init__(self, settings):
        super(FlaskApp).__init__(settings)

    def run(self):
        print('启动app')
        socketio = SocketIO()
        socketio.init_app(self.app)
        socketio.run(self.app)


