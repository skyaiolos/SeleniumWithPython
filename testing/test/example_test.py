#!/usr/bin/python3 
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/10/26

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        
"""
import unittest


def my_func():
    try:
        x = int('s')
    except ValueError as err:
        print('met the value error')
        raise err


class TestExcample(unittest.TestCase):
    def setUp(self):
        pass

    # 判断是否相等
    def test_asssert_equal(self):
        self.assertEqual(1, 2)

    # 判断约等于
    def test_assert_almost_equal(self):
        self.assertAlmostEqual(1, 1.6, delta=0.5)

    # 判断大于
    def test_assert_greater(self):
        self.assertGreater(2, 1)

    # 判断是否抛出异常
    def test_assert_raise(self):
        self.assertRaises(ValueError, my_func)

    # 判断成员是否在序列之内
    def test_assert_in(self):
        # self.assertIn(9, [1, 2, 3])
        self.assertIn('s', 'sorry')

    def tearDown(self):
        pass
