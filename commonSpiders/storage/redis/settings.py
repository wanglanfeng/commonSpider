#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/14 23:07
 @File    : settings.py
 @desc    :
'''

host = 'localhost'
port = '6379'
pwd = None


def get_db_config(host, port, db, pwd):
    return {
        'host': host,
        'port': port,
        'db': db,
        'pwd': pwd
    }


redis_db = {
    'redis_0': get_db_config(host, port, 0, pwd)
}


def get_redis_config(db):
    return redis_db['redis_%s' % db]