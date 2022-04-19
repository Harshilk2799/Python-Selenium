from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service(executable_path="/home/harshil/Selenium/Drivers/chromedriver_linux64/chromedriver")

driver = webdriver.Chrome(service = service_obj)
driver.implicitly_wait(5)

driver.get("https://www.google.com/")


search_box = driver.find_element(By.XPATH, "//input[@title='Search']")
search_box.send_keys("Selenium")
search_box.submit()

# time.sleep(5)


driver.find_element(By.XPATH, "//h3[normalize-space()='Selenium']").click()

driver.close()