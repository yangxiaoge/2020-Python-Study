# -*- coding = utf-8 -*-
# @Time : 2020/11/5 14:24
# @Author : Bruce Yang
# @File : demo3.py
# @Software : PyCharm

'''
if True:
    print("true")
else:
    print("false")

for i in range(-20, -10, 2):
    print(i)
'''

'''
a = ["aa", "bb", "cc"]
for item in a:
    print(a.index(item), item)
'''

# 1-100求和

a = 100
sum = 0
while 0 <= a <= 100:
    sum += a
    a -= 1
print("1到100的和为：%d" % sum)
