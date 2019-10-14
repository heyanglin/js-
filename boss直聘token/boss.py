
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
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:69.0) Gecko/20100101 Firefox/69.0',
    # 'cookie':'__zp_stoken__={}'.format(requests.utils.quote(token))

}

def get_token(ts, seed):
    js_f = execjs.compile(jss)
    token = js_f.call('get_token', ts, seed)
    return token


# print(resp.text)
for i in range(50):
    resp = requests.get(
        'https://www.zhipin.com/job_detail/72c651d2edca0cca03d42Nq_EFM~.html?ka=search_list_1', headers=headers,
        proxies={'http': 'https://HC5585Q01M52728P:393427EE17B0B9BF@http-pro.abuyun.com:9010'}
    )
    print(resp.url)
    if 'boss直聘' not in resp.text:
        ts = re.findall('ts=(.*?)&', resp.url)[0]
        seed = re.findall('seed=(.*?)&', resp.url)[0]
        seed = requests.utils.unquote(seed)
        token = get_token(ts,seed)
        headers1 = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:69.0) Gecko/20100101 Firefox/69.0',
            'cookie':'__zp_stoken__={}'.format(requests.utils.quote(token))

        }
        resp2 = requests.get(
            'https://www.zhipin.com/job_detail/72c651d2edca0cca03d42Nq_EFM~.html?ka=search_list_1', headers=headers1,
            proxies={'http': 'https://HC5585Q01M52728P:393427EE17B0B9BF@http-pro.abuyun.com:9010'}
        )
        if 'BOSS直聘' in resp2.text:
            print(resp2.text)
        else:
            print('失败')
    else:
        print('直接访问')
