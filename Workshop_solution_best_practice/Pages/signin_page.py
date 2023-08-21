from Pages.base_page import BasePage
from Resources.locators import SignInPageLocators

class SignInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def click_register(self):
        self.click(SignInPageLocators.register_button)
        
    def signin(self, username, password):
        self.enter_text(SignInPageLocators.username_field, username)
        self.clear_text(SignInPageLocators.password_field)
        self.enter_text(SignInPageLocators.password_field, password)
        self.click(SignInPageLocators.signin_button)