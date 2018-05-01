#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/1 21:58
 @File    : server.py
 @desc    :
'''
import threading

from commonSpiders.net.server.flask.app.app import App
from commonSpiders.net.server.flask.flask_context_extend import FlaskContextExtend


def context_list_init(context_init_list):
    '''
    初始化app扩展上下文
    :param context_init_list:
    :return:
    '''
    if not context_init_list or not isinstance(context_init_list, list):
        print('初始化app扩展上下文失败')
        return
    for context in context_init_list:
        # 异步
        if context.async:
            threading.Thread(target=context.start)
        # 同步
        else:
            context.start()


def run_server(app, context_extend_list=[]):
    '''
    启动socket服务
    :param socketio_app:
    :param context_extend_list:
    :return:
    '''
    if not isinstance(app, App):
        raise Exception('启动socket服务发生错误，app参数应该为App对象')
    server = app
    # 在app初始化之前需要进行初始化的对象
    context_init_before_list = []
    # 在app初始化之后需要进行初始化的对象
    context_init_after_list = []
    for context in context_extend_list:
        if isinstance(context, FlaskContextExtend):
            server.set_context(context.key, context.obj)
            if context.priority >= server.DEFAULT_PRIORITY:
                context_init_before_list.append(context)
            else:
                context_init_after_list.append(context)
    context_init_before_list = sorted(context_init_before_list, cmp=lambda context: context.priority)
    context_init_after_list = sorted(context_init_after_list, cmp=lambda context: context.priority)
    context_list_init(context_init_before_list)
    server.start()
    context_list_init(context_init_after_list)
