from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service("./chromedriver")
driver = webdriver.Chrome(service = service_obj, options=chrome_options)

driver.maximize_window()
driver.get("https://petstore.octoperf.com/actions/Catalog.action")

driver.find_element(By.LINK_TEXT,"Sign In").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Register").click()
# driver.implicitly_wait(2)
print(driver.find_element(By.XPATH,"//h3[normalize-space()='Account Information']").text)
driver.find_element(By.CSS_SELECTOR,"input[name*='firstName']").send_keys("testFirst")
driver.find_element(By.XPATH,"//input[@name='account.lastName']").send_keys("testLast")
driver.find_element(By.XPATH,"//input[@name='account.lastName']").clear()
driver.find_element(By.NAME,"keyword").send_keys("goldfish")
driver.find_element(By.NAME,"searchProducts").click()

