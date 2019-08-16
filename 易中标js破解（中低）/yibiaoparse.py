#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/6/19 10:57
# software: PyCharm
import  execjs
import requests
import json
import os,io

os.environ["EXECJS_RUNTIME"] = "Node"
#生成js运行文件
with open('2.js','r') as f:
    jss = f.read()
# print(jss)
fun = execjs.compile(jss)

page= """{"typeNum":0,"limit":20,"start":16,"title":""}"""

# 得到salt,data的值
salt = fun.call('r')
data = fun.call('o',page,salt)
post_data={
    'salt':salt,
    'data':data,
}
print(post_data)

#开始请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyTm8iOiJ0ZXN0X3BlcnNvbjIiLCJleHAiOjE1NjI0MDY1NTEsImlhdCI6MTU2MjMyMDE1MX0.AF9mJnJjMOhoIIiXXOXHhrlGuH0T6cgF4EwUan6W49s',
    'Origin': 'http://192.168.1.33:8888',
    'Referer': 'http://192.168.1.33:8888/',
}
url = 'http://www.ebidwin.cn/ow/bidInfo/bidResultList'
resp = requests.post(url,headers=headers,data=post_data)
# print(resp)
jsons = json.loads(resp.text)
res_salt = jsons['data']['salt']
res_data = jsons['data']['data']


#解密
result = fun.call('a',res_data,res_salt)
# print(requests.utils.unquote(result))
print(result)
