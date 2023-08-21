import os
import sys
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

base_dir = os.path.dirname(__file__) or '.'
parent_dir = os.path.abspath(os.path.join(base_dir, '..'))
sys.path.append(parent_dir)

from Pages.home_page import HomePage
from Pages.signin_page import SignInPage
from Pages.signup_page import SignUpPage
from Resources.registerform import RegisterForm

def test_totalcost():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    service_obj = Service("../Drivers/chromedriver")
    driver = webdriver.Chrome(service = service_obj, options=chrome_options)

    driver.maximize_window()
    driver.get("https://petstore.octoperf.com/actions/Catalog.action")
    driver.implicitly_wait(5)

    homePage    = HomePage(driver)
    signinPage  = SignInPage(driver)
    signupPage  = SignUpPage(driver)
    
    register_data = RegisterForm(username   = "test_champ_"+str(uuid.uuid1()).split("-")[-2],
                                 password   = "cccc",
                                 firstname  = "testfirst",
                                 lastname   = "testlast",
                                 email      = "test@gmail.com",
                                 phone      = "0675847632",
                                 address    = "home",
                                 city       = "city",
                                 state      = "state",
                                 zip        = "10346",
                                 country    = "thailand",
                                 language   = "",
                                 favourite  = "CATS",
                                 myList     = True,
                                 myBanner   = False)

    homePage.click_signin()
    signinPage.click_register()
    signupPage.fill_form(register_data)
    homePage.click_signin()
    signinPage.signin(register_data.Username, register_data.Password)
    homePage.add_persian()
    homePage.add_golden()
    actual_value = homePage.get_total_cost_from_sum_table()
    expect_value = homePage.get_total_cost_ref()
    
    assert expect_value == actual_value, "test fail actual value != expect value"
    
    driver.close()
    driver.quit()
    
    
# test_totalcost()