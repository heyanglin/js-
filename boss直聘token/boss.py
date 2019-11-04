
"""
@date: 2019/10/11 上午11:44 
@name: boss.py
@author：heyanglin
@desc
"""

import requests
import re

import execjs

with open('boss.js') as f:
    jss = f.read()


headers = {
    'User-Agent': "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
}

def get_token(ts, seed,js):
    js_f = execjs.compile(jss)
    token = js_f.call('get_token', ts, seed,js)
    return token

for i in range(100):
    resp = requests.get(
        'https://www.zhipin.com/job_detail/30d92ad98a4acd891XB529u5FFM~.html?ka=search_list_1', headers=headers,
    )
    print(resp.url)
    if 'boss直聘' not in resp.text:
        ts = re.findall('ts=(.*?)&', resp.url)[0]
        seed = re.findall('seed=(.*?)&', resp.url)[0]
        seed = requests.utils.unquote(seed)
        js = requests.get('https://www.zhipin.com/web/common/security-js/{}.js'.format(re.findall('name=(.*?)&', resp.url)[0]),headers=headers,
                          ).text
        token = get_token(ts,seed,js)
        print(token)
        headers1 = {
            'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            'cookie':'__zp_stoken__={}'.format(requests.utils.quote(token))

        }
        resp2 = requests.get(
            'https://www.zhipin.com/job_detail/30d92ad98a4acd891XB529u5FFM~.html?ka=search_list_1', headers=headers1,
        )
        if 'BOSS直聘' in resp2.text:
            print(resp2.text)
        else:
            print('失败')
    else:
        print('直接访问')
