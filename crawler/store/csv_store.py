# -*- coding: utf-8 -*-
# @Time ： 2024/6/28 20:57
# @Auth ： HongBao
# @File ：csv_store.py
# @IDE ：PyCharm

import csv
import pprint


def save_csv_dict(header: list, save_data: dict, filename: str):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()  # 写入列标题
        writer.writerows(save_data)  # 写入数据行
    pass


def save_csv_list(header: list, save_data: list, filename: str):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)  # 写入头
        writer.writerows(save_data)  # 写入数据

def append_csv(save_data: list, filename: str):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(save_data)


def read_csv_data(filename: str) -> list:
    result = []
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            result.append(row)

    return result


if __name__ == '__main__':
    data = read_csv_data('test2.csv')
    pprint.pprint(data)
    # data = [
    #     ["Alice", 30, "New York"],
    #     ["Bob", 25, "Los Angeles"],
    #     ["Charlie", 35, "Chicago"]
    # ]
    #
    # # 头
    # header = ["Name", "Age", "City"]
    # append_csv(data, "test2.csv")
