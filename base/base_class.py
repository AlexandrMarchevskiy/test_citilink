import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, driver):
        self.driver = driver
    
    # get current url
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'current url {get_url}')
    
    # assert word
    def assert_word(self, word: str, result: str):
        value_word = word.text
        assert value_word == result
        print('ok')
    
    # screenshot
    
    def get_screen_shot(self, step):
        now_date = datetime.datetime.utcnow().strftime('%d.%m - %H.%M.%S')
        name_screenshot = 'screenshot-' + step + now_date + '.png'
        self.driver.save_screenshot('D:\\test_shop_project\\screen\\' + name_screenshot)
    
    # assert url
    
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result, get_url
        print('ok value url')
        
    def get_element(self, element):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, element)))
