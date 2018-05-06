#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/6 9:03
 @File    : server_utils.py
 @desc    : 服务端要使用的通用工具
'''
import hashlib
import uuid

mac = None


def get_mac_address():
    '''
    获取mac地址
    :return:
    '''
    global mac
    if not mac:
        temp = uuid.UUID(int=uuid.getnode()).hex[-12:]
        mac = ":".join([temp[e:e+2] for e in range(0, 11, 2)])
    return mac


def get_guid_by_mac(name):
    prefix = get_mac_address()
    myMd5 = hashlib.md5()
    myMd5.update('%s%s' % (prefix, name or ''))
    myMd5_Digest = myMd5.hexdigest()
    return myMd5_Digest
