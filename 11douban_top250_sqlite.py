# -*- coding = utf-8 -*-
# @Time : 2020/11/6 10:40
# @Author : Bruce Yang
# @File : 11douban_top250_sqlite.py
# @Software : PyCharm


import re
import sqlite3

import requests
from bs4 import BeautifulSoup

url = "https://movie.douban.com/top250?start"

# 正则
findLinkRE = re.compile(r'<a href="(.*?)">', re.S)
findImgRE = re.compile(r'<img.*src="(.*?)"', re.S)
findTitleRE = re.compile(r'<span class="title">(.*?)</span>', re.S)
findRatingRE = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>', re.S)
findCommentRE = re.compile(r'<span>(\d*)人评价</span>')
findGeneralRE = re.compile(r'<p class="">(.*?)</p>', re.S)
findInqRE = re.compile(r'<span class="inq">(.*?)</span>', re.S)

dbPath = "豆瓣Top250.db"


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
                data.append(str(title[0]).strip())
                data.append(str(title[1]).replace("/", "").strip())
            else:
                data.append(str(title[0]).strip())
                data.append('')

            rating = re.findall(findRatingRE, item)  # 评分
            data.append(rating[0])
            comment = re.findall(findCommentRE, item)  # 评价数
            data.append(comment[0])
            general = re.findall(findGeneralRE, item)  # 概括
            general = str(general[0])
            general = re.sub('<br/>', "", general)
            general = general.replace("/", "")
            general = general.replace("/", "")
            data.append(general.strip())
            inq = re.findall(findInqRE, item)  # 相关信息
            data.append(inq[0])

            datalist.append(data)

    return datalist


def saveDb(datalist):
    init_db()  # 创建表
    conn = sqlite3.connect(dbPath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                # score,rating列是数字类型
                continue
            data[index] = '"' + data[index] + '"'

        sql = '''
            insert into douban (
             link,pic,ctitle,otitle,score,rating,introduction,info)
             values (%s);
        ''' % ",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()

    cur.close()
    conn.close()
    print("插入数据库完成")


def init_db():
    sql = '''
            create table douban
                (
                id integer primary key autoincrement ,
                link text,
                pic text,
                ctitle varchar,
                otitle varchar,
                score numeric,
                rating numeric,
                introduction text,
                info text
                )
        '''

    conn = sqlite3.connect(dbPath)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()
    print("创建表成功")


if __name__ == '__main__':
    dataList = getmovielist()
    saveDb(dataList)
