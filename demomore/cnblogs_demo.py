#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/11/29

__author__ = "Sky Jin "

"""
    Description:
        1. 进入我的博客园
        2. 点击随笔 
"""
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep

url = "http://www.sublimetext.com/3"
#  制定火狐浏览器的二进制.exe 文件路径
ff_bin = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')

# 配置FF配置文件
ff_profile = webdriver.FirefoxProfile()

driver = webdriver.Firefox(firefox_binary=ff_bin)

driver.implicitly_wait(20)
driver.maximize_window()

url = 'http://www.cnblogs.com/'
myblogs = url + 'jinsky'
driver.get(myblogs)

driver.find_element_by_id("blog_nav_newpost").click()
print(driver.title)
if driver.title == u"用户登录 - 博客园":
    driver.find_element_by_css_selector("#input1").send_keys('skyaiolos0426')

    password = open(r'pwd.txt').read()
    driver.find_element_by_css_selector("#input2").send_keys(password)

    driver.find_element_by_css_selector('#signin').click()

sleep(3)

driver.get_screenshot_as_file(r"..\Captures\cnblogs_jinsky.png")
alert = driver.switch_to.alert
alert.dismiss()
driver.get("https://i.cnblogs.com/EditPosts.aspx?opt=1")
