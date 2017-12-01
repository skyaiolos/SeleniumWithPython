#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/12/1

__author__ = "Sky Jin "

"""
    Description:
        练习 1 ： 去掉页面动态窗： 这里举一个新世界教育官网首页的例子
        由于alert弹窗不美观，现在大多数网站都会使用自定义弹窗，
        使用Selenium自带的方法就驾驭不了了，此时就要搬出JS大法
        driver.execute_script(js_monitor
   
"""
from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()
driver.get("http://sh.xsjedu.org/")
driver.implicitly_wait(20)

# js = driver.execute_script('document.getElementById("doyoo_monitor").style.display')
# print(js)

# 关闭悬浮框的显示。
js_monitor = 'document.getElementById("doyoo_monitor").style.display = "none"'
driver.execute_script(js_monitor)
sleep(2)
driver.quit()
