# -*- coding: utf-8 -*-
# @Time ： 2024/7/1 8:41
# @Auth ： 陈楷雄
# @File ：project3.py
# @IDE ：PyCharm
import pprint
import requests
import re
import json

def getHTMLText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'
    pass

def fillBookList(blist, html):
    rule = re.compile('window.__DATA__ =(.*?)};', re.S)
    print(html)
    print(re.findall(rule, html)[0])
    books_data = json.loads(re.findall(rule, html)[0] +"}")

    pprint.pprint(books_data['items'])
    for book in books_data['items']:
        temp = {
            '标题': book.get('title',''),
            '作者': book.get('abstract','').split('/')[0],
            '评分': book.get('rating',{}).get('value',''),
            '评论人数':book.get('rating',{}).get('count','')
        }
        if temp['标题']:
            blist.append(temp)
        pass
    pass

def printBookList(blist, num):
    print("{}".format('图书信息'))
    for i in blist:
        print("标题：{:<30} 作者：{:<30} 评分；{:<20} 评论人数；{:<20}".format(i["标题"], i['作者'],i['评分'],i['评论人数']))


def main():
    binfo = []
    url = "https://search.douban.com/book/subject_search?search_text=红楼梦&cat=1001"
    html = getHTMLText(url)

    fillBookList(binfo, html)
    printBookList(binfo, 20)
main()
