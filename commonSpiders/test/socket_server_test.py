#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/1 22:36
 @File    : socket_server_test.py
 @desc    :
'''
from commonSpiders.net.server.flask.app.app import SocketIoApp
from commonSpiders.net.server.flask.server import run_server

if __name__ == '__main__':
    app = SocketIoApp()
    run_server(app)