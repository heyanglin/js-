#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/7/12 11:15
# software: PyCharm

import  requests


url = 'https://www.che300.com/pinggu/v22c22m1234355r2019-1g45?click=homepage/&rt=1562900718120'
# url_get = 'https://www.che300.com/pinggu/v22c22m1234355r2019-1g45?click=homepage/&rt=1562912414973'
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'cookie':'spidercooskieXX12=1562915142; spidercodeCI12X3=1c49ebd8c7635a2df465ae002df8d140;'
}


session = requests.session()
resp = session.get(url,headers=headers)
print(resp.text)
# session.cookies['spidercooskieXX12']= '1562901514;path=/;'
# session.cookies['spidercodeCI12X3'] = 'b0a5e3855bd1ccbd1ef656c86480d125;path=/;'
# print(session.cookies)
# resp2 = session.get(url,headers=headers)
# print(resp2.text)

