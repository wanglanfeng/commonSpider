#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/3 20:02
 @File    : run.py
 @desc    :
'''
from commonSpiders.net.server.flask.server import SocketIoApp
from commonSpiders.net.server.flask.server_run import FlaskRun
from commonSpiders.scrapy_clusters_manager.net.context_extend import RedisContextExtend
from commonSpiders.scrapy_clusters_manager.net.socketio_server_namespace import Heart
from commonSpiders.storage.redis.redis_client import RedisClient

if __name__ == '__main__':
    app = SocketIoApp('commonSpiders.scrapy_clusters_manager.net.settings')
    app.socketio.on_namespace(Heart(Heart.KEY))
    FlaskRun(app, [RedisContextExtend('redis', RedisClient(), 1)]).run()