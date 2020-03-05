# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from .sql_db import SqlDb

class PaperSeniorPipeline(object):
    def process_item(self, item, spider):
        mysql_conn = SqlDb('127.0.0.1', 'test_paper', 'root', 'root')
        if item['paper_name'].find('答案') >= 0:
            path = 'D:/code_code_code试卷网/第一试卷网/doc/daan/{}.rar'.format(item['paper_name'])
            with open(path, "wb") as code:
                code.write(item['down_content'].content)
            state = int(1)
            sql = 'insert into scrapy_paper(id,subject,grade,paper_name,down,stater) ' \
                  'values (default,%s,%s,%s,%s,%s)'
            canshu = [
                item['subject'],
                item['grade'],
                item['paper_name'],
                item['down'],
                state
            ]
            num = mysql_conn.execute_sql(sql, canshu)
            if num > 0:
                print('写入成功')
            else:
                print('写入失败')
        else:
            path = 'D:/code_code_code/试卷网/第一试卷网/doc/wudaan/{}.rar'.format(item['paper_name'])
            with open(path, "wb") as code:
                code.write(item['down_content'].content)
            state = int(0)
            sql = 'insert into scrapy_paper(id,subject,grade,paper_name,down,stater) ' \
                  'values (default,%s,%s,%s,%s,%s)'
            canshu = [
                item['subject'],
                item['grade'],
                item['paper_name'],
                item['down'],
                state
            ]
            num = mysql_conn.execute_sql(sql, canshu)
            if num > 0:
                print('写入成功')
            else:
                print('写入失败')
        return item
