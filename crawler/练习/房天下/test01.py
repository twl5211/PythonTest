# -*- coding: utf-8 -*-
# @Time ： 2024/6/29 14:49
# @Auth ： HongBao
# @File ：test01.py
# @IDE ：PyCharm

from crawler.util.my_requests import MyRequests
import csv

mr = MyRequests()
mr.request(url='https://zz.esf.fang.com/', method='GET')
xpaths = {
    '标题': ['//*[@id="kesfqbfylb_A01_01_03"]/dd[1]/h4/a/span/text()'],
    '几室几厅': ['//*[@id="kesfqbfylb_A01_01_03"]/dd[1]/p[1]/text()[1]'],
    '面积': ['//*[@id="kesfqbfylb_A01_01_03"]/dd[1]/p[1]/text()[2]'],
    '层次': ['//*[@id="kesfqbfylb_A01_01_03"]/dd[1]/p[1]/text()[3]'],
    '朝向': ['//*[@id="kesfqbfylb_A01_01_03"]/dd[1]/p[1]/text()[4]'],
    '建造时间': ['//*[@id="kesfqbfylb_A01_01_03"]/dd[1]/p[1]/text()[5]'],
    '出售人': ['//*[@id="kesfqbfylb_A01_01_03"]/dd[1]/p[1]/span/a/text()'],
    '小区': ['//*[@id="kesfqbfylb_A01_01_03"]/dd[1]/p[2]/a/text()'],
    '地址': ['//*[@id="kesfqbfylb_A01_01_03"]/dd[1]/p[2]/span/text()'],
    '交通' : ['//*[@id="kesfqbfylb_A01_01_03"]/dd[1]/p[3]/span/text()']
}
mr.get_data_by_xpath(xpaths)
print(mr.parser_data)
