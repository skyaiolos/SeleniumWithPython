#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/11/26

from PageObjectDesignPettern.cellphone import Person
from PageObjectDesignPettern.cellphone import CellPhone
from datetime import datetime

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        继承Person()
"""


class Student(Person):
    def __init__(self, name, age, course):
        Person.__init__(self, name, age)
        self.course = course

    def learning(self, time):
        print("{}于{}学习{}".format(self.name, time, self.course))


if __name__ == '__main__':
    mike = Person('Mike', 23)
    mike = Student('Mike', 23, 'Python')
    mike.learning(datetime.now())
    mi = CellPhone('Mi Note', price=1900, size=5.5)
    mike.send_message(mi, 'Jerry', '我在上课')
