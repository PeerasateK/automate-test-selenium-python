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
