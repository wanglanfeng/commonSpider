#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/15 20:19
 @File    : main.py
 @desc    :
'''
from commonSpiders.creeper.loader.loader import CrawlerLoader
from commonSpiders.test.my_thread import myThread

if __name__ == '__main__':
    crawler_loader = CrawlerLoader()
    myThread(crawler_loader.process).start()
    crawler_loader.start_craw()
