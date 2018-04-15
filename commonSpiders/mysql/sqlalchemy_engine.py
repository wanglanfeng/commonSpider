# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from commonSpiders.mysql.settings import db




class SqlSession(object):
    '''
    获取mysql的session
    '''

    def __init__(self):
        self.engine = create_engine("mysql+pymysql://%s:%s@%s:%s/%s" % (db['uname'], db['pwd'], db['ip'], db['port'], db['dbname']), encoding=db['encoding'], echo=db['echo'])
        self.DBSession = sessionmaker(bind=self.engine)
        self.session = self.DBSession()

    def get_sql_session(self):
        return self.session

