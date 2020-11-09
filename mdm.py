# -*- coding = utf-8 -*-
# @Time : 2020/11/5 13:40
# @Author : Bruce Yang
# @File : mdm.py
# @Software : PyCharm

import json

import requests

headers = {'Content-Type': 'application/json'}


# mdm登录
def login():
    body = """
        {"deviceCustom":{"assetTag":"","brand":"SEUIC","fn":"X2(C)","id":"C107H0175000","imei":"863347030051305",
        "item1":"5.1.1","item2":"192.168.1.105","mac":"68:9C:5F:01:80:96","meid":"86862102008148",
        "os":"Android 5.1.1_D700C_V1.2.3","type":"CRUISE"},"pageIndex":0,"pageSize":20} 
    """
    r = requests.post('http://47.99.132.49:8080/MDMServer/device/login.action', headers=headers, data=body)
    print(r.text)
    result = json.loads(r.text)
    print(result['success'], result['data'], result['error'])
    # 添加cookie
    headers.setdefault('cookie', r.headers.get('Set-Cookie'))
    print(r.headers.get('Set-Cookie'))


def get_appstore_list():
    body = """
        {"appCustom":{},"pageIndex":0,"pageSize":10}
    """
    r = requests.post('http://47.99.132.49:8080/MDMServer/app/findAppByDevice.action', headers=headers, data=body)
    print(r.text)


if __name__ == '__main__':
    for i in range(1):
        login()
        get_appstore_list()
