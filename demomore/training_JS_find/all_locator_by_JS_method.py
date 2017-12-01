#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/12/1

__author__ = "Sky Jin "

"""
    Description:
        以下总结了5种js定位的方法:
        document.getElementById() 	返回对拥有指定 id 的第一个对象的引用。

        document. getElementsByClassName() 	返回文档中所有指定类名的元素集合，作为 NodeList 对象。
        document.getElementsByName() 	返回带有指定名称的对象集合。
        document.getElementsByTagName() 	返回带有指定标签名的对象集合。
        document.querySelectorAll( "css selector" )
        
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

JS_n = 'document.getElementById("blog_nav_contact").click()'

driver.execute_script(JS_n)
print(driver.title)
sleep(6)

JS_u = 'document.getElementsByClassName("input-text")[0].value="skyaiolos0426"'
driver.execute_script(JS_u)
sleep(1)

JS_p = 'document.getElementsByClassName("input-text")[1].value="0426"'
driver.execute_script(JS_p)
sleep(1)

JS_r = 'document.getElementsByName("remember_me")[0].click()'
driver.execute_script(JS_r)
sleep(1)

JS_l = 'document.querySelectorAll("#signin")[0].click()'
driver.execute_script(JS_l)
sleep(3)

driver.switch_to_alert().dismiss()
# driver.quit()
