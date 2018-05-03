#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/2 21:55
 @File    : client_run.py
 @desc    :
'''
from commonSpiders.net.client.client import Client
from commonSpiders.net.run import Run


class ClientRun(Run):

    def __init__(self, app, contexts=[]):
        if not isinstance(app, Client):
            raise Exception("服务端app必须继承Client类")
        super(ClientRun, self).__init__(app, contexts)
        for context in self.context_dict['all']:
            self.app.set_context(context.key, context.obj)
