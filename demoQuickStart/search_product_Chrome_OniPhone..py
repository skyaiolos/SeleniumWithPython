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

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
# 伪装成iphone 登录
option.add_argument('--user-agent=iphone')
driver = webdriver.Chrome(chrome_options=option)
driver.implicitly_wait(20)

url = 'https://www.tmall.com/'
driver.get(url)

login_btn = driver.find_elements_by_xpath('//*[@id="header"]/div[4]')

login_btn.click()

sleep(3)

products = driver.find_elements_by_xpath('//div[@id="J_ItemList"]/div/div/p[2]/a')

print(len(products))

for product in products:
    print(product.text)

driver.quit()
