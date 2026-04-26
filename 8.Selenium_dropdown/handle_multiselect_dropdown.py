from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()

driver.get("https://demoqa.com/select-menu")
driver.maximize_window()

# Locate multi-select dropdown
cars_element = driver.find_element(By.XPATH, "//*[@id='cars']")
cars_ms = Select(cars_element)

# -------- SELECT METHODS --------

# 1. Select by index
cars_ms.select_by_index(0)

# 2. Select by value
cars_ms.select_by_value("saab")

# 3. Select by visible text
cars_ms.select_by_visible_text("Opel")
cars_ms.select_by_visible_text("Audi")

time.sleep(2)

# -------- DESELECT METHODS --------

# 1. Deselect by index
cars_ms.deselect_by_index(0)

# 2. Deselect by value
cars_ms.deselect_by_value("saab")

# 3. Deselect by visible text
cars_ms.deselect_by_visible_text("Opel")

# 4. Deselect all
cars_ms.deselect_all()

time.sleep(2)

driver.quit()