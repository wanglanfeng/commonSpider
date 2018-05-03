#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/2 23:00
 @File    : run.py
 @desc    :
'''
from commonSpiders.creeper.net.socketio_client_namespace import HeartNamspace
from commonSpiders.net.client.client import Client
from commonSpiders.net.client.client_run import ClientRun

if __name__ == '__main__':
    client = Client()
    client.set_namespace(HeartNamspace.KEY, HeartNamspace)
    ClientRun(client).run()