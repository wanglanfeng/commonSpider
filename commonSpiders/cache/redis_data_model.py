#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/5 13:09
 @File    : redis_data_model.py
 @desc    :
'''


class RedisInfo(dict):

    # 过期时间，若为None或0则表示不过期
    EX = None
    KEY_PREFIX = []
    KEY_PREFIX_SEP = ':'

    def get_key(self, key):
        key_list = [dir_name for dir_name in self.KEY_PREFIX]
        if isinstance(key, list):
            key_list += key
        elif isinstance(key, str):
            key_list.append(key)
        key_list = map(lambda x: x.upper(), key_list)
        key = self.KEY_PREFIX_SEP.join(key_list)
        return key

