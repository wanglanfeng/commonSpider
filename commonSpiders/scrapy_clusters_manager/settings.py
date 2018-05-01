#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/30 10:48
 @File    : settings.py
 @desc    :
'''
# 全部采用mongodb存储
'''
数据库配置
1：爬虫服务器名称存储--server
{
    id: '',
    name: '',服务名（若不存在则自动生成，若存在且与其他冲突，则添加时间戳）
    ip: '',服务器ip
    port: '',服务器端口
    token: '',与该服务器通信的token（由爬虫服务器携带过来，若过期后由命名服务器主动去获取）
    register_time: '',注册时间
}
2：爬虫服务器进程默认配置信息
{
    id: '',
    name_id: ''，名称配置中的id，与爬虫服务器对应
    settings: { # json配置
        'BOT_NAME'： 'BOT_NAME',
        'SPIDER_MODULES': ['commonSpiders.creeper.spiders', 'commonSpiders.spiders_test'],
        'DEFAULT_REQUEST_HEADERS': {
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Accept-Language': 'en',
        }
    }, 
}
# 每个任务至少有一个计划，通过计划把所有内容爬取完成
3：爬取任务计划--plan
{
    id: '',
    task_id: '', 任务id
    duration_reservation: ''多少秒
    start_time:''本次爬取开始时间
    end_time: ''本次爬取结束时间
}
4：任务对应的个性配置信息--settings
{
    id: '',
    task_id: '', 任务id,
    settings: {}
}
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
6 category配置
{
    id: '',
    name: '',名称
    desc: ''描述
}
7 item配置
{
    id: '',
    task_id: '', 任务id
    category_id: '', 类目id
    key: '', item的key
    name: '', item的名称
    desc: '', item的描述
    item_metas: [
        {
            key: '', 字段的key
            name: '', 字段的名称
            desc: '' 字段的描述
        }
    ]
}
8：存储配置--datasource
{
    id: ''
    type: '',# 存储类型
    ip: '', # 存储地址ip
    port: '', # 存储地址端口
    username: '',# 存储地址连接用户名
    pwd: ''# 存储地址连接密码
}
8：数据存放位置信息
{
    id: '',
    task_id: '', 任务id
    plan_id: '', 计划id
    items_datasource: [
        {
            item_id: '', # item配置id，方便查找数据
            datasource_id: '', # 数据源地址信息
            namespace: '' # 数据源下的命名空间
        }
    ]
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
