"""
@date: 2019/10/16 下午4:31 
@name: toutiao.py
@author：heyanglin
@desc
"""
import requests
import execjs
import time
import json

headers = {
    'User-Agent': '5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko',
    'cookie': 'tt_webid=6748729577482929677'
}
url = 'https://www.toutiao.com/api/pc/feed/?max_behot_time={}&category=__all__&utm_source=toutiao&widen=1&tadrequire=true&as={}&cp={}&_signature={}'
with open('toutiao.js') as f:
    jss = f.read()


ex = execjs.compile(jss)
def req(t,url='https://www.toutiao.com/api/pc/feed/?max_behot_time={}&category=__all__&utm_source=toutiao&widen=1&tadrequire=true&as={}&cp={}&_signature={}'):
    di = ex.call('o', )
    sa = di.get('as')
    cp = di.get('cp')
    _signature = ex.call('sign', t)
    print(_signature)
    get_url = url.format(t, sa, cp, _signature)
    print(get_url)
    resp = requests.get(get_url, headers=headers)
    dicts = json.loads(resp.text)
    print(dicts)
    abstract = dicts.get('data')
    if abstract:
        for i in abstract:
            print(i.get("abstract"))
            print('>>>')
        return dicts.get('next').get('max_behot_time')
    else:
        print('meiyou')

#t=req(0,url='https://m.toutiao.com/list/?min_behot_time={}&tag=__all__&ac=wap&count=20&format=json_raw&as={}&cp={}&_signature={}')
hh = req(1572075942)
