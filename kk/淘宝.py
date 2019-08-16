#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/7/22 10:57
# software: PyCharm
import os
import time
import random
import asyncio
import pyppeteer



#Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});


class LoginTaoBao:

    def __init__(self):
        os.environ['PYPPETEER_CHROMIUM_REVISION'] = '575458'
        pyppeteer.DEBUG = True
        self.page = None

    async def _injection_js(self,page):
        """
        注入js 突破淘宝封锁
        :return:
        """

        # 这个是关键参数, 主要靠这个
        await page.evaluate('''() =>{

                   Object.defineProperties(navigator,{
                     webdriver:{
                       get: () => false
                     }
                   })
                }''')

        await page.evaluate('''() => {
            window.navigator.chrome = {
            runtime: {},
            // etc.
            };
            }''')

        await page.evaluate('''() => {
                  const originalQuery = window.navigator.permissions.query;
                  return window.navigator.permissions.query = (parameters) => (
                    parameters.name === 'notifications' ?
                      Promise.resolve({ state: Notification.permission }) :
                      originalQuery(parameters)
                  );
                }
            ''')

        await page.evaluate('''() =>{
            Object.defineProperty(navigator, 'languages', {
            get: () => ['en-US', 'en']
                });
            }''')

        await page.evaluate('''() =>{
            Object.defineProperty(navigator, 'plugins', {
            get: () => [1, 2, 3, 4, 5],
                });
            }''')

    async def _init(self):
        """
        初始化浏览器
        :return:
        """
        # 设置浏览器参数
        self.browser = await pyppeteer.launch(
                                        {'headless': False,
                                         # 'userDataDir': "./userdata",
                                          'args': [
                                              '--disable-extensions',
                                              '--hide-scrollbars',
                                              '--disable-bundled-ppapi-flash',
                                              '--mute-audio',
                                              '--no-sandbox',
                                              '--disable-setuid-sandbox',
                                              '--disable-gpu',
                                          ],
                                          'dumpio': True,
                                          })
        # 创建浏览器对象
        self.page = await self.browser.newPage()
        # 设置浏览器头部
        await self.page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                     '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
        # 设置浏览器大小
        await self.page.setViewport({'width': 1080, 'height': 960})

    async def get_cookie(self):
        cookies_list = await self.page.cookies()
        cookies = ''
        for cookie in cookies_list:
            str_cookie = '{0}={1};'
            str_cookie = str_cookie.format(cookie.get('name'), cookie.get('value'))
            cookies += str_cookie
        print(cookies)
        return cookies

    async def mouse_slider(self):
        """
        滑动滑块
        :return: None 滑动失败 或者 True滑动成功
        """
        await asyncio.sleep(3)
        try:
            await self.page.hover('#nc_1_n1z')
            # 鼠标按下按钮
            await self.page.mouse.down()
            # 移动鼠标
            await self.page.mouse.move(1000, 0, {'steps': 30})
            # 松开鼠标
            await self.page.mouse.up()
            await asyncio.sleep(2)
        except Exception as e:
            print(e, '      :slider login error')
            return None
        else:
            await asyncio.sleep(3)
            # 获取元素内容
            ua = await self.page.evaluate('navigator.webdriver')
            print(ua)
            await self.page.screenshot({'path': './headless-slide-result.png'})
            slider_again = await self.page.querySelectorEval('#nc_1__scale_text', 'node => node.textContent')
            if slider_again != '验证通过':
                return None
            else:
                # 截图
                await self.page.screenshot({'path': './headless-slide-result.png'})
                print('验证通过')
                return True

    async def move_slider(self):
        """
        滑动滑块
        :return: None 滑动失败 或者 True滑动成功
        """
        await asyncio.sleep(3)
        try:
            await self.page2.hover('#nc_1_n1z')
            # 鼠标按下按钮
            await self.page2.mouse.down()
            # 移动鼠标
            await self.page2.mouse.move(1000, 0, {'steps': 30})
            # 松开鼠标
            await self.page2.mouse.up()
            await asyncio.sleep(2)
        except Exception as e:
            print(e, '      :slider login error')
            return None
        else:
            await asyncio.sleep(3)
            # 获取元素内容
            ua = await self.page2.evaluate('navigator.webdriver')
            print(ua)
            await self.page2.screenshot({'path': './headless-slide-result.png'})
            slider_again = await self.page2.querySelectorEval('#nc_1__scale_text', 'node => node.textContent')
            if slider_again != '验证通过':
                return None
            else:
                # 截图
                await self.page2.screenshot({'path': './headless-slide-result.png'})
                print('验证通过')
                return True



    async def main(self, username_, pwd_):
        """
        登陆并获取cookie
        :param username_: 账号
        :param pwd_: 密码
        :return: cookie 或 None
        """
        # 初始化浏览器
        await self._init()
        # 打开淘宝登陆页面
        await self.page.goto('https://login.taobao.com')
        # 注入js
        await self._injection_js(self.page)
        # 点击密码登陆按钮
        await self.page.click('div.login-switch')
        time.sleep(random.random() * 2)
        # 输入用户名
        await self.page.type('#TPL_username_1', username_, {'delay': random.randint(100, 151) - 50})
        # 输入密码
        await self.page.type('#TPL_password_1', pwd_, {'delay': random.randint(100, 151)})
        time.sleep(random.random() * 2)
        # 获取滑块元素
        slider = await self.page.querySelector('#J_Form')
        width =   slider.boundingBox()
        if slider:
            print('有滑块')
            # 移动滑块
            flag = await self.mouse_slider()
            # 判断滑块是否滑动成功
            if not flag:
                print('滑动滑块失败')
                return None
            time.sleep(random.random() + 0.5)
            # 点击登陆
            await self.page.click('#J_SubmitStatic')
        else:
            print('没滑块')
            # 按下回车
            await self.page.keyboard.press('Enter')
        # 等待
        # await self.page.waitFor(5)
        # 等待导航, 等待跳转
        await asyncio.sleep(5)
        self.page.goto("https://www.taobao.com")
        context = await self.browser.createIncognitoBrowserContext()
        self.page2 = await context.newPage()
        await self.page2.setViewport({'width': 1080, 'height': 960})
        await self.page2.goto('https://list.tmall.com/search_product.htm?q=%B0%D7%BE%C6')
        await self._injection_js(self.page2)
        count = 1
        while True:
            html = await self.page2.content()
            if '亲，小二正忙，滑动一下马上回来' in html:
                await self.move_slider()
                break

            html = await self.page2.content()
            with open(f'{count}.html','w',encoding='utf8') as f:
                f.write(html)
            await asyncio.sleep(random.randint())
            await self.page2.click('a.ui-page-next')
            await self.page2.evaluate('''() =>{

                               Object.defineProperties(navigator,{
                                 webdriver:{
                                   get: () => false
                                 }
                               })
                            }''')
            count += 1



if __name__ == '__main__':
    username = 'wjheart00'
    pwd = 'he..651349'
    login = LoginTaoBao()
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(login.main(username, pwd))
    loop.run_until_complete(task)
    print(task.result())
