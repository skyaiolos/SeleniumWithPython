#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/11/29

__author__ = "Jianguo Jin - jinjianguo@zhizhangyi.com "

"""
    Description: 
        ----Homework---
        login the http://mail.163.com
        Test Case:
            1. Input the name
            2. nput the password
            3. Checked the "十天内免登录"
            4. Click on Login.         
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

url = "http://mail.163.com/"
options = webdriver.ChromeOptions()
options.add_argument("disable-infobars")
driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(20)
sleep(5)

# 使焦点定位到登录的iframe 上
# 1。
# driver.switch_to_frame("x-URS-iframe")
driver.switch_to.frame("x-URS-iframe")
# 2. 切换iframe
iframe = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(iframe)

# 点击用户名和密码
driver.find_element_by_name("email").send_keys("skyaiols")
password = driver.find_element_by_name("password")
password.send_keys("123456")

# css 通过标签与id 属性的组合定位。
# driver.find_element_by_partial_link_text("十天内免登录")
driver.find_element_by_css_selector("label[for='un-login']").click()
sleep(2)

# 因为上一部的comment 信息遮盖到了 登录的按钮，影响点击。所以要把鼠标移到password ，然后再点击登录。
ActionChains(driver).move_to_element(password).perform()
driver.find_element_by_id("dologin").click()
sleep(3)

# 释放iframe , 重新回到主页面上
driver.switch_to_default_content()

#  Question:
    # 如何判断元素是否在iframe 上？
    # 1. 定位到元素后，切换到firepath界面
    # 2. 看firebug 工具左上角，如果显示Top Window说明没有iframe
    # 3. 如果显示iframe#XXX , 说明在iframe 上 # 后面是它的id.


driver.quit()
