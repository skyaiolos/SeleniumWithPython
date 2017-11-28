#!/usr/bin/python3 
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/10/23

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        Person  
            字段
            属性
            方法
"""
from datetime import date, datetime


class Person:
    def __init__(self, name, age, birthdate, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.birthdate = birthdate
        self._salary = 0.0

    @property  # 属性装饰器
    def salary(self):
        return self._salary

    @salary.setter  # 设置器
    def salary(self, value):
        if value <= 0.0:
            self._salary = 0.0
        else:
            self._salary = value

    def say(self, word):
        print("{} 说 ：{}".format(self.name, word))

    def __str__(self):
        return "<Person {}>".format(self.name)

    def get_age(self):
        return date.today().year - self.birthdate.year


if __name__ == '__main__':
    p = Person("San", 20, date(2000, 3, 1), "女")
    p.salary = 5000
    print(p)
    print(p.salary)
    p.salary = -5000
    print(p.salary)
