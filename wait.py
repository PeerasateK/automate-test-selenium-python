from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service("./chromedriver")
driver = webdriver.Chrome(service = service_obj, options=chrome_options)

driver.maximize_window()
driver.get("https://petstore.octoperf.com/actions/Catalog.action")
driver.implicitly_wait(5)

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_all_elements_located(By.CSS_SELECTOR,".someclass"))