#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/11/29

__author__ = "Sky Jin "

"""
    Description:
        爬去页面的源码
"""
import re
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=option)

driver.maximize_window()
driver.implicitly_wait(20)
driver.get("http://www.baidu.com")
page = driver.page_source
# print(page)

# 用re的正则表达式匹配： 费贪婪模式
url_list = re.findall('href=\"(.*?)\"', page, re.S)
url_all = []
# findall 方法返回的是一个list 集合。
for url in url_list:
    if 'https' in url:
        url_all.append(url)
print(url_all)
