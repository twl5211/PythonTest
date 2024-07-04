# -*- coding: utf-8 -*-
# @Time ： 2024/7/2 16:41
# @Auth ： HongBao
# @File ：mysql_store.py
# @IDE ：PyCharm
import logging
from typing import List, Dict

import pymysql
from crawler.config import base_config


class MySQLStore:

    def __init__(self):
        self.connection = None
        self.cursor = None
        self.mysql_url = base_config.MYSQL_URL
        self.mysql_db = base_config.MYSQL_DB
        self.mysql_user = base_config.MYSQL_USER
        self.mysql_password = base_config.MYSQL_PASSWORD

    def connect(self):
        self.connection = pymysql.connect(host=self.mysql_url,
                                  user=self.mysql_user,
                                  password=self.mysql_password,
                                  database=self.mysql_db)
        self.cursor = self.connection.cursor()
        pass

    def table_exists(self, table_name):
        self.cursor.execute(f"SHOW TABLES LIKE '{table_name}';")
        result = self.cursor.fetchone()
        return result is not None

    def create_table(self, create_table_sql: str):
        self.cursor.execute(create_table_sql)
        pass

    def sava_data_to_db(self, table_name, data: List[Dict[str, any]]):
        table_exists = self.table_exists(table_name)
        if not table_exists:
            logging.error(f" 数据表 {table_name} 不存在")
            raise Exception
            pass
        placeholders = ', '.join(['%s'] * len(data[0]))
        columns = ', '.join(data[0].keys())
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        for i in data:
            self.cursor.execute(sql, list(i.values()))
        self.connection.commit()
        pass

    def disconnect(self):
        self.connection.close()
        pass
