from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# service_obj = Service()
# driver = webdriver.Chrome(service = service_obj)
# driver.get("https://google.com")

service_obj = Service("/Users/a667194/Workspace/Knowledge/Automated-Test/python-selenium/chromedriver")
driver = webdriver.Chrome(service = service_obj)
driver.maximize_window()
driver.get("https://google.com")
print(driver.title)
print(driver.current_url)
driver.get("https://youtube.com")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()
