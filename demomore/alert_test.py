
from selenium import webdriver
import unittest, time

#!/usr/bin/python3 
# -*- coding:utf-8 -*-  
# Created on 2017/11/12

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        测试警告框
"""

url = "file:///P:/Project_python/SeleniumwithPython/selenium-site/page-02.html"


class AlertTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('disable-infobars')
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(20)
        self.driver.get(url)

    def test_alert(self):
        btn = self.driver.find_element_by_partial_link_text('弹出框')
        btn.click()
        alert = self.driver.switch_to.alert
        txt = alert.text
        print(txt)
        self.assertEqual('确认删除吗', txt)
        time.sleep(5)
        alert.accept()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
