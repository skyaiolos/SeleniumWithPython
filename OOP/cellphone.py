#!/usr/bin/python3 
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/10/23

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
       OOP   
       __repr__
       __str__
"""
from datetime import date, datetime


class CellPhone:
    def __init__(self, brand, color, size, price=0.00, date_of_manufacture=None):
        self.brand = brand
        self.color = color
        self.size = size
        self.price = price
        self.date_of_manufacture = date_of_manufacture if date_of_manufacture is not None else date.today()

    def on(self):
        print("手机开了")

    def off(self):
        print("手机关了")

    def __str__(self):
        return "Brand is %s , the date of manufacture is %s" % (self.brand, self.date_of_manufacture)

    def __repr__(self):
        return "<cellPhone : {}, {}".format(self.brand, self.price)

    def __add__(self, other):
        return self.price + other.price


if __name__ == '__main__':
    c1 = CellPhone("iPhone 6", 'Gold', 4.7, 4900)
    print(c1)
    print(c1.date_of_manufacture)
    c1.on()

    c2 = CellPhone("Mi", "black", 5.5, 2900.00, date(2015, 3, 1))
    print(c2)
