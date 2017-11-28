#!/usr/bin/python3 
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/10/23

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        
"""
from datetime import date, datetime


class Student:
    def __init__(self, name, gender, birthdate):
        self.name = name
        self.gender = gender
        self.birthdate = birthdate

    @property
    def age(self):
        return date.today().year - self.birthdate.year

    @age.setter
    def age(self, value):
        raise AttributeError("年龄不能赋值 ! ")

    def __repr__(self):
        return '<Student : {} > '.format(self.name)

    def learning(self):
        print("{} 同学正在学习Python".format(self.name))


if __name__ == '__main__':
    s1 = Student("Tom", '男', date(2000, 1, 1))
    print(s1)
    s1.age = 30
