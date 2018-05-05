#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/5 8:38
 @File    : crawler_run.py
 @desc    :
'''
from commonSpiders.creeper.net.context_extend import CrawlerProcessExtend
from commonSpiders.creeper.net.crawlerprocess_net import CrawlerProcessNetSocketIO
from commonSpiders.net.client.client_run import ClientRun


class CrawlerRun(ClientRun):

    def __init__(self, app, contexts=[]):
        super(CrawlerRun, self).__init__(app, contexts)
        for context in self.context_dict['all']:
            if context.key == CrawlerProcessExtend.KEY:
                setattr(context.obj.process, 'net', CrawlerProcessNetSocketIO(app))


