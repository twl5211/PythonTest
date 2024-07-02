# -*- coding: utf-8 -*-
# @Time ： 2024/7/1 12:23
# @Auth ： 陈楷雄
# @File ：project6.py
# @IDE ：PyCharm

import pandas as pd
import requests
from sqlalchemy import Table, Column, Integer, String, MetaData,Double,Text

from sqlalchemy import create_engine, MetaData, Column
# 爬取股票信息
def stock_zh_a_spot_em() -> pd.DataFrame:

    """
    东方财富网-沪深京 A 股-实时行情
    https://quote.eastmoney.com/center/gridlist.html#hs_a_board
    :return: 实时行情
    :rtype: pandas.DataFrame
    """
    url = "https://82.push2.eastmoney.com/api/qt/clist/get"
    params = {
        "pn": "1",
        "pz": "50000",
        "po": "1",
        "np": "1",
        "ut": "bd1d9ddb04089700cf9c27f6f7426281",
        "fltt": "2",
        "invt": "2",
        "fid": "f3",
        "fs": "m:0 t:6,m:0 t:80,m:1 t:2,m:1 t:23,m:0 t:81 s:2048",
        "fields": "f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,"
        "f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152",
        "_": "1623833739532",
    }
    r = requests.get(url, timeout=15, params=params)
    data_json = r.json()
    if not data_json["data"]["diff"]:
        return pd.DataFrame()
    temp_df = pd.DataFrame(data_json["data"]["diff"])
    temp_df.columns = [
        "_",
        "最新价",
        "涨跌幅",
        "涨跌额",
        "成交量",
        "成交额",
        "振幅",
        "换手率",
        "市盈率-动态",
        "量比",
        "5分钟涨跌",
        "代码",
        "_",
        "名称",
        "最高",
        "最低",
        "今开",
        "昨收",
        "总市值",
        "流通市值",
        "涨速",
        "市净率",
        "60日涨跌幅",
        "年初至今涨跌幅",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
    ]
    temp_df.reset_index(inplace=True)
    temp_df["index"] = temp_df.index + 1
    temp_df.rename(columns={"index": "序号"}, inplace=True)
    temp_df = temp_df[
        [
            "序号",
            "代码",
            "名称",
            "最新价",
            "涨跌幅",
            "涨跌额",
            "成交量",
            "成交额",
            "振幅",
            "最高",
            "最低",
            "今开",
            "昨收",
            "量比",
            "换手率",
            "市盈率-动态",
            "市净率",
            "总市值",
            "流通市值",
            "涨速",
            "5分钟涨跌",
            "60日涨跌幅",
            "年初至今涨跌幅",
        ]
    ]
    temp_df["最新价"] = pd.to_numeric(temp_df["最新价"], errors="coerce")
    temp_df["涨跌幅"] = pd.to_numeric(temp_df["涨跌幅"], errors="coerce")
    temp_df["涨跌额"] = pd.to_numeric(temp_df["涨跌额"], errors="coerce")
    temp_df["成交量"] = pd.to_numeric(temp_df["成交量"], errors="coerce")
    temp_df["成交额"] = pd.to_numeric(temp_df["成交额"], errors="coerce")
    temp_df["振幅"] = pd.to_numeric(temp_df["振幅"], errors="coerce")
    temp_df["最高"] = pd.to_numeric(temp_df["最高"], errors="coerce")
    temp_df["最低"] = pd.to_numeric(temp_df["最低"], errors="coerce")
    temp_df["今开"] = pd.to_numeric(temp_df["今开"], errors="coerce")
    temp_df["昨收"] = pd.to_numeric(temp_df["昨收"], errors="coerce")
    temp_df["量比"] = pd.to_numeric(temp_df["量比"], errors="coerce")
    temp_df["换手率"] = pd.to_numeric(temp_df["换手率"], errors="coerce")
    temp_df["市盈率-动态"] = pd.to_numeric(temp_df["市盈率-动态"], errors="coerce")
    temp_df["市净率"] = pd.to_numeric(temp_df["市净率"], errors="coerce")
    temp_df["总市值"] = pd.to_numeric(temp_df["总市值"], errors="coerce")
    temp_df["流通市值"] = pd.to_numeric(temp_df["流通市值"], errors="coerce")
    temp_df["涨速"] = pd.to_numeric(temp_df["涨速"], errors="coerce")
    temp_df["5分钟涨跌"] = pd.to_numeric(temp_df["5分钟涨跌"], errors="coerce")
    temp_df["60日涨跌幅"] = pd.to_numeric(temp_df["60日涨跌幅"], errors="coerce")
    temp_df["年初至今涨跌幅"] = pd.to_numeric(
        temp_df["年初至今涨跌幅"], errors="coerce"
    )
    return temp_df
# 创建引擎
def creae_engine():
    # MySQL 连接信息
    username = 'root'
    password = '123456'
    host = 'localhost'
    port = 3306
    database = 'stocks'
    engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

    return engine
    pass

# 创建数据表
def create_table(table_name):
    # 元数据对象
    metadata = MetaData()
    example_table = Table(
        table_name, metadata,
        Column('序号', Integer, primary_key=True),
        Column('代码', Text),
        Column('名称', Text),
        Column('最新价', Double),
        Column('涨跌幅', Double),
        Column('涨跌额', Double),
        Column('成交量', Double),
        Column('成交额', Double),
        Column('振幅', Double),
        Column('最高', Double),
        Column('最低', Double),
        Column('今开', Double),
        Column('昨收', Double),
        Column('量比', Double),
        Column('换手率', Double),
        Column('市盈率-动态', Double),
        Column('市净率', Double),
        Column('总市值', Double),
        Column('流通市值', Double),
        Column('涨速', Double),
        Column('5分钟涨跌', Double),
        Column('60日涨跌幅', Double),
        Column('年初至今涨跌幅', Double),
    )
    # 创建数据表
    metadata.create_all(engine)
    pass

# 保存数据到mysql
def save_date_mysql(data,table_name):
    df = pd.DataFrame(data)
    # 将 DataFrame 写入 MySQL 数据库
    df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
    print(f"DataFrame 已成功存储到表 {table_name}")

    pass

if __name__ == '__main__':
    data = stock_zh_a_spot_em()
    print(data)
    engine = creae_engine()
    table_name = 'tb_stocks'
    create_table(table_name)
    save_date_mysql(data,table_name)
    pass
