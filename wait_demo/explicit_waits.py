#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/12/2

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        http://selenium-python.readthedocs.io/waits.html
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://somedomain/url_that_delays_loading")
driver.implicitly_wait(10)
try:
    element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.ID, "myDynamicElement")
                )
            )
finally:
    driver.quit()
