# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/11/7

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        SEC 31 同步测试 1
"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

URL = 'https://www.tmall.com'


class TmallTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(URL)
        self.driver.implicitly_wait(5)

    def test_wait(self):
        login_line = WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.LINK_TEXT, '请登录')))
        self.assertEqual('sn-login', login_line.get_attribute('class'))

        # login_line.click()
        # self.driver.implicitly_wait(20)

    # def test_element_to_be_enalble(self):
    #     self.driver.find_element_by_link_text('请登录').click()
    #     free_sign_up = WebDriverWait(self.driver, 30).until(
    #         expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="J_QRCodeLogin"]/div[5]/a[2]')))
    #     free_sign_up.click()
    #
    #     agree_btn = WebDriverWait(self.driver, 20).until(
    #         expected_conditions.element_to_be_clickable((By.LINK_TEXT, '同意协议')))
    #     agree_btn.click()
    #     WebDriverWait(self.driver, 20).until(expected_conditions.title_contains('天猫注册'))

    def test_custom_coditions(self):
        self.driver.get(URL)
        # WebDriverWait(self.driver, 20).until(self.check_q())
        WebDriverWait(self.driver, 20).until(lambda d: d.find_element_by_name('q').get_attribute('title') == '请输入搜索文字')
        search_field = self.driver.find_element_by_name('q')
        self.assertEqual('请输入搜索文字', search_field.get_attribute('title'))

    def tearDown(self):
        self.driver.quit()

    # 可以代替lambda 表达式， return True
    def check_q(self):
        if self.driver.find_element_by_name('q').get_attribute('title') =='请输入搜索文字':
            return True

        else:
            return False


if __name__ == '__main__':
    unittest.TestCase()
