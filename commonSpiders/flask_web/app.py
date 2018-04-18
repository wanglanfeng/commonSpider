#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/18 22:58
 @File    : app.py
 @desc    :
'''
from flask import Flask

from commonSpiders.starter.loader import CrawlerLoader

app = Flask(__name__)

crawler_manager = CrawlerLoader()

if __name__ == '__main__':
    app.debug = True
    app.run()
    crawler_manager.start_craw()
    app.__setattr__('crawler_manager', crawler_manager)
