# -*- coding = utf-8 -*-
# @Time : 2020/11/5 16:54
# @Author : Bruce Yang
# @File : demo6.py
# @Software : PyCharm
import random

office = [[], [], []]
names = ["A", "B", "C", "D", "R", "F", "G", "H"]

for name in names:
    index = random.randint(0, 2)
    office[index].append(name)
print(office)

products = [["iphone 12", 11999], ["macpro", 14600], ["小米10Pro", 6999], ["Coffee", 10]]

print("-" * 6 + " 商品列表 " + "-" * 6)
index = 0
for pro in products:
    print("%d  %s  %d" % (index, pro[0], pro[1]))
    index += 1

buy = []
while True:
    inputStr = input("请输入商品编号，选购完成后输入q可以结算")
    if inputStr == "q":
        break
    else:
        try:
            proIndex = int(inputStr)
            if 0 <= proIndex <= len(products) - 1:
                pro = products[proIndex]
                buy.append(pro)
                print("商品：%s 价格：%d 成功加入购物车" % (pro[0], pro[1]))
            else:
                print("商品编号%d不存在，请重新输入编号" % proIndex)
        except ValueError:
            print("错误，请输入商品数字编号！！！")

if len(buy) > 0:
    print("-" * 6 + " 您选购的商品如下 " + "-" * 6)
    count = 0
    for pro in buy:
        print("%s  %d" % (pro[0], pro[1]))
        count += pro[1]
    print("商品总价 %d" % count)
else:
    print("您未选购任何商品！")
