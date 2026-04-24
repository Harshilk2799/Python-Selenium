from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException

driver = webdriver.Chrome()

# mywait = WebDriverWait(driver, 10)  # explicit wait declaration
mywait = WebDriverWait(driver, 10, poll_frequency= 2,ignored_exceptions=[NoSuchElementException, 
                                        ElementNotVisibleException,
                                        ElementNotSelectableException, Exception])

driver.get("https://www.google.com/")


search_box = driver.find_element(By.XPATH, "//input[@title='Search']")
search_box.send_keys("Selenium")
search_box.submit()

searchbox_click = mywait.until(EC.presence_of_element_located((By.XPATH, "//h3[normalize-space()='Selenium']")))
searchbox_click.click()

# driver.find_element(By.XPATH, "//h3[normalize-space()='Selenium']").click()

driver.close()