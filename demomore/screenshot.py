#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/11/12

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        网页截图
"""

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import time
import os

build_versoin = 2.06_1110

ff_bin = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox(firefox_binary=ff_bin)
driver.implicitly_wait(20)
driver.set_window_size(1500, 1000)
driver.get('http://ke.qq.com')

driver.get_screenshot_as_file(os.path.abspath('./Captures/{}_test01.png').format(build_versoin))
time.sleep(2)
driver.quit()
