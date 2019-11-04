"""
@date: 2019/9/24 下午8:37
@name: zhilian.py
@author：gongtengfei
@desc
"""
import requests
import re
import execjs

def test():
    resp = requests.get(
                        'https://jobs.zhaopin.com/CC376764819J90250443000.html',
                        )
    arg1 = re.findall("var arg1='(.*?)';",resp.text)
    if arg1:
        with open('zhilian.js') as f:
            jss = f.read()
        jsss = execjs.compile(jss)
        arg2 = jsss.call('arg2',arg1[0])
        headers = {
            'cookie':'acw_sc__v2='+arg2,
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        resp2 = requests.get(
                                'https://jobs.zhaopin.com/CC376764819J90250443000.html',
                                headers=headers,
                             )
        # print(resp2.text)
        print(arg1)
        print(arg2)
        return  resp2
    else:
        return  resp



count = 0
for i in range(50):
    while True:
        resp = test()
        if '智联招聘' in resp.text:
            print('结束',count)
            # print(resp.text)
            break
        count +=1
        print(count)

