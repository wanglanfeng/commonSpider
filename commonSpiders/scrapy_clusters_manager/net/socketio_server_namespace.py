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


class Heart(ServerBaseNamespace):

    KEY = '/heart'

    def on_connect(self):
        print('客户端连接')

    def on_ping(self, data):
        print('服务端心跳ping')
        self.emit('pong', {'aa': 1})

    def on_pong(self, data):
        print('服务端心跳响应')
        self.emit('ping', {'aa': 1})


class CrawlerProcessNamespace(ServerBaseNamespace):
    '''
    用于与其他服务器上的爬虫管理通信
    '''

    KEY = '/crawler'

    def on_register_crawlerprocess(self, data):
        '''
        注册爬虫管理器
        :param data:
        :return:
        1 获取服务器cpu，内存
        2 获取爬虫管理器状态
        3
        '''


    def on_logout(self, data):
        '''
        注销
        :param data:
        :return:
        1 消除爬虫管理器的信息
        2 消除爬虫管理器下所有工作者信息
        '''
        pass

    def on_register_crawler_job_info(self, data):
        '''
        注册爬虫工作者信息
        :param data:
        :return:
        1 初始化爬虫状态对象
        2 初始化爬虫信息
        3 初始化爬虫工作者配置
        '''

    def on_register_crawler_obj(self, data):
        '''
        注册爬虫对象信息
        :param data:
        :return:
        1 初始化爬虫工作者对象状态
        '''

    def on_update_crawler_ojb_status(self, data):
        '''
        更新爬虫对象状态
        :param data:
        :return:
        1 更新爬虫工作者对象状态
        '''

    def on_cmd_callback(self, data):
        '''
        接受爬虫管理器的命令反馈
        :param data:
        :return:
        '''
