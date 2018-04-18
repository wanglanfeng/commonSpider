#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/18 23:12
 @File    : blueprint.py
 @desc    :
'''
from app import app
from commonSpiders.flask_web.apps.test import index

app.register_blueprint(index, url_prefix='/test')