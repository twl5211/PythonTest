import pprint
import re
import time

import pandas as pd
import requests
from lxml import etree
from sqlalchemy import Table, Column, Integer, String, MetaData, Double, Text, create_engine,Time, text,BigInteger


def get_book_data(url):
    books_data = []
    time.sleep(2)

    response = requests.get(url)
    element = etree.HTML(response.text)
    father_element = element.xpath('//*[@id="component_59"]/li')
    print(len(father_element))
    for i in father_element:
        book_data = {}
        '''//product.dangdang.com/29709583.html'''
        id = i.xpath('./p[@class="name"]/a/@href')
        bt = (i.xpath('./p[@class="name"]/a/text()'))
        ms = i.xpath('./p[@class="detail"]/text()')
        jg = i.xpath('./p[@class="price"]/span/text()')
        pl = i.xpath('./p[@class="search_star_line"]/a/text()')
        pj = i.xpath('./p[@class="search_star_line"]/span/span/@style')
        zz = i.xpath('./p[@class="search_book_author"]/span[1]/a/@title')
        sj = i.xpath('./p[@class="search_book_author"]/span[2]/text()')
        cbs = i.xpath('./p[@class="search_book_author"]/span[3]/a/text()')
        book_data['id'] = int(id[0].split('.')[-2].split('/')[-1])
        book_data['标题'] = bt[0].strip(' ') if bt else ''
        print(ms)
        book_data['描述'] = ms[0] if ms else ''
        book_data['优惠价'] = Double(jg[0] if jg else '')
        book_data['原价'] = Double(jg[1] if jg else '')
        book_data['评论数'] = int(re.search(r'\d+', pl[0]).group()) if pl else ''
        book_data['评价'] = int(re.search(r'\d+', pj[0]).group()) if pj else ''
        book_data['作者'] = '/'.join(zz) if zz else ''
        book_data['时间'] = sj[0].replace(' /', '') if sj else ''
        book_data['出版社'] = cbs[0]

        books_data.append(book_data)
    return books_data
    pass

def create_table(table_name):
    # 元数据对象
    metadata = MetaData()
    example_table = Table(
        table_name, metadata,
        Column('id', BigInteger, primary_key=True),
        Column('标题', Text),
        Column('描述', Text),
        Column('优惠价', Double),
        Column('原价', Double),
        Column('评论数', Integer),
        Column('评价', Integer),
        Column('作者', Text),
        Column('时间', Time),
        Column('出版社', Text),
    )
    # 创建数据表
    metadata.create_all(engine)
    pass
def creae_database(database_name):
    # MySQL 连接信息
    username = 'root'
    password = '123456'
    host = 'localhost'
    port = 3306

    engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}')
    # 创建数据库（如果不存在）
    # 使用连接执行 SQL 语句创建数据库
    with engine.connect() as connection:
        connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {database_name}"))
    # 连接到新创建的数据库
    engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database_name}')
    return engine
    pass
def save_date_mysql(data,table_name):
    df = pd.DataFrame(data)
    # 将 DataFrame 写入 MySQL 数据库
    df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
    print(f"DataFrame 已成功存储到表 {table_name}")
    pass

if __name__ == '__main__':

    url = 'https://search.dangdang.com/?key=%D7%F7%BC%D2%B3%F6%B0%E6%C9%E7&category_path=01.05.16.00.00.00&page_index=1'
    book_data = get_book_data(url)
    pprint.pprint(book_data)
    database_name = 'db_book'
    table_name = 'books'
    engine = creae_database(database_name)

    create_table('books')
    save_date_mysql(book_data,table_name)
    pass

