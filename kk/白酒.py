#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/7/18 16:33
# software: PyCharm

'''
1.登录需要翻页
2.
3.滑块验证
8066da81b1718e687c688e9e9a393d0d

'''

import requests
import parsel
import redis
import fake_useragent


class tianMao(object):
    ua = fake_useragent.UserAgent()

    def  __init__(self):
        self.list_url = 'https://list.tmall.com/search_product.htm?q=%B0%D7%BE%C6'
        # self.list_url = 'https://list.tmall.com/search_product.htm?&s=0&q=%B0%D7%BE%C6'
        self.headers = {
            'user-agent': self.ua.random,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': 'lid=wjheart00; cna=Ne0EFSxtwlQCAbaUDpad/R8w; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; x=__ll%3D-1%26_ato%3D0; hng=CN%7Czh-CN%7CCNY%7C156; enc=WgTj1jMrtT5wkquRIdbe1b5TSmmNi0yj7W9%2BdaO71l8qy6wblg3eLn8McjMKNQCtpc7QX1hAD3zRkMhggF0hvA%3D%3D; cq=ccp%3D1; _uab_collina=156344527743420655277029; _med=dw:2399.9999642372136&dh:1349.9999798834326&pw:1920&ph:1080&ist:0; _m_h5_tk=f16540646e29ba76faa00fee0936e940_1563526158321; _m_h5_tk_enc=4d139935aa8b132f55da4aed8807e5e4; t=de28d182f651db63be2e9ef73a90c3ef; tracknick=wjheart00; _tb_token_=7ba9b43fe7300; cookie2=1d0390778565c0d78a81664ea185c86d; tt=tmall-main; res=scroll%3A2296*5510-client%3A2296*1110-offset%3A2296*5510-screen%3A1920*1080; pnm_cku822=098%23E1hv%2FQvUvbpvUvCkvvvvvjiPRFMZAjDvPF5Zzj3mPmP9tjEhn2SpgjDCRszWljrnRphvCvvvvvvPvpvhvv2MMqyCvm9vvvmZphvvWvvv3UXvpCCXvvm2phCvhRvvvUnvphvppvvv9AavpvsLuphvmvvv92XEw1UOkphvC99vvOCzp9yCvhQhO%2BWvCsqwTWsyVt3%2BVd0DyOvO5onmsX7v1C6tExjxAfev%2Bul68NoxfwoKHAnb3wynSL8Avc79D7zZdiB%2Bm7zOaNoAdcpiJXxrz8g7vphvC9vhvvCvp8wCvvpvvUmm; isg=BN3d7-aRXE38qzntNdNdr2le7LkXUhOIa-J9OZ-iaDT0Vv-IZkuzHeMEgAp1likE; l=cBLD6x8gvlHbmGPyBOCZCuI8UuQ9MIRVguPRwdYki_5QB1dFpk_OkqNyWep6cjWFG-8p4XOjjVJTAeoU-yWjihJWuYP3VmC..'
}
        self.commodity_page_list = []
        self.commodity_url_list = []
        self.commodity_detail_list=[]
        self.chaoshi_url_list=[]

    def get_ip(self):
        conn = redis.Redis(host='192.168.1.62',port='6379',db=1)
        ip = conn.zrange('proxy:ips', -1, -1)[0]
        return ip


    def get_list_data(self):    #获取商品列表页数据
        session =requests.session()
        ip = self.get_ip().decode().replace('http','https')
        resp = session.get(self.list_url, headers=self.headers,proxies={'https': ip})
        if '亲，小二正忙，滑动一下马上回来' in resp.text:
            print('滑动页面')
            resp2 =session.get('https://cf.aliyun.com/nocaptcha/analyze.jsonp?a=X82Y__2ce9475aeaf38ee29777ad7449d379c2&t=8ac57031e7e607670982bd5e7d7ff926&n=118%23ZVWZzajIQYPK2ZX4%2Bg27eZZTZe7h4ewoZZ4YJsiTzfQZZZZZUTiWtmgMle4oEeZVZZVCZOiTzeWzZgCucHZYy4mK5eChXHRYuZ2ZZwqh4XGizZZZXTNVzeDSI46eVHCCZZ2uZYqhzHRZZgCZXoqYZH2zZZChXHhbZZ2uZYqhzFWaGeHZV68ZGehtYV2Z9QPl%2FBlZEHB6zDAZ%2FY2gsm5e%2FFLfJT2yLi3JC0COCCg7ZZe3L4PXZZxqtgWA%2BCmbZYiP%2B7hH7edP2ncpjCL2WnbqlexX2L3ZALwOrqM0pQvT1XGoiqDRQa%2FSOR5Y6aRvIRi3WCeIoMUV%2B0CjQYS5IdOew5WqF3DK0Wtw%2FoHEaQJ9olHCrTwIGPbTMCC%2FiLqeFORr7qmlEOTwS8JX4lwWjF%2FufHAjjaPIjd1Nl%2FMmeCyly5DxN%2BBCEB5XUbHHWOoDlfZKHBr64WCalyOie2ajlOL63HSRRFtokDGcLqxQeKee8Nav1DjAFnOrLkPatO1DhnIerBX%2BtA2M%2FvwGpCFrg2mgWbdNw3jVNJtsgZNSCMrcNe0XCAVWCvxDQGr5%2FOy3eUwD%2F7fZrazeCPexMmVNxYqQFJ1WoDvElCb%2BGhFyw296QbSmixEcZNIrz3ikeotSsMC7G56LYLgeaOOPDgc0Bit0efBeWDQNaiSGGULaXikFI7OvGO5V3Pc9NW1wGLb7NbtJdckj4z0m1OXfNCkMkidOViG15wMjoNSoNvCJGCSeLd05EOxtK5grEIR9f4VESHWzM9rtWdO35z1qEEvruoNXN%2B%2F2wz9fG6dzag5ZjyHubpqPv%2FX2UjaW407BurWWWrWIV4d5eqcH5J2Aj6VkMmUoZ3hXQ3IV%2FHtx2tAslKSzTEoPllqulW4hGBiKimsjLVQLqXc%2BOzRFFxLHkaP1Ruppa1cr9tr%2FptVFWmL4UcoylEvf3h6tiAmt7U76%2FmJrwzQzL1j2fMDtnSNbJcvR2SOotCBMp%2F7P4v5CfZOouHKd3%2Bu8qdf7VIZCcfnSrQu0yOo0kkSmqwIMl5TLstIMenHUZBPodAM5UdqEmQmBUmiFuhr2H4TBa1MixQYc48P8UlswJ9NTiNzaOCCb%2Bwv0F1rXLLd1MDbTcvOSohmb4OHJrWewiUeoimkM4kUEkDGSsmMx8gh92CREmXRwxKEaUbETeVO7%2FcrSFdqLxrkyTrfweoOJVj4HgIXio1Q00kFFXRdxujqf%2FqipWeI2R%2Fv2KhLGYfqJz9GknbN4kxe5uCFSlvdlH5HS4McbpjIN9A6SErdK0Bln51O4keTwp8MR4Cpo69Ja&p=%7B%22ncSessionID%22%3A%225e701ed93767%22%2C%22umidToken%22%3A%22T5E99A4C405E5115E20F363E2461D25BC975CBF503690513763925FF501%22%7D&scene=register&asyn=0&lang=cn&v=972&callback=jsonp_017202294777921368')
            print(resp2.text)
            resp3 = session.get('https://list.tmall.com/search_product.htm?&s=60&q=%B0%D7%BE%C6')
            print(resp3.text)
            return
        elif "正在登录...\">登 录" in resp.text:

            print('登录页面')
            print(resp.text)
        html = parsel.Selector(resp.text)
        print('第{}页'.format(html.xpath('//b[@class="ui-page-cur"]/text()').extract_first()))
        self.commodity_page_list.append(resp.text)


    def parse_list(self):     #解析商品列表页获取id
        html = self.commodity_page_list[0]
        html = parsel.Selector(html)
        a_list = html.xpath('//div[@class="view grid-nosku "]/div')
        for a in a_list:
            url_A = a.xpath('./div/p[2]/a/@href').extract_first()
            url = 'https://chaoshi.'+ url_A[2:]
            type = a.xpath('./div/div[2]/a/text()').extract_first().strip()
            if '天猫超市' not in type:
                self.commodity_url_list.append(url)
            else:
                self.chaoshi_url_list.append(url)


    def get_commodity_detail(self,detail_url):   #获取商品详情信息

        resp2 = requests.get(detail_url,headers = self.headers)

        #页面解析

        html = parsel.Selector(resp2.text)
        title = html.xpath('//div[@class="tb-detail-hd"]/h1/text()').extract_first().strip()
        row = html.xpath('//ul[@id="J_AttrUL"]/li')
        desc = []
        for li in row:
            infor = li.xpath('./text()').extract_first().replace('\xa0','').strip()
            desc.append(infor)
        item = {
            'title':title,
            'desc':desc
        }
        print(item)

    def main(self):
        self.get_list_data()
        self.parse_list()
        for url in self.commodity_url_list:
            self.get_commodity_detail(url)

#99d0f5c1ed2b6f8413622e58ebfa6e14


if __name__ == '__main__':

    t = tianMao()
    t.main()

