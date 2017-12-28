#!/usr/bin/python3 
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/10/27

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        搜索天猫某产品列表展示商品数
"""
from selenium import webdriver
from time import sleep
url = 'https://www.tmall.com/'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(20)

search_field = driver.find_element_by_name('q')
search_field.clear()
search_field.send_keys('小米 Note')

search_field.submit()
sleep(3)

products = driver.find_elements_by_xpath('//div[@id="J_ItemList"]/div/div/p[2]/a')

print(len(products))

for product in products:
    print(product.text)

driver.quit()

