#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/6 0:07
 @File    : cmd.py
 @desc    : 创建mysql表
'''

import sys
from importlib import import_module


from commonSpiders.storage.mysql.sqlalchemy_engine import SqlSession

reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == "__main__":
    # models_path_list = sys.argv[0]
    sqlSession = SqlSession()
    objs = import_module('commonSpiders.scrapy_clusters_manager.mysql.models')
    models = [getattr(objs, info, {}) for info in dir(objs) if getattr(getattr(objs, info, {}), '__tablename__', None)]
    if models:
        models[0].metadata.create_all(sqlSession.engine)
