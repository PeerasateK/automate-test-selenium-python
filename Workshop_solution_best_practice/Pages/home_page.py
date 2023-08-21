from Pages.base_page import BasePage
from Resources.locators import HomePageLocators

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def click_signin(self):
        self.click(HomePageLocators.signin_button)
        
    def add_persian(self):
        self.click(HomePageLocators.cats_button)
        self.click(HomePageLocators.persian_button)
        self.click(HomePageLocators.persian_add_button)
        
    def add_golden(self):
        self.enter_text(HomePageLocators.search_field, "golden")
        self.click(HomePageLocators.search_button)
        self.click(HomePageLocators.golden_button)
        self.click(HomePageLocators.golden_add_button)
        
    def get_total_cost_from_sum_table(self):
        totalCost = 0
        for ele in self.get_list_data(HomePageLocators.products_list):
            totalCost += float(ele.text[1:])
        return totalCost
    
    def get_total_cost_ref(self):
        return float(self.get_text(HomePageLocators.total_cost_ref).split("$")[1])