#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/11/29

__author__ = "Sky Jin "

"""
    Description:
        单选框和复选框 （radiobox, checkbox）
"""

from selenium import webdriver
from time import sleep

import time

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=option)
driver.implicitly_wait(20)
driver.maximize_window()

url = 'file:///F:/SeleniumwithPython/selenium-site/radio_check_box.html'
driver.get(url)
girl = driver.find_element_by_id("girl")
if girl.is_selected() is not True:
    girl.click()

r = driver.find_element_by_id('boy').is_selected()

if r is not True:
    driver.find_element_by_id('boy').click()

else:
    print(r)
checkboxes = driver.find_elements_by_xpath("//*[@type='checkbox']")
"//*[@type='checkbox']"
"/html/body/form[3]/text()[1]"
for i in checkboxes:
    i.click()
    sleep(1)
