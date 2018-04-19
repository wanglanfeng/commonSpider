#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/19 19:13
 @File    : page.py
 @desc    :
'''
from flask import current_app, render_template

from commonSpiders.flask_web.apps.page import page


@page.route('/index')
def index():
    aa = current_app
    return render_template('test.html')