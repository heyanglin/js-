#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/7/9 18:13
# software: PyCharm
import requests
import time



headers = {
    # 'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Access-Key': '3588939af15343d491b5b470be0964c5',
    # 'Access-Token': 'tiGrHIkgQuGq6bGjfnVupg',
    # 'Connection': 'keep-alive',
    # 'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'i18next=cn-CH; Hm_lvt_343da2e65bae821f8ac4d16c0776d6f4=1565602955,1565686894,1565765130; Hm_lpvt_343da2e65bae821f8ac4d16c0776d6f4=1565768487',
    # 'Host': 'www.wuliangye.com.cn',
    # 'Referer': 'https://www.wuliangye.com.cn/zh/main/main.html',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Sec-Fetch-Site': 'same-origin',
    # 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36',
    # 'X-Requested-With': 'XMLHttpReques',
}
url = 'https://www.wuliangye.com.cn/wly_eap/cn/api/v1/publix/product/category_list'
print(url)
resp = requests.get('https://i.emaotai.cn/smartsales-trade-application/api/v1/smartsales/trade/mall/index/brand/list',headers=headers)
print(resp.text)