#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/12/16

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        test the uitls\calculate.py
"""

import unittest
from testing.app.utils.calculate import add


# 测试类的名称必须是以 Test 开头
class TestCalculate(unittest.TestCase):
    """测试类中的方法也要以 test  开头。"""

    def test_add_method(self):
        try:
            self.assertEqual(8, add(3, 4))

        except AssertionError as err:
            print("err", err)


if __name__ == '__main__':
    unittest.main()
