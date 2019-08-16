#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/7/16 15:00
# software: "PyCharm",
"""
# 正则源匹配
(.+): (.+)$

# 替换匹配
"$1": "$2",
"""

import  requests
import execjs
import json

with open('dd.js','r',encoding='utf8') as f:
        content = f.read()
        # print(content)
jss = execjs.compile(content)


v5_url = 'http://wenshu.court.gov.cn/List/List?sorttype=1&conditions=searchWord+1++%E6%B0%91%E4%BA%8B%E6%A1%88%E4%BB%B6+%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B:%E6%B0%91%E4%BA%8B%E6%A1%88%E4%BB%B6'
url = 'http://wenshu.court.gov.cn/List/ListContent'
headers = {
        'Accept': "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "wenshu.court.gov.cn",
        "Origin": "http://wenshu.court.gov.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest'",

}
v5 = requests.get(v5_url,headers=headers).cookies['vjkl5']
vl5x = jss.call('GetKey',v5,)
guid = jss.call('getguid',)

data = {
        'Param':'案件类型:刑事案件',
        'Index':'2',
        'Page':'10',
        'Order':'法院层级',
        'Direction':'asc',
        'vl5x':vl5x,
        'number':'0.03518503566290253',
        'guid':guid,

}
print(data)
headers['Cookie'] = f"vjkl5={v5};"
print(headers)
resp = requests.post(url,headers=headers,data=data)
print(resp.text)
jsons = eval(json.loads(resp.text))
RunEval = jsons[0]['RunEval']
# print(jsons[0]['RunEval'],type(jsons))
# print(resp.text)
