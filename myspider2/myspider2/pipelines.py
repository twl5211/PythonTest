# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
import pymysql
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Myspider2Pipeline:
    def __init__(self, mysql_url, mysql_db, mysql_user, mysql_password):
        self.mysql_url = mysql_url
        self.mysql_db = mysql_db
        self.mysql_user = mysql_user
        self.mysql_password = mysql_password

    @classmethod
    def from_crawler(cls, crawler):
        return cls(mysql_url=crawler.settings.get('MYSQL_URL'), mysql_db=crawler.settings.get('MYSQL_DB'),
                   mysql_user=crawler.settings.get('MYSQL_USER'), mysql_password=crawler.settings.get('MYSQL_PASSWORD'))

    def open_spider(self, spider):
        print(self.mysql_url, self.mysql_db)
        self.client = pymysql.connect(user=self.mysql_user, password=self.mysql_password, host=self.mysql_url,
                                      db=self.mysql_db)
        self.cursor = self.client.cursor()

    def process_item(self, item, spider):
        print(item['id'])
        id = int(item['id'])
        item['优惠价'] = float(item['优惠价'][1:-1])
        item['原价'] = float(item['原价'][1:-1])
        item['时间'] = datetime.strptime(item['时间'], '%Y-%m-%d').date()
        print(item['时间'])
        print(type(item['时间']))
        # SQL 插入语句，使用 %s 作为占位符
        sql = '''insert into books(id, 标题, 描述,优惠价, 原价, 评论数,评价, 作者, 时间,出版社) values (%s, %s, %s,%s, %s, %s,%s, %s, %s, %s)'''
        # 执行参数化查询
        self.cursor.execute(sql, (
        id, item['标题'], item['描述'], item['优惠价'], item['原价'], item['评论数'], item['评价'],
        item['作者'], item['时间'], item['出版社']))
        # 提交事务
        self.client.commit()
        # 从item中取出数据
        return item

    def close_spider(self, spider):
        self.client.close()
