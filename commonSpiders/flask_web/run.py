#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/19 19:24
 @File    : run.py
 @desc    :
'''

from commonSpiders.flask_web.app import FlaskApp
from commonSpiders.starter.loader import CrawlerLoader

crawler_manager = CrawlerLoader()


if __name__ == '__main__':

    app = FlaskApp("settings")
    app.set_context('crawler_manager', crawler_manager)
    app.start()
    crawler_manager.start_craw()