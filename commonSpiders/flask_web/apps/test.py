#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/18 23:12
 @File    : test.py
 @desc    :
'''
from flask import Blueprint

test = Blueprint('test', __name__)


@test.route('/index')
def index():
    return 'index'
