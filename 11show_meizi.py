# -*- coding = utf-8 -*-
# @Time : 2020/11/6 13:52
# @Author : Bruce Yang
# @File : 11show_meizi.py
# @Software : PyCharm
import os
import re

import requests
from bs4 import BeautifulSoup

url = "https://www.showmeizi.com"
folder = "meizi"
findTitle = re.compile(r'title="(.*?)"', re.S)
findHref = re.compile(r'href="(.*?)"', re.S)
findDate = re.compile(r'<b class="b1">(.*?)</b>', re.S)
findViews = re.compile(r'<b class="b2">(\d*)</b>', re.S)
findSrc = re.compile(r'lazysrc="(.*?)"', re.S)

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
}


# 获取网站首页的html
def getHomeHtml():
    r = requests.get(url, headers=header)
    # print(r.text)
    return r.text


def getHomeMeiziImg():
    html = getHomeHtml()
    soup = BeautifulSoup(html, "html.parser")

    for line in soup.find_all("ul", class_="twoline"):
        # print(line)
        for item in line:
            # print(item)
            item = str(item)
            if len(item.strip()) == 0:
                # 过滤空item
                continue
            title = re.findall(findTitle, item)[0]
            # print(title)
            href = re.findall(findHref, item)[0]
            # print(url + href)
            date = re.findall(findDate, item)[0]
            # print(date)
            views = re.findall(findViews, item)[0]
            # print(views)
            src = re.findall(findSrc, item)[0]
            # print(url + src)
            # 下载图片
            # download_img(folder, src)

            # 获取详情页图片
            getDetailHtml(url + href)


def getDetailHtml(detail_url):
    r = requests.get(detail_url, headers=header)
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all("div", class_="swiper-slide"):
        item = str(item)
        img = re.findall(re.compile(r'data-src="(.*?)"', re.S), item)[0]
        print(img)
        # 下载图片
        download_img(folder, img)


def download_img(folder_path, src):
    if not os.path.exists(folder_path):
        print("文件夹不存在, 创建文件夹.")
        os.makedirs(folder_path)
    print("尝试下载图片: {}".format(src))
    filename = src.split('/')[-1]
    filepath = folder_path + '/' + filename
    file_url = url + src
    print(file_url)
    if os.path.exists(filepath):
        print("文件已存在，跳过")
    else:
        try:
            r = requests.get(file_url, stream=True, headers=header)
            with open(filepath, "wb") as file:
                for chunk in r.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        file.write(chunk)
        except Exception as e:
            print("异常啦：" + e)

    print("下载完成啦")


if __name__ == '__main__':
    getHomeMeiziImg()
