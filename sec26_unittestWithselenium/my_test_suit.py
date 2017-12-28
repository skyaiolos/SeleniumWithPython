#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/12/26

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        test suit 测试套装，整合测试Case
"""
import unittest

from sec26_unittestWithselenium.search_test import SearchTest
from sec26_unittestWithselenium.homepage_test import HomePageTest

# 载入所有要分组集成的测试用例类。
search_test = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# 创建Test Suite, 合并测试用例
tests = unittest.TestSuite([search_test, home_page_test])

unittest.TextTestRunner().run(tests)
