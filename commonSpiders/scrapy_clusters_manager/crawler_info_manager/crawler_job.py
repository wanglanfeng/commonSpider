#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/25 23:08
 @File    : crawler_job.py
 @desc    :
'''


class CrawlerJobInfo:
    '''
    爬虫工作者信息类
    '''

    def __init__(self, job_guid, spider_guid, settings):
        # 爬虫工作者全局id
        self.job_guid = job_guid
        # 爬虫工作者使用的爬虫类全局id
        self.spider_guid = spider_guid
        # 爬虫工作者使用的个性化配置
        self.crawler_job_settings = settings
        # 爬虫工作者实际拥有的爬虫工作对象
        self.crawler_job_info_status = CrawlersJobInfoStatus(job_guid)
        # 爬虫工作在爬虫类中的解析配置（url， 数据）
        self.crawler_job_info_parse_config = CrawlerJobInfoParseConfig(job_guid)
        # 爬虫工作类数据管理处理配置（存在哪，怎么存，存那些数据）
        self.crawler_job_info_pipeline_config = CrawlerJobInfoPipeLineConfig(job_guid)


class CrawlerStatus:
    '''
    爬虫对象状态
    '''
    STANDING = 'standing'
    RUNNING = 'running'
    DIE = 'die'

    def __init__(self, crawler_guid):
        self.guid = crawler_guid
        # 当前爬虫对象的运行状态
        self.state = self.STANDING

    def running(self):
        self.state = self.RUNNING

    def standing(self):
        self.state = self.STANDING

    def stop(self):
        self.state = self.DIE

    def is_running(self):
        return self.state == self.RUNNING

    def is_standing(self):
        return self.state == self.STANDING

    def is_die(self):
        return self.state == self.DIE


class CrawlersJobInfoStatus:

    '''
    爬虫工作状态类
    '''

    def __init__(self, job_guid):
        self.job_guid = job_guid
        self.crawler_guid_list = []
        self.crawler_count = 0
        self.standing_crawler_count = 0
        self.running_crawler_count = 0
        self.die_crawler_count = 0
        self.crawler_status_table = {}

    def get_all_crawler_guid(self):
        '''
        返回所有爬虫工作者guid
        :return:
        '''
        return self.crawler_guid_list

    def get_all_count(self):
        '''
        返回爬虫工作者总数
        :return:
        '''
        return self.crawler_count

    def get_running_count(self):
        '''
        返回爬虫工作者运行中数
        :return:
        '''
        return self.running_crawler_count

    def get_standing_count(self):
        '''
        返回爬虫工作者待命数
        :return:
        '''
        return self.standing_crawler_count

    def get_die_count(self):
        '''
        返回爬虫工作者死亡数
        :return:
        '''
        return self.die_crawler_count

    def init_crawler_status(self, crawler_guid):
        '''
        初始化爬虫工作者状态
        :param crawler_guid:
        :param status:
        :return:
        '''
        if self.crawler_status_table.get(crawler_guid, None) is None:
            self.crawler_status_table.update({
                crawler_guid: CrawlerStatus(crawler_guid)
            })
            self.crawler_guid_list.append(crawler_guid)
            self.crawler_count += 1
            self.standing_crawler_count += 1

    def run_crawler(self, crawler_guid):
        '''
        爬虫状态改为运行
        :param crawler_guid:
        :return:
        '''
        crawler_status = self.crawler_status_table.get(crawler_guid, None)
        if crawler_status and crawler_status.is_standing():
            self.crawler_status_table[crawler_guid].running()
            self.standing_crawler_count -= 1
            self.running_crawler_count += 1

    def pause_crawler(self, crawler_guid):
        '''
        爬虫状态改为等待中
        :param crawler_guid:
        :return:
        '''
        crawler_status = self.crawler_status_table.get(crawler_guid, None)
        if crawler_status and crawler_status.is_running():
            self.crawler_status_table[crawler_guid].standing()
            self.standing_crawler_count += 1
            self.running_crawler_count -= 1

    def stop_crawler(self, crawler_guid):
        '''
        爬虫状态改为死亡
        :param crawler_guid:
        :return:
        '''
        crawler_status = self.crawler_status_table.get(crawler_guid, None)
        if crawler_status:
            self.crawler_status_table[crawler_guid].stop()
            self.die_crawler_count += 1
            if crawler_status.is_standing():
                self.standing_crawler_count -= 1
            else:
                self.running_crawler_count -= 1


class CrawlerJobInfoParseConfig:

    def __init__(self, job_guid):
        self.job_guid = job_guid
        self.parse_table = {}


class CrawlerJobInfoPipeLineConfig:

    def __init__(self, job_guid):
        self.job_guid = job_guid
        self.pipline_table = {}
