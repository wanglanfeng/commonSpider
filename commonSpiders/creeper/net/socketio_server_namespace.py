#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/3 19:58
 @File    : socketio_server_namespace.py
 @desc    :
'''
from flask import current_app
from flask_socketio import Namespace


class ServerBaseNamespace(Namespace):
    '''
    基础类
    '''
    KEY = '/base'

    def __init__(self, namespace=None):
        super(ServerBaseNamespace, self).__init__(namespace)
        self.extend_context = current_app