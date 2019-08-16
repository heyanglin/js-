#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/7/10 14:31
# software: PyCharm

import  requests
import json
import execjs
word = 'run'
url = 'https://fanyi.baidu.com/v2transapi'
headers = {
        # 'content-type': 'application/x-www-form-urlencoded; charset=UTF8',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        # 'x-requested-with': 'XMLHttpRequest',
        # 'origin': 'https://fanyi.baidu.com',
        # 'referer': 'https://fanyi.baidu.com/?aldtype=16047',
        # ':authority': 'fanyi.baidu.com',
        # ':method': 'POST',
        # ':path': '/v2transapi',
        # ':scheme': 'https',
        'cookie': 'BAIDUID=CE2258E3133F74560F320A2C2C2C9F52:FG=1; BIDUPSID=CE2258E3133F74560F320A2C2C2C9F52; PSTM=1551678445; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1557999414; H_WISE_SIDS=131798_126125_127815_114553_132246_130499_130409_114745_130510_131964_130163_120154_132271_132378_132325_132212_131517_132260_118895_118871_131401_118850_118818_118789_132211_131651_131575_131535_131534_131530_130222_131293_131871_131390_129565_107312_131796_131392_130128_131874_130569_131194_117329_130348_117435_131241_129647_131247_127026_131435_131687_131036_131906_132090_131046_132203_130826_131423_110085_127969_131506_123290_132350_127316_127417_131831_131265_131263_128602_131975_100457; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; locale=zh; delPer=0; H_PS_PSSID=1433_21093_29237_28519_29099_28830_29220_26350; PSINO=3; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1562634630,1562653631,1562728003,1562740193; yjs_js_security_passport=75b9c3b5c934e2298874de1601d0f53ed0190736_1562741311_js; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1562743963; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D',
        # 'accept': '*/*',
        # 'accept-encoding': 'gzip, deflate, br',
        # 'accept-language': 'zh-CN,zh;q=0.9'
}
with open('1.js','r',encoding='gbk') as f:
    te = f.read()
jss = execjs.compile(te)
sign = jss.call('e',word)
data = {
        'from': 'en',
        'to': 'zh',
        'query': word,
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': sign,
        'token': '5e6aae0c2d02624371df513003cfdddc',

}

resp = requests.post(url,headers=headers,data=data)
resp.encoding = 'utf-8'
text = json.loads(resp.text)
print(text['trans_result'])