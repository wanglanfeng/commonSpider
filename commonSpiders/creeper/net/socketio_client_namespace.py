#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/2 23:02
 @File    : socketio_client_namespace.py
 @desc    :
'''

from socketIO_client import BaseNamespace


class ClientBaseNamespace(BaseNamespace):

    KEY = '/base'

    REGISTER = False

    def __init__(self, io, path):
        super(ClientBaseNamespace, self).__init__(io, path)
        self.extend_context = self.__dict__['_io'].__dict__['extend_context']


class CrawlerProcessNamespace(BaseNamespace):
    '''
    用于主动向服务端注册爬虫管理器
    '''
    KEY = '/crawler_process'

    def on_connect(self):
        '''
        连接服务器需要注册
        :return:
        '''
        print('客户端连接')
        self.register_crawler_process()

    def on_reconnect(self):
        '''
        重连成功也需要注册
        :return:
        '''
        self.register_crawler_process()

    def on_disconnect(self):
        '''
        断开连接需要登出
        :return:
        '''
        self.logout_crawler_process()

    def on_register_success(self, data):

        print('注册成功')

    def on_logout_success(self, data):

        print('登出成功')

    def register_crawler_process(self):
        '''
        注册爬虫管理器
        :return:
        '''
        self.emit('register', {})

    def logout_crawler_process(self):
        '''
        注销爬虫管理器
        :return:
        '''
        self.emit('logout', {})


class ServerInfoNamespace(BaseNamespace):
    '''
    用于主动向服务器发送系统运行情况
    '''
    KEY = '/server_info'

    DEFAULT_INTREVAL = 20

    def on_test(self, data):
        print('测试')
