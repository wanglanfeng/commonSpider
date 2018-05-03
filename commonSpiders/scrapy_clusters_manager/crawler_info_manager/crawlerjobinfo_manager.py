#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/27 21:42
 @File    : crawlerjobinfo_manager.py
 @desc    :
'''


class CrawlerJobInfoManager:
    '''
    爬虫工作者状态管理器
    '''

    def __init__(self):
        self.crawler_job_info_table = {}
