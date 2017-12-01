
from selenium import webdriver
import unittest, time

#!/usr/bin/python3 
# -*- coding:utf-8 -*-  
# Created on 2017/11/12

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        测试警告框 ：            
            alert、confirm、prompt 
            switch_to.alert()     
            text:       获取文本值
            accept():   点击“确认”
            dismiss():  点击“取消” 或者叉掉对话框
            send_keys():输入文本内容
"""

url = "file:///F:/SeleniumwithPython/selenium-site/page-02.html"


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
