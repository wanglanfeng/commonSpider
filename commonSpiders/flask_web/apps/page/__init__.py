#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/19 20:57
 @File    : __init__.py.py
 @desc    :
'''
from flask import Blueprint

page = Blueprint('page', __name__)

from commonSpiders.flask_web.apps.page import views
