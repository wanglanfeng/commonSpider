#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/25 23:12
 @File    : utils.py
 @desc    :
'''
import uuid


def guid_generate():
    return uuid.uuid1().__str__()
