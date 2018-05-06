#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/15 0:38
 @File    : models.py
 @desc    :
'''
from sqlalchemy import Column, Integer, String

from commonSpiders.storage.mysql.models import Base


class Header(Base):
    '''
    http的头
    '''
    __tablename__ = 'header'

    id = Column(Integer, primary_key=True)
    # header的键名称
    name = Column(String)
    # header的键值
    value = Column(String)