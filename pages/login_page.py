import time

import allure
from base.base_class import Base
from utilities.logger import Logger


class Login_page(Base):

    url = 'https://www.citilink.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    login_button = '//*[@id="__next"]/div/div[3]/div/div[2]/div/div/div[2]/div[2]/div[1]'
    email_or_phone_field = '//input[@name="login"]'
    password_field = '//input[@name="pass"]'
    enter_button = '//button[@class="e4uhfkv0 css-1yh1imp e4mggex0"]'

  
  
    # Actions
    
    def click_login_button(self):
        self.get_element(self.login_button).click()
        print('click login button')
    
        
    def input_email_or_phone_field(self, email_or_phone):
        self.get_element(self.email_or_phone_field).send_keys(email_or_phone)
        print('input email or phone')

    def input_password(self, password):
        self.get_element(self.password_field).send_keys(password)
        print('input password')
    
    def click_enter_button(self):
        self.get_element(self.enter_button).click()
        print('click enter button')
        
        


    # Methods

    def authorisation(self):
        with allure.step('Authorisation'):
            Logger.add_start_step(method='authorisation')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.driver.refresh()
            self.get_current_url()
            self.click_login_button()
            self.input_email_or_phone_field('IQBusinessCoffee@yandex.ru')
            self.input_password('16092014_Iii')
            self.click_enter_button()
            self.assert_url('https://www.citilink.ru/?_action=login&_success_login=1')
            Logger.add_end_step(url=self.driver.current_url, method='authorisation')

