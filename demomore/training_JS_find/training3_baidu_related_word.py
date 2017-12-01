#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/12/1

__author__ = "Sky Jin "

"""
    Description:
        练习题3 :定位百度-输入框联想词      
            通过get_attribute() 方法获取到文本信息
   
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()
url = "http://www.baidu.com"
driver.get(url)
driver.implicitly_wait(20)

driver.find_element_by_id('kw').send_keys(u'博客')

# 获取输入框的
sleep(1)

bd = driver.find_elements_by_class_name("bdsug-overflow")

for i in bd:
    print(i.get_attribute("data-key"))

    # 点击其中一个
if len(bd) > 1:
    bd[1].click()
    print(driver.current_url)
    for i in range(1, len(bd)):
        print(i)
        # driver.find_element_by_id('kw').clear()
        # driver.find_element_by_id('kw').send_keys(u'博客')
        # bd[i].click()
        # sleep(1)

else:
    print("Not fond")

driver.quit()
