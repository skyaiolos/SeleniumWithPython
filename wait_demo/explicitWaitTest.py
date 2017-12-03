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
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

URL = 'https://www.tmall.com'


class TmallTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(URL)
        self.driver.implicitly_wait(5)

    def test_wait(self):
        login_link = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, '请登录')))
        self.assertEqual('sn-login', login_link.get_attribute('class'))


        # login_line.click()
        # self.driver.implicitly_wait(20)

    def test_element_to_be_enalble(self):
        # self.driver.find_element_by_link_text('请登录').click()
        login = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, '请登录')))
        login.click()

        #  注意，有关用户登录，一定注意要先 switch_to.frame(iframe)
        iframe = self.driver.find_element_by_tag_name("iframe")
        WebDriverWait(self.driver, 30).until(EC.frame_to_be_available_and_switch_to_it(iframe))

        free_sign_up = WebDriverWait(self.driver, 30).until(
            # EC.presence_of_element_located((By.XPATH, '//*[@id="J_QRCodeLogin"]/div[5]/a[2]')))
            EC.visibility_of_element_located((By.LINK_TEXT, "免费注册")))
        free_sign_up.click()

        sleep(6)

        #  难点， 无法定位到同意协议窗体。

        # iframe = self.driver.find_element_by_tag_name("iframe")
        # WebDriverWait(self.driver, 30).until(EC.frame_to_be_available_and_switch_to_it(iframe))

        agree_btn = self.driver.find_element_by_class_name('btn-large')
        sleep(2)
        # agree_btn = WebDriverWait(self.driver, 20).until(
        #     EC.visibility_of_element_located((By.XPATH, '//*[@id="J_AgreementBtn"]')))

        agree_btn.click()

        WebDriverWait(self.driver, 20).until(EC.title_contains('天猫注册'))
        self.assertEqual("天猫注册", self.driver.title)

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
        if self.driver.find_element_by_name('q').get_attribute('title') == '请输入搜索文字':
            return True

        else:
            return False


if __name__ == '__main__':
    unittest.TestCase()
