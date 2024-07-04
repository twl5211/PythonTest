# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os.path
import pprint

# useful for handling different item types with a single interface
class MyspiderPipeline:
    def spider_opened(self, spider):
        pass

    def process_item(self, item, spider):
        data = {
            '标题': item.get('标题'),
            '正文': item.get('正文'),
            '作者': item.get('作者'),
            '时间': item.get('时间'),
            '评论人数': item.get('评论人数'),
            '点赞人数': item.get('点赞人数'),
            '观看人数': item.get('观看人数'),
        }
        self.save_data(data)

    def spider_closed(self, spider):
        pass

    def save_data(self,data):
        # 文件名
        filename = 'data.csv'
        # 检查文件是否存在
        file_exists = os.path.isfile(filename)
        pprint.pprint(data)
        # 如果数据不为空，获取字典的键作为 CSV 标题行
        headers = list(data.keys())
        print(headers)
        # 打开 CSV 文件（存在时以追加模式打开，不存在时以写模式打开）
        with open(filename, 'a' if file_exists else 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            if not file_exists:
                # 写入标题行
                writer.writeheader()
            # 写入原始数据
            if data:
                writer.writerow(data)
        pass
