#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/21 13:08
 @File    : namespace.py
 @desc    :
'''
from flask import current_app
from flask_socketio import Namespace, emit


class TestName(Namespace):

    def on_connect(self):
        aa = current_app
        print('连接')

    def on_disconnect(self):
        pass

    def on_request_for_response(self, data):
        emit('response', data)