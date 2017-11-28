#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/11/12

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        Cookies 处理测试
"""
from selenium import webdriver
import os, time

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

ff_bin = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox(firefox_binary=ff_bin)

driver.implicitly_wait(20)
driver.set_window_size(1200, 600)
driver.get('https://www.baidu.com')

#  添加一个cookies
driver.add_cookie({'name': 'uke', 'value': 'www.codeclass.com', 'path': '/'})

cookies = driver.get_cookies()
print('百度上{} 个cookies，用来记录用户信息 '.format(len(cookies)))
# pprint(cookies)
# c = driver.get_cookie('BAIDUID')
# print(c.get('domain', None))
# print('-' * 30)
# pprint(c)

# 删除cookie
driver.delete_cookie('uke')

cookies = driver.get_cookies()

c = driver.get_cookie('uke')

if c not in cookies:
    print('已经被删除!')

time.sleep(5)
driver.quit()
