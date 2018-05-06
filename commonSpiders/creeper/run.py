#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/2 23:00
 @File    : run.py
 @desc    :
'''
from commonSpiders.creeper.manager.manager import CrawlerProcessManager
from commonSpiders.creeper.net.crawler_run import CrawlerRun
from commonSpiders.creeper.net.socketio_client_namespace import CrawlerProcessNamespace
from commonSpiders.net.client.client import Client

if __name__ == '__main__':
    client = Client()
    client.set_namespace(CrawlerProcessNamespace.KEY, CrawlerProcessNamespace)
    CrawlerRun(client, [CrawlerProcessManager()]).run()