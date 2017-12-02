#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/11/12

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        执行JS
        JS ： 
            document.write('hello')
            window.location.href = 'http://codr.cn'
            window.scrollTo(100,1500)  # 滚动条移动的位置
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

js_hello = 'alert("Hello , I am sky")'


#  下面的方法执行多次,Fixed
def run_js():
    driver.execute_script(js_hello)


# For loop
for i in range(1, 6):
    if i <= 2:
        run_js()
        time.sleep(1)
        driver.switch_to.alert.dismiss()
        time.sleep(1)

# while loop
i = 1
driver.execute_script('alert("Now is the while loop")')
time.sleep(1)
driver.switch_to.alert.dismiss()
while i <= 3:
    driver.execute_script(js_hello)
    time.sleep(1)
    driver.switch_to.alert.dismiss()
    time.sleep(1)
    i += 1

time.sleep(2)
driver.quit()
