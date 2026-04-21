from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()    # maximize window
# driver.minimize_window()   # minimize window


# ID and NAME Locators
# driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# driver.find_element(By.NAME, "q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

time.sleep(5)

# Link_text and Partial_Link_text Locators
# driver.find_element(By.LINK_TEXT, "Register").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()
# time.sleep(5)


driver.close()
# driver.quit()