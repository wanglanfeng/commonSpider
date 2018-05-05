#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/15 20:19
 @File    : main.py
 @desc    :
'''
from commonSpiders.creeper.loader.loader import CrawlerLoader

if __name__ == '__main__':
    crawler_loader = CrawlerLoader()
    crawler_loader.start_craw()
