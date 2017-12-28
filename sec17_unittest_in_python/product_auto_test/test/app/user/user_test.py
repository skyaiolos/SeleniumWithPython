#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/12/18

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description
        :
        
"""
import unittest

from sec17_unittest_in_python.product_auto_test.app.user.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.u = User('Tom', 'tom@yahoo.com', '11111')
        self.users = [self.u, User('Jerry', 'jerry@tom.com', '111111')]

    def test_add_method(self):
        # u = User('Tom', 'tom@yahoo.com', '11111')
        self.assertEqual(5, self.u.add(2, 3))

    def test_user_is_valid(self):
        # u = User('Tom', 'Ton@yahoo.com', '111111')
        # self.assertEqual(True, self.u.user_is_valid('Tom', '111111'))
        self.assertTrue(self.u.user_is_valid('Tom', '11111'))

    def test_user_in(self):
        mary = User('Mary', 'test@cs.com', '1111')
        self.assertIn(self.u, self.users)

        # self.assertIn(mary, self.users)


if __name__ == '__main__':
    unittest.main()
