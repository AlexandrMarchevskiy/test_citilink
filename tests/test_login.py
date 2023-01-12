import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import Login_page



def test_login(set_group):
    
    options = webdriver.ChromeOptions()
    options.add_argument('log-level=3')  # отключение предупреждения ошибки рукопожатия
    
    s = Service('D:\\Selenium_Learn\\test_citilink\\chromedriver.exe')
    driver = webdriver.Chrome(service=s, options=options)
    
    login = Login_page(driver)
    login.authorisation()