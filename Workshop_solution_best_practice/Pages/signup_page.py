from Pages.base_page import BasePage
from Resources.locators import SignUpPageLocators

class SignUpPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def fill_form(self, register_form):
        self.enter_text(SignUpPageLocators.username_field, register_form.Username)
        self.enter_text(SignUpPageLocators.password_field, register_form.Password)
        self.enter_text(SignUpPageLocators.repeat_password_field, register_form.Password)
        self.enter_text(SignUpPageLocators.firstname_field, register_form.Firstname)
        self.enter_text(SignUpPageLocators.lastname_field, register_form.Lastname)
        self.enter_text(SignUpPageLocators.email_field, register_form.Email)
        self.enter_text(SignUpPageLocators.phone_field, register_form.Phone)
        self.enter_text(SignUpPageLocators.address_field, register_form.Address)
        self.enter_text(SignUpPageLocators.city_field, register_form.City)
        self.enter_text(SignUpPageLocators.state_field, register_form.State)
        self.enter_text(SignUpPageLocators.zip_field, register_form.Zip)
        self.enter_text(SignUpPageLocators.country_field, register_form.Country)
        if register_form.Language != "":
            self.select_dropdown(SignUpPageLocators.language_field,register_form.Language)
        if register_form.Favourite != "":
            self.select_dropdown(SignUpPageLocators.favourite_field,register_form.Favourite)
        if register_form.MyList:
            self.click(SignUpPageLocators.list_field)
        if register_form.MyBanner:
            self.click(SignUpPageLocators.banner_field)
        self.click(SignUpPageLocators.save_account_button)