from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/")
driver.maximize_window()    # maximize window
                
# CSS Selector Locator

# tag & class & attribute
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("Username")
driver.find_element(By.CSS_SELECTOR, "input[name='pass']").send_keys("Password@123")

time.sleep(5)

driver.close()