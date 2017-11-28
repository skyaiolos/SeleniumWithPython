#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/11/12

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        在火狐浏览器上下载文件
"""
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os, time

url = "http://www.sublimetext.com/3"
#  制定火狐浏览器的二进制.exe 文件路径
ff_bin = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')

# 配置FF配置文件
ff_profile = webdriver.FirefoxProfile()
ff_profile.set_preference('browser.download.folderList', 2)
ff_profile.set_preference('browser.download.manager.showWhenStarting', False)
ff_profile.set_preference('browser.download.dir', os.path.abspath('./downloads'))
ff_profile.set_preference('browser.helpApps.neverAsk.SaveToDisk', 'application/octer-stream')

driver = webdriver.Firefox(firefox_binary=ff_bin)
driver.implicitly_wait(20)
driver.get(url)
driver.find_element_by_css_selector("#dl_win_64 > a:nth-child(2)").click()
time.sleep(10)
