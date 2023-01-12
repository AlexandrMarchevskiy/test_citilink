import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from base.base_class import Base
from utilities.logger import Logger


class Login_page(Base):

    url = 'https://www.citilink.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    login_button = '//div[@class="HeaderMenu__buttons  HeaderMenu__buttons_user"]'
    email_or_phone_field = '//input[@class=" InputBox__input js--InputBox__input  js--SignIn__login__container-input"]'
    password_field = '//input[@class=" InputBox__input js--InputBox__input  js--SignIn__password js--InputPassword InputPassword__container-input"]'
    enter_button = '//button[@class="SignIn__button js--SignIn__action_sign-in  Button  jsButton Button_theme_primary Button_size_m Button_full-width"]'

    # Getters

    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))
    
    def get_email_or_phone_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email_or_phone_field)))
    
    def get_password_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password_field)))
    
    def get_enter_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    # Actions


    def click_login_button(self):
        self.get_login_button().click()
        print('click login button')
        
        
    def input_email_or_phone_field(self, email_or_phone):
        self.get_email_or_phone_field().send_keys(email_or_phone)
        print('input email or phone')

    def input_password(self, password):
        self.get_password_field().send_keys(password)
        print('input password')
    
    def click_enter_button(self):
        self.get_enter_button().click()
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
            self.assert_url('https://www.citilink.ru/?_from_page=login')
            Logger.add_end_step(url=self.driver.current_url, method='authorisation')

