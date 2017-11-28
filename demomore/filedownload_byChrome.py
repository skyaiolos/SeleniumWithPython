#!/usr/bin/python3 
# -*- coding:utf-8 -*-  
# Created on 2017/11/12

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        文件下载
"""
from selenium import webdriver
import os

url = "http://www.sublimetext.com/3"
# 构造Chrome 选项
option = webdriver.ChromeOptions()
prefs = {'download.default_directory': os.path.abspath('./downloads')}
option.add_argument('disable-infobars')
option.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(chrome_options=option)
driver.implicitly_wait(10)
driver.get(url)

# find_by_xpath(//*[@id="dl_win_64"]/a[2])
driver.find_element_by_css_selector("#dl_win_64 > a:nth-child(2)").click()
