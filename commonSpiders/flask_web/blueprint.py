#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/18 23:12
 @File    : blueprint.py
 @desc    :
'''
from commonSpiders.flask_web.apps.page import page


def register_blueprint(app):
    app.register_blueprint(page, url_prefix='/page')