# -*- coding: utf-8 -*-
# @Time ： 2024/7/1 14:54
# @Auth ： HongBao
# @File ：test03.py
# @IDE ：PyCharm

from sqlalchemy import Table, Column, Integer, String, MetaData, Double, Text, create_engine, Time, text, Date

from datetime import datetime

from sqlalchemy.ext.asyncio import session

DATABASE_URL = 'mysql+pymysql://root:123456@localhost/db_book'
Base = declarative_base()
engine = create_engine(DATABASE_URL)
class Book(Base):
    __tablename__ = 'table_books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    published_date = Column(Date)
    isbn = Column(String(20), unique=True)

book_data = {
    'title': "Example Book",
    'author': "Author Name",
    'published_date': '2023-07-27',
    'isbn': "1234567890"
}

Base.metadata.create_all(engine)
# 将字符串转换成日期对象
book_data['published_date'] = datetime.strptime(book_data['published_date'], '%Y-%m-%d').date()

# 将字典数据转换成 ORM 对象并添加到会话
new_book = Book(**book_data)
session.add(new_book)
session.commit()

# 查询数据以验证插入
books = session.query(Book).all()
for book in books:
    print(f"{book.title} by {book.author}")

# 关闭会话
session.close()
