#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/27 22:05
 @File    : down_middlewares.py
 @desc    :
'''


class Test1Middleware(object):

    def __init__(self):
        pass

    def process_request(self, request, spider):
        print '<<'
        print 'test1'
        print(spider)
        print '>>'


class Test2Middleware(object):

    def __init__(self):
        pass

    def process_request(self, request, spider):
        print '<<'
        print 'test2'
        print(spider)
        print '>>'
