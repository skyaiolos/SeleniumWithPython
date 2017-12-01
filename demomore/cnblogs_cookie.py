#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/11/29

__author__ = "Sky Jin "

"""
    Description:
        1. 进入我的博客园
        2. 点击随笔 
"""
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep

url = "http://www.sublimetext.com/3"
#  制定火狐浏览器的二进制.exe 文件路径
ff_bin = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')

# 配置FF配置文件
ff_profile = webdriver.FirefoxProfile()

driver = webdriver.Firefox(firefox_binary=ff_bin)

driver.implicitly_wait(20)
driver.maximize_window()

url = 'http://www.cnblogs.com/'
myblogs = url + 'jinsky'
driver.get(myblogs)

driver.find_element_by_id("blog_nav_newpost").click()
print(driver.title)
if driver.title == u"用户登录 - 博客园":
    driver.find_element_by_css_selector("#input1").send_keys('skyaiolos0426')

    password = open(r'pwd.txt').read()
    driver.find_element_by_css_selector("#input2").send_keys(password)

    driver.find_element_by_css_selector('#signin').click()

    c1 = {u'domain': u'.cnblogs.com',
          u'name': u'.CNBlogsCookie',
          u'value': u'EE38E167BA1C1CD3AC54468E282EFCC12CFE70091143076648CDE490BD9BB6974906D8A7FA528AB2CE9D0AD8576931056119AC7CE55C342EAEA9ABB6AB82CB897CEF32089EEA1EFE859A7AE8162A4FA50503837D0E67238124C9E09399CD61761E5AEDC4',
          u'expiry': 1511953073,
          u'path': u'/',
          u'httpOnly': True,
          u'secure': False}

    c2 = {u'domain': u'.cnblogs.com',
          u'name': u'.Cnblogs.AspNetCore.Cookies',
          u'value': u'CfDJ8BMYgQprmCpNu7uffp6PrYYyBttaSY-cNT6B5pCQYr9rGrHmFfCs0Os8YtcKmCDcqe-BHRcQiWF_wHrC_4j0DkYY9o2_i6GC5Mgs8SiMP4Om3dfeemGsHWfDWz_aswd2Es8D9gTiVzfap19lANiYqPioPwq7F6VWUyBbNc5XDNJc3TQ8bI4YOZlhABID4xsyJbHyBOl19J_6WL7v7Y25us8LZh2-5k3MekFIG460Zezb87WQyEhz1PIRECwgpjNvRSTWV4g84G_-ieIJHkapTgGxBKhmrZblJAYvXTxpAIZ7',
          u'expiry': 1511953073,
          u'path': u'/',
          u'httpOnly': True,
          u'secure': False}
    driver.add_cookie(c1)
    driver.add_cookie(c2)
    sleep(3)
    driver.refresh()
