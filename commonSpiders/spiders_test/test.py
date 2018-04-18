#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/17 20:48
 @File    : test.py
 @desc    :
'''
from commonSpiders.cookies.models import Cookie
from commonSpiders.spiders_test.TestSpider import TestSpider
from commonSpiders.utils.class_load_utils import get_module_by_path, get_class_obj_by_package_or_module, \
    get_class_obj_by_pm_list

if __name__ == '__main__':

    print('测试-start')
    array = get_module_by_path('commonSpiders')
    spider = TestSpider
    cookie = Cookie
    array = get_class_obj_by_pm_list(['commonSpiders.spiders', 'commonSpiders.spiders_test'], spider)
    print(array)
    print('测试-end')

