#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/6/13 17:36
# software: PyCharm

import requests
import execjs



with open('tudi.js','r') as f:
    js = f.read()
js = execjs.compile(js)
url = js.call('YunSuoAutoJump')
sseion = requests.session()
#第一次请求
resp1 = sseion.get('http://www.landchina.com/default.aspx?tabid=226')
#第二次请求
resp2 = sseion.get(url)
#第三次请求
resp3 = sseion.get('http://www.landchina.com/default.aspx?tabid=226')
# print(resp3.text)
