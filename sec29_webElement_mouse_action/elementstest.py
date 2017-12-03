#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/12/2

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        Web element 处理
"""
from selenium import webdriver
from time import sleep

BASE_URL = "http://test.vcoding.com/checkboxes/"
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=option)

driver.maximize_window()
driver.implicitly_wait(20)
driver.get(BASE_URL)
sleep(2)

# find_elements_by_tag_name
checkboxes_0 = driver.find_elements_by_tag_name('input')

# find_elements_by_xpath - input-type
checkboxes_1 = driver.find_elements_by_xpath('//input[@type="checkbox"]')

# find_elements_by_xpath (starts-with)
checkboxes_2 = driver.find_elements_by_xpath('//input[starts-with(@id,"chk")]')

# find_elements_by_css_selector
checkboxes_3 = driver.find_elements_by_css_selector('input[type="checkbox"]')

print(type(checkboxes_0))
print(len(checkboxes_0))
checkboxes = []

for chk in checkboxes_0:
    print(chk.text)
    if chk.get_attribute('type') == 'checkbox':
        chk.click()
        sleep(1)

for chk in checkboxes_1:
    print(chk.text)
    if chk.get_attribute('type') == 'checkbox':
        chk.click()
        sleep(1)

for chk in checkboxes_2:
    print(chk.text)
    if chk.get_attribute('type') == 'checkbox':
        chk.click()
        sleep(1)

for chk in checkboxes_3:
    print(chk.text)
    if chk.get_attribute('type') == 'checkbox':
        chk.click()
        sleep(1)

checkboxes_0[-1].click()

sleep(2)
driver.quit()
