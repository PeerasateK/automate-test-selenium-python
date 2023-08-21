from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    
    def click(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator)).click()
    
    def enter_text(self, by_locator, text):
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        
    def clear_text(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator)).clear()
        
    def select_dropdown(self, by_locator, text):
        dropdown = Select(self.wait.until(EC.visibility_of_element_located(by_locator)))
        dropdown.select_by_visible_text(text)
        
    def get_list_data(self, by_locator):
        return self.wait.until(EC.visibility_of_all_elements_located(by_locator))
    
    def get_text(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).text