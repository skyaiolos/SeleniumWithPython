#!/usr/bin/python3 
# -*- coding:utf-8 -*-  
# Created on 2017/11/12

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        switch to  between windows handle and form
        Demo site:
        file:///P:/Project_python/SeleniumwithPython/selenium-site/page-01.html
"""

from selenium import webdriver
import time

url = 'file:///P:/Project_python/SeleniumwithPython/selenium-site/page-01.html'

options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=options)

driver.implicitly_wait(10)
driver.set_window_size(1600, 1000)
driver.get(url)
driver.implicitly_wait(20)

f1 = driver.find_element_by_id("frm1")
driver.switch_to.frame(f1)
driver.find_element_by_id('kw').send_keys('优品课堂')

# 将当前的窗口句柄保存到引用
current_window = driver.current_window_handle

driver.switch_to.window(current_window)

f2 = driver.find_element_by_id("frm2")
driver.switch_to.frame(f2)
search_field = driver.find_element_by_name('q')
search_field.clear()
search_field.send_keys('优品课堂')
search_field.submit()

driver.quit()