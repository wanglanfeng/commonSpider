#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/6 9:03
 @File    : server_utils.py
 @desc    :
'''
import uuid


def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0, 11, 2)])
