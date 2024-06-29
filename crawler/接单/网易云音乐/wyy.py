# -*- coding: utf-8 -*-
# @Time ： 2024/6/29 16:35
# @Auth ： HongBao
# @File ：wyy.py
# @IDE ：PyCharm
import csv
import json
import pprint
import requests
from lxml import etree


# 请求html
def request_html(url: str):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/114.0.0.0 Safari/537.36",
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        print("爬取成功")
        return response.text
    else:
        print("爬取失败")
        return None


# 解析html
def parse_html(html: str, xpath: list):
    element = etree.HTML(html)
    parse_data = element.xpath(xpath[0])
    data = parse_data[0]
    json_data = json.loads(data)
    print("解析成功")
    return json_data
    pass


# 保存数据 json
def save_data_json(data, filename: str):
    with open(filename + '.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"保存成功, 文件名 {filename}")
    pass


# 保存数据 csv
def save_data_csv(header: list, save_data: list, filename: str):
    with open(filename + '.csv', mode='w', newline='', encoding='utf_8') as file:
        writer = csv.writer(file)
        writer.writerow(header)  # 写入头
        writer.writerows(save_data)  # 写入数据
        print(f"保存成功, 文件名 {filename}")
    pass


def start(mode):
    url = mode['url']
    filename = mode['filename']
    xpath = [
        '//*[@id="song-list-pre-data"]/text()',
    ]
    html = request_html(url)
    hot_data = parse_html(html, xpath)
    save_data = []
    header = [
        'id', '歌曲名', '专辑', '时间', '作者',
    ]

    # 数据打包保存
    for song_data in hot_data:
        # 时间处理
        total_seconds = int(song_data['duration']) / 1000
        minutes = int(total_seconds // 60)
        seconds = int(total_seconds % 60)
        time = f'{minutes}:{seconds}'
        # 作者处理
        artists = '/'.join(i['name'] for i in song_data['artists'])
        temporary = [song_data['id'],
                     song_data['name'],
                     song_data['album']['name'],
                     time,
                     artists
                     ]
        save_data.append(temporary)
    print(header)
    pprint.pprint(save_data)
    save_data_csv(header, save_data, filename)
    pass


if __name__ == '__main__':
    # 飙升榜
    soaring_List = {
        'url': 'https://music.163.com/discover/toplist?id=19723756',
        'filename': 'soaring_List'
    }
    # 新歌棒
    new_list = {
        'url': 'https://music.163.com/discover/toplist?id=3779629',
        'filename': 'new_list'
    }
    # 原创榜
    original_list = {
        'url': 'https://music.163.com/discover/toplist?id=2884035',
        'filename': 'original_list'
    }
    # 热歌榜
    hot_list = {
        'url': 'https://music.163.com/discover/toplist?id=3778678',
        'filename': 'host_list'
    }
    start(soaring_List)
    pass
