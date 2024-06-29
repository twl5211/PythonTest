# -*- coding: utf-8 -*-
# @Time ： 2024/6/28 22:58
# @Auth ： HongBao
# @File ：stock.py
# @IDE ：PyCharm
import os.path

import akshare as ak
import pandas as pd


def get_stock_history_data(symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
    # 获取历史数据
    stock_history_data = ak.stock_zh_a_hist(symbol=symbol, period="daily", start_date=start_date, end_date=end_date, adjust="qfq")
    return stock_history_data


def get_all_stock_today_data() -> pd.DataFrame:
    stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
    return stock_zh_a_spot_em_df
    pass


if __name__ == '__main__':
    pass