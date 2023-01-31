import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import Login_page
from pages.select_goods_steps import Select_goods


def test_smoke(set_group, set_up):
    
    options = webdriver.ChromeOptions()
    options.add_argument('log-level=3')  # отключение предупреждения ошибки рукопожатия
    
    s = Service('D:\\Selenium_Learn\\test_citilink\\chromedriver.exe')
    driver = webdriver.Chrome(service=s, options=options)
    
    login = Login_page(driver)
    login.authorisation()
    
    s_g = Select_goods(driver)
    s_g.select_goods()