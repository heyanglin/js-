#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/7/10 10:28
# software: PyCharm
import requests
import execjs

with open('js.js','r',encoding='utf-8') as f :
    text = f.read()
jss = execjs.compile(text)
i4m = r"""{"csrf_token":"","limit":"20","offset":"0","rid":"R_SO_4_28310080","total":"false"}"""
li = jss.call('dd',i4m,)

headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
}
url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_28310080?csrf_token='
data = {
    'params': li[0],
    'encSecKey':li[1],
}
resp = requests.post(url,headers=headers,data=data)
print(resp.text)