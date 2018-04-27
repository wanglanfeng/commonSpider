#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/21 14:09
 @File    : socketio_server.py
 @desc    :
'''
from flask_socketio import emit

from commonSpiders.web.flask_web.app import SocketIoApp
from commonSpiders.web.flask_web.apps.socketio.namespace import TestName

app = SocketIoApp("settings")


def get_sockio_server():
    '''
    获取app对象
    :return:
    '''
    return app


socketio = app.socketio

# 以下为sockio事件注册


socketio.on_namespace(TestName('/test'))


@socketio.on('test', namespace='/test')
def test(data):
    print('接受')
    print(socketio)
    emit('response', {'code': '200', 'msg': 'start to process...'})


print(1)





