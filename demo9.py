# -*- coding = utf-8 -*-
# @Time : 2020/11/5 19:04
# @Author : Bruce Yang
# @File : demo9.py
# @Software : PyCharm

def printline(lines):
    print("---------------\n" * lines)


printline(3)


def add3num(a, b, c):
    return a + b + c


def average2num(a, b, c):
    return add3num(a, b, c) // 3  # //整除  /除


print(average2num(1, 2, 3))
