#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/5 16:51
 @File    : mongo_client.py
 @desc    :
'''
from mongoengine import register_connection


class MongoDbClient(object):
    '''
    mongo客户端
    '''

    connect_default = {'alias': 'default', 'db': 'spider_settings', 'host': ['localhost', ], 'port': 27017,
                       'username': '', 'password': '', 'maxpoolsize': 50}

    def __init__(self):

        self.connect_database()

    def connect_database(self):
        connect_dict = self.connect_default
        for i in range(len(connect_dict['host'])):
            try:
                # conn = pymongo.Connection(connect_dict['host'][i] + ':' + str(connect_dict['port']))
                register_connection(connect_dict['alias'], connect_dict['db'], host=connect_dict['host'][i],
                                    port=connect_dict['port'], username=connect_dict['username'],
                                    password=connect_dict['password'], maxpoolsize=connect_dict['maxpoolsize'])
                # conn.disconnect()
                break
            except Exception as e:
                continue
