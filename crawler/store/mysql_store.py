# -*- coding: utf-8 -*-
# @Time ： 2024/7/2 16:41
# @Auth ： HongBao
# @File ：mysql_store.py
# @IDE ：PyCharm

import pymysql
from crawler.config import base_config
class MysqlStore:

    def __init__(self):
        self.db = None
        self.mysql_url = base_config.MYSQL_URL
        self.mysql_db = base_config.MYSQL_DB
        self.mysql_user = base_config.MYSQL_USER
        self.mysql_password = base_config.MYSQL_PASSWORD

    def connect(self):
        self.db = pymysql.connect(host=self.mysql_url,
                             user=self.mysql_user,
                             password=self.mysql_password,
                             database=self.mysql_db)
        pass

    def disconnect(self):
        self.db.close()
        pass