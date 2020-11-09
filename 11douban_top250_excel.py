# -*- coding = utf-8 -*-
# @Time : 2020/11/5 19:53
# @Author : Bruce Yang
# @File : 11douban_top250_excel.py
# @Software : PyCharm

import re

import requests
from bs4 import BeautifulSoup
from xlwt import Workbook

url = "https://movie.douban.com/top250?start"

# 正则
findLinkRE = re.compile(r'<a href="(.*?)">', re.S)
findImgRE = re.compile(r'<img.*src="(.*?)"', re.S)
findTitleRE = re.compile(r'<span class="title">(.*?)</span>', re.S)
findRatingRE = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>', re.S)
findCommentRE = re.compile(r'<span>(\d*)人评价</span>')
findGeneralRE = re.compile(r'<p class="">(.*?)</p>', re.S)
findInqRE = re.compile(r'<span class="inq">(.*?)</span>', re.S)

filePath = "豆瓣Top250.xlsx"


# 获取每一页的html文本
def getTop250PageHtml(newurl):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    }
    r = requests.get(newurl, headers=headers)
    html = r.text
    return html


def getmovielist():
    datalist = []
    for index in range(0, 10):
        html = getTop250PageHtml(url + str(index * 25))
        # print(html)
        soup = BeautifulSoup(html, "html.parser")
        # 找到当前页面的25个item列表
        for item in soup.find_all('div', class_="item"):
            data = []  # 保存每部电影信息
            item = str(item)
            link = re.findall(findLinkRE, item)
            data.append(link[0])  # 电影链接

            img = re.findall(findImgRE, item)  # 图片
            data.append(img[0])

            title = re.findall(findTitleRE, item)  # 标题
            # 添加中文，外文标题
            if len(title) == 2:
                data.append(title[0])
                data.append(str(title[1]).replace("/", "").strip())
            else:
                data.append(title[0])
                data.append('')

            rating = re.findall(findRatingRE, item)  # 评分
            data.append(rating[0])
            comment = re.findall(findCommentRE, item)  # 评价数
            data.append(comment[0])
            general = re.findall(findGeneralRE, item)  # 概括
            general = str(general[0])
            general = re.sub('<br/>', "", general)
            general = general.replace("/", "")
            data.append(general.strip())
            inq = re.findall(findInqRE, item)  # 相关信息
            data.append(inq[0])

            datalist.append(data)

    return datalist


def saveExcel(filepath, datalist):
    # 创建一个工作表对象
    workbook = Workbook(encoding="utf-8")
    # sheet名
    sheet = workbook.add_sheet("豆瓣Top250")

    # 标题数据
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外国名", "评分", "评价数", "概括", "相关信息")
    for i in range(len(col)):
        sheet.write(0, i, col[i])
    # 填充数据
    # for i,item in enumerate(dataList):
    for i in range(len(datalist)):
        for j in range(len(datalist[i])):
            print("写入%d行，%d列" % (i + 1, j + 1))
            sheet.write(i + 1, j, datalist[i][j])

    workbook.save(filepath)
    print("豆瓣Top250写入Excel完成！")


if __name__ == '__main__':
    dataList = getmovielist()
    saveExcel(filePath, dataList)
