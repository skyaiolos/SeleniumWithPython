#!/usr/bin/python3 
# -*- coding:utf-8 -*-  
# Created on 2017/11/12

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        文件上传
"""
from selenium import webdriver
import os, time

url = 'file:///P:/Project_python/SeleniumwithPython/selenium-site/page-03.html'

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=option)

driver.implicitly_wait(20)
driver.get(url)
driver.find_element_by_id('avatar').send_keys(os.path.normpath('C:\员工登记表.xlsx'))
time.sleep(5)
# driver.find_element_by_css_selector('input[type="submit"]').submit()
time.sleep(5)
