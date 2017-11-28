#!/usr/bin/env python3 
# -*- coding:utf-8 -*-  
# Created on 2017/11/28
__author__ = "Jianguo Jin - jinjianguo@zhizhangyi.com "

"""
    Description:
        Demo for the finding elements , 8 kinds
"""

from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=options)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://www.baidu.com')

# 1. 通过它的 name 属性定位到这个元素 search_field = driver.find_element_by_name("wd")
search_field = driver.find_element_by_name("wd")
search_field.clear()
search_field.send_keys("Python")

# 2. 通过它的 id 属性定位到这个元素
search_btn = driver.find_element_by_id('su')
search_btn.click()
sleep(3)

# 3. 通过它的 class name 属性定位到这个元素
baidu_home_page = driver.find_element_by_class_name('toindex')
baidu_home_page.click()

# 4. 通过它的 tag (标签) 属性定位到这个元素
links = driver.find_elements_by_tag_name('a')
print(len(links))

for link in links:
    print(link.text)

sleep(3)

# 5. 通过它的 链接文字 定位到这个元素
news = driver.find_element_by_link_text("新闻")
news.click()
sleep(2)

# 6. 通过它的 部分链接文字 定位到这个元素
homepage = driver.find_element_by_partial_link_text("首页")
homepage.click()
sleep(2)

# 7. 通过它的 css 定位到元素     -  最推荐的
setting_btn = driver.find_element_by_css_selector('#u1 > a.pf')
setting_btn.click()
sleep(1)

# 8. 通过它的 xpath 定位到元素  -  推荐的
search_setting = driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[1]')
# search_setting = driver.find_element_by_css_selector('#wrapper > div.bdpfmenu > a:nth-child(3)')

search_setting.click()
sleep(2)
driver.get_screenshot_as_file(r"..\Captures\Search_Setting.png")

driver.quit()
