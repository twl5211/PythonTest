import requests
import json
from lxml import etree
import logging


class MyRequests(object):

    def __init__(self):
        # 配置日志级别，默认为WARNING
        logging.basicConfig(
            level=logging.DEBUG,  # 设置日志级别
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # 日志格式
            datefmt='%Y-%m-%d %H:%M:%S',  # 时间格式
            # filename='app.log',  # 日志文件名（如不指定，则输出到控制台）
            filemode='w'  # 写入模式 'w' 或 'a' (append)
        )
        self.html = None
        self.data = None

    def request(self, method, url, **kwargs):
        global response
        if method == "GET":
            response = requests.get(url, **kwargs)
        elif method == "POST":
            response = requests.post(url, **kwargs)

        if response.status_code == 200:
            self.html = response.text

    def get_data_by_xpath(self, xpath):
        self.html = '''
                <data>
                    <item type="fruit">
                        <name>Apple</name>
                        <value>1</value>
                    </item>
                    <item type="vegetable">
                        <name>Carrot</name>
                        <value>2</value>
                    </item>
                </data>
        '''
        element = etree.HTML(self.html)
        data = element.xpath(xpath)
        logging.info("解析数据: {}".format(data))
        self.data = data
        pass

    def save_data(self):

        pass


if __name__ == '__main__':
    myRequests = MyRequests()
    myRequests.request('GET', 'https://www.baidu.com')
    myRequests.get_data_by_xpath('//item[@type="fruit"]/name/text()')
