# -*- coding = utf-8 -*-
# @Time : 2020/11/5 18:30
# @Author : Bruce Yang
# @File : demo7.py
# @Software : PyCharm

"""
tup1 = ()
print(type(tup1))
tup1 = (50)
print(type(tup1))
tup1 = (50,)
print(type(tup1))
tup1 = (50,60,70)
print(type(tup1))
"""
tuple1 = ("abc", "def", 2020, 2020)
print(tuple1[0])
print(tuple1[-1])  # -1，从末尾反向下标取值
print(tuple1[1:3])  # 左闭右开
print(tuple1.count(2020))
