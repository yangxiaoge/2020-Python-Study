# -*- coding = utf-8 -*-
# @Time : 2020/11/6 10:41
# @Author : Bruce Yang
# @File : test_sqlite.py
# @Software : PyCharm

import sqlite3

"""
conn = sqlite3.connect("test.db")  # 打开或创建数据库
print("打开数据成功")

c = conn.cursor()  # 获取游标

sql = '''
create
table
company
(id int primary key not null,
name text not null,
age int not null,
address char(50),
salary
real);
'''

c.execute(sql)  # 执行sql语句
conn.commit()  # 提交数据库操作
conn.close()  # 关闭数据库连接

print("成功建表")
"""

"""
# 插入数据
conn = sqlite3.connect("test.db")  # 打开或创建数据库
print("打开数据成功")

c = conn.cursor()  # 获取游标

sql = '''
    insert into company
            (id,name,age,address,salary)
            values (1,'小王',18,'南京',30000);
'''

c.execute(sql)  # 执行sql语句
conn.commit()  # 提交数据库操作
conn.close()  # 关闭数据库连接

print("插入数据完毕")
"""

# 查询数据
conn = sqlite3.connect("test.db")  # 打开或创建数据库
print("打开数据成功")

c = conn.cursor()  # 获取游标

sql = '''
    select * from company;
'''

course = c.execute(sql)
for row in course:
    print(row)

conn.close()
print("查询数据完毕")