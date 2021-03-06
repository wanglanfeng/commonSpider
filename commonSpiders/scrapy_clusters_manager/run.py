#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/3 20:02
 @File    : run.py
 @desc    :
'''
from commonSpiders.net.server.flask.server import SocketIoApp
from commonSpiders.net.server.flask.server_run import FlaskRun
from commonSpiders.scrapy_clusters_manager.net.socketio_server_namespace import  CrawlerProcessNamespace
from commonSpiders.scrapy_clusters_manager.service.service import Service

if __name__ == '__main__':
    app = SocketIoApp('commonSpiders.scrapy_clusters_manager.settings')
    app.socketio.on_namespace(CrawlerProcessNamespace(CrawlerProcessNamespace.KEY))
    FlaskRun(app, [Service()]).run()