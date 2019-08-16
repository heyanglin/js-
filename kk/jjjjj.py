#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/7/19 17:29
# software: PyCharm
import pyppeteer
import asyncio
import time

class tianmao(object):
    username = '88888888'
    password = '00000000'

    async def injection_js(self):
        """
        注入js 突破淘宝封锁
        :return:
        """

        # 这个是关键参数, 主要靠这个
        await self.page.evaluate('''() =>{

                   Object.defineProperties(navigator,{
                     webdriver:{
                       get: () => false
                     }
                   })
                }''')

        await self.page.evaluate('''() => {
            window.navigator.chrome = {
            runtime: {},
            // etc.
            };
            }''')

        await self.page.evaluate('''() => {
                  const originalQuery = window.navigator.permissions.query;
                  return window.navigator.permissions.query = (parameters) => (
                    parameters.name === 'notifications' ?
                      Promise.resolve({ state: Notification.permission }) :
                      originalQuery(parameters)
                  );
                }
            ''')

        await self.page.evaluate('''() =>{
            Object.defineProperty(navigator, 'evaluatelanguages', {
            get: () => ['en-US', 'en']
                });
            }''')

        await self.page.evaluate('''() =>{
            Object.defineProperty(navigator, 'plugins', {
            get: () => [1, 2, 3, 4, 5],
                });
            }''')

    async def Init_browser(self):
        self.browser = await pyppeteer.launch(
            {'headless': False,
             'userDataDir': "./userdata",
             'args': [
                 '--disable-extensions',
                 '--hide-scrollbars',
                 '--disable-bundled-ppapi-flash',
                 '--mute-audio',
                 '--disable-infobars',
                 '--no-sandbox',
                 '--disable-setuid-sandbox',
                 '--disable-gpu',
             ],
             'dumpio': True,
             }
        )
        self.page = await  self.browser.newPage()
        await self.page.setViewport({'width': 1866, 'height': 768})
        await self.page.setUserAgent(
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
        await self.injection_js()
        await self.page.evaluateOnNewDocument("""
                var _navigator = {};
                for(name in window.navigator){
                    if(name !="webdriver"){
                    _navigator[name] = window.navigator[name]
                    }
                }
                Object.defineProperty(window,'navigator',{
                    get:()=>__navigator,
                
                })
        """)
        await self.page.goto('https://www.taobao.com/')
        self.page2 = (await self.browser.pages())[2]
        await self.page2.goto('https://list.tmall.com/search_product.htm?q=%B0%D7%BE%C6')
        await self.page.goto('https://www.tmall.com/')
        await self.page.click('a.sn-login')  #点击登录
        # iframe = await self.page.waitFor('iframe#J_loginIframe')

        await asyncio.sleep(5)
        frame = self.page.frames
        print(frame)
        await frame[1].click('a.forget-pwd.J_Quick2Static')  #密码登录
        await frame[1].type('input#TPL_username_1',self.username)
        await frame[1].type('input#TPL_password_1',self.password)
        await asyncio.sleep(10)
        await self.page.click('button.J_Submit')










    def main(self):

        start_time = time.time()
        asyncio.get_event_loop().run_until_complete(self.Init_browser())
        print(time.time()-start_time)
        # await self.browser.close()




if __name__ == '__main__':

    t =tianmao()
    t.main()