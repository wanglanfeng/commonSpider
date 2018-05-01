#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/26 21:51
 @File    : item_meta.py
 @desc    :
'''


class BaseDataMeta:

    # 文字类型数据
    TEXT_TYPE = 0
    # 图片
    PHOTO_TYPE = 1
    # 视频
    VIDEO_TYPE = 2
    # 文件
    FILE_TYPE = 3
    # URL
    URL_TYPE = 4
    # 元数据类型
    type = ''


class CommonDataMeta(BaseDataMeta):
    '''
    通用数据元模型
    '''

    def __init__(self, key, data, response):
        self.type = BaseDataMeta.TEXT_TYPE
        # 元数据的key
        self.key = key
        # 元数据的值
        self.data = data


class TextDataMeta(BaseDataMeta):

    '''
    文本数据元
    '''
    def __init__(self, key, data, response):
        super(TextDataMeta, self).__init__(key, data, response)
        self.type = BaseDataMeta.TEXT_TYPE
        self.data = data


class UrlDataMeta(BaseDataMeta):
    '''
    url数据元，用于继续请求的url
    '''
    # 是否是正确的url表达式
    _is_url = False
    # 是否需要再请发送请求
    _is_request = True
    # TODO 是否需要单独下载（对于大文件数据需要进行一步下载，首先需要测试连接是否可用）
    is_async_down = True
    # 数据是否可用，文件是否可下载
    is_abled = False
    # 图片header，为了解决反盗链问题，设置refer，user-agent
    _headers = {}
    # meta
    _meta = {}
    # http通用信息
    _general = {}

    def __init__(self, key, url, response):
        super(UrlDataMeta, self).__init__(key, url, response)
        self.type = self.URL_TYPE
        self._is_url = self._check_url()
        self._headers.update(response.headers)
        self._meta.update(response.meta)

    def set_headers(self, **headers):
        self._headers.update(headers)

    def get_headers(self):
        return self._headers or {}

    def is_request(self):
        return self._is_request

    def is_url(self):
        return self._is_url

    def _check_url(self):
        return True


class FileDataMeta(UrlDataMeta):
    '''
    文件类型数据
    '''

    def __init__(self, key, url, response):
        super(FileDataMeta, self).__init__(key, url, response)
        self.type = BaseDataMeta.FILE_TYPE
        self._is_request = False


class PhotoDataMeta(FileDataMeta):
    '''
    图片类型数据
    '''

    def __init__(self, key, url, response):
        super(PhotoDataMeta, self).__init__(key, url, response)
        self.type = BaseDataMeta.PHOTO_TYPE
        self._is_request = False


class VideoDataMeta(FileDataMeta):
    '''
    视频类型数据
    '''
    def __init__(self, key, url, response):
        super(VideoDataMeta, self).__init__(key, url, response)
        self.type = BaseDataMeta.VIDEO_TYPE
        self._is_request = False

