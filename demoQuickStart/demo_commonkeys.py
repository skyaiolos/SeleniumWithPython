#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/11/28

__author__ = "Jianguo Jin - jinjianguo@zhizhangyi.com "

"""
    Description:
       模拟键盘鼠标操作 
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=option)
driver.maximize_window()
driver.get('http://www.baidu.com')
driver.implicitly_wait(20)

# 鼠标悬停在百度的搜索设置按钮上
setting_btn = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(setting_btn).perform()

# 获取当前的窗口句柄 ：
current_page = driver.current_window_handle

# 获取多窗口句柄
all_h = driver.window_handles
