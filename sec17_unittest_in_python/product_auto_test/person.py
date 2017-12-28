#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/12/16

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self, word):
        print(f"{self.name}说{word}")
