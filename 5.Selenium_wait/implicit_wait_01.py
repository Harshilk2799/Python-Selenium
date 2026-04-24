from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://www.google.com/")


search_box = driver.find_element(By.XPATH, "//input[@title='Search']")
search_box.send_keys("Selenium")
search_box.submit()

# time.sleep(5)


driver.find_element(By.XPATH, "//h3[normalize-space()='Selenium']").click()

driver.close()