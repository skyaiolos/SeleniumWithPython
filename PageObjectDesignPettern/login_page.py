#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/11/26

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        
"""
from PageObjectDesignPettern.path_object import Page

from selenium.webdriver.common.by import By


class Login_Page(Page):
    # 元素定位器的方法
    username_loc = (By.ID, 'username')
    password_loc = (By.ID, 'password')
    login_btn_loc = (By.ID, 'submit')

    def type_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def login_submit(self):
        self.find_element(*self.login_btn_loc).click()

    def test_user_login(self, username, password):
        self.open_url()
        self.type_username(username)
        self.type_password(password)
        self.login_submit()
