from datetime import datetime

"""
Script Descripion:

"""
__author__ = "Jin Jianguo"


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self, to, word):
        print(f"{self.name}对{to}说: {word}")

    def send_message(self, cellphone, to, message):
        print(f"{self.name} 使用手机{cellphone.brand}发信息")
        cellphone.send_message(to, message)


class CellPhone:
    def __init__(self, brand, price, size):
        self.brand = brand
        self.price = price
        self.size = size

    def on(self):
        print("手机开了")

    def off(self):
        return " 手机关机 "

    def send_message(self, to, message):
        print("信息发送给：{}, 内容是：{}".format(to, message))


if __name__ == '__main__':
    tom = Person("Tom", 23)
    iphone = CellPhone("iPhone6", size=4.7, price=4900)
    iphone.on()
    iphone.send_message(tom.name, '快来上课')
    off = iphone.off()
    print(off)

    print()
    tom.send_message(iphone, 'Jerry', 'Python 开发')
