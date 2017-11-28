#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/11/12

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        执行JS
"""

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import time
import os

version = 2.06_1111

ff_bin = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox(firefox_binary=ff_bin)

driver.set_window_size(1200, 800)
driver.implicitly_wait(20)
driver.get('https://www.w3.org/standards')
time.sleep(5)

# Java script
js = 'window.scrollTo(100, 1500)'
driver.execute_script(js)
driver.get_screenshot_as_file(os.path.abspath('Captures/{}_test02.png'.format(version)))

#  下面的方法执行多次，但是有问题。
# def run_js():
#     driver.execute_script(js)
#
#
# # for i in range(6):
# #
# for i in range(1, 6):
#     run_js()
#     time.sleep(1)

# i = 1
# while i <= 6:
#     driver.execute_script(js)
#     i += 1
#     time.sleep(1)
time.sleep(5)
driver.quit()
