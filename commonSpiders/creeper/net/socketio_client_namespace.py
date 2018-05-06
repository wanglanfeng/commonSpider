#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/2 23:02
 @File    : socketio_client_namespace.py
 @desc    :
'''
import time

from socketIO_client import BaseNamespace

from commonSpiders.creeper.manager.manager import KEY


def get_extend_context(namespace):
    '''
    获取命名空间的扩展对象
    :param namespace:
    :return:
    '''
    return namespace.__dict__['_io'].__dict__['extend_context'] if namespace and isinstance(namespace, BaseNamespace) else {}


class ClientBaseNamespace(BaseNamespace):
    KEY = '/base'

    REGISTER = False


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
        print('客户端连接成功')
        manager = get_extend_context(self).get(KEY, None)
        while manager.INIT_CRAWLER_PROCESS_FLAG:
            time.sleep(2)
            process_dict = manager.process_dict
            process_info_list = [{
                'guid': key
            } for key, process in process_dict.items()]
            self.register_crawler_process(process_info_list)

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

    def register_crawler_process(self, data):
        '''
        注册爬虫管理器
        :return:
        '''
        self.emit('register', data)

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
