#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/15 0:11
 @File    : models.py
 @desc    :
'''
from sqlalchemy import Column, Integer, String

from commonSpiders.storage.mysql.models import Base


class UserAgent(Base):

    __tablename__ = 'user_agent'

    id = Column(Integer, primary_key=True)
    # user-agent
    ua = Column(String)
    # 浏览器类型
    browser = Column(String)
    # 平台类型
    platform = Column(String)

