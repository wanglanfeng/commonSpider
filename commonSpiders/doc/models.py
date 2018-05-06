#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/3 22:55
 @File    : models.py
 @desc    :
'''
# 全部采用mongodb存储
'''
数据库配置

5：url配置信息
{
    id: '',
    task_id: '', 任务id,
    item_parse_config: {
        html_url_reg: '', 匹配的页面url
        key: '', 存储时所使用的key（若没有则自动生成）
        parse_factory: 'reg',(解析器解析方式：正则，xpath，css，pyjquery)
        item_meta_parser_configs: [
            {
                key: '', 字段key
                dom_reg: '', 字段匹配的url
                parser_type: ''字段解析类型（遇到什么类型的数据该怎么解析（text, url, file, photo, video））
            }
        ]
    }
}


9：数据结构
{   
    id: '',
    task_id: '', 任务id
    plan_id: '', 计划id
    time: '', 入库时间
    item: {
        key: val,
        ...
    }
}
10：爬取过程日志存放信息
{
    id: '',
    task_id: '', 任务id
    plan_id: '', 计划id
    time: '', 产生时间
    level: '', 级别（success，warning， info，error）
    msg: '', 消息
    error: '', 错误问题
    ip: '' 发生错误的服务器ip
}

'''
