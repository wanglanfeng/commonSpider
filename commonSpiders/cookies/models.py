#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/15 0:10
 @File    : models.py
 @desc    :
'''
from sqlalchemy import Column, String, Integer

from commonSpiders.mysql.models import Base

class Cookie(Base):

    __tablename__ = 'cookie'

    id = Column(Integer, primary_key=True)
    # 平台类型
    platform = Column(String)
    # cookie名
    name = Column(String)
    # cookie值
    value = Column(String)
    domain = Column(String)
    path = Column(String)
    # cookie过期时间
    expires = Column(String)
    size = Column(Integer)
    http = Column(String)
    secure = Column(String)
    samesite = Column(String)
