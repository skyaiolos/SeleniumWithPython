#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/12/1

__author__ = "Sky Jin "

"""
    Description:
        练习 1 ： 练习题2:定位百度-更多产品 里面的'全部产品'        
        document.getElementById() 	        返回对拥有指定 id 的 { 第一个对象 } 的引用。
                
        document. getElementsByClassName() 	返回文档中所有指定类名的 { 元素集合 }，作为 NodeList 对象。        
        document.getElementsByName() 	    返回带有指定名称的 { 对象集合 }。
        document.getElementsByTagName() 	返回带有指定标签名的 { 对象集合 }。
        document.querySelectorAll( "css selector" )
   
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

more_products = driver.find_element_by_link_text("更多产品")
ActionChains(driver).move_to_element(more_products).perform()
sleep(1)

ele = driver.find_element_by_class_name("bdbrievenmore")
print(ele.text)
# 能找到元素，但是点击失效了
# ele.click()

# 这时候可以用JS 大发 , 注意 ： getElementsByName() 复数形式，返回一个列表
JS_all_pro = 'document.getElementsByName("tj_more")[0].click()'
driver.execute_script(JS_all_pro)
sleep(5)
# driver.quit()
