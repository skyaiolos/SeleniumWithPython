#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/11/12

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        模块化测试 - 脚本测试
"""
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import time, os

URL = "http://test.vcoding.com/login/"
version = 2.06_1111
ff_bin = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox(firefox_binary=ff_bin)

driver.implicitly_wait(20)
driver.set_window_size(1920, 1080)


def init_driver():
    pass


def test_login():
    driver.get(URL)
    driver.find_element_by_id('username').send_keys('Tom')
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_id('submit').click()
    driver.get_screenshot_as_file(os.path.abspath("../Captures/{}_test03.png".format(version)))
    print(driver.title)
    if driver.title == '用户中心':
        print('登录成功')


def test_operation():
    email_td = driver.find_element_by_css_selector('.table > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2)')
    print(email_td.text)


def test_logout():
    driver.find_element_by_partial_link_text("管理").click()
    driver.find_element_by_partial_link_text("退出").click()
    if driver.title == '用户登录':
        print('退出成功')


if __name__ == '__main__':
    test_login()
    # test_operation()
    test_logout()
