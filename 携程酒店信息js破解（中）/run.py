#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/7/10 17:44
# software: PyCharm
import requests
import time

url = 'https://hotels.ctrip.com/Domestic/tool/AjaxHotelCommentList.aspx?MasterHotelID=425164&hotel=425164&property=0&card=0&cardpos=0&NewOpenCount=0&AutoExpiredCount=0&RecordCount=3270&OpenDate=2014-08-01&currentPage=1&orderBy=2&viewVersion=c&eleven=2f0e4055730ff56175de8a383baafe329734b87d408a1505726165d7d9f952b3&callback=CASjpCMdtevreGPKj&_={}'.format(str(time.time()*100000)[:13])
de_Url = 'https://hotels.ctrip.com/Domestic/tool/AjaxHotelCommentList.aspx?MasterHotelID=28374130&hotel=28374130&property=0&card=0&cardpos=0&NewOpenCount=0&AutoExpiredCount=0&RecordCount=296&OpenDate=&currentPage=1&orderBy=2&viewVersion=c&eleven=645570d3252e14af92b92cabd5705c409f36b760f20ca77d9161410561f4fe5c&callback=CASCtHWVWsTTaMrTc&_={}'.format(str(time.time()*100000)[:13])
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'cookie':'_abtest_userid=d5f9a4c2-381f-4e5a-b5db-47414cfc538f; _RSG=bmaKWDJqzD1FNuelUtR849; _RDG=287c3d64e69497260001748fc0b6444be8; _RGUID=137dd133-6052-4c25-9108-6f77afa385cf; _ga=GA1.2.1353993333.1559717969; Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; IntHotelCityID=splitsplitsplit2019-06-27split2019-06-28splitsplitsplit0splitsplit; __utma=13090024.1353993333.1559717969.1561543336.1561543336.1; __utmz=13090024.1561543336.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); clientid=51482034110359288936; hoteluuid=qFUhuBD0f1QgVk5t; _HGUID=QSW%04%04QSSMVPURMT%03RUMYQPXMV%06WW%01%06%01SXU%03%06; MKT_Pagesource=PC; magicid=PccCGSQmykyvvYlRjVzM78pojl7Zq52v/uxeb69/E9PBaLSQv4yIN4/TI76Mhhde; gad_city=be2e953e1ae09d16d9cc90a550611388; Union=SID=155952&AllianceID=4897&OUID=index; _RF1=182.148.15.149; _gid=GA1.2.1209940348.1563173262; ASP.NET_SessionId=qi2wbwa4izpuvrpysjthfupd; fcerror=992218360; _zQdjfing=65b02e65b02e3365ac3365ac1336fa3a923a5fa4cc275ad04ea084; OID_ForOnlineHotel=15628405087161suyss1563173264221102003; HotelDomesticVisitedHotels1=425164=0,0,4.2,3270,/hotel/53000/52741/941abc93388f496cb660691cf8b48bde.jpg,&28374130=0,0,4.7,298,/200512000000siebvAC31.jpg,; MjAxNS8wNi8yOSAgSE9URUwgIERFQlVH=OceanBall; _gat=1; _jzqco=%7C%7C%7C%7C1563173262241%7C1.1721266199.1562840202692.1563174835172.1563174847011.1563174835172.1563174847011.undefined.0.0.10.10; __zpspc=9.3.1563173262.1563174847.7%234%7C%7C%7C%7C%7C%23; _bfi=p1%3D102003%26p2%3D102003%26v1%3D21%26v2%3D20; appFloatCnt=8; hoteluuidkeys=nTBJpFKfmeL3EBdJbYZYSkY6fEGYzYH0e5aEFnjMfWgYkYB1WFsjsMvQde1Y8YTbwdhw8ZitcjZYHYa4jBbWF7Ig1jAYkY5SKBSJztyqAjAzvcqeGpYXNjBSynY5YFOv3cRL4Y0zrApIL3egQibqY1YLYTY5YgXv6neU1YdUizlYqYNY8YnYMnEHtKoqw1QiqtRtAj1rogYTBJAhy6rl9YdoWDZvOSx8OedhYqgx9Qx7bY0biDFwBtjQcEGPJFtW0BjzrBLJmbi40w6GvL0RmOj7GYtNjLrtlyQDiFtw8GR30EZsjs3xdoxUaEb9E4HE1gWPNe3Xwg9ELmjTZedOishY0MrD8eU9eT6xX9idLic9xsMWfNj8peLPw4UKHzw4SiSbRXQjDaeO3EBTyUDvXmi4AEf5yG9vqlKk3EODKZMwQsiN8RsgjBrl1YgLJhLyArs1j5Qe4QjcpKdcj5kwGZxfcxQoxMqxOBEkZEHmEXPW3qeoBwSnE7bjbkehPiStYQHrPTEd9y40vq3iofEF3yscvOTKdLWb0E4Qj6oefbxkmjLr6cEcXWH8ebcjZcYUcjcQxBdxlQxmtx4ZEBGE9kEqdWU8e40wGnEgBj9BehDi7SYSfrGNefgenXYlXEshwgMW84iBBKDOEpmEADETSWhkeAXwH5EkSjpHezPi3BY58rGZeToeaLE5bYh1E7Ow4BWDfihYbYGnYkhiohinUiPUjSYqY48vlpYUly9oEDTwOgj3fyAhicYQYn1RBbJ4ZwXHi0tR5GyBTEnBjgkwTmyHqE8SinGvlY0YZ0JZFyAMymOKFSvD6izSJ7nWFAvLFRUAiz4xLajqDrHmJ07; _bfa=1.1562840508716.1suyss.1.1562900434544.1563173255897.4.22; _bfs=1.9; utc=1563146068167; htltmp=be8bae88e6716; htlstmp=3dcdfacd7d00cdcdfafad13dfa',
    'content-type': 'application/x-www-form-urlencoded; charset=utf-8'
}
param = {
    'MasterHotelID': '28374130',
    'hotel': '28374130',
    'property': '0',
    'card': '0',
    'cardpos': '0',
    'NewOpenCount': '0',
    'AutoExpiredCount': '0',
    'RecordCount': '296',
    'OpenDate': '',
    'currentPage': '1',
    'orderBy': '2',
    'viewVersion': 'c',
    'eleven': '645570d3252e14af92b92cabd5705c409f36b760f20ca77d9161410561f4fe5c',
    'callback': 'CASCtHWVWsTTaMrTc',
    '_': str(time.time()*100000)[:13]
}

resp = requests.get(url,headers=headers)
print(resp.text)


