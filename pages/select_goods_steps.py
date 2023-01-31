import time

import allure
from selenium.webdriver import ActionChains

from base.base_class import Base
from utilities.logger import Logger


class Select_goods(Base):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    # Locators
    
    catalog_btn = "//span[contains(text(),'Каталог товаров')]" # //span[text()='Каталог товаров'] //div[@class="MainHeader__catalog"]
    
    
        # Cats
    samsung_phones = '//a[@href="/catalog/smartfony--samsung-m/?ref=mainmenu"]' # //span[text()='Смартфоны Samsung']
    
    computers_cat = '//a[@data-category-alias="computers_and_notebooks"]'
    pc_sub_cat = '//*[@id="__next"]/div/main/div[1]/div/div[2]/aside/div/div/div[2]/ul/li[2]/a'  #'//a[@href="/catalog/kompyutery/"]'
    
    
    
    
        #Optional
    sort_by_price = "//span[text()='по цене']" #'//div[@data-alias="price"]'
    # sort_by_price_pc = "//span[text()='по цене']"
    
    add_to_cart = '//div[@class="ProductPageCTAButtonsSection__buy-buttons js--ProductPageCTAButtonsSection__buy-buttons"]' #'//button[@class="ProductPageCTAButtonsSection__add-to-cart js--ProductPageCTAButtonsSection__add-to-cart Button jsButton Button_theme_primary Button_size_l Button_with-icon"]'
    
    continue_after_add_to_cart = '//button[@data-label="Продолжить покупки"]'
    
        #Goods
    samsung_smartphone = "//a[contains( text(),'Смартфон Samsung Galaxy Z Fold3 12/256Gb,  SM-F926B,  черный')]"
    pc_hyper_pc = '//a[@title="Компьютер HYPERPC LUMEN MAX,  Intel Core i7 12700KF,  DDR5 32ГБ, 2ТБ(SSD),  NVIDIA GeForce RTX 3070Ti - 8192 Мб,  Windows 11 Home,  серебристый"]'
    
    
    
    #Actions
    
    def click_catalog_button(self):
        self.get_element(self.catalog_btn).click()
        print('click catalog button')
    
    def click_samsung_cat(self):
        self.get_element(self.samsung_phones).click()
        print('click samsung cat btn')
        
    def click_computers_cat(self):
        self.get_element(self.computers_cat).click()
        print('click computers cat')
    
    def click_pc_sub_cat(self):
        self.get_element(self.pc_sub_cat).click()
        print('click pc sub cat')
    
    def sort_goods_by_price(self):
        actionChains = ActionChains(self.driver)
        actionChains.double_click(self.get_element(self.sort_by_price)).perform()
        print('sorting phones by price desc')
    
    def select_phone(self):
        self.get_element(self.samsung_smartphone).click()
        print('phone selected')
        
    def added_to_cart(self):
        self.get_element(self.add_to_cart).click()
        print('added to cart')
    
    def continue_shopping(self):
        self.get_element(self.continue_after_add_to_cart).click()
        print('alert close')
    
    
    # def sort_pc_by_price(self):
    #     actionChains = ActionChains(self.driver)
    #     actionChains.double_click(self.get_element(self.sort_by_price)).perform()
    #     print('sorting pc by price desc')
    
    def select_pc(self):
        self.get_element(self.pc_hyper_pc).click()
        print('pc selected')
        
        
    # Methods

    def select_goods(self):
        with allure.step('Select goods'):
            Logger.add_start_step(method='select_goods')
            self.click_catalog_button()
            self.click_samsung_cat()
            self.sort_goods_by_price()
            time.sleep(5)
            self.select_phone()
            self.assert_url('https://www.citilink.ru/product/smartfon-samsung-galaxy-z-fold3-sm-f926b-256gb-12gb-chernyi-3g-4g-2sim-1784686/')
            time.sleep(5)
            self.added_to_cart()
            self.click_catalog_button()
            self.click_computers_cat()
            time.sleep(3)
            self.click_pc_sub_cat()
            time.sleep(5)
            self.sort_goods_by_price()
            # time.sleep(2)
            # self.sort_goods_by_price()
            self.select_pc()
            self.assert_url('https://www.citilink.ru/product/pk-hyperpc-lumenmax-i5-12700kf-32gb-ssd2tb-rtx-3070ti-w11-1871335/')
            self.added_to_cart()
            Logger.add_end_step(url=self.driver.current_url, method='select_goods')