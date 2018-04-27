#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/15 0:10
 @File    : models.py
 @desc    :
'''
from tokenize import String

from sqlalchemy import Column, Integer, Boolean, DateTime

from commonSpiders.storage.mysql.models import Base


class HttpProxy(Base):

    '''
    http,https代理
    '''

    __tablename__ = 'proxy'

    id = Column(Integer, primary_key=True)
    # 协议
    protocol = Column(String)
    # ip
    ip = Column(String)
    # 端口
    port = Column(String)
    # 预定过期时间
    expire_time = Column(DateTime)
    # 是否过期
    is_expire = Column(Boolean)
