#!/usr/bin/python3 
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/10/26

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        
"""
import unittest
from app.user.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.u = User('Tom', 'tom@tom.com', '123455')
        self.users = [self.u, User('Jerry', 'jerry@tom.com', '456123')]

    def test_add_method(self):
        self.assertEqual(6, self.u.add(2, 3))

    def test_user_is_valid(self):
        # self.assertEqual(True, u.user_is_valid('Tom', '123455'))
        self.assertTrue(self.u.user_is_valid('Tom', '123455'))

    def test_user_in(self):
        jerry = User('Jerry', 'jerry@tom.com', '456123')
        # self.assertIn(jerry, self.users)
        self.assertIn(self.u, self.users)


if __name__ == '__main__':
    unittest.main()
