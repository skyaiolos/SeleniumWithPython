#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/11/26
from selenium import webdriver
from time import sleep

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        http://test.vcoding.com/profile/#
            User: Tom
            PWD: 123456
"""

options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=options)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://test.vcoding.com/login/")

username = driver.find_element_by_css_selector('#username')
username.clear()
username.send_keys("Tom")
password = driver.find_element_by_css_selector('#password')
password.clear()
password.send_keys("123456")
login = driver.find_element_by_css_selector("#submit")
login.click()

sleep(1)
if driver.title == "用户中心":
    print(driver.title)
    print("登录成功！")

sleep(2)

driver.quit()
