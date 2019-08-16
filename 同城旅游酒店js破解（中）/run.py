#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/7/11 10:46
# software: PyCharm
import requests
import time

url = 'https://www.ly.com/hotel/api/tmapi/comment/list/'
de_Url = 'https://hotels.ctrip.com/Domestic/tool/AjaxHotelCommentList.aspx?MasterHotelID=28374130&hotel=28374130&property=0&card=0&cardpos=0&NewOpenCount=0&AutoExpiredCount=0&RecordCount=296&OpenDate=&currentPage=1&orderBy=2&viewVersion=c&eleven=645570d3252e14af92b92cabd5705c409f36b760f20ca77d9161410561f4fe5c&callback=CASCtHWVWsTTaMrTc&_={}'.format(str(time.time()*100000)[:13])
headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'www.ly.com',
            'Cookie': 'qdid=-9999; 17uCNRefId=RefId=0&SEFrom=&SEKeyWords=; TicketSEInfo=RefId=0&SEFrom=&SEKeyWords=; CNSEInfo=RefId=0&tcbdkeyid=&SEFrom=&SEKeyWords=&RefUrl=; Hm_lvt_c6a93e2a75a5b1ef9fb5d4553a2226e5=1562830529; Hm_lvt_f97c1b2277f4163d4974e7b5c8aa1e96=1562830529; __tctmc=144323752.96792345; __tctmd=144323752.205791637; __tctma=144323752.1562830554771764.1562830554838.1562830554838.1562830554838.1; __tctmb=144323752.4358292040234512.1562830554838.1562830554838.1; __tctmu=144323752.0.0; __tctmz=144323752.1562830554838.1.1.utmccn=(direct)|utmcsr=(direct)|utmcmd=(none); longKey=1562830554771764; __tctrack=0; wangba=1562839554632; td_sid=MTU2MjgzMDU1NywwOTU2N2VlNTBkYzEzNDA3ZGI1MjM1ODhlNjUyNTEzZjA0ODZlNGZlMzY0NWEzODZiM2VjZjg1ODJjYjdjMTEzLDJhNWU0YTQ3MzYzYTBjMTljYjUxN2YwY2UxNmRkOWI3ZGViNTI4MDBjNDQ2NDFkYjUwNzZlZjVhOTI2ODkyYTc=; k_st=182.148.13.238|1562830557; td_did=GaJK%2FQ9FJup2cuwVZg3gTPieys%2BOZU4Zcc118G1qhGHz%2BrziWXLMFMOoigeJ10qv7i5SQncpI9TO3vyhVvjzRKK41aHjUOrKXCvMR5dDIMS2RG9FSz4jOqaWL05%2B7STbWKJSyva1RF%2BflF00DfVYoSWH4XvKmwpT68EBuIEDg1d%2BBSaPiMRT1Ro24iOJcmMvzaCijg%2FkkIs%2BcvYvc8pZPRunTl3e3Dt7gFkWS1k0zdQnvRlQhmwQEZe48fRO2Agx; t_q=1562830531061; Hm_lpvt_c6a93e2a75a5b1ef9fb5d4553a2226e5=1562830635; route=f0004d02a0ba0e34264e5ff621ad2c06; Hm_lpvt_f97c1b2277f4163d4974e7b5c8aa1e96=1562830635',
            'Referer': 'https://www.ly.com/HotelInfo-50101461.html?spm0=10002.2001.1.0.1.4.11',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
}
param = {
    'hotelid': '90634882',
    'page': '1',
    'pageSize': '10',
    'commentType':'0',
    'roomTypeId':'',
    'tripPurposeId':'',
    'RankType': '1',
    'mainTagId': '',
    'subTagId':'',
    # 'antitoken': '07aa41dd5dbd01e7244bbee9a68283d4',
    'antitoken': '96e5b9771ce914c3a940c705005f0a69',
}

resp = requests.get(url,headers=headers,params=param)
print(resp.text)