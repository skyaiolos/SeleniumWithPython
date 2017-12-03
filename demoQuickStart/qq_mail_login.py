#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/12/2

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        QQ Mail Login
"""

from selenium import webdriver
from time import sleep

url = 'https://mail.qq.com'

options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')

driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(20)
iframe = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(iframe)
sleep(1)

JS_login_tab = 'document.getElementById("switcher_plogin").click()'
driver.execute_script(JS_login_tab)
sleep(3)

driver.find_element_by_css_selector("#u").send_keys("3124724")
sleep(1)
password = open('pwd.txt').read()
print("password is : {}".format(password))

driver.find_element_by_css_selector("#p").send_keys(password)

JS_login_btn = 'document.getElementById("login_button").click()'

driver.execute_script(JS_login_btn)
sleep(5)

if driver.title == "QQ邮箱":
    print("Login success")
    print("Done")

else:
    error = driver.find_element_by_class_name("err_m")
    print("Login fail.")
    print(error.text)

driver.quit()
