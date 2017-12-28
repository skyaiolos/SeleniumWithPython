#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/11/26

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        测试 POM
"""
import unittest
from sec38_PageObjectDesignPettern.login_page import Login_Page


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.lp = Login_Page(path='/login/')

    def test_login(self):
        username = 'Tom'
        password = '123456'

        self.lp.test_user_login(username, password)
        self.assertEqual('用户中心', self.lp.get_title())

    def tearDown(self):
        self.lp.dispose()
