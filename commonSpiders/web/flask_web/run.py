#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/19 19:24
 @File    : run.py
 @desc    :
'''
from flask_pymongo import PyMongo

from commonSpiders.creeper.loader.loader import CrawlerLoader
from commonSpiders.web.flask_web.socketio_server import get_sockio_server

mdb = PyMongo()

if __name__ == '__main__':
    server = get_sockio_server()
    # 配置pymongo
    mongo_settings = server.settings.get("PYMONGODB_SETTINGS", None)
    if mongo_settings:
        mdb.init_app(server.app)
    # 配置爬虫管理器
    crawler_manager = CrawlerLoader()
    server.set_context('crawler_manager', crawler_manager)
    server.start()
    crawler_manager.start_craw()