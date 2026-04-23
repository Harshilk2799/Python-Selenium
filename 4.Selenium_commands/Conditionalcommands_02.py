from selenium import webdriver 
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")

driver.maximize_window()

# is_displayed()   = is_displayed method is used to check if element it visible to user or not. It return a boolean value True or False. 
# is_enabled()     = is_enabled method is used to check if element is enabled or not. It return a boolean value True or False. 
# is_selected()    = is_selected method is used to check if element is selected or not. It return a boolean value True or False. 



# search_box = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# print(search_box.is_displayed())


# search_box = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# print(search_box.is_enabled())



# is_selected() = radio button and checkbox

rd_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
rd_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")
print("Default radio button status...")
print(rd_male.is_selected())
print(rd_female.is_selected())

rd_male.click()

print("After selecting male radio button...")
print(rd_male.is_selected())
print(rd_female.is_selected())

rd_female.click()

print("After selecting female radio button...")
print(rd_male.is_selected())
print(rd_female.is_selected())

driver.close()