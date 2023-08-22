from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import uuid

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service("./chromedriver")
driver = webdriver.Chrome(service = service_obj, options=chrome_options)

driver.maximize_window()
driver.get("https://petstore.octoperf.com/actions/Catalog.action")
driver.implicitly_wait(5)

username = "test_champ_"+str(uuid.uuid1()).split("-")[-2]
password = "cccc"

# HomePage
driver.find_element(By.LINK_TEXT,"Sign In").click()

# SignInPage
driver.find_element(By.PARTIAL_LINK_TEXT,"Register").click()

# SignUpPage
driver.find_element(By.NAME,"username").send_keys(username)
driver.find_element(By.NAME,"password").send_keys(password)
driver.find_element(By.NAME,"repeatedPassword").send_keys(password)
driver.find_element(By.NAME,"account.firstName").send_keys("testfirst")
driver.find_element(By.NAME,"account.lastName").send_keys("testlast")
driver.find_element(By.NAME,"account.email").send_keys("testmail@gmail.com")
driver.find_element(By.NAME,"account.phone").send_keys("0684938576")
driver.find_element(By.NAME,"account.address1").send_keys("home")
driver.find_element(By.NAME,"account.city").send_keys("city")
driver.find_element(By.NAME,"account.state").send_keys("state")
driver.find_element(By.NAME,"account.zip").send_keys("10160")
driver.find_element(By.NAME,"account.country").send_keys("thailand")
dropdownFavCat = Select(driver.find_element(By.NAME,"account.favouriteCategoryId"))
dropdownFavCat.select_by_visible_text("CATS")
driver.find_element(By.NAME,"account.listOption").click()
driver.find_element(By.NAME,"newAccount").click()

# HomePage
driver.find_element(By.LINK_TEXT,"Sign In").click()

# SignInPage
driver.find_element(By.CSS_SELECTOR,"input[name*='name']").send_keys(username)
driver.find_element(By.CSS_SELECTOR,"input[name*='pass']").clear()
driver.find_element(By.CSS_SELECTOR,"input[name*='pass']").send_keys(password)
driver.find_element(By.CSS_SELECTOR,"input[name*='sign']").click()

# HomePage
driver.find_element(By.CSS_SELECTOR,"div[id*='Sidebar'] a img[src*='cats']").click()

# SearchPage (Persian)
driver.find_element(By.LINK_TEXT,"FL-DLH-02").click()
driver.find_element(By.CSS_SELECTOR,"a[href*='workingItemId=EST-16']").click()

# ShoppingCartPage
driver.find_element(By.CSS_SELECTOR,"input[name*='key']").send_keys("golden")
driver.find_element(By.CSS_SELECTOR,"input[name*='search']").click()

# SearchPage (Golden)
driver.find_element(By.CSS_SELECTOR,"img[src*='dog1']").click()
driver.find_element(By.CSS_SELECTOR,"a[href*='workingItemId=EST-28']").click()


# ShoppingCartPage
totalCost = 0
productWebElements = driver.find_elements(By.XPATH,"//tr/td[7]")
for ele in productWebElements:
    totalCost += float(ele.text[1:])

totalCostRef = float(driver.find_element(By.CSS_SELECTOR,"td[colspan='7']").text.split("$")[1])

print(totalCost)
print(totalCostRef)

assert totalCostRef == totalCost