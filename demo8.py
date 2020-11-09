# -*- coding = utf-8 -*-
# @Time : 2020/11/5 18:43
# @Author : Bruce Yang
# @File : demo8.py
# @Software : PyCharm

# 字典
info = {"name": "杨小哥", "age": "20"}

print(info["name"])
print(info["age"])

# 访问不存在的键
# print(info["gender"])  # 报错
print(info.get("gender"))  # get方法，找不到键，默认返回None
print(info.get("gender", "默认值"))

mylist = ["a", "b", "c"]
for i, x in enumerate(mylist):
    print(i, x)
