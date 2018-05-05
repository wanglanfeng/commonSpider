#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/5 17:27
 @File    : mongo_model.py
 @desc    :
'''
from bson import ObjectId
from mongoengine import Document


class BaseDocument(Document):

    OBJECT_ID_KEY = '_id'
    QUERY_ID_KEY = 'id'

    meta = {'abstract': True}

    @classmethod
    def to_json(cls, json_data, delete_id=True):

        '''
        将json中的ObjectId对象转成字符串
        :param json_data:
        :return:
        '''

        if isinstance(json_data, dict):
            _id = json_data.get(cls.OBJECT_ID_KEY, '')
            if delete_id:
                json_data.pop(cls.OBJECT_ID_KEY)
            json_data.update({
                cls.QUERY_ID_KEY: _id.__str__()
            })
            return json_data
        else:
            return {}

    @classmethod
    def to_mongo_query(cls, query):
        '''
        将json查询条件转成mongo查询条件
        :param json_data:
        :return:
        '''
        if isinstance(query, dict):
            id = query.get(cls.QUERY_ID_KEY, None)
            if id:
                query.pop(cls.QUERY_ID_KEY)
                query.setdefault(cls.OBJECT_ID_KEY, ObjectId(id))
            return query
        else:
            return {}

    @classmethod
    def get_connect(cls):
        return cls._get_collection()
