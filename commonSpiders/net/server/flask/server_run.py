#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/2 21:32
 @File    : server_run.py
 @desc    :
'''
from commonSpiders.net.run import Run
from commonSpiders.net.server.flask.server import App


class FlaskRun(Run):

    def __init__(self, app, contexts=[]):
        if not isinstance(app, App):
            raise Exception("服务端app必须继承App类")
        super(FlaskRun, self).__init__(app, contexts)
        for context in self.context_dict['all']:
            self.app.set_context(context.key, context.obj)
