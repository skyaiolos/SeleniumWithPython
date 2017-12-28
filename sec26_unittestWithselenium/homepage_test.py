#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/12/25

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        天猫首页测试用例
"""
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

url = "https://www.tmall.com"


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(url)

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False

        return True
