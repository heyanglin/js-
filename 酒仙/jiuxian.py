import requests
import re
import execjs

headers = {
    'Host': 'www.jiuxian.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'
}

session = requests.Session()
resp1 = session.get('http://www.jiuxian.com/goods-8230.html',headers=headers).text
with open('jx.js','r',encoding='utf8') as f:
    jss = f.read()
    # print(jss)
jsss = execjs.compile(jss)
cookie = jsss.call('getcookie',resp1)
# print(cookie)
session.cookies[cookie.split('=')[0]] = cookie.split('=')[1]
resp2 = session.get('http://www.jiuxian.com/goods-8752.html',headers=headers).text
print(resp2)


