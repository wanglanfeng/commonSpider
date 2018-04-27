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

    type = ''


class CommonDataMeta(BaseDataMeta):

    def __init__(self, value):
        self.type = BaseDataMeta.TEXT_TYPE
        self.value = value


class FileDataMeta(BaseDataMeta):
    '''
    文件类型数据
    '''

    # TODO 是否需要单独下载（对于大文件数据需要进行一步下载，首先需要测试连接是否可用）
    is_async_down = True
    # 数据是否可用，文件是否可下载
    is_abled = False
    # 图片header，为了反盗链，设置refer，user-agent
    header = {}

    def __init__(self, url):

        self.type = BaseDataMeta.FILE_TYPE
        self.url = ''


class PhotoDataMeta(FileDataMeta):
    '''
    图片类型数据
    '''

    def __init__(self, url, base64_str):

        self.type = BaseDataMeta.PHOTO_TYPE
        self.url = url
        self.base64_str = base64_str


class VideoDataMeta(FileDataMeta):
    '''
    视频类型数据
    '''
    def __init__(self, url):
        self.type = BaseDataMeta.VIDEO_TYPE
        self.url = url

