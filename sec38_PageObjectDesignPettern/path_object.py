#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/11/26
from selenium import webdriver

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        POM
"""

class Page:
    def __init__(self, driver = None ,wait = 30, base_url='http://test.vcoding.com', path='/'):
        self.driver = driver if driver else  webdriver.Chrome()
        self.driver.implicitly_wait(wait)
        self.base_url = base_url
        self.path = path

    def open_url(self):
        self.driver.get(self.base_url + self.path)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_title(self):
        return self.driver.title

    def dispose(self):
        self.driver.quit()



