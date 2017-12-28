#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/12/16

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        基于类的TestCase
        实例函数， 类函数，静态函数的区别
        
"""
import unittest
from selenium import webdriver


class SearchTest(unittest.TestCase):
    """【天猫产品搜索】单元测试版本 """

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        cls.driver.get('https://www.tmall.com')
        cls.driver.maximize_window()

    def test_search_by_name(self):
        search_field = self.driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('小米 Note')
        search_field.submit()

        products = self.driver.find_elements_by_xpath('//*[@id="J_ItemList"]/div/div/div/a[1]')
        self.assertEqual(156, len(products))

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
