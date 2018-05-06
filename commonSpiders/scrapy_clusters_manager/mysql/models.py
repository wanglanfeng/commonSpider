#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
 @Time    : 2018/5/5 20:27
 @File    : models.py
 @desc    :
"""
import datetime

from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SqlBase(Base):

    __tablename__ = "BASE"
    __abstract__ = True
    __table_args__ = {
        "mysql_engine": "InnoDB",
        "mysql_charset": "utf8"
    }
    id = Column(Integer, primary_key=True, comment="主键", autoincrement=True)
    create_time = Column(DateTime, comment="创建时间", default=datetime.datetime.now())

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


class CrawlerProcessInfo(SqlBase):
    """
    爬虫管理器信息
    """
    __tablename__ = "crawler_process_info"

    crawler_process_guid = Column(String(50), comment="爬虫全局唯一标识")
    ip = Column(String(50), comment="爬虫所在服务器ip")
    token = Column(String(50), comment="爬虫通信使用的token")
    last_register_time = Column(DateTime, comment="最近一次注册时间", onupdate=datetime.datetime.now())


class CrawlerTask(SqlBase):
    """
    爬虫任务
    """
    __tablename__ = "crawler_task"

    name = Column(String(50), default="")
    desc = Column(String(50), default="")
    start_time = Column(DateTime, comment="任务开始时间")
    end_time = Column(DateTime, comment="任务结束时间")
    min_item_num = Column(Integer, comment="爬取item下限", default=0)
    max_item_num = Column(Integer, comment="爬取item上限", default=1)
    scrapyed_num = Column(Integer, comment="已爬取item数量", default=0)

    crawler_num = Column(Integer, comment="需要配置的爬虫数", default=0)


class CrawlerGroupSettingsItem(SqlBase):
    '''
    某次任务使用的爬虫配置
    '''

    __tablename__ = "crawler_group_settings_item"

    task_id = Column(Integer, ForeignKey("crawler_task.id"), comment="任务id")
    key = Column(String(50), default="", comment="配置key")
    value = Column(String(50), default="", comment="配置value")


class ItemInfo(SqlBase):
    """
    爬虫item信息
    """
    __tablename__ = "item_info"

    task_id = Column(Integer, ForeignKey("crawler_task.id"), comment="任务id")
    item_datasource_id = Column(Integer, ForeignKey("item_data_source.id"), comment="数据源id")
    key = Column(String(50), comment="item的key", default="")
    name = Column(String(50), comment="item的名称", default="")
    desc = Column(String(50), comment="item的描述", default="")

    # item解析
    html_url_reg = Column(String(50), comment="匹配的页面正则", default="")
    # reg, xpath, css, pyjquery
    parse_ruler = Column(String(50), comment="item解析规则器", default="reg")


class ItemMeta(SqlBase):
    """
    item字段信息
    """
    __tablename__ = "item_meta"

    item_id = Column(Integer, ForeignKey("item_info.id"), comment="itemid")
    key = Column(String(50), comment="item字段的key", default="")
    name = Column(String(50), comment="item字段的名称", default="")
    desc = Column(String(50), comment="item字段的描述", default="")

    # item字段解析
    dom_rule = Column(String(50), comment="解析器使用的解析规则", default="")
    # （text， url， file， image， video）
    parser_type = Column(String(50), comment="解析数据类型", default="")


class ItemDataSource(SqlBase):
    """
    item存放数据元
    """
    __tablename__ = "item_data_source"

    name = Column(String(50), comment="数据源名称", default="")
    desc = Column(String(50), comment="数据源描述", default="")
    type = Column(String(50), comment="数据源类型", default="")
    ip = Column(String(50), comment="数据源ip", default="")
    port = Column(String(50), comment="数据源端口", default="")
    path = Column(String(50), comment="数据源存放路径", default="")
    # 加盐加密，存放密文
    username = Column(String(50), comment="接入用户名", default="")
    # 加盐加密（存放密文）
    password = Column(String(50), comment="接入密码", default="")




