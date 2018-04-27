#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/19 19:13
 @File    : page.py
 @desc    :
'''
from flask import current_app, render_template

from commonSpiders.web.flask_web.apps.page import page
from commonSpiders.web.flask_web.run import mdb


@page.route('/home')
def index():
    aa = current_app

    aa = mdb.db
    return render_template('modules/common/home.html')