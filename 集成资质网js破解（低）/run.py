#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/7/5 10:28
# software: PyCharm
import requests
import execjs

url = 'http://www.csi-s.org.cn/LEAP/Service/RPC/RPC.DO?callService=web&method=getzzbcompany&sid=D7375FEDD3A44B74A4006BE9D3BE733E.03&parlen=2'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Host': 'www.csi-s.org.cn',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Origin': 'http://www.csi-s.org.cn',
    "Content-Type": "application/x-www-form-urlencoded",
    'Post-Type': '1',
    'Cache-Control': 'no-cache',
    'lrqvt': '3',
    'Data-Type': '6',
    'lrq-vt': '3',
    'Accept': '*/*',
    'Referer': 'http://www.csi-s.org.cn/miitnew_webmap/miitnew_jcqycx/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}
def open_js_file(dr):
    with open('01.js','r',encoding='utf-8') as f:
        con = f.read()
    return con
js_s = open_js_file(1)
num = '1'
data = r'''["{\"qcertificatenum\":\"\",\"enterprisename\":\"\",\"qualificationlevel\":\"\",\"areacn\":\"\",\"approvaldate1\":\"\",\"approvaldate2\":\"\",\"firstcertificationdate1\":\"\",\"firstcertificationdate2\":\"\",\"keywords\":\"\",\"type\":\"1\"}","5"]'''
jsf = execjs.compile(js_s)
post_data = jsf.call('geta',data)
resp = requests.post(url,headers=headers,data='a='+post_data[1])


print('LLLLLLLLLLLLLLLL',resp.text)
