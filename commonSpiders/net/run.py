#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/5/2 21:06
 @File    : run.py
 @desc    :
'''
import threading

from commonSpiders.net.app import BaseApp
from commonSpiders.net.extend_context import ContextExtend


class Run(object):

    def __init__(self, app, contexts):
        if not isinstance(app, BaseApp):
            raise Exception('app对象需要是BaseApp类的对象或子类对象')
        self.app = app
        self.context_dict = {
            'before': [],
            'after': [],
            'all': []
        }
        self._init_context(contexts)

    def _init_context(self, contexts):
        if not isinstance(contexts, list):
            return
        self.context_dict['all'] += contexts
        for context in contexts:
            if isinstance(context, ContextExtend):
                if context.priority <= self.app.DEFAULT_PRIORITY:
                    self.context_dict['before'].append(context)
                else:
                    self.context_dict['after'].append(context)
        self.context_dict['before'] = sorted(self.context_dict['before'], key=lambda context: context.priority)
        self.context_dict['after'] = sorted(self.context_dict['after'], key=lambda context: context.priority)

    def _before_context_init(self):

        for context in self.context_dict['before']:
            self._context_classify_init(context)

    def _after_context_init(self):

        for context in self.context_dict['after']:
            self._context_classify_init(context)

    @staticmethod
    def _context_classify_init(context):
        # 异步
        if context.async:
            threading.Thread(target=context.start).start()
        # 同步
        else:
            context.start()

    def run(self):
        self._before_context_init()
        self.app.start()
        self._after_context_init()