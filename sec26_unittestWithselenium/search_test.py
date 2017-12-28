#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/12/16

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        
"""
import unittest
from selenium import webdriver


class SearchTest(unittest.TestCase):
    """【天猫产品搜索】单元测试版本 """

    def test_search_by_name(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(20)
        driver.get('https://www.tmall.com')

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('小米 Note')
        search_field.submit()

        products = driver.find_elements_by_xpath('//*[@id="J_ItemList"]/div/div/div/a[1]')
        self.assertEqual(158, len(products))


if __name__ == '__main__':
    unittest.main()
