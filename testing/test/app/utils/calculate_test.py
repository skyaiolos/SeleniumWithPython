#!/usr/bin/python3 
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/10/26

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        calculate test case
"""
import unittest
from app.utils.calculate import add


class TestCalculate(unittest.TestCase):
    def test_add_method(self):
        self.assertEqual(4, add(2, 2))


if __name__ == '__main__':
    unittest.main()
