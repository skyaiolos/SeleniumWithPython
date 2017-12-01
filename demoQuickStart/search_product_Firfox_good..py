#!/usr/bin/python3 
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/10/27

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        使用Firefox 浏览器 
"""
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#  制定火狐浏览器的二进制.exe 文件路径
ff_bin = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')

# 配置FF配置文件
ff_profile = webdriver.FirefoxProfile()

driver = webdriver.Firefox(firefox_binary=ff_bin)
driver.maximize_window()

url = 'https://www.tmall.com/'
driver.get(url)

search_field = driver.find_element_by_name('q')
search_field.clear()
search_field.send_keys('小米 Note')

search_field.submit()

sleep(3)

products = driver.find_elements_by_xpath('//div[@id="J_ItemList"]/div/div/p[2]/a')

print(len(products))

for product in products:
    print(product.text)

driver.quit()
