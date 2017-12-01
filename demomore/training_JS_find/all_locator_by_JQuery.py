#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/12/1

__author__ = "Sky Jin "

"""
    Description:
        通过 JQuery 定位
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
# JS locator
JS_n = 'document.getElementById("blog_nav_contact").click()'

# JQuery
# jquery_n = '$("#blog_nav_contact").click()'

# driver.execute_script(jquery_n)
driver.execute_script(JS_n)

sleep(8)
print(driver.title)

# JS_u = 'document.getElementsByClassName("input-text")[0].value="skyaiolos0426"'
jquery_clear = "$('#input1').var('')"
jquery_u = "$('#input1').var('skyaiolos0426')"

driver.execute_script(jquery_clear)
driver.execute_script(jquery_u)
sleep(1)

# JS_p = 'document.getElementsByClassName("input-text")[1].value="0426"'
jquery_p = "$('#input2').var('1234')"
driver.execute_script(jquery_p)
sleep(1)

# JS_r = 'document.getElementsByName("remember_me")[0].click()'
jquery_r = "$('#remember_me').click()"
driver.execute_script(jquery_r)
sleep(1)

JS_l = 'document.querySelectorAll("#signin")[0].click()'
jquery_l = "$('#signin').click()"
driver.execute_script(jquery_l)
sleep(3)

driver.switch_to_alert().dismiss()
# driver.quit()
