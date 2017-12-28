#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/12/16

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        实例方法级别的TestCase
        
"""
import unittest
from selenium import webdriver


class SearchTest(unittest.TestCase):
    """【天猫产品搜索】单元测试版本 """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.get('https://www.tmall.com')
        self.driver.maximize_window()

    def test_search_by_name(self):
        search_field = self.driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('小米 Note')
        search_field.submit()

        products = self.driver.find_elements_by_xpath('//*[@id="J_ItemList"]/div/div/div/a[1]')
        self.assertEqual(156, len(products))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
