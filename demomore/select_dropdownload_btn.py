#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/11/29

__author__ = "Jianguo Jin - jinjianguo@zhizhangyi.com "

"""
    Description:
        select 下拉框
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep

url = "http://www.baidu.com"
options = webdriver.ChromeOptions()
options.add_argument("disable-infobars")
driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(20)

# setting_btn = driver.find_element_by_css_selector("#s_usersetting_top > span")
setting_btn = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(setting_btn).perform()
sleep(2)
# driver.find_element_by_css_selector("#wrapper > div.bdpfmenu > a.setpref").click()
driver.find_element_by_link_text("搜索设置").click()
sleep(2)

# 1. 分2步定位.
s = driver.find_element_by_id('nr')
s.click()
driver.find_element_by_css_selector("#nr > option:nth-child(2)").click()
driver.get_screenshot_as_file(r"..\Captures\Setting_Option2.png")

# 2. 通过索引：select_by_index()
Select(s).select_by_index(2)
driver.get_screenshot_as_file(r"..\Captures\Setting_Option3.png")

# 3. 通过value值定位
Select(s).select_by_value("10")
driver.get_screenshot_as_file(r"..\Captures\Setting_Option1.png")

# 3. 通过文本值定位
Select(s).select_by_visible_text("每页显示50条")
driver.get_screenshot_as_file(r"..\Captures\Setting_Option_50.png")

driver.find_element_by_class_name("prefpanelgo").click()
sleep(2)
# alert = driver.switch_to_alert()
alert = driver.switch_to.alert

print(alert.text)
alert.accept()
