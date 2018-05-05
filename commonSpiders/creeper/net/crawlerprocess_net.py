#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/5 9:05
 @File    : crawlerprocess_net.py
 @desc    : 爬虫管理器对外的网络接口
'''


class CrawlerProcessNetInter(object):

    def __init__(self, net=None):
        self.net = net

    def send(self, *args, **kwargs):
        print('爬虫网络默认发送接口')

    def receive(self, data, *args, **kwargs):
        print('爬虫网络默认接收接口， 数据：'+ data)


class CrawlerProcessNetSocketIO(CrawlerProcessNetInter):

    '''
    利用socketio-client扩展爬虫网络接口
    '''

    def __init__(self, client):
        print(client)
        super(CrawlerProcessNetSocketIO, self).__init__(client)

    def send(self, path, event, data):
        self.net.socketIO.emit(event, data, path=path)
        print(self.net.socketIO)


