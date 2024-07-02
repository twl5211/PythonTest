# -*- coding: utf-8 -*-
# @Time ： 2024/7/1 8:17
# @Auth ： HongBao
# @File ：project1.py
# @IDE ：PyCharm
import requests

# 输入你要查看的域名
domain = 'www.douban.com'

# 构造robots.txt文件的URL
robots_url = f'https://{domain}/robots.txt'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36",
}
# 发送GET请求
response = requests.get(robots_url,headers=headers)
# 检查响应状态码
if response.status_code == 200:
    print("robots.txt 内容：")
    print(response.text)
else:
    print(f"无法访问 robots.txt 文件，状态码: {response.status_code}")
