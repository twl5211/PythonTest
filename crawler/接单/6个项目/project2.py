# -*- coding: utf-8 -*-
# @Time ： 2024/7/1 8:23
# @Auth ： 陈楷雄
# @File ：project2.py
# @IDE ：PyCharm

# 导入请求库
import urllib.request
# 需要访问的网址
url = 'https://www.baidu.com'

# 创建 Request 对象，并添加请求头
request = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
})

# 发送请求
response = urllib.request.urlopen(request)
# 得到请求的html
html = response.read()
# 通过utf-8解码
content = html.decode('utf-8')
# 打印html
print(content)
