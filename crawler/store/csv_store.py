# -*- coding: utf-8 -*-
# @Time ： 2024/6/28 20:57
# @Auth ： HongBao
# @File ：csv_store.py
# @IDE ：PyCharm

import csv
import os.path
import pprint
from typing import List, Dict


def save_csv_dict(save_data: List[Dict[str, any]], filename: str):
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a' if file_exists else 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=save_data[0].keys())
        if not file_exists:
            writer.writeheader()  # 文件不存在时写入标题行
        writer.writerows(save_data)  # 追加写入数据


def save_csv_list(header: list, save_data: list, filename: str):
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a' if file_exists else 'w', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(header)  # 写入头
        writer.writerows(save_data)  # 写入数据


def read_csv_data(filename: str) -> list:
    result = []
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            result.append(row)

    return result


if __name__ == '__main__':
    data = [
        {'Age': '30', 'City': 'beijing', 'Name': 'lisi'},
        {'Age': '30', 'City': 'beijing', 'Name': 'lisi'},
        {'Age': '30', 'City': 'beijing', 'Name': 'lisi'}
    ]

    save_csv_dict(data, filename='data.csv')
