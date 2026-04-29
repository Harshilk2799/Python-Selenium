from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://en.wikipedia.org/wiki/Machine_learning")

# 1. scrolling to a specific element
# ai_subtopic = driver.find_element(By.XPATH, "//*[@id='toc-Data_mining']")
# driver.execute_script("arguments[0].scrollIntoView();", ai_subtopic)


# 2. scrolling vertically
# driver.execute_script("window.scrollBy(0, 2500);")
# time.sleep(5)
# driver.execute_script("window.scrollBy(0, -1500)")


# 3. scrolling horizontally
# driver.execute_script("window.scrollBy(5000, 0)")


# 4. scrolling to page height
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")

time.sleep(5)

driver.quit()