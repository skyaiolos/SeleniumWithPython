#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/12/16

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        
"""


class User():
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return '<User {} {} {} >'.format(self.name, self.email, self.password)

    def user_is_valid(self, name, password):
        if self.name == name and self.password == password:
            return True

        return False

    def add(self,a, b):
        return a + b