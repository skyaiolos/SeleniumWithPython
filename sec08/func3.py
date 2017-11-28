#!/usr/bin/python3 
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/10/20

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        Advance func
"""


def func(a, b, c):
    print(a, b, c)


def func_1(a, b, *args):  # *args is a tuple
    print(a, b, args)


def avg(a, *args):
    pass


def func_2(a, b, **kwargs):
    print(a, b, kwargs)


if __name__ == '__main__':
    func(3, 4, c=6, )
    func_1(3, 4, 5, 6, 7, 8)  # The third parameter is the tuple
