#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/11/29

__author__ = "Jianguo Jin "

"""
    Description:
       获取多个地址，随机选取一个进行操作 
"""
from selenium import webdriver
from time import sleep

import random

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.implicitly_wait(10)
driver.find_element_by_id('kw').send_keys(u"测试部落")
driver.find_element_by_id('kw').submit()
sleep(3)

# find_elementsssssss
s = driver.find_elements_by_css_selector("h3.t>a")
print(s)
# 设置随机值
t = random.randint(0, 9)
# 随机取一个结果获取url地址
a = s[t].get_attribute('href')
print(a)
s[t].click()

driver.get(a)
