from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service("/home/harshil/Selenium/Drivers/chromedriver_linux64/chromedriver")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()    # maximize window
                
# CSS Selector Locator

# tag & id
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("Harshil")
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys("Harshil")

# tag & class
# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("Harshil")
# driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("Harshil")


# tag & attribute
# driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_email]").send_keys("Harshil")
# driver.find_element(By.CSS_SELECTOR, "[data-testid=royal_email]").send_keys("Harshil")

# tag & class & attribute
driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_email]").send_keys("Username")
driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_pass]").send_keys("Password@123")

time.sleep(5)

driver.close()