from selenium.webdriver.common.by import By

class HomePageLocators():
    signin_button          = (By.LINK_TEXT,"Sign In")
    cats_button            = (By.CSS_SELECTOR,"div[id*='Sidebar'] a img[src*='cats']")
    persian_button         = (By.LINK_TEXT,"FL-DLH-02")
    golden_button          = (By.CSS_SELECTOR,"img[src*='dog1']")
    persian_add_button     = (By.CSS_SELECTOR,"a[href*='workingItemId=EST-16']")
    golden_add_button      = (By.CSS_SELECTOR,"a[href*='workingItemId=EST-28']")
    search_field           = (By.CSS_SELECTOR,"input[name*='key']")
    search_button          = (By.CSS_SELECTOR,"input[name*='search']")
    products_list          = (By.XPATH,"//tr/td[7]")
    total_cost_ref         = (By.CSS_SELECTOR,"td[colspan='7']")
    
class SignInPageLocators():
    register_button = (By.PARTIAL_LINK_TEXT,"Register")
    username_field  = (By.CSS_SELECTOR,"input[name*='name']")
    password_field  = (By.CSS_SELECTOR,"input[name*='pass']")
    signin_button   = (By.CSS_SELECTOR,"input[name*='sign']")
    
class SignUpPageLocators():
    username_field          = (By.NAME,"username")
    password_field          = (By.NAME,"password")
    repeat_password_field   = (By.NAME,"repeatedPassword")
    firstname_field         = (By.NAME,"account.firstName")
    lastname_field          = (By.NAME,"account.lastName")
    email_field             = (By.NAME,"account.email")
    phone_field             = (By.NAME,"account.phone")
    address_field           = (By.NAME,"account.address1")
    city_field              = (By.NAME,"account.city")
    state_field             = (By.NAME,"account.state")
    zip_field               = (By.NAME,"account.zip")
    country_field           = (By.NAME,"account.country")
    language_field          = (By.NAME,"account.languagePreference")
    favourite_field         = (By.NAME,"account.favouriteCategoryId")
    list_field              = (By.NAME,"account.listOption")
    banner_field            = (By.NAME,"account.bannerOption")
    save_account_button     = (By.NAME,"newAccount")
    