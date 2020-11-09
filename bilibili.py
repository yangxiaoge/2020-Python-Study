# -*- coding = utf-8 -*-
# @Time : 2020/11/6 15:50
# @Author : Bruce Yang
# @File : bilibili.py
# @Software : PyCharm
# @Description :
import requests

url = "https://www.bilibili.com/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
}


# 获取网站首页的html
def getHomeHtml():
    r = requests.get(url, headers=header)
    print(r.text)
    return r.text


if __name__ == '__main__':
    getHomeHtml()
