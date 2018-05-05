#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/5 8:16
 @File    : socketio_msg.py
 @desc    :
'''


class Msg(object):

    def __init__(self):
        # 消息类型，便于后期处理
        self.type = ''
        # 消息数据
        self.data = None
