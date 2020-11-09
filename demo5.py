# -*- coding = utf-8 -*-
# @Time : 2020/11/5 15:59
# @Author : Bruce Yang
# @File : demo5.py
# @Software : PyCharm

namelist = ["小王", "小李", "小杨", 666, 0xffff]
print(namelist[0])
# 增加一个
namelist.append("小海")
for name in namelist:
    print(name)

a = [1, 2]
b = [3, 4]
a.append(b)  # 追加
print(a)
del a[2]  # 删除下标2处的元素
a.extend(b)  # 拆散追加
print(a)

sss = ["bb", "aa", "cc"]
sss.sort()
print(sss)



