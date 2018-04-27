#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/19 19:26
 @File    : settings.py
 @desc    :
'''
import os

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = os.urandom(24)
STATIC_URL_PATH = ""
# DEBUG = True
PORT = 10000

MONGODB_SETTINGS = {
    'db': 'settings',
    'host': 'localhost',
    'port': 27017
    # 'username':'webapp',
    # 'password':'pwd123'
}
PYMONGODB_SETTINGS = {
    'MONGO_HOST' : 'localhost',
    'MONGO_PORT' : 27017,
    'MONGO_USERNAME' : 'bjhee',
    'MONGO_PASSWORD' : '111111',
    'MONGO_DBNAME' : 'settings'
}