#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/12/16

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        测试脚本文件命名规则 ：
            要测试的类的名称_test.py
            
        e.g.:
            user_test.py
            calculate_test.py
            example_test.py
            
        脚本文件中：
            类名：是以Test 开头
            方法：是以test开头。         
"""

import unittest

def my_func():
    try:
        x = int('x')
    except ValueError as err:
        print('遇到值错误')
        raise err

class TestExample(unittest.TestCase):
    # 判断是否相等
    def test_assert_equal(self):
        self.assertEqual(1, 1)

    # 判断约等于
    def test_assert_almost_equal(self):
        self.assertAlmostEqual(1, 1.6, delta=0.5)  # delta 是定义误差区间，只要在0.5 都是正确的。

    # 判断大于
    def test_assert_greater(self):
        self.assertGreater(3, 2)

    # 判断小于
    def test_assert_less(self):
        self.assertLess(1, 3)

    # 判断异常是否抛出的正确
    def test_assert_except(self):
        self.assertRaises(ValueError, my_func)

    # 判断成员是否在序列之内
    def test_assert_in(self):
        self.assertIn(3, [1, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
